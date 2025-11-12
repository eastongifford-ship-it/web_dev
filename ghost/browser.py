import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QHBoxLayout, QToolBar
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.browser = QWebEngineView()

        # Load custom HTML UI
        html_path = os.path.abspath("interface.html")
        self.browser.setUrl(QUrl.fromLocalFile(html_path))

        # Navigation bar
        nav_bar = QHBoxLayout()
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

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

        self.layout.addLayout(nav_bar)
        self.layout.addWidget(self.browser)

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("True Python Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        new_tab_btn = QPushButton("New Tab")
        new_tab_btn.clicked.connect(self.add_tab)
        toolbar.addWidget(new_tab_btn)

        self.add_tab()

    def add_tab(self):
        tab = BrowserTab()
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
