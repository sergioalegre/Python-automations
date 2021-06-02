#Basado https://www.youtube.com/watch?v=FX9lrNUjhlA&list=PLlb2ZjHtNkpiSbrOfeRASNsvpHD6bEWoA&index=2 minuto 3
#cada OS suele tener un TTL y basado en esto el programa detectara el OS

#!/usr/bin/python

import subprocess, re, sys #subprocess para hacer ping, re para expresiones regulares, sys para que el programa maneje argumentos

def return_ttl(direccion_ip_a_escanear): #funcion que:
        proc = subprocess.Popen(["ping -c 1 %s" % direccion_ip_a_escanear, ""], stdout=subprocess.PIPE, shell=True) #definir ping
        (out,err) = proc.communicate() #lanzar el ping y separamos el output de los errores
        out = out.split() #esta sera la salida del ping con mucha informacion
        out = re.findall(r"\d{1,3}",out[12]) #nos quedamos solo con el valor del campo 12 que es el del TTL y con expresiones regulares nos quedamos solo con el numero de TTL
        return out[0] #es una lista, devolvemos el primer elemento

def return_ttl_os_name(ttl_number):
        if ttl_number >= 0 and ttl_number <=64:
                return "Linux"
        elif ttl_number >=65 and ttl_number <=128:
                return "Windows"
        else:
                return "OS desconocido"



if len(sys.argv) !=2: #si no hay dos parametros le recordamos como usar este programa
        print "\n[*] Uso: python " + sys.argv[0] + " <ip-address>\n"
        sys.exit(1) #salir con estado 1 es como decir que termino de manera anomala


if __name__ == '__main__': #esto lo ejecutara si los parametros estan bien
        direccion_ip_a_escanear = sys.argv[1]
        print direccion_ip_a_escanear
        ttl = return_ttl(direccion_ip_a_escanear)

        try:
                print "\n%s -> %s" % (direccion_ip_a_escanear, return_ttl_os_name(int(ttl)))
        except:
                pass
