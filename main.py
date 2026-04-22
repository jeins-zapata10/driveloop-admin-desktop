import sys
from PySide6.QtWidgets import QApplication
from app.ui.login_window import LoginWindow
from app.utils.styles import APP_STYLE


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()