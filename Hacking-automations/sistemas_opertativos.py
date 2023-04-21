#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050260#overview
import os

#ruta actual
print("Ruta actual: " + os.getcwd())

#cambair de directorio
os.chdir("C:\TEMP")

#hacer un dir
print(os.listdir(os.getcwd()))

#hacer un directorio
os.mkdir("carpeta_neuva")

#borrar un directorio
os.rmdir("carpeta_neuva")

#renombrar fichero
os.rename('nombre_antiguo.txt', 'nombre_nuevo.txt')

#estadisticas de fichero
print(os.stat(fichero.txt))

os.system("ping www.google.es")

#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050276#overview
import subprocess

#evitar que la ejecución evite dar outputs
salida_nula=open(os.devnull,'w') #que abra devnull en escritura
p=subprocess.call(['ping','-c','2','www.google.es'],stdout=salida_nula, stderr=subprocess.STDOUT) #si va bien deberia devolver 0
if p==0:
    print("El comando se ejecuto OK")
else:
    print("El comando fallo")


#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050266#overview
#vamos a ejecutar un sisteminfo en un sistema windows y guardarlo en un fichero
from subprocess import STDOUT, check_output
import subprocess

info_sistema=check_output('systeminfo',stderr=subprocess.STDOUT)
file=open('info.txt','w+')
file.write(info_sistema)
file.close()

#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050284#overview
#crear un gusano autoreplicante
#creara tantas copias de si mismo como el numero que pasemos de parametro

import shutil
import sys

def main():
    if len(sys.argv) == 2:
        for i in range(0,int(sys.argv[1])):
            shutil.copy(sys.argv[0], sys.argv[0]+str(i)+'.py')
    else:
        print("Argumentos insuficientes")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
