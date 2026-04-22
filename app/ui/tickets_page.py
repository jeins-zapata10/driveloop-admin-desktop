from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView, QPushButton,
    QAbstractItemView
)
from app.services.tickets_service import TicketsService
from app.ui.ticket_detalle_dialog import TicketDetalleDialog


class TicketsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.tickets_data = []
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        titulo = QLabel("Gestión de tickets")
        titulo.setObjectName("pageTitle")
        layout.addWidget(titulo)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setShowGrid(False)
        self.table.setWordWrap(False)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        self.tickets_data = TicketsService.listar_tickets()

        columnas = [
            "Usuario", "Fecha", "Estado", "Prioridad", "Acción"
        ]

        self.table.setColumnCount(len(columnas))
        self.table.setHorizontalHeaderLabels(columnas)
        self.table.setRowCount(len(self.tickets_data))

        for row, ticket in enumerate(self.tickets_data):
            usuario = f"{ticket['usuario_nombre'] or ''} {ticket['usuario_apellido'] or ''}".strip()

            self.table.setItem(row, 0, QTableWidgetItem(usuario))
            self.table.setItem(row, 1, QTableWidgetItem(str(ticket["feccre"] or "")))
            self.table.setItem(row, 2, QTableWidgetItem(str(ticket["estado"] or "")))
            self.table.setItem(row, 3, QTableWidgetItem(str(ticket["prioridad"] or "")))

            btn_detalle = QPushButton("Ver detalle")
            btn_detalle.setMinimumWidth(120)
            btn_detalle.setMaximumWidth(140)
            btn_detalle.setMinimumHeight(34)
            btn_detalle.setStyleSheet("""
                QPushButton {
                    background-color: #C91843;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 6px 12px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #9B1B39;
                }
                QPushButton:pressed {
                    background-color: #870027;
                }
            """)
            btn_detalle.clicked.connect(
                lambda checked=False, t=ticket: self.abrir_detalle(t)
            )

            self.table.setCellWidget(row, 4, btn_detalle)
            self.table.setRowHeight(row, 42)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)           # Usuario
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Fecha
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # Estado
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  # Prioridad
        header.setSectionResizeMode(4, QHeaderView.Fixed)             # Acción

        self.table.setColumnWidth(4, 150)

        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def abrir_detalle(self, ticket):
        dialog = TicketDetalleDialog(ticket, self)
        dialog.exec()