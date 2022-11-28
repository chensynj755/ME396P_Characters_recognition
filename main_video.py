import cv2
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from simple_facerec import SimpleFacerec

# Encode faces from a folder
cwd_path =str(os.getcwd())
img_path = cwd_path + "/images"
sfr = SimpleFacerec()
sfr.load_encoding_images(img_path)

# Constan Values
width = 640
height = 360
count = 0
pause = False
file_name = None
frame = None
wiki_link = {'Captain america':"https://en.wikipedia.org/wiki/Captain_America"
            ,'Black widow':"https://en.wikipedia.org/wiki/Black_Widow_(Natasha_Romanova)"
            ,'Bruce':"https://en.wikipedia.org/wiki/Hulk"
            ,'Proxima':"https://en.wikipedia.org/wiki/Proxima_Midnight"
            ,'Thor':"https://en.wikipedia.org/wiki/Thor_(Marvel_Comics)"}

# Set up GUI
root = Tk()
root.title('Approximately Intelligent')
guiFrame = ttk.Frame(root,padding=10)
guiFrame.grid()

# Set up control are above video
controlFrame = ttk.Frame(guiFrame, padding=10)
controlFrame.grid(column=0,row=0)

# Create Buttons

# def selectFile():
#     global file_name, pause
#     file_name = fd.askopenfilename()
#     pause = False
#     pass
# btn_select_file = ttk.Button(controlFrame, text = 'Select File', command = selectFile)
# btn_select_file.grid(column = 0, row = 0)

def identify():
    global pause
    pause = True
    pass
btn_identify = ttk.Button(controlFrame, text = 'Identify', command = identify)
btn_identify.grid(column = 0, row = 0)

def playvid():
    global pause
    pause = False
    pass
btn_play = ttk.Button(controlFrame, text = 'Play', command = playvid)
btn_play.grid(column = 1, row = 0)

def quitGUI():
    cap.release()
    root.destroy()
    pass
btn_quit = ttk.Button(controlFrame, text = 'Quit', command = quitGUI)
btn_quit.grid(column = 2, row =  0)

# Set up video area
imageFrame = ttk.Frame(guiFrame, width = 640, height = 360)
imageFrame.grid(column = 0,row = 1)
l_img = ttk.Label(imageFrame)
l_img.grid(column = 0, row = 0)

# Load Camera 'Movie.mp4'
cap = cv2.VideoCapture('Movie.mp4')
fps = int(cap.get(cv2.CAP_PROP_FPS))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

# Embed openCV with face_recognition to Tkinter
def run():
    global frame, count
    if not pause:
        count = 0
        ret, frame = cap.read()
    else:
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            if count < 1:
                count += 1
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                print("Now is ",name+".")
                if name in wiki_link:
                    print("Here is the link:",wiki_link[name])
    frameRGBA = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frameRGBA)
    imgtk = ImageTk.PhotoImage(image = img)
    l_img.imgtk = imgtk
    l_img.configure(image = imgtk)
    l_img.after(int(500/fps),run)

run()
root.mainloop()
