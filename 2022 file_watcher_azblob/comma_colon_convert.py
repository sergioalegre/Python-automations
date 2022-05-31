import csv, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time

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
            os.rename(path_file,rand_name)
            
        except Exception as e:
            if e.winerror == 32:
                time.sleep(twaiting)
            else:
                is_used = False

def on_created(event):
    secure_waiting(event.src_path)
    reader = csv.reader(open(event.src_path, "r"), delimiter=',')
    _, filename = os.path.split(event.src_path)
    output = "\\\\SERVER\OTRO_PATH\\"+filename
    print(output)
    with open(output, "w", newline="") as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerows(reader)

def run():
    """
    Main process
    :return:
    """
    source = r'\\SERVER\PATH' #Cambiamos al server y path en el que estaremos observando
    # Initialize Event Handler for every source/destination
    observer = Observer()
    my_event_handler = PatternMatchingEventHandler(["*.csv"], None, False, True) #estaremos a la espera en ese path de ficheros .CSV
    # partial_created = functools.partial(on_created, destination=sourcedest[s])
    my_event_handler.on_created = on_created
    observer.schedule(my_event_handler, source, recursive=True)
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

