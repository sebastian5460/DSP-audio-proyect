#------------------excepciones---------------
def sumar_d():
    while True:
        try:
            a=int(input("dame el primer número: \n"))
            b=int(input("dame el segundo número: \n"))
            res=a+b
        except:
            print("te pedí un número, vuelve a intentarlo")
        else:
            break
        finally:
            print("esto va siempre, ejemplo: manejo finalizado")
    return res

print(f"el resultado es {sumar_d()}")