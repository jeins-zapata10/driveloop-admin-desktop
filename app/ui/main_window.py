from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QStackedWidget, QSizePolicy,
    QFrame
)

from app.ui.dashboard_page import DashboardPage
from app.ui.vehiculos_page import VehiculosPage
from app.ui.usuarios_page import UsuariosPage
from app.ui.tickets_page import TicketsPage


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("DriveLoop Admin Desktop")
        self.resize(1280, 760)
        self.setWindowIcon(QIcon("app/assets/driveloop_logo.png"))
        self.build_ui()

    def build_ui(self):
        central = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(280)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(18, 18, 18, 18)
        sidebar_layout.setSpacing(12)

        logo_card = QFrame()
        logo_card.setObjectName("logoCard")
        logo_layout = QVBoxLayout()
        logo_layout.setContentsMargins(16, 16, 16, 16)
        logo_layout.setSpacing(8)

        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("app/assets/driveloop_logo.png")
        if not pixmap.isNull():
            logo.setPixmap(
                pixmap.scaled(170, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            logo.setText("DriveLoop")
            logo.setObjectName("brandTitle")
            logo.setAlignment(Qt.AlignCenter)

        brand_title = QLabel("Panel Administrativo")
        brand_title.setObjectName("brandTitle")
        brand_title.setAlignment(Qt.AlignCenter)

        brand_subtitle = QLabel(f"{self.user['nom']} {self.user['ape']}")
        brand_subtitle.setObjectName("brandSubtitle")
        brand_subtitle.setAlignment(Qt.AlignCenter)

        logo_layout.addWidget(logo)
        logo_layout.addWidget(brand_title)
        logo_layout.addWidget(brand_subtitle)
        logo_card.setLayout(logo_layout)

        sidebar_layout.addWidget(logo_card)

        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_vehiculos = QPushButton("Vehículos")
        self.btn_usuarios = QPushButton("Usuarios")
        self.btn_tickets = QPushButton("Tickets")

        botones = [
            self.btn_dashboard,
            self.btn_vehiculos,
            self.btn_usuarios,
            self.btn_tickets,
        ]

        for btn in botones:
            btn.setObjectName("menuButton")
            btn.setCheckable(True)
            btn.setMinimumHeight(46)
            sidebar_layout.addWidget(btn)

        self.btn_dashboard.setChecked(True)

        sidebar_layout.addStretch()

        sidebar_user = QLabel("DriveLoop Admin Desktop")
        sidebar_user.setObjectName("sidebarUser")
        sidebar_user.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(sidebar_user)

        sidebar.setLayout(sidebar_layout)

        self.stack = QStackedWidget()
        self.stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.dashboard_page = DashboardPage()
        self.vehiculos_page = VehiculosPage()
        self.usuarios_page = UsuariosPage()
        self.tickets_page = TicketsPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.vehiculos_page)
        self.stack.addWidget(self.usuarios_page)
        self.stack.addWidget(self.tickets_page)

        self.btn_dashboard.clicked.connect(lambda: self.change_page(0))
        self.btn_vehiculos.clicked.connect(lambda: self.change_page(1))
        self.btn_usuarios.clicked.connect(lambda: self.change_page(2))
        self.btn_tickets.clicked.connect(lambda: self.change_page(3))

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

        central.setLayout(main_layout)
        self.setCentralWidget(central)

    def change_page(self, index):
        self.stack.setCurrentIndex(index)

        self.btn_dashboard.setChecked(index == 0)
        self.btn_vehiculos.setChecked(index == 1)
        self.btn_usuarios.setChecked(index == 2)
        self.btn_tickets.setChecked(index == 3)