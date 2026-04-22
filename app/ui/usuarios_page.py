from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from app.services.usuarios_service import UsuariosService


class UsuariosPage(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()

        titulo = QLabel("Gestión de usuarios")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(titulo)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        usuarios = UsuariosService.listar_usuarios()

        columnas = ["ID", "Nombre", "Apellido", "Correo", "Teléfono", "Activo"]
        self.table.setColumnCount(len(columnas))
        self.table.setHorizontalHeaderLabels(columnas)
        self.table.setRowCount(len(usuarios))

        for row, usuario in enumerate(usuarios):
            self.table.setItem(row, 0, QTableWidgetItem(str(usuario["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(str(usuario["nom"] or "")))
            self.table.setItem(row, 2, QTableWidgetItem(str(usuario["ape"] or "")))
            self.table.setItem(row, 3, QTableWidgetItem(str(usuario["email"] or "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(usuario["tel"] or "")))
            self.table.setItem(row, 5, QTableWidgetItem("Sí" if usuario["is_active"] else "No"))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)