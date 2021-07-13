#based https://www.youtube.com/watch?v=xhG2AeyJXcU&list=PLst9mKBGfYJdcLU0MG3BEl7b00KC9f13a&index=33
#leemos de la webcam, detectará rostros, y cuando detecte una sonrisa hará un selfie

#requisitos
import cv2
import datetime
cap = cv2.VideoCapture(1) #normalemente será VideoCapture(0)
face_cascade = cv2.CascadeClassifier('2021_face_smile_selfie_recognition_requisites\haarcascade_frontalface_default.xml') #detectar caras
smile_cascade = cv2.CascadeClassifier('2021_face_smile_selfie_recognition_requisites\haarcascade_smile.xml') #detectar sonrisas

while True: #correr sin fin
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #ponemos en escala de grises nuestro canvas
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'selfie-{time_stamp}.png'
            cv2.imwrite(file_name, original_frame)
    cv2.imshow('cam star', frame) #cam star es el nombre del popup
    if cv2.waitKey(10) == ord('q'): #si presionamos q paramos el programa
        break