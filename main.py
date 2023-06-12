from moduloTelnet import generarArchivo
from moduloFTP import *

def elegirDispositivo():
    print("\n 1) RCPlive-1")
    print("\n 2) RCPlive-2")
    opc = input("Elige un dispositivo ")
    if (opc == '1'):
        opc = "30.30.30.1"
    if (opc == '2'):
        opc = "192.168.1.2"
    return opc
opc = ""

while (opc != 'c'):
    opc = ""
    print("1) Generar la configuración de un dispositivo de manera remota.")
    print("2) Extraer el archivo de configuración de un dispositivo a otro.")
    print("3) Importar la configuración desde un dispositivo a otro\n")
    print("Para SALIR preciona \"c\" \n \n")
    opc = input("Elige una de las opciones anteriores: ")

    if(opc == '1'):
        print("\t =GENERACION DE ARCHIVO REMOTO=")
        generarArchivo(elegirDispositivo())
        print("\n .: ARCHIVO GENERADO :. \n")
    else:
        if (opc == '2'):
            print("\t =EXTRAER ARCHIVO DE CONFIGURACION")
            extraerArchivo(elegirDispositivo(), input("Nombre del archivo: "))
            print("\n .: ARCHIVO EXTRAIDO :. \n")
        else:
            if (opc == '3'):
                print("\t =IMPORTAR LA CONFIGURACION=")
                enviarArchivo(elegirDispositivo())
                print("\n .: ARCHIVO IMPORTADO :. \n")
            else:
                if (opc == 'c'):
                    break
                else:
                    print("OPCION NO VALIDA")
