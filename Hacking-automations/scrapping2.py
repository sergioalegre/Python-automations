#Basado en https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/15139802#overview
#muestra el contenido de los <li> de un html eliminando las etiquetas html

def title():
    files = open('web.html','r')
    inicio='<title>'
    fin='</title>'

    for l in files.readlines():
        if inicio in l:
            p = l.find(inicio)
            print(l[p+len(inicio):-len(final)-1])

def main():
    title()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
