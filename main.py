from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"E:\ing\download.jpeg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"E:\ing\download.jpeg")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"E:\ing\download.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        img3= Image.open(r"E:\ing\1_DPNoWJ3Au35Fw58Sn2oj1w.png")
        img3= img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=200)
        
        #bg button
        img4 = Image.open(r"E:\ing\iStock-classroom-girls-students-school.jpg")
        img4= img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)


        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=250,height=220)

        
        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200,y=300,width=250,height=40)

        #face button
        img5 = Image.open(r"E:\ing\88060Learn-Facial-Recognition-scaled.jpg")
        img5= img5.resize((220, 220))
        self.photoimg5= ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=250,height=220)

        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500,y=300,width=250,height=40)

        # attendence

        img6 = Image.open(r"E:\ing\download (1).jpeg")
        img6= img6.resize((220, 220))
        self.photoimg6= ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=250,height=220)

        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800,y=300,width=250,height=40)

        # help face button

        img7 = Image.open(r"E:\ing\images.jpeg")
        img7= img7.resize((220, 220))
        self.photoimg7= ImageTk.PhotoImage(img7)


        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=250,height=220)

        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100,y=300,width=250,height=40)

        # train face

        img8 = Image.open(r"E:\ing\images (1).jpeg")
        img8= img8.resize((220, 220))
        self.photoimg8= ImageTk.PhotoImage(img8)


        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=250,height=220)

        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200,y=580,width=250,height=40)

        # photos

        img9 = Image.open(r"E:\ing\images (2).jpeg")
        img9= img9.resize((220, 220))
        self.photoimg9= ImageTk.PhotoImage(img9)


        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=250,height=220)

        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500,y=580,width=250,height=40)

        # developer
        img10 = Image.open(r"E:\ing\download (2).jpeg")
        img10= img10.resize((220, 220))
        self.photoimg10= ImageTk.PhotoImage(img10)


        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=250,height=220)

        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800,y=580,width=250,height=40)

        #exit button
        img11= Image.open(r"E:\ing\images (3).jpeg")
        img11= img11.resize((220, 220))
        self.photoimg11= ImageTk.PhotoImage(img11)


        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=250,height=220)

        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100,y=580,width=250,height=40)

    def open_img(self):
        os.startfile("data")


#-----------------function button -----------

    def  student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)

    def  train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
