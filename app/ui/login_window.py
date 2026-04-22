from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QFrame
)

from app.services.auth_service import AuthService
from app.ui.main_window import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setWindowTitle("DriveLoop Admin - Login")
        self.setWindowIcon(QIcon("app/assets/driveloop_logo.png"))
        self.setFixedSize(430, 520)
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(32, 32, 32, 32)
        main_layout.setSpacing(16)

        main_layout.addStretch()

        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("app/assets/driveloop_logo.png")
        if not pixmap.isNull():
            self.logo_label.setPixmap(
                pixmap.scaled(200, 85, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            self.logo_label.setText("DriveLoop")
            self.logo_label.setStyleSheet(
                "font-size: 28px; font-weight: bold; color: #C91843;"
            )

        self.title = QLabel("Iniciar sesión")
        self.title.setObjectName("pageTitle")
        self.title.setAlignment(Qt.AlignCenter)

        card = QFrame()
        card.setObjectName("card")

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(24, 24, 24, 24)
        card_layout.setSpacing(14)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Correo electrónico")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Contraseña")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Ingresar")
        self.btn_login.clicked.connect(self.handle_login)

        card_layout.addWidget(self.input_email)
        card_layout.addWidget(self.input_password)
        card_layout.addWidget(self.btn_login)

        card.setLayout(card_layout)

        main_layout.addWidget(self.logo_label)
        main_layout.addWidget(self.title)
        main_layout.addWidget(card)

        main_layout.addStretch()
        self.setLayout(main_layout)

    def handle_login(self):
        email = self.input_email.text().strip()
        password = self.input_password.text().strip()

        if not email or not password:
            QMessageBox.warning(
                self,
                "Campos requeridos",
                "Completa correo y contraseña."
            )
            return

        result = AuthService.login(email, password)

        if not result["success"]:
            QMessageBox.warning(
                self,
                "Acceso denegado",
                result["message"]
            )
            return

        user = result["user"]

        self.main_window = MainWindow(user)
        self.main_window.show()
        self.close()