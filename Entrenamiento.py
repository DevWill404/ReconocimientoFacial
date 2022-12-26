import os
import cv2 
import numpy as np

# CARGAMOS LA LISTA DED PERSONAS ALMACENADAS
dataPath = 'D:\Codes\Python\Reconocimiento Facial\Data'
peopleList = os.listdir(dataPath)
print('lista de personas: {}'.format(peopleList))

labels = []
facesData = []

label = 0

# RECORREMOS LAS PERSONAS ALMACENADAS
for nameDir in peopleList:
    personPath = '{}/{}'.format(dataPath,nameDir)
    print('Leyendo todas las imagenes...')

    for fileName in os.listdir(personPath):
        print('\n Scripting: \n Nombre del sujeto:{} \n Nivel de peligro: Alto \n File: {} \n'.format(nameDir, fileName))
        labels.append(label)

        facesData.append(cv2.imread('{}/{}'.format(personPath, fileName), 0))
        image = cv2.imread('{}/{}'.format(personPath, fileName), 0)
    
    label += 1

# ENTRENAMIENTO
# MODELO A USAR EigenFaceRecognizer

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
print('\n Estamos realizando el entrenamiento...')

face_recognizer.train(facesData, np.array(labels))

face_recognizer.write('ModelFaceFrontalData.xml')
print('\n Modelo guardado')