"""
Basado en https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050318#overview

instalar nmap en el ordenador y luego el modulo para python:
    pip install python-nmap
    import nmap

listar las clases de este modulo
    dir(nmap)

entre los objetos vemos uno llamado PortScanner()
    nuevo_objeto = nmap.PortScanner()

"""

#!/usr/bin/env python
#_*_ coding: utf8 _*_

import nmap

def main():
    nm = nmap.PortScanner()
    ip_objetivo = raw_input("Cual es la IP objetivo:") #pedimos la ip objetivo al usuario
    nm.scan(hosts=ip_objetivo, arguments="--top-ports 1000 -sV --version-intensity 3") #argunmentos son los de nmap
    print("Comando ejecutado: {}".format(nm.command_line()))
    print(nm.scaninfo())
    print("Protocolos utilizados: {}".format(nm[ip_objetivo].all_protocols()))
    print("Estado de la maquina: {}".format(nm[ip_objetivo].state())) #saber si estaba encendida o apagada
    print(nm[ip_objetivo]['tcp'])
    for puerto in nm[ip_objetivo]['tcp'].keys():
        for data in nm[ip_objetivo]['tcp'][puerto]:
            print(data + " : " + nm[ip]['tcp'][puerto][data])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()