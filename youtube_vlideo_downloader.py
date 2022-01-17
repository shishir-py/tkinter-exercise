from tkinter import *
from tkinter import messagebox
from pytube import YouTube
root = Tk()
root.geometry("300x300")
root.title("Youtube video downloader")
root.config(background="lightgray")
url = StringVar()
def download():
  youtube_link = url.get()
  video =YouTube(youtube_link)
  final_video =video.streams.first()
  final_video.download()
  messagebox.showinfo("downloaded successfully")
label = Label(text="url:")
label.pack()
link = Entry(root, textvariable=url, font="Arial 14")
link.pack()
download_button = Button(root, text="download", command=download())
download_button.pack()
root.mainloop()