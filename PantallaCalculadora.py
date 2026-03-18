from PySide6 import QtWidgets

# Se importa la clase generada por el comando pyside6-uic
from ui_calculadora import Ui_Calculadora as form_class


from PySide6 import QtWidgets
from ui_calculadora import Ui_Calculadora as form_class

class Pantalla(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    # --- MÉTODOS PARA EL PRESENTADOR ---
    def entrada(self):
        """Devuelve los valores de los QLineEdit como floats."""
        return float(self.entrada1.text()), float(self.entrada2.text())

    def salida(self, valor):
        """Muestra el resultado en el label."""
        self.resultado.setText(str(valor))

    def mensaje(self, titulo, texto):
        """Muestra un error si algo falla (ej. dividir por cero)."""
        QtWidgets.QMessageBox.critical(self, titulo, texto)

if __name__ == "__main__":
    import sys
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    pantalla = Pantalla()
    pantalla.show()
    sys.exit(app.exec())
