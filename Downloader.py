import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog
from pytube import YouTube

window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry('500x200')
window.resizable(False,False)

def Download_mp4():
    try:
        my_video = YouTube(video_Link.get())
    except:
        messagebox.showerror('Error','Video not found or network error')
        quit()
    download_Folder = download_Path.get()
    ask = messagebox.askokcancel('Confirm','Download? \n')
    bar = Progressbar(length = 100)
    if ask == True:
        
        highquality = my_video.streams.first()
        highquality.download(download_Folder)
        bar['value']=100
        bar.grid(row=7, column=1)
        messagebox.showinfo('Success','Downloaded and saved in \n'+download_Folder) 

def Download_mp3():
    try:
        my_video = YouTube(video_Link.get())
    except:
        messagebox.showerror('Error','Video not found or network error')
        quit()
    download_Folder = download_Path.get()
    ask = messagebox.askokcancel('Confirm','Download Audio?')
    bar = Progressbar(length = 100)
    if ask == True:
        
        audmp3 = my_video.streams.filter(only_audio=True).first()
        audmp3.download(download_Folder)
        bar['value']=100
        bar.grid(row=7, column=1)
        messagebox.showinfo('Success','Downloaded and saved in \n'+download_Folder) 
        
def browse():    
    dir = filedialog.askdirectory(initialdir="C:/")
    download_Path.set(dir)
    
def Widgets():
    
    link_txt = tk.Label(text="Enter Video URL")
    inp = tk.Entry(width=50, textvariable=video_Link)
    link_txt.grid(row=1, column=0, padx=5,pady=5)
    inp.grid(row=1, column=1)
    inp.focus()
    
    location_txt = tk.Label(text = "Destination:")
    location = tk.Entry(width=25, textvariable=download_Path)
    browse_btn = tk.Button(text="Browse", command = browse)
    location_txt.grid(row=3, column=0)
    location.grid(row=3, column=1)
    browse_btn.grid(row=3, column=2, padx=1, pady=1)

    btn_download_mp4 = tk.Button(text="Download Video", bg="yellow", fg="black", width=20, command = Download_mp4)
    btn_download_mp4.grid(row=5, column=1, padx=10, pady=10, sticky="sw")
    
    btn_download_mp3 = tk.Button(text="Download MP3", bg="yellow", fg="black", width=20, command = Download_mp3)
    btn_download_mp3.grid(row=6, column=1, padx=10, pady=10, sticky="se")

# Creating the tkinter Variables
video_Link = tk.StringVar()
download_Path = tk.StringVar()

#Calling Widgets function
Widgets()

window.mainloop()

