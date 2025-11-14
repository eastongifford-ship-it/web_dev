const express = require('express');
const fetch = require('node-fetch');
const cheerio = require('cheerio');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files (so webrowser.html is reachable at /webrowser.html)
app.use(express.static(__dirname));

app.get('/proxy', async (req, res) => {
  const target = req.query.url;
  if (!target) return res.status(400).send('Missing url parameter');

  try {
    const response = await fetch(target, { redirect: 'follow' });
    const contentType = (response.headers.get('content-type') || '').toLowerCase();

    // If HTML, rewrite resource links to go through the proxy as well
    if (contentType.includes('text/html')) {
      const text = await response.text();
      const $ = cheerio.load(text, { decodeEntities: false });

      const rewriteAttr = (selector, attr) => {
        $(selector).each((i, el) => {
          const val = $(el).attr(attr);
          if (!val) return;
          try {
            const abs = new URL(val, response.url).href;
            $(el).attr(attr, '/proxy?url=' + encodeURIComponent(abs));
          } catch (e) {
            // ignore invalid URLs
          }
        });
      };

      rewriteAttr('a', 'href');
      rewriteAttr('link', 'href');
      rewriteAttr('img', 'src');
      rewriteAttr('script', 'src');
      rewriteAttr('iframe', 'src');
      rewriteAttr('source', 'src');
      rewriteAttr('video', 'src');
      rewriteAttr('audio', 'src');

      // Rewrite form actions
      $('form').each((i, el) => {
        const action = $(el).attr('action') || '';
        try {
          const abs = new URL(action || response.url, response.url).href;
          $(el).attr('action', '/proxy?url=' + encodeURIComponent(abs));
        } catch (e) {}
      });

      const html = $.html();
      res.set('content-type', 'text/html; charset=utf-8');
      return res.send(html);
    }

    // For non-HTML, stream/forward the content with the original content-type
    const buf = Buffer.from(await response.arrayBuffer());
    if (response.headers.get('content-length')) {
      res.set('content-length', response.headers.get('content-length'));
    }
    if (response.headers.get('content-type')) {
      res.set('content-type', response.headers.get('content-type'));
    }
    return res.send(buf);
  } catch (err) {
    console.error('Proxy error:', err && err.stack ? err.stack : err);
    return res.status(500).send('Proxy error: ' + String(err));
  }
});

app.listen(PORT, () => {
  console.log(`Webrowser proxy running at http://localhost:${PORT}/webrowser.html`);
});
