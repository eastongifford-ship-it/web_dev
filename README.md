# Webrowser — Simple Local Browser

This project is a minimal local "browser" UI (`webrowser.html`) plus a small Node proxy (`server.js`) pm installthat fetches and rewrites pages so they can be loaded and navigated from the local UI.

Why a proxy? Many websites block framing or use absolute/relative resource URLs that won't load correctly if simply embedded — the proxy fetches pages and rewrites resource links so the UI can load them.

Quick start

1. Install dependencies:

```bash
cd /workspaces/web_dev
n
```

2. Start the proxy server:

```bash
npm start
# or: PORT=3000 node server.js
```

3. Open the frontend in your browser:

Navigate to `http://localhost:3000/webrowser.html` and use the address bar to browse.

Notes and limitations
- This is a simple educational proxy. It rewrites common attributes (`href`, `src`, etc.) but doesn't fully replicate a real browser engine.
- Some websites actively block scraping or rely on complex JavaScript that may not work through this proxy.
- Use responsibly and respect site terms of service.

If you want, I can:
- Add support to rewrite inline CSS `url()` references.
- Persist bookmarks or add downloads handling.
- Add a small UI to run the server via a button.
