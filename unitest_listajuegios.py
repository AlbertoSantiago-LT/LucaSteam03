import unittest
import pandas as pd
import functions as f

class TestsLucaSteam03(unittest.TestCase):
    
    # def test_listado_nintendo(self):
    #     data = pd.DataFrame()
    #     data = f.listado_nintendo()
    #     self.assertTrue("Nintendo" in data["Publisher"].values)
        
    def test_listado_plataforma(self):
        data = pd.DataFrame()
        data = f.listado_plataforma()
        self.assertTrue("Platform" in data["Genre"].values)
                   

if __name__ == '__main__' : unittest.main()