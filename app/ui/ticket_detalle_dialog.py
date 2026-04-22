from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QFrame, QPushButton,
    QGridLayout
)


class TicketDetalleDialog(QDialog):
    def __init__(self, ticket, parent=None):
        super().__init__(parent)
        self.ticket = ticket
        self.setWindowTitle(f"Detalle del ticket #{ticket['cod']}")
        self.setMinimumWidth(650)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        titulo = QLabel(f"Detalle del ticket #{self.ticket['cod']}")
        titulo.setObjectName("pageTitle")
        layout.addWidget(titulo)

        card = QFrame()
        card.setObjectName("card")

        grid = QGridLayout()
        grid.setContentsMargins(18, 18, 18, 18)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(12)

        usuario = f"{self.ticket['usuario_nombre'] or ''} {self.ticket['usuario_apellido'] or ''}".strip()
        soporte = f"{self.ticket['soporte_nombre'] or ''} {self.ticket['soporte_apellido'] or ''}".strip()

        datos = [
            ("Código", self.ticket["cod"]),
            ("Usuario", usuario or "N/A"),
            ("Fecha creación", self.ticket["feccre"] or ""),
            ("Fecha proceso", self.ticket["fecpro"] or ""),
            ("Fecha cierre", self.ticket["feccie"] or ""),
            ("Estado", self.ticket["estado"] or ""),
            ("Prioridad", self.ticket["prioridad"] or ""),
            ("Asunto", self.ticket["asu"] or ""),
            ("Descripción", self.ticket["des"] or ""),
            ("Respuesta", self.ticket["res"] or ""),
            ("Soporte asignado", soporte or "N/A"),
            ("Reserva relacionada", self.ticket["codres"] or "N/A"),
        ]

        for i, (label_text, value) in enumerate(datos):
            label = QLabel(f"{label_text}:")
            label.setStyleSheet("font-weight: bold;")
            valor = QLabel(str(value))
            valor.setWordWrap(True)

            grid.addWidget(label, i, 0)
            grid.addWidget(valor, i, 1)

        card.setLayout(grid)
        layout.addWidget(card)

        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.close)
        layout.addWidget(btn_cerrar)

        self.setLayout(layout)