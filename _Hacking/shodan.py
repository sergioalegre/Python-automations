#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050308#overview
#usar el buscador Shodan

import sys
from shodan import shodan
reload(sys)
sys.setdefaultencoding('utf8')
key=< key api de nuestro perfil en shodan>

motor = Shodan(key)
try:
    query = motor.search("struts")
    print("Total de resultados: {}".format(query['total']))
    for host in query['matches']:
        print("IP: {}".format(host['ip_str']))
        print("Puerto: {}".format(host['port']))
        print("Organizacion: {}".format(host['org']))
        try:
            print("ASN: {}".format(host['asn']))
        except:
            pass
        for i in host['location']:
            print(i + " : " + str(host['location'][i]))

except:
    print("Ocurrio un error")

#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/13831390#overview
#escaneo de un host especifico ip.ip.ip.ip

import sys
from shodan import shodan
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    api = Shodan('key api de nuestro perfil en shodan')
    host= api.host('ip.ip.ip.ip')
    print('''
        direccion: {}
        ciudad: {}
        ISP: {}
        org: {}
        puertos: {}
    '''.format(host['ip_str'],host['city'],host['isp'],host['org'],host['ports']))

    file = open('escaneo.txt','a+') #si no existe este fichero que lo cree y le añada contenido

    for elemento in host['data']:
        lista = elemento.keys()
        for l in elemento:
            print(str(elemento[l]))
    
    file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/13831404#overview

import sys
from shodan import shodan
import argparse
reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query',help="Busqueda")
parser.add_argument('-a','--api',help="Tu API key")
parser = parser.parse_args()

def main()
    if parser.query: #si el usuario ha introducido algo
        if parser.api:
            api = Shodan.(parser.api)
            try:
                resultados=api.search(parser.query)
                print("Total de objetivos: {}".format(resultados['total'])) #cuantos resultados nos devuelve esta consulta
                for i in resultados['matches']:
                    print("Target: {}".format(i['ip_str']))
            except:
                print("Error en la consulta")
        else:
            print("Introduce tu API key")
    else:
        print("introduce busqueda")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
