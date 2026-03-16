from PySide6 import QtWidgets

# Se importa la clase generada por el comando pyside6-uic
from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):
    """
    Clase básica que carga la interfaz generada por QtDesigner.
    Utiliza herencia múltiple para extender QMainWindow [7], [8].
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    pantalla = Pantalla()
    pantalla.show()
    sys.exit(app.exec())
