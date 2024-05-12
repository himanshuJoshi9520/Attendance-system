from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        #-1st-image--
        img_top = Image.open(r"C:\Users\asus\Pictures\Screenshots\Screenshot 2024-04-26 154302.png")
        img_top = img_top.resize((650,700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        
        
        #2nd-image
        img_top = Image.open(r"C:\Users\asus\Pictures\Screenshots\Screenshot 2024-04-26 154302.png")
        img_top = img_top.resize((950,700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=650, y=55, width=950, height=700)
                
        # button
        b1_1=Button(self.root,text="FACE RECOGNITION",cursor="hand2",font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=365,y=620,width=250,height=60)
        
    # facerecognitation====
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf)
        grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(grey_image,scaleFactor,minNeighbors)

        coord=[]
        for(x,y,w,h) in featyres:
            cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(grey_image[y:y+h,x:x+w])
            confidence=int((100*(1-predict/300)))
            
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognizer")
            my_cursor = conn.cursor()
                  
            my_cursor.execute("select Name from student where Student_id="+str(id))
            n=my_cursor.fetchone()
            n="+".join(n)
            
            my_cursor.execute("select Rol from student where Student_id="+str(id))
            r=my_cursor.fetchone()
            r="+".join(r)
            
            my_cursor.execute("select Dep from student where Student_id="+str(id))
            d=my_cursor.fetchone()
            d="+".join(d)
            
            my_cursor.execute("select  from student where Student_id="+str(id))
            i=my_cursor.fetchone()
            i="+".join(i)
            
            
            if confidence>78:
                cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FOUND_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FOUND_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FOUND_HERSHEY_COMPLEX,0,8,(255,255,255),3)
            else:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,"unknown face",(x,y-5),cv2.FOUND_HERSHEY_COMPLEX,0,8,(255,255,255),3)
            
            coord=[x,y,w,y]
       
        return coord      
        
        
        def recognize(img,clf,faceCascade):  
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img     
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.videoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome To face recognition",img)
            if cv2.waitkey(1)==13:
                break
            video_cap.release()
            cv2,destroyAllwindow()   
            
                

      if __name__ == "__main__":
             root = Tk()
             obj = Face_Recognition(root)
             root.mainloop() 