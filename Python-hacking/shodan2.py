#Basado en https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/13831404#overview
# Buscar dispositivos conectados a internet mediante Shodan, permitiendo busquedas personalizadas del usuario
# si ejecuamos con "python shodan2.py -h" nos saldra la ayuda que sale por defecto con argparse
# ejemplo de ejecucion: python shodan2.py -q webcams -a MIAPIKEY

#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan
import argparse

reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query',help="Busqueda") #permitimos este parametro a nuestro programa
parser.add_argument('-a','--api',help="Tu api") #permitimos este parametro a nuestro programa
parser = parser.parse_args()

def main():
	if parser.query: #nos aaseguramos tengamos este parametro obligatorio
		if parser.api: #nos aaseguramos tengamos este parametro obligatorio
			
			api = Shodan(parser.api)

			try:
				resultados_busqueda = api.search(parser.query)
				print("Total de objetivos: {}".format(resultados_busqueda['total']))
				for i in resultados_busqueda['matches']:
					print("Target encontrado: {}".format(i['ip_str']))
			except:
				print("Error en la consulta")

		else: #si no han puesto este paramtro obligatorio
			print("Introduce tu api key")
	else: #si no han puesto este paramtro obligatorio
		print("Introduce un caractar de Busqueda") 

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()