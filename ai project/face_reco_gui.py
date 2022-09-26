from tkinter import *
import main_video as mv
root = Tk()

root.geometry("720x480")

Button(root, text="Start", command=mv.face_reco, width=40, height=20).pack()

root.mainloop()
