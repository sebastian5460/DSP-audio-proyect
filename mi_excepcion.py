#crenado la propia sxcepcion
class MiExcepcion(Exception):
    def __init__(self, error):
        print(f"el error es: {error}")
#manejando la excepcion
try:
    #así la lanzaría para que saltara el error
    raise MiExcepcion("Está mal!")
except:
    print("acá estamos manejando lo que sale mal")
    