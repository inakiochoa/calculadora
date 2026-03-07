# Probando mi feature
class CalculadoraLogica:
    def __init__(self):
        # Aquí podríamos guardar historial en el futuro
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por 0"
        return a / b

# --- BLOQUE DE PRUEBAS ---
# Esto solo se ejecuta si le das al Play en este archivo,
# pero no molestará cuando lo importes en la interfaz.
if __name__ == "__main__":
    calc = CalculadoraLogica()
    print("Probando suma (5 + 3):", calc.sumar(5, 3))
    print("Probando resta (10 - 4):", calc.restar(10, 4))
    print("Probando división por cero:", calc.dividir(5, 0))