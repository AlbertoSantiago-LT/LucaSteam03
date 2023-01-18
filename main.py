import pandas as pd
import functions

data = pd.read_csv("vgsales.csv")
print(type(data))

print(functions.alta_juego(data))
    