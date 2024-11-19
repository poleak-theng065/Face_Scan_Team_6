import cv2 
import face_recognition

known_face_encodings = []
know_face_name = []

know_person1_image = face_recognition.load_image_file('images/p1.png')
know_person2_image = face_recognition.load_image_file('images/p2.png')
know_person3_image = face_recognition.load_image_file('images/p3.png')



known_person1_ecoding = face_recognition.face_encodings(know_person1_image)[0]
known_person2_ecoding = face_recognition.face_encodings(know_person2_image)[0]
known_person3_ecoding = face_recognition.face_encodings(know_person3_image)[0]


known_face_encodings.append(known_person1_ecoding)
known_face_encodings.append(known_person2_ecoding)
known_face_encodings.append(known_person3_ecoding)


know_face_name.append('Kin Doung')
know_face_name.append('Chann Dy')
know_face_name.append('Porleak')


video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    face_locationas = face_recognition.face_locations(frame)
    face_ecodings = face_recognition.face_encodings(frame, face_locationas)

    for (top, right, bottom, left), face_ecoding in zip(face_locationas, face_ecodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_ecoding)
        name = ('Unknown')
        if True in matches:
            first_match_index = matches.index(True)
            name = know_face_name[first_match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0 , 255, 0), 5)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
            
video_capture.release()
cv2.destroyAllWindows() 