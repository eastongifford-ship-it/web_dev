import sys
import threading
import requests
from flask import Flask, request, Response, send_file
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# --- Flask proxy + UI server ---
app = Flask(__name__)

HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Ghost</title>
  <style>
    body { margin:0; font-family:sans-serif; background:#000; color:#fff; }
    .toolbar { background:#111; padding:8px; display:flex; gap:8px; }
    .address { flex:1; padding:6px; border-radius:6px; border:none; }
    iframe { width:100%; height:calc(100vh - 40px); border:none; }
    button { background:#222; color:#fff; border:none; padding:6px 10px; border-radius:6px; cursor:pointer; }
  </style>
</head>
<body>
  <div class="toolbar">
    <input id="address" class="address" placeholder="Enter URL" />
    <button onclick="go()">Go</button>
  </div>
  <iframe id="view"></iframe>
  <script>
    function normalize(u){
      if(!u) return "about:blank";
      return /^(https?:)/i.test(u) ? u : "https://" + u;
    }
    function go(){
      const u = normalize(document.getElementById("address").value.trim());
      document.getElementById("view").src = "/proxy?url=" + encodeURIComponent(u);
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML_UI

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return "No URL", 400
    try:
        resp = requests.get(url, headers={"User-Agent": "GhostBrowser/1.0"})
        excluded = ["content-encoding","transfer-encoding","connection","x-frame-options","content-security-policy"]
        headers = [(k,v) for k,v in resp.headers.items() if k.lower() not in excluded]
        return Response(resp.content, resp.status_code, headers)
    except Exception as e:
        return f"Error fetching {url}: {e}", 500

# --- Run Flask in background thread ---
def run_server():
    app.run(port=5000, debug=False, use_reloader=False)

# --- PyQt Browser window ---
def run_browser():
    qt_app = QApplication(sys.argv)
    view = QWebEngineView()
    view.setWindowTitle("Ghost")
    view.resize(1200,800)
    view.setUrl(QUrl("http://localhost:5000"))
    view.show()
    sys.exit(qt_app.exec_())

if __name__ == "__main__":
    t = threading.Thread(target=run_server)
    t.daemon = True
    t.start()
    run_browser()

