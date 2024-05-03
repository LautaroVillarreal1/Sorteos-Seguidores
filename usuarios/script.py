import csv
import time
import pyautogui as pg
x="lauutarov"

#el link de abajo es la extencion que debes usar. Con eso descargas el archivo necesario, metelo en la carpeta de este script
'https://chromewebstore.google.com/detail/igexporter-ig-follower-ex/chmicphoaiifenjibjabgnhpilccfilo'

#aca abajo el archivo que acabas de descargar(IGExporter-usuario-xx-followers). Si no esta dentro de la carpeta no va a funcionar.
archivoCsv = 'IGExporter-lauutarov-234-followers.csv'


#agrega a todos los usuarios del archivo a una lista.
with open(archivoCsv, 'r', encoding='utf-8') as archivo:
    lectorCsv = csv.reader(archivo)
    listaUsuarios=[]
    for fila in lectorCsv:
        nombreDeUsuario = fila[1].strip('""')
        UsuarioInstagram=(nombreDeUsuario)
        listaUsuarios.append(UsuarioInstagram)


#nombre del archivo con los seguidores
nombreArchivo = "UsuariosInstagram.csv"

#crea el archivo con los seguidores 
with open(nombreArchivo, "w") as archivo:
    for elemento in listaUsuarios:
        archivo.write(elemento + "\n")
    archivo.write(x)     
time.sleep(3)#(3 segundos) agregar mas si son muchos(+300) ususarios o pc lenta



#Cuenta la cantidad de usuarios
elementos=[]
with open('UsuariosInstagram.csv', newline='') as archivoCsv:
    lectorCsv = csv.reader(archivoCsv)  
    for fila in lectorCsv:
        elementos.append(fila[0])
        cantidad=len(elementos)
        
        
#recorre linea a linea, e imprime el usuario con @ #Llamar la funcion una vez creado el archivo
#etiquetado comenzara a funcionar luego de 5 segundos, si se necesita mas se aumenta el time.sleep()
def etiquetado():
    time.sleep(5)        
    indice=1
    while indice<=cantidad:
        personas=elementos[indice] 
        pg.hotkey('ctrl', 'alt', 'q')#si tu teclado no pone @ con esas teclas, cambialo.
        pg.write(personas)
        pg.press('enter')
        indice+=1
        time.sleep(60)#no cambiar esto, intagram solo deja hacer 60 comentarios por hora
    pg.alert("Terminó")
etiquetado()



