from sys import argv
#datos del fichero: nombre#edad#curso#genero#otrosDatos(separador ",")

from misfunciones import comprobarEdad

fe = open(argv[1], "r")
fs = open(argv[2], "w")
linea = fe.readline().strip()
while linea != "":
  palabras = linea.split("#")
  if palabras[1] > 18:
  	edad=comprobarEdad(palabras[0])
  	print(palabras[0]+" no estara en el fichero de salida por que tiene "+str(edad)+" anyos.")
  	fs.write(linea)
  linea = fe.readline().strip()
fe.close()
fs.close()


