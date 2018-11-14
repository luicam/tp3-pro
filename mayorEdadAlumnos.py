from sys import argv
#datos del fichero: nombre#edad#curso#genero#otrosDatos(separador ",")
fe = open(argv[1], "r")
fs = open(argv[2], "w")
linea = fe.readline().strip()
while linea != "":
  palabras = linea.split("#")
  if palabras[1] > 18:
  	fs.write(line)
  linea = fe.readline().strip()
fe.close()
