import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime


def face_reco():
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    # cap = cv2.VideoCapture("try.mp4")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (200, 200, 200), 1)

        cv2.imshow("Frame", frame)

        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            for name in face_names:
                if name not in nameList:
                    now = datetime.now()
                    time = now.strftime('%I:%M:%S:%p')
                    date = now.strftime('%d-%B-%Y')
                    f.writelines(f'{name}, {time}, {date}\n')
        # input()
        if cv2.waitKey(1) == ord('q'):
            break
    # input()
    cap.release()
    cv2.destroyAllWindows()
