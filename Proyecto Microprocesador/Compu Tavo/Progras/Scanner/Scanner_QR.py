# Importamos librerias para lecturas
import cv2
from pyzbar.pyzbar import decode
from Clases import *

def lectura_Inicial():
    global lista_Suministro1

    lista_Suministro1 = []
    contador_R_Suministro = 0
    contador_G_Suministro = 0
    contador_B_Suministro = 0
    
    # Ciclo para recorrer la zona de suministro.
    pos_actual = 0
    while (pos_actual < 25):
        #Mover motores a pos_actual del suministro

        color = leer_QR()
        caja = Suministro(0,0,color,True)
        if (color == "L"):
            caja.ocupada = False
        
        elif (color == "R"):
            contador_R_Suministro += 1
        
        elif (color == "G"):
            contador_G_Suministro += 1

        elif (color == "B"):
            contador_B_Suministro += 1
        
        lista_Suministro1.append(caja)

        """#Suena las alarmas
        #Alarma 1
        if (contador_R_Suministro < contador_R_Carga):
            #Llama a la función de alarma 1
        if (contador_G_Suministro < contador_G_Carga):
            #Llama a la función de alarma 1
        if (contador_B_Suministro < contador_B_Carga):
            #Llama a la función de alarma 1
        
        #Alarma 2
        if (contador_R_Suministro > contador_R_Carga):
            #Llama a la función de alarma 2
        if (contador_G_Suministro > contador_G_Carga):
            #Llama a la función de alarma 2
        if (contador_B_Suministro > contador_B_Carga):
            #Llama a la función de alarma 2"""

        pos_actual += 1
    
        print("SUMINISTRO")
        b= []
        for pos,elem in enumerate(lista_Suministro1):
            a = elem.color
            if elem.ocupada == False:
                a = "-"
            print(pos, "      ",a)
    # Ciclo para recorrer la zona de carga.
    """pos_actual = 0
    while (pos_actual < 25):
        #Mover motores a pos_actual de la Carga

        color = leer_QR()
        if (color != "V"):
            #Llama a la función de alarma 3

        pos_actual += 1"""


def leer_QR():
    # Creamos la videocaptura
    cap = cv2.VideoCapture(0)
    leyo = False

    # Empezamos
    while True:
        # Leemos los frames
        ret, frame = cap.read()

        # Leemos los codigos QR
        for codes in decode(frame):
            # Decodidficamos
            info = codes.data.decode("utf-8") # En código ASCII

            # Tipo de caja, LETRA en ASCII
            tipo = info[0:2]
            tipo = int(tipo)

            #Formato para los códigos:
            #Caja Roja: 82
            if tipo == 82:  # R->82, RED
                color = "R"
                leyo = True
                break

            #Formato para los códigos:
            #Caja Verde: 71
            if tipo == 71:  # G->71, GREEN
                color = "G"
                leyo = True
                break
            
            #Formato para los códigos:
            #Caja Azul: 66
            if tipo == 66:  # B->66, BLUE
                color = "B"
                leyo = True
                break

            #Formato para los códigos:
            #Espacio Libre: 76
            if tipo == 76:  # L->76, Espacio Libre
                color = "L"
                leyo = True
                break
        if (leyo == True):
            break
        
    cv2.destroyAllWindows()
    cap.release()

    return (color)


lectura_Inicial()
