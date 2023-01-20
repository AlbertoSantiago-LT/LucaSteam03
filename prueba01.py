
"""
import unittest
import functions

class TestAltaJuego(unittest.TestCase):
    def test_alta_juego(self):
        #preparación
        nombre_juego = "Super Mario"
        plataforma = "Nintendo Switch"
        anio = 2020
        genero = "Plataforma"
        empresa = "Nintendo"
        ventas_na = 10
        ventas_eu = 8
        ventas_jp = 7
        otras_ventas = 5
        ventas_globales = 30

        #acción
        result = functions.alta_juego(nombre_juego, plataforma, anio, genero, empresa, ventas_na, ventas_eu, ventas_jp, otras_ventas, ventas_globales)
        
        #afirmación
        self.assertEqual(result, "Alta juego")
"""


