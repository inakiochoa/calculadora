class Presenter:
    """Actúa como puente entre la lógica y la interfaz [19]."""

    def __init__(self, view, model):
        # Agregación: recibe instancias externas
        self.vista = view
        self.modelo = model

        # Suscripción a las señales de la vista [21], [20]
        self.vista.btnsuma.connect(self.fsuma)
        # TODO: Conectar el resto de señales (btnresta, etc.)

    def fsuma(self):
        """Flujo de la operación suma [20, 22]."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.suma(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    # TODO: Implementar fresta(), fmult() y fdiv() [23], [22]