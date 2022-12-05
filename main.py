from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()

root.title("Weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

Search_image=PhotoImage(file="img/searchbar.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=14,font=("poppins",25,"bold"),border=0)
textfield.place(x=37,y=24)
textfield.focus()
Search_icon=PhotoImage(file="img/search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#FFFFFF")
myimage_icon.place(x=310,y=29)


root.mainloop()