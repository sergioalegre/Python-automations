from azure.storage.blob import ContainerClient
import sys, os, traceback
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time, functools
from azure.keyvault.secrets import SecretClient
from azure.identity import CertificateCredential
from datetime import date

today = date.today()

# Initial definitions

tenant_id='0f####a9'
client_id='88####47'
certificate_path ='C:\Certificate\SERVER.pfx'
credential = CertificateCredential(tenant_id=tenant_id, client_id=client_id, certificate_path= certificate_path, password= "1234")

keyVaultName = "kv-####-001" #Azure Key Vault se utiliza para almacenar de forma segura tokens, contraseñas, certificados, claves de API y otros secretos
KVUri = f"https://{keyVaultName}.vault.azure.net"
secretName = "DLS-####-001"

client = SecretClient(vault_url=KVUri, credential=credential)
retrieved_secret = client.get_secret(secretName)

url = "https://STORAGEACCOUNT.blob.core.windows.net/CONTAINER" # cambiar el storage account y el container name
token = retrieved_secret.value
container_client = ContainerClient.from_container_url(
    container_url=url,
    credential=token
)

def secure_waiting(path_file, twaiting = 0.1):
    """
    waits while some file is opened by other process
    :param path_file:
    :param twaiting:
    :return:
    """
    # Let's wait while opened..
    rand_name= str(time.time_ns()) + '.tmp'
    is_used = True
    while is_used:
        try:
            #print(path_file)
            os.rename(path_file,rand_name)
            
        except Exception as e:
            if e.winerror == 32:
                #print('File {} is opened by other process'.format(path_file))
                time.sleep(twaiting)
            else:
                #print(e)
                is_used = False
    # redo to the initial name
    # os.rename(rand_name, path_file)

def on_created(event, destination):
    start1 = time.time()
    # let's wait while this file is opened by other process
    secure_waiting(event.src_path)
    #time.sleep(2)
    duration1 = time.time() - start1

    start2 = time.time()
    #Upload file
    p, filename = os.path.split(event.src_path)
    try:
        if os.path.isfile(event.src_path):
            bob = container_client.get_blob_client(destination+filename)

            with open(event.src_path, "rb") as data:
                bob.upload_blob(data,overwrite=True)
        else:
            print("File not Found -> {}".format(event.src_path))
            with open("Error_log.txt", 'a') as missingfile:
                missingfile.write(str("File is missing ---" + filename.lstrip()+';' + p.split('\\')[-1])+" at "+str(time.strftime("%I %M %p",time.localtime(time.time())))+ " on " + str(today)+ "\n")
            return
    except FileNotFoundError as error:
        print("File not Found in {}".format(destination))
        with open("Error_log.txt", 'a') as filenotfound:
            filenotfound.write(str("File not Found in {}".format(destination))+" at "+str(time.strftime("%I %M %p",time.localtime(time.time())))+ " on " + str(today) +"\n")
        return
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        with open("Error_log.txt", 'a') as exception:
            exception.write(str(traceback.print_exception(type(ex), ex, ex.__traceback__))+" at "+time.strftime("%I %M %p",time.localtime(time.time()))+ " on " + str(today)+"\n")
            exception.write(str(ex)+"\n")
        return

    duration2 = time.time() - start2
    print(filename.lstrip()+ ' from: ' + p.split('\\')[-1] + ' --- Uploaded to: ' + destination.split('/')[-2] +' at '+ str(time.strftime("%H:%M:%S", time.localtime()))+ " on " + str(today))
    #with open("Error_log.txt", 'a') as log:
     #   log.write(str(filename.lstrip()+ ' from: ' + p.split('\\')[-1] + ' --- Uploaded to: ' + destination.split('/')[-2] +' at '+ str(time.strftime("%I %M %p",time.localtime(time.time())))+ " on " + str(today)+"\n"))

    print("Waiting time : " +str(duration1)+"    and     Upload time : --- %s seconds" % duration2)
    #with open("times_AZ.txt", 'a') as timesfile:
     #   timesfile.write(str(duration2)+"\n")

def load_paths():
    """
    Loads the paths
    :return:
    """
    if len(sys.argv) < 2:
        path = "Azure_location.csv" #carga desde un csv la lista de origen/destino
    else:
        path = sys.argv[1]
    # read source destination paths
    sourcedest = {}
    with open(path) as f:
        for l in f.readlines():
            sourcedest[l.split(';')[0].strip()] = l.split(';')[1].strip()
    return sourcedest


def run():
    """
    Main process
    :return:
    """
    sourcedest = load_paths() #carga desde un csv la lista de origen/destino

    # Initialize Event Handler for every source/destination
    observer = Observer()
    for s in sourcedest:
        my_event_handler = PatternMatchingEventHandler(["*"], None, False, True)
        partial_created = functools.partial(on_created, destination=sourcedest[s])
        my_event_handler.on_created = partial_created
        observer.schedule(my_event_handler, s, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Connection ended well")
    observer.join()


if __name__ == '__main__':
    run()
