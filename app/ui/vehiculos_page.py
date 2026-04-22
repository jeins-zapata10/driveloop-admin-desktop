from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView, QPushButton,
    QAbstractItemView
)
from app.services.vehiculos_service import VehiculosService
from app.ui.vehiculo_detalle_dialog import VehiculoDetalleDialog
from app.ui.vehiculo_reservas_dialog import VehiculoReservasDialog


class VehiculosPage(QWidget):
    def __init__(self):
        super().__init__()
        self.vehiculos_data = []
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        titulo = QLabel("Gestión de vehículos")
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
        self.vehiculos_data = VehiculosService.listar_vehiculos()

        columnas = [
            "Código",
            "Usuario",
            "Disponible",
            "Marca",
            "Línea",
            "Ciudad",
            "Acción",
            "Reservas"
        ]

        self.table.setColumnCount(len(columnas))
        self.table.setHorizontalHeaderLabels(columnas)
        self.table.setRowCount(len(self.vehiculos_data))

        for row, vehiculo in enumerate(self.vehiculos_data):
            usuario = f"{vehiculo['usuario_nombre'] or ''} {vehiculo['usuario_apellido'] or ''}".strip()

            self.table.setItem(row, 0, QTableWidgetItem(str(vehiculo["cod"])))
            self.table.setItem(row, 1, QTableWidgetItem(usuario))
            self.table.setItem(row, 2, QTableWidgetItem("Sí" if vehiculo["disp"] else "No"))
            self.table.setItem(row, 3, QTableWidgetItem(str(vehiculo["marca"] or "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(vehiculo["linea"] or "")))
            self.table.setItem(row, 5, QTableWidgetItem(str(vehiculo["ciudad"] or "")))

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
                lambda checked=False, v=vehiculo: self.abrir_detalle(v)
            )
            self.table.setCellWidget(row, 6, btn_detalle)

            total_reservas = int(vehiculo.get("total_reservas") or 0)
            reservas_activas = int(vehiculo.get("reservas_activas") or 0)

            if reservas_activas > 0:
                texto_boton = "Ver reservas"
                estilo_boton = """
                    QPushButton {
                        background-color: #282828;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        padding: 6px 12px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #3f3f46;
                    }
                """
            elif total_reservas > 0:
                texto_boton = "FINALIZADAS"
                estilo_boton = """
                    QPushButton {
                        background-color: #6B7280;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        padding: 6px 12px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #4B5563;
                    }
                """
            else:
                texto_boton = "Sin reservas"
                estilo_boton = """
                    QPushButton {
                        background-color: #D1D5DB;
                        color: #111111;
                        border: none;
                        border-radius: 8px;
                        padding: 6px 12px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #C4C9D1;
                    }
                """

            btn_reservas = QPushButton(texto_boton)
            btn_reservas.setMinimumWidth(125)
            btn_reservas.setMaximumWidth(150)
            btn_reservas.setMinimumHeight(34)
            btn_reservas.setStyleSheet(estilo_boton)
            btn_reservas.clicked.connect(
                lambda checked=False, v=vehiculo: self.abrir_reservas(v)
            )

            self.table.setCellWidget(row, 7, btn_reservas)
            self.table.setRowHeight(row, 42)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.Stretch)
        header.setSectionResizeMode(6, QHeaderView.Fixed)
        header.setSectionResizeMode(7, QHeaderView.Fixed)

        self.table.setColumnWidth(6, 150)
        self.table.setColumnWidth(7, 160)

        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def abrir_detalle(self, vehiculo):
        dialog = VehiculoDetalleDialog(vehiculo, self)
        if dialog.exec():
            self.load_data()

    def abrir_reservas(self, vehiculo):
        dialog = VehiculoReservasDialog(vehiculo, self)
        dialog.exec()