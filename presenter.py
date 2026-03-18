class Presenter:
    def __init__(self, view, model):
        self.vista = view
        self.modelo = model

        # Conectamos las señales (Fíjate que los nombres coincidan con ui_calculadora)
        self.vista.btsuma.clicked.connect(self.fsuma)
        self.vista.btresta.clicked.connect(self.fresta)
        self.vista.btmulti.clicked.connect(self.fmult)
        self.vista.btdivi.clicked.connect(self.fdiv)
        self.vista.btsalida.clicked.connect(self.vista.close)

    def fsuma(self):
        self._operar(self.modelo.suma)

    def fresta(self):
        self._operar(self.modelo.resta)

    def fmult(self):
        self._operar(self.modelo.multiplicacion)

    def fdiv(self):
        self._operar(self.modelo.division)

    def _operar(self, funcion_logica):
        """Función auxiliar para no repetir código."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = funcion_logica(v1, v2)
            self.vista.salida(resultado)
        except ValueError:
            self.vista.mensaje('Error', 'Introduce números válidos')
        except Exception as e:
            self.vista.mensaje('Error', str(e))