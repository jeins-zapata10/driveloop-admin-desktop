from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QComboBox, QFrame
)
from app.services.vehiculos_service import VehiculosService


class VehiculoEditDialog(QDialog):
    def __init__(self, vehiculo, parent=None):
        super().__init__(parent)
        self.vehiculo = vehiculo
        self.setWindowTitle(f"Editar vehículo #{vehiculo['cod']}")
        self.setMinimumWidth(420)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        titulo = QLabel(f"Editar vehículo #{self.vehiculo['cod']}")
        titulo.setObjectName("pageTitle")
        layout.addWidget(titulo)

        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(18, 18, 18, 18)
        card_layout.setSpacing(12)

        self.input_modelo = QLineEdit(str(self.vehiculo["mod"] or ""))
        self.input_color = QLineEdit(str(self.vehiculo["col"] or ""))
        self.input_pasajeros = QLineEdit(str(self.vehiculo["pas"] or ""))
        self.input_precio = QLineEdit(str(self.vehiculo["prerent"] or ""))

        self.select_disponible = QComboBox()
        self.select_disponible.addItem("Sí", 1)
        self.select_disponible.addItem("No", 0)

        valor_disp = 1 if self.vehiculo["disp"] else 0
        index = self.select_disponible.findData(valor_disp)
        if index != -1:
            self.select_disponible.setCurrentIndex(index)

        card_layout.addWidget(QLabel("Modelo"))
        card_layout.addWidget(self.input_modelo)

        card_layout.addWidget(QLabel("Color"))
        card_layout.addWidget(self.input_color)

        card_layout.addWidget(QLabel("Pasajeros"))
        card_layout.addWidget(self.input_pasajeros)

        card_layout.addWidget(QLabel("Precio renta"))
        card_layout.addWidget(self.input_precio)

        card_layout.addWidget(QLabel("Disponible"))
        card_layout.addWidget(self.select_disponible)

        btn_guardar = QPushButton("Guardar cambios")
        btn_guardar.clicked.connect(self.guardar)

        card_layout.addWidget(btn_guardar)
        card.setLayout(card_layout)

        layout.addWidget(card)
        self.setLayout(layout)

    def guardar(self):
        try:
            modelo = self.input_modelo.text().strip()
            color = self.input_color.text().strip()
            pasajeros = self.input_pasajeros.text().strip()
            precio = self.input_precio.text().strip()
            disponible = self.select_disponible.currentData()

            if not modelo or not color or not pasajeros or not precio:
                QMessageBox.warning(self, "Campos requeridos", "Completa todos los campos.")
                return

            data = {
                "mod": modelo,
                "col": color,
                "pas": int(pasajeros),
                "prerent": float(precio),
                "disp": int(disponible)
            }

            VehiculosService.actualizar_vehiculo(self.vehiculo["cod"], data)

            QMessageBox.information(self, "Éxito", "Vehículo actualizado correctamente.")
            self.accept()

        except ValueError:
            QMessageBox.warning(
                self,
                "Datos inválidos",
                "Pasajeros debe ser número entero y precio debe ser numérico."
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No fue posible actualizar el vehículo.\n\n{e}")