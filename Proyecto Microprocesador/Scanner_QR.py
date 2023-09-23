# Importamos librerias para lecturas
import cv2
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

# Creamos la videocaptura
cap = cv2.VideoCapture(0)

listaR_repetidos = []
listaG_repetidos = []
listaB_repetidos = []
lista_Letras_repetidos = []

listaR = []
listaG = []
listaB = []
lista_Letras = []

# Empezamos
while True:
    # Leemos los frames
    ret, frame = cap.read()

    # Leemos los codigos QR
    for codes in decode(frame):
        # Extraemos info
        #info = codes.data

        # Decodidficamos
        info = codes.data.decode("utf-8") # En código ASCII

        # Tipo de caja, LETRA en ASCII
        tipo = info[0:2]
        tipo = int(tipo)

        # Extraemos coordenadas
        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        # Redimensionamos
        pts = pts.reshape((-1,1,2))

        #Formato para los códigos:
        #Caja Roja 01: 8201
        #Caja Roja 12: 8212
        if tipo == 82:  # R->82, RED
            # Dibujamos
            cv2.polylines(frame, [pts], True, (0, 0, 255), 5)
            cv2.putText(frame, "ROJO_" + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print("Caja roja numero", str(info[2:]))

            # Agrega dentro de la lista de cajas azules.
            listaR_repetidos.append(str(info[2:]))
            for elemento in listaR_repetidos:
                if elemento not in listaR:
                    listaR.append(str(info[2:]))

            # Agrega dentro de la lista de cajas en general.
            lista_Letras_repetidos.append("R_" + str(info[2:]))
            for elemento in lista_Letras_repetidos:
                if elemento not in lista_Letras:
                    lista_Letras.append("R_" + str(info[2:]))
        
        #Formato para los códigos:
        #Caja Verde 01: 7101
        #Caja Verde 06: 7106
        if tipo == 71:  # G->71, GREEN
            # Dibujamos
            cv2.polylines(frame, [pts], True, (0, 255, 0), 5)
            cv2.putText(frame, "VERDE_" + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print("Caja verde numero", str(info[2:]))

            # Agrega dentro de la lista de cajas azules.
            listaG_repetidos.append(str(info[2:]))
            for elemento in listaG_repetidos:
                if elemento not in listaG:
                    listaG.append(str(info[2:]))

            # Agrega dentro de la lista de cajas en general.
            lista_Letras_repetidos.append("G_" + str(info[2:]))
            for elemento in lista_Letras_repetidos:
                if elemento not in lista_Letras:
                    lista_Letras.append("G_" + str(info[2:]))
        
        #Formato para los códigos:
        #Caja Azul 01: 6601
        #Caja Azul 06: 6606
        if tipo == 66:  # B->66, BLUE
            # Dibujamos
            cv2.polylines(frame, [pts], True, (255, 0, 0), 5)
            cv2.putText(frame, "AZUL_" + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            print("Caja azul numero", str(info[2:]))

            # Agrega dentro de la lista de cajas azules.
            listaB_repetidos.append(str(info[2:]))
            for elemento in listaB_repetidos:
                if elemento not in listaB:
                    listaB.append(str(info[2:]))

            # Agrega dentro de la lista de cajas en general.
            lista_Letras_repetidos.append("B_" + str(info[2:]))
            for elemento in lista_Letras_repetidos:
                if elemento not in lista_Letras:
                    lista_Letras.append("B_" + str(info[2:]))

        # Imprimimos
        print("Rojas:",listaR)
        cant_Rojas = len(listaR)
        print("Cantidad letras rojas:",cant_Rojas)
        print("---------------------------------")

        print("Verdes:",listaG)
        cant_Verdes = len(listaG)
        print("Cantidad letras verdes:",cant_Verdes)
        print("---------------------------------")
        
        print("Azules:",listaB)
        cant_Azules = len(listaB)
        print("Cantidad letras azules:",cant_Azules)
        print("---------------------------------")

        print("Lista de cajas:",lista_Letras)

    # Mostramos FPS
    cv2.imshow("LECTOR DE QR", frame)
    # Leemos teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()
