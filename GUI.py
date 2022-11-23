#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:56:13 2022

@author: jiaminxu
"""

# import tkinter as tk
# from tkVideoPlayer import TkinterVideo

# root = tk.Tk()
# root.geometry("1280x720")

# videoplayer = TkinterVideo(master=root, scaled=True)
# videoplayer.load(r"Characters_recognition.avi")
# videoplayer.pack(expand=True, fill="both")

# videoplayer.play() # play the video

# root.mainloop()




import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"GoT.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()