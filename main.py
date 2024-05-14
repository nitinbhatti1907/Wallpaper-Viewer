"Title: Wallpaper Viewer" 
"Description: A Python application designed with Tkinter and PIL to create a user-friendly interface for viewing wallpapers stored in a specified directory. It dynamically loads images from the 'wallpapers' folder, allowing users to cycle through them using the 'Next' button. The GUI is styled with a black background and white text, maintaining readability with Verdana font. It offers a seamless experience for browsing and enjoying various wallpapers effortlessly."

from tkinter import *
from PIL import ImageTk,Image
import os

def loop_pics():
    global counter
    img_lable.config(image=img_array[counter%len(img_array)])
    counter+=1

counter = 1
root = Tk()
root.title('Wallpepar_viewer')
root.geometry('350x500')
root.config(bg='Black')
root.resizable(0,0)

name_label = Label(root,text='Images',bg='black',fg='white')
name_label.config(font=('verdana',15))
name_label.pack(pady=20)

files = os.listdir('wallpapers')
img_array=[]
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_lable = Label(root,image=img_array[0])
img_lable.pack(pady=20)


next_btn= Button(root,text='Next',bg='white',fg='Black',command=loop_pics)
next_btn.config(font=('verdana',15))
next_btn.pack()
root.mainloop()