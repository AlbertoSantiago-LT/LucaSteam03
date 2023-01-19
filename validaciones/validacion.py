def is_numero_positivo(texto):
    validar=0
    while validar == 0:
        try:
            numero = int(input(texto))
            if numero < 0:
                raise ValueError
            return numero
        except ValueError:
            print("Tiene que ser un número positivo")