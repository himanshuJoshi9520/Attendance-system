from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime




class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=100)


        #-1st-image--
        img_top = Image.open(r"E:\ing\images (1).jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=70, width=650, height=700)

        # 2nd-image
        img_bottom = Image.open(r"C:\Users\hj952\Desktop\MicrosoftTeams-image-246-1024x599.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=70, width=950, height=700)

        # button
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=250, height=60)
        b1_1.config(command=self.face_recog)
       #===============attendance============
    def mark_attendance(self,i,r,n,d):
        with open("h.csv", "r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list)and (r not in name_list) and(n not in name_list)and(d not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")



    # facerecognitation====
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors=minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognizer",port=3306)
                my_cursor = conn.cursor()

                # my_cursor.execute("select Name from student where Student_id=" + str(id))
                # my_cursor.execute("slect Name from (SELECT Name, ROW_NUMBER() OVER() AS row_num FROM student) AS temp WHERE row_num = %s", (id))
                my_cursor.execute("SELECT Name FROM student LIMIT %s, 1", (id-1 ,))

                n = my_cursor.fetchone()
                if n:
                    n = n[0]

                # my_cursor.execute("select Roll from student where Student_id=" + str(id))
                my_cursor.execute("SELECT Roll FROM student LIMIT %s, 1", (id-1 ,))
                r = my_cursor.fetchone()
                if r:
                    r = r[0]

                # my_cursor.execute("select Dep from student where Student_id=" + str(id))
                my_cursor.execute("SELECT Dep FROM student LIMIT %s, 1", (id-1 ,))
                d = my_cursor.fetchone()
                if d:
                    d = d[0]

                # my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                my_cursor.execute("SELECT Student_id FROM student LIMIT %s, 1", (id-1 ,))
                i = my_cursor.fetchone()
                if i:
                    i = i[0]

                                

                if confidence > 78:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),2)
                    #if n is not None:
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    #if d is not None:
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome To face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



