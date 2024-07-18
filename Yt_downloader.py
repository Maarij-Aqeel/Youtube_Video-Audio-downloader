import tkinter as tk
from tkinter import filedialog as fd
from pytubefix import YouTube as yt
from tkinter import messagebox
import pyperclip



def starter_code(): 
    window=tk.Tk()
    frame=tk.Frame(bg="#FF0000")
    window.configure(bg="#FF0000")
    window.geometry("1280x720")
    window.resizable(False,False)
    window.title("YT Audio/Video Downloader")
    widgets(frame,window)
    window.mainloop()

def set_value(value,mp3,mp4):
    global option
    option=value
    if value==1:
        mp3.config(relief="sunken",bg="#A4E9D5",fg="black")
        mp4.config(relief="raised",bg="#333333",fg="#FFFFFF") 
    else:
        mp4.config(relief="sunken",bg="#A4E9D5",fg="black")
        mp3.config(relief="raised",bg="#333333",fg="#FFFFFF")

    

def widgets(frame,window):
    global option

    #Checking the Clipboard
    if "youtube.com" in pyperclip.paste():
        link=pyperclip.paste()
    else:
        link="Insert link here"

    #Creating Widgets
    Title=tk.Label(frame,text="Youtube Downloader",bg="#FF0000",fg="#FFFFFF",font=("Arial",20))
    Url=tk.Label(window,text="URL",bg="#FF0000",fg="white",font=("Arial",15))
    Url_entry=tk.Entry(window,font=("Arial",15))
    Resolution_lab=tk.Label(window,text="Resolution",bg="#FF0000",fg="white",font=("Arial",15))
    Resolution=tk.Entry(window,font=("Arial",15),width=10)
    Url_entry.insert(0,link)
    Option_mp3=tk.Button(window,text="mp3",bg="#333333",fg="#FFFFFF",font=("Arial",15)
                         ,command=lambda: set_value(1,Option_mp3,Option_mp4),activebackground="#A4E9D5",activeforeground="blue",cursor="hand2",relief="raised")
    Option_mp4=tk.Button(window,text="mp4",bg="#333333",fg="#FFFFFF",font=("Arial",15)
                         ,command=lambda: set_value(2,Option_mp3,Option_mp4),activebackground="#A4E9D5",activeforeground="blue",cursor="hand2",relief="raised")
    Download=tk.Button(window,text="Download",bg="#F5F0F6",fg="black"
                       ,font=("Arial",15),command=lambda:Logic(Url_entry.get(),option,Resolution),activebackground="#A4E9D5",activeforeground="blue")
    #Placing on Screen
    Title.grid(row=0,column=0,columnspan=2,pady=30,sticky="news")
    Url.place(x=170,y=250)
    Url_entry.place(x=420,y=250)
    Resolution_lab.place(x=170,y=350)
    Resolution.place(x=550,y=350)
    Option_mp3.place(x=500,y=450)
    Option_mp4.place(x=750,y=450)
    Download.place(x=570,y=550)
    frame.pack()


def Logic(url,option,res):
    if "youtube.com" in url and option!=0:
        url=str(url)
        yt_obj=yt(url)
        if option==2:
            videos=yt_obj.streams.get_by_resolution(res.get())
            if videos==None:
                videos=yt_obj.streams.get_highest_resolution()
                obt_res=str(videos)
                messagebox.showwarning(title="Warning",message=res.get()+" is not available, highest resolution available is "+obt_res[46:50])
                res.delete(0,5)
                res.insert(0,obt_res[46:50])
            else:
                path=fd.askdirectory()
                videos.download(path)
                messagebox.showinfo(title="Status",message="Successfully downloaded")
        elif option==1:
            audio=yt_obj.streams.get_audio_only()
            if audio ==None:
                messagebox.showerror(title="Error",message="Unable to find music. An Error occured")
            else:
                path=fd.askdirectory()
                audio.download(path)
                messagebox.showinfo(title="Status",message="Successfully downloaded")
    elif ("youtube.com"in url)==False:
        messagebox.showerror(title="Error",message="Invalid URL")
    else:
        messagebox.showerror(title="Error",message="Please select a format")

option=0
starter_code()

