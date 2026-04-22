from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QFrame,
    QPushButton, QGridLayout, QMessageBox, QHBoxLayout
)
from app.services.vehiculos_service import VehiculosService
from app.ui.vehiculo_edit_dialog import VehiculoEditDialog


class VehiculoDetalleDialog(QDialog):
    def __init__(self, vehiculo, parent=None):
        super().__init__(parent)
        self.vehiculo = vehiculo
        self.setWindowTitle(f"Detalle del vehículo #{vehiculo['cod']}")
        self.setMinimumWidth(560)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        titulo = QLabel(f"Detalle del vehículo #{self.vehiculo['cod']}")
        titulo.setObjectName("pageTitle")
        layout.addWidget(titulo)

        card = QFrame()
        card.setObjectName("card")

        grid = QGridLayout()
        grid.setContentsMargins(18, 18, 18, 18)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(12)

        usuario = f"{self.vehiculo['usuario_nombre'] or ''} {self.vehiculo['usuario_apellido'] or ''}".strip()

        datos = [
            ("Código", self.vehiculo["cod"]),
            ("Usuario", usuario or "N/A"),
            ("Disponible", "Sí" if self.vehiculo["disp"] else "No"),
            ("Marca", self.vehiculo["marca"] or ""),
            ("Línea", self.vehiculo["linea"] or ""),
            ("Clase", self.vehiculo["clase"] or ""),
            ("Ciudad", self.vehiculo["ciudad"] or ""),
            ("Modelo", self.vehiculo["mod"] or ""),
            ("Color", self.vehiculo["col"] or ""),
            ("Pasajeros", self.vehiculo["pas"] or ""),
            ("Precio renta", self.vehiculo["prerent"] or ""),
            ("VIN", self.vehiculo["vin"] or ""),
            ("Cilindraje", self.vehiculo["cil"] or ""),
            ("Combustible", self.vehiculo["combustible"] or ""),
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

        botones_layout = QHBoxLayout()
        botones_layout.setSpacing(10)

        btn_editar = QPushButton("Editar")
        btn_editar.setStyleSheet("""
            QPushButton {
                background-color: #282828;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3f3f46;
            }
        """)

        btn_eliminar = QPushButton("Eliminar")
        btn_eliminar.setStyleSheet("""
            QPushButton {
                background-color: #B91C1C;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #991B1B;
            }
        """)

        btn_cerrar = QPushButton("Cerrar")

        btn_editar.clicked.connect(self.editar_vehiculo)
        btn_eliminar.clicked.connect(self.eliminar_vehiculo)
        btn_cerrar.clicked.connect(self.reject)

        botones_layout.addWidget(btn_editar)
        botones_layout.addWidget(btn_eliminar)
        botones_layout.addStretch()
        botones_layout.addWidget(btn_cerrar)

        layout.addLayout(botones_layout)
        self.setLayout(layout)

    def editar_vehiculo(self):
        dialog = VehiculoEditDialog(self.vehiculo, self)
        if dialog.exec():
            self.accept()

    def eliminar_vehiculo(self):
        validacion = VehiculosService.validar_eliminacion(self.vehiculo["cod"])

        if not validacion["puede_eliminar"]:
            detalle = []
            if validacion["documentos"] > 0:
                detalle.append(f"- Documentos asociados: {validacion['documentos']}")
            if validacion["reservas"] > 0:
                detalle.append(f"- Reservas asociadas: {validacion['reservas']}")

            QMessageBox.warning(
                self,
                "No se puede eliminar",
                "Este vehículo no se puede eliminar.\n\n"
                + validacion["mensaje"]
                + "\n\n"
                + "\n".join(detalle)
            )
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Estás seguro de eliminar este vehículo?\n\nEsta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                VehiculosService.eliminar_vehiculo(self.vehiculo["cod"])
                QMessageBox.information(self, "Eliminado", "Vehículo eliminado correctamente.")
                self.accept()
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No fue posible eliminar el vehículo.\n\n{e}"
                )