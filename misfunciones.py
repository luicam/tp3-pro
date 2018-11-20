from sys import argv


def comprobarEdad(nombre):
  with open(argv[1], "r") as f:
      for line in f:  
        campos = line.strip().split('#')
        if campos[0] == nombre:
          return campos[1]
