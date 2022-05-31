[#Upload_file_to_Azure.py](#Upload_file_to_Azure.py)

[#Azure_location.csv](#Azure_location.csv)

[#requirements.txt](#requirements.txt)

[#comma_colon_convert.py](#comma_colon_convert.py)

[#Task_Scheduler_Windows](#Task_Scheduler_Windows)


### Upload_file_to_Azure.py
  - aaa

### Azure_location.csv
  - CSV con la lista de path de origen y destinos

### requirements.txt
  - dependencias de la aplicación

### comma_colon_convert.py
  - convierte de ',' a ';'

### Task_Scheduler_Windows
  - En el inicio del server y cada 5 minutos hay dos tareas programadas cada una arranca cada uno de los 2 .py con la Action: **"C:\Program Files\Python39\python.exe" comma_colon_convert.py**
  - Los .py tienen un bucle infinito para que el programa no acabe, pero en caso el server se reinicie o el script falle, el task scheduler lo pondria a funcionar de nuevo
