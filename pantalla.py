import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from logica import CalculadoraLogica


class CalculadoraGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora PySide6")
        self.setFixedSize(300, 400)

        self.cerebro = CalculadoraLogica()

        self.operacion_actual = ""
        self.valor_anterior = 0

        self.configurar_interfaz()

    def configurar_interfaz(self):
        widget_central = QWidget()
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        self.pantalla = QLineEdit()
        self.pantalla.setReadOnly(True)
        self.pantalla.setStyleSheet("font-size: 30px; padding: 10px; text-align: right;")
        layout_principal.addWidget(self.pantalla)

        layout_botones = QGridLayout()

        botones = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for texto, fila, columna in botones:
            boton = QPushButton(texto)
            boton.setFixedSize(60, 60)
            boton.setStyleSheet("font-size: 20px; font-weight: bold;")

            boton.clicked.connect(lambda checked, t=texto: self.boton_presionado(t))

            layout_botones.addWidget(boton, fila, columna)

        layout_principal.addLayout(layout_botones)

    def boton_presionado(self, texto):
        """Esta función decide qué hacer cuando se pulsa cualquier botón"""

        if texto in '0123456789':
            self.pantalla.setText(self.pantalla.text() + texto)

        elif texto == 'C':
            self.pantalla.clear()
            self.operacion_actual = ""
            self.valor_anterior = 0

        elif texto in ['+', '-', '*', '/']:
            if self.pantalla.text():
                self.valor_anterior = float(self.pantalla.text())
                self.operacion_actual = texto
                self.pantalla.clear()

        elif texto == '=':
            if self.pantalla.text() and self.operacion_actual:
                valor_actual = float(self.pantalla.text())
                resultado = 0

                if self.operacion_actual == '+':
                    resultado = self.cerebro.sumar(self.valor_anterior, valor_actual)
                elif self.operacion_actual == '-':
                    resultado = self.cerebro.restar(self.valor_anterior, valor_actual)
                elif self.operacion_actual == '*':
                    resultado = self.cerebro.multiplicar(self.valor_anterior, valor_actual)
                elif self.operacion_actual == '/':
                    resultado = self.cerebro.dividir(self.valor_anterior, valor_actual)

                self.pantalla.setText(str(resultado))
                self.operacion_actual = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraGUI()
    ventana.show()
    sys.exit(app.exec())