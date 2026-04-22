from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView, QPushButton,
    QAbstractItemView
)
from app.services.vehiculos_service import VehiculosService


class VehiculoReservasDialog(QDialog):
    def __init__(self, vehiculo, parent=None):
        super().__init__(parent)
        self.vehiculo = vehiculo
        self.setWindowTitle(f"Reservas del vehículo #{vehiculo['cod']}")
        self.setMinimumWidth(950)
        self.setMinimumHeight(500)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        titulo = QLabel(f"Reservas del vehículo #{self.vehiculo['cod']}")
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

        layout.addWidget(self.table)

        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.close)
        layout.addWidget(btn_cerrar)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        reservas = VehiculosService.obtener_reservas_por_vehiculo(self.vehiculo["cod"])

        columnas = [
            "Código", "Usuario", "Email", "Teléfono",
            "Fecha creación", "Fecha inicio", "Fecha fin",
            "Valor", "Estado", "Confirmado"
        ]

        self.table.setColumnCount(len(columnas))
        self.table.setHorizontalHeaderLabels(columnas)
        self.table.setRowCount(len(reservas))

        for row, reserva in enumerate(reservas):
            usuario = f"{reserva['usuario_nombre'] or ''} {reserva['usuario_apellido'] or ''}".strip()

            self.table.setItem(row, 0, QTableWidgetItem(str(reserva["cod"])))
            self.table.setItem(row, 1, QTableWidgetItem(usuario))
            self.table.setItem(row, 2, QTableWidgetItem(str(reserva["email"] or "")))
            self.table.setItem(row, 3, QTableWidgetItem(str(reserva["tel"] or "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(reserva["fecrea"] or "")))
            self.table.setItem(row, 5, QTableWidgetItem(str(reserva["fecini"] or "")))
            self.table.setItem(row, 6, QTableWidgetItem(str(reserva["fecfin"] or "")))
            self.table.setItem(row, 7, QTableWidgetItem(str(reserva["val"] or "")))
            self.table.setItem(row, 8, QTableWidgetItem(str(reserva["estado"] or "")))
            self.table.setItem(
                row,
                9,
                QTableWidgetItem("Sí" if reserva["confirmado_propietario"] else "No")
            )

            self.table.setRowHeight(row, 40)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QHeaderView.ResizeToContents)