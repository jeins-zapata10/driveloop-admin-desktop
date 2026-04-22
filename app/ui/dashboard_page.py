from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout
from app.services.dashboard_service import DashboardService


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()

    def build_ui(self):
        metrics = DashboardService.get_metrics()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        titulo = QLabel("Dashboard administrativo")
        titulo.setObjectName("pageTitle")
        main_layout.addWidget(titulo)

        grid = QGridLayout()
        grid.setHorizontalSpacing(16)
        grid.setVerticalSpacing(16)

        datos = [
            ("Total usuarios", metrics["usuarios"]),
            ("Total vehículos", metrics["vehiculos"]),
            ("Vehículos disponibles", metrics["vehiculos_disponibles"]),
            ("Tickets abiertos", metrics["tickets_abiertos"]),
            ("Total reservas", metrics["reservas"]),
        ]

        positions = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]

        for (texto, valor), (row, col) in zip(datos, positions):
            card = QFrame()
            card.setObjectName("card")
            card.setMinimumHeight(120)

            card_layout = QVBoxLayout()
            card_layout.setContentsMargins(18, 18, 18, 18)
            card_layout.setSpacing(8)

            label_title = QLabel(texto)
            label_title.setObjectName("sectionTitle")

            label_value = QLabel(str(valor))
            label_value.setObjectName("metricValue")

            card_layout.addWidget(label_title)
            card_layout.addWidget(label_value)
            card_layout.addStretch()

            card.setLayout(card_layout)
            grid.addWidget(card, row, col)

        main_layout.addLayout(grid)
        main_layout.addStretch()
        self.setLayout(main_layout)