import unittest
import pandas as pd
import functions as f

class TestsLucaSteam03(unittest.TestCase):


    # def test_listado_nintendo(self):
    #     data = pd.DataFrame()
    #     data = f.listado_nintendo()
    #     self.assertTrue("Nintendo" in data["Publisher"].values)



    # def test_genero_plataforma(self):
    #     data = pd.DataFrame()
    #     data = f.listado_platforma()
    #     self.assertTrue("Plataform" in data["Genre"].values)

    def test_listado_segun_rango(self):
        data = pd.DataFrame()
        data = f.listado_rango()
        self.assertTrue(data)

if __name__ == '__main__' : unittest.main()