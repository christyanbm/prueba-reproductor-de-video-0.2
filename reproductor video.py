import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_video():
    global cap
    video_path = filedialog.askopenfilename()
    cap = cv2.VideoCapture(video_path)
    play_video()

def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)
        lbl_video.after(10, play_video)
    else:
        cap.release()

root = tk.Tk()
root.title("Reproductor de Video")

lbl_video = tk.Label(root)
lbl_video.pack()

btn_select = tk.Button(root, text="Seleccionar Video", command=select_video)
btn_select.pack()

root.mainloop()
