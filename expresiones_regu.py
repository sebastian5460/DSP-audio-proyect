import re

texto='''hola esta2596. ab es. la cane1
dfgdfgsdfg1. lineabb
tercera16565. lineabbb'''

#res=re.search("linea",texto) #encuentra una coicidencia, devuelve una tupla con las posiciones
#res_todas=re.findall("df",texto) #encuentra todas las coincidencias, devuelve una lista o tupla con todas las veces que la encuentra
#res_digitos=re.findall(r"\d",texto) #encuentra en el texto los decimales, cuando pongo la D mayuscula saca todos menos los decimales(como invertir el método)
#res_alfanumeri=re.findall(r"\w",texto) #encuentra lso alfanumericos[a-z A-Z 0-9 _] y con \W encuentra todos menos lso alfanumericos
#reemplanzado \s en \w muestras espacios en blanco y saltos del linea
#res=re.findall(r"\d{4}\.\s",texto) #encuentra varias cosas juntas y consecutivas
#res_rango=re.findall(r"\d{0,4}\.\s",texto) #encuentra coincidencias según un rango (puedo cumplirque tenga 0 o hasta 4 numeros)
#res_inicio_text=re.findall(f"^ter",texto,flags=re.M) #devuelve los carasteres que le pasas si están al inicio de el texto, el flags=re.M es para que sea multilinea
#res_final_text=re.findall(f"linea$",texto, flags=re.M) #devuelve los caracteres que le apsa si lo encuentra al final de una lina, los devuelve la cantidad de veces que lo encuentre


#res_raro=re.findall(r'ab{1,3}|Hola',texto) #encuentra a con una, dos o tres b seguidas, tambien devulve hola

#print(res_inicio_text)
#------------------------------------------------------------nuevo-----------------------------------------------------------
text='''la fecha es 95/29/5895 el numero 555-666-999'''

remplazo="no se puede mostrar"
nueva=re.sub(r"\d{2}/\d{2}/\d{4}",remplazo,text) #reemplazar un dato degún una secuencia específica

print(nueva)

#----------------------el ultimo---------------------------------------------


