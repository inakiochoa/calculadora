import sys
from PySide6 import QtWidgets
from PantallaCalculadora import Pantalla
from presenter import Presenter


# Supongamos que tu lógica se llama LogicaCalculadora
# from logica import LogicaCalculadora

class ModeloTemporal:
    """Si aún no tienes el código de lógica, esto te sirve para probar."""

    def suma(self, a, b): return a + b

    def resta(self, a, b): return a - b

    def multiplicacion(self, a, b): return a * b

    def division(self, a, b): return a / b if b != 0 else "Error Div/0"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    vista = Pantalla()
    modelo = ModeloTemporal()  # Aquí pondrás tu clase de lógica real
    presentador = Presenter(vista, modelo)

    vista.show()
    sys.exit(app.exec())