#Basado en https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/15139798#overview
#muestra el contenido de los <li> de un html eliminando las etiquetas html

def main():
    web = open('web.html','r') #abrimos el archivo descargardo web.html en solo lectura
    inicio = '<li>'
    final = '</li>'
    for l in web.readlines():
        if inicio in l:
            if not "a href=" in l:
                inicio = l.find(inicio) #find devuleve un entero con la posicion dentro de la cadena donde se encuentra el elemento buscado
                ini = ini + len(inicio)
                fin = l.find(final)
                print(l[ini:fin])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
