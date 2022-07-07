from distutils import extension
from importlib.resources import path
import os
import shutil

print("\n\nPRO-C102: SEPARACIÓN AUTOMATIZADA DE ARCHIVOS\n\n〔ఠﭛ ఠ〕👍\n\nNote: VSC acepta rutas con “ / “.\n\n")

from_dir = input("¿Cual es La ruta de origen?: ")
to_dir = input("¿Cual es La ruta de destino?: ")

list_of_files = os.listdir(from_dir)
#print("\n\n"+list_of_files)

for file_name in list_of_files:
    name, extension = os.splitext(file_name)
    print("Name: "+name)
    print("Extension: "+extension)
    print("\n")
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', 'pdf']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+"Archivos_Documentos"
        path3 = to_dir+'/'+"Archivos_Documentos"+file_name
        if os.path.exists(path2):
            print("Moviendo: "+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moviendo: "+file_name+"...")
            shutil.move(path1,path3)