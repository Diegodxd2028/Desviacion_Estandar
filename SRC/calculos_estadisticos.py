import math

class CalculosEstadisticos:

    def calcular_media(self, numeros):
        """Calcula la media de una lista de números"""
        if not numeros:
            return None
        return sum(numeros) / len(numeros)

    def calcular_desviacion_estandar(self, numeros):
        """Calcula la desviación estándar muestral de una lista de números"""
        if not numeros:
            return None

        media = self.calcular_media(numeros)
        # Dividimos por (n-1) en lugar de n para desviación estándar muestral
        varianza = sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1)
        return math.sqrt(varianza)