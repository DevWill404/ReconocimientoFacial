import cv2
import imutils
import os

personName = 'test'
dataPath = 'D:\Codes\Python\Reconocimiento Facial\Data'
personPath = '{}/{}'.format(dataPath, personName)

# PREGUNTAMOS SI LA CARPETA YA FUE CREADA.
if(not os.path.exists(personPath)):
    print('Carpeta creada: {}'.format(personPath))
    os.makedirs(personPath)

# VAMOS A CREAR UNA VARIABLE PARA SABER LA CANTIDAD DE FOTOS QUE VAMOS A TOMAR.
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

# CAPTURAMOS LA CAMARA DE NUESTOR EQUIPO
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# CREAMOS UN BUCLE DONDE VAMOS A GENERAL EL FRAME QUE NOS MOSTRARA LA IMAGEN DE NUESTRA CAMARA.
while True:
    ret, frame = capture.read()
    
    if(ret == False):
        break
    
    frame = imutils.resize(frame, width = 600)
    auxFrame = frame.copy()

    #PASAMOS A ESCALA DE GRISES.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for(x , y, w, h) in faces:
        # CREAMOS EL RECTANGULO
        cv2.putText(frame, 'Reconociendo', (x, y - 25),2 , 1.1, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x , y), (x + w, y + h), (0, 255, 0))
        face = auxFrame[y:y + h, x:x + w]
        face = cv2.resize(face, (720, 720), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/face_{}.jpg'.format(count), face)
        count+=1

    key = cv2.waitKey(1)
    if(key == 27 or count >= 300):
        break

    cv2.imshow('Capture', frame)

    # PREGUNTAMOS SI EL USUARIO PRESIONO ALGUNA TECLA, Y SI LA TECLA ES ESC CERRARA LA VENTANA Y TERMINARA EL PROGRAMA.
    if(cv2.waitKey(1) == 27):
        break

capture.release()
cv2.destroyAllWindows()