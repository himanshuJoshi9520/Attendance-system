from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Background Image
        img_top = Image.open(r"E:\ing\images (10).jpeg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dep_label = Label(f_lbl, text="Email: officialjoshi11@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dep_label.place(x=550, y=220)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
