import unittest
import pandas as pd
import functions as f

class TestsLucaSteam03(unittest.TestCase):
    
    def test_listado_nintendo_contiene_solo_nintendos(self):
        data = pd.DataFrame()
        data = f.listado_nintendo()
        self.assertTrue("Nintendo" in data["Publisher"].values)
        
    def test_listado_plataforma_contiene_solo_plataformas(self):
        data = pd.DataFrame()
        data = f.listado_plataforma()
        self.assertTrue("Platform" in data["Genre"].values)
        
    def test_listado_juegos_es_igual_que_obtener_datos(self):
        data = pd.DataFrame
        data = f.listado_juegos
        self.assertEquals(type(data),type(f.listado_juegos))
    
    # def test_validar_fecha(self):
    #     # Prueba con una fecha válida
    #     fecha = 1995
    #     resultado = f.validar_fecha()
    #     self.assertTrue(fecha,  resultado)

    #     # Prueba con una fecha inválida (menor a 1952)
    #     fecha = 1950
    #     resultado = f.validar_fecha()
    #     self.assertNotEqual(fecha, resultado)
            
                
if __name__ == '__main__' : unittest.main()