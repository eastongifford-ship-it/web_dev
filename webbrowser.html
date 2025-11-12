import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QHBoxLayout, QToolBar, QSplashScreen,
    QCompleter
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QUrl, Qt, QTimer

BOOKMARKS = {
    "Google": "https://www.google.com",
    "OpenAI": "https://www.openai.com",
    "YouTube": "https://www.youtube.com"
}

HTML_SPLASH = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Ghost</title>
  <style>
    body {
      margin: 0;
      background-color: #000;
      color: white;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .splash {
      text-align: center;
      opacity: 0;
      animation: fadeIn 2s forwards;
    }
    .logo {
      width: 120px;
      margin-bottom: 20px;
    }
    .title {
      font-size: 2.5em;
      margin: 0;
    }
    .subtitle {
      font-size: 1.2em;
      margin-top: 10px;
      color: #aaa;
    }
    @keyframes fadeIn {
      to {
        opacity: 1;
      }
    }
  </style>
</head>
<body>
  <div class="splash">
    <img src="ghost_logo.png" class="logo" />
    <h1 class="title">Ghost</h1>
    <p class="subtitle" id="status">Launching...</p>
    <script>
      setTimeout(() => {
        document.getElementById("status").textContent = "Ready!";
      }, 2500);
    </script>
  </div>
</body>
</html>
"""

class BrowserTab(QWidget):
    def __init__(self, history_list):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.browser = QWebEngineView()
        self.history_list = history_list

        splash_path = os.path.abspath("splash.html")
        with open(splash_path, "w", encoding="utf-8") as f:
            f.write(HTML_SPLASH)

        self.browser.setUrl(QUrl.fromLocalFile(splash_path))
        self.browser.urlChanged.connect(self.update_history)

        nav_bar = QHBoxLayout()
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        self.completer = QCompleter()
        self.completer.setModel(self.address_bar.model())
        self.address_bar.setCompleter(self.completer)

        back_btn = QPushButton("←")
        forward_btn = QPushButton("→")
        reload_btn = QPushButton("⟳")

        back_btn.clicked.connect(self.browser.back)
        forward_btn.clicked.connect(self.browser.forward)
        reload_btn.clicked.connect(self.browser.reload)

        nav_bar.addWidget(back_btn)
        nav_bar.addWidget(forward_btn)
        nav_bar.addWidget(reload_btn)
        nav_bar.addWidget(self.address_bar)

        bookmark_bar = QHBoxLayout()
        for name, url in BOOKMARKS.items():
            btn = QPushButton(name)
            btn.clicked.connect(lambda _, u=url: self.browser.setUrl(QUrl(u)))
            bookmark_bar.addWidget(btn)

        self.layout.addLayout(nav_bar)
        self.layout.addLayout(bookmark_bar)
        self.layout.addWidget(self.browser)

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_history(self, qurl):
        url = qurl.toString()
        if url not in self.history_list:
            self.history_list.append(url)
            self.completer.model().setStringList(self.history_list)

class Ghost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ghost")
        self.setGeometry(100, 100, 1200, 800)

        self.history_list = []

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        new_tab_btn = QPushButton("New Tab")
        new_tab_btn.clicked.connect(self.add_tab)
        toolbar.addWidget(new_tab_btn)

        self.add_tab()

    def add_tab(self):
        tab = BrowserTab(self.history_list)
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)

    def close_tab(self, index):
        self.tabs.removeTab(index)

class GhostSplash(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap("ghost_logo.png")
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setFont(QFont("Arial", 16))
        self.showMessage("Launching Ghost...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    def fade_in(self):
        for opacity in range(0, 11):
            self.setWindowOpacity(opacity / 10)
            QTimer.singleShot(opacity * 50, lambda: None)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = GhostSplash()
    splash.fade_in()
    splash.show()
    QTimer.singleShot(2000, splash.close)

    window = Ghost()
    QTimer.singleShot(2000, window.show)

    sys.exit(app.exec_())
