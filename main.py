from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
from dotenv import load_dotenv
import os
import locale
locale.setlocale(locale.LC_TIME, "hu_HU") 

def configure():
    load_dotenv()

def getWeather():
    city=textfield.get()
    
    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj= TimezoneFinder()
    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude)}°N\t{round(location.longitude)}°E")
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lang=hu&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid="+os.getenv('api_key')+""
    print(api)
    #weather
    json_data= requests.get(api).json()
    #current
    temp= json_data['current']['temp'] # reading temperature out of json
    humidity= json_data['current']['humidity'] # reading humidity out of json
    pressure= json_data['current']['pressure'] # reading pressure out of json
    wind= json_data['current']['wind_speed'] # reading wind speed out of json
    description= json_data['current']['weather'][0]['description'] # reading description out of json

    t.config(text=(temp,"°C"))  # setting eatch lables text 
    h.config(text=(humidity,"%"))
    p.config(text=(pressure, 'hPa'))
    w.config(text=(wind,"m/s"))
    d.config(text=description)
    
    
    #first cell / today
    firstdayimage= json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"img/weather_states/{firstdayimage}@2x.png")
    firstimage.config(image=photo1) # displaying icon of the weather
    firstimage.image=photo1
    
    tempday1 = json_data['daily'][0]['temp']["day"] # today's temp at daytime
    tempnight1=json_data['daily'][0]['temp']['night'] # today's temp at nighttime
    day1temp.config(text=f"Nappal:\n{tempday1} °C\n Éjszaka:\n{tempnight1} °C") # displaying both
    
    #second cell / like before but it's the following day and it goes on until the last day of the week
    seconddayimage= json_data['daily'][1]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{seconddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    
    tempday2 = json_data['daily'][1]['temp']["day"]
    tempnight2=json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Nappal:\n{tempday2} °C\n Éjszaka:\n{tempnight2} °C")
    
    #thrird cell
    thirddayimage= json_data['daily'][2]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{thirddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thrirdimage.config(image=photo3)
    thrirdimage.image=photo3
    
    tempday3 = json_data['daily'][2]['temp']["day"]
    tempnight3=json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Nappal:\n{tempday3} °C\n Éjszaka:\n{tempnight3} °C")
    
    #fourth cell
    fourthdayimage= json_data['daily'][3]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{fourthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    
    tempday4 = json_data['daily'][3]['temp']["day"]
    tempnight4=json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Nappal:\n{tempday4} °C\n Éjszaka:\n{tempnight4} °C")
    
    #fifth cell
    fifthdayimage= json_data['daily'][4]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{fifthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    
    tempday5 = json_data['daily'][4]['temp']["day"]
    tempnight5=json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Nappal:\n{tempday5} °C\n Éjszaka:\n{tempnight5} °C")
    
    #sixth cell
    sixthdayimage= json_data['daily'][5]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{sixthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    
    tempday6 = json_data['daily'][5]['temp']["day"]
    tempnight6=json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Nappal:\n{tempday6} °C\nÉjszaka:\n{tempnight6} °C")
    
    #seventh cell
    seventhdayimage= json_data['daily'][6]['weather'][0]['icon']
    img=(Image.open(f"img/weather_states/{seventhdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    
    tempday7 = json_data['daily'][6]['temp']["day"]
    tempnight7=json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Nappal:\n{tempday7} °C\n Éjszaka:\n{tempnight7} °C")
    
    #days
    first = datetime.now() # displaying the todays dayname
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth. strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth. strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A") )

    seventh = first+timedelta(days=4)
    day7.config(text=seventh. strftime("%A"))



root=Tk()
root.title='Weather app'
root.geometry('890x470+300+300')
root.configure(bg='#57adff')
root.resizable(False,False)
 

Round_box=PhotoImage(file='img/rounded_rectangle.png') # current weather background box
Label(root, image=Round_box, bg='#57adff') .place(x=30, y=110)

#label / current tepmeratue, humidity etc.
label1=Label(root,text='Hőmérséklet', font=('Helvetica',11),fg='white',bg='#203243')
label1.place(x=50,y=120)

label2=Label(root, text='Páratartalom', font=('Helvetica',11),fg='white', bg='#203243')
label2.place(x=50,y=140)

label3=Label(root, text='Nyomás', font=('Helvetica',11),fg='white', bg='#203243')
label3.place(x=50,y=160)

label4=Label (root, text='Szél', font=( 'Helvetica' ,11),fg='white', bg='#203243')
label4.place(x=50,y=180)

label5=Label (root, text='Leírás', font=( 'Helvetica' ,11),fg='white', bg='#203243')
label5.place(x=50,y=200)


##search box
Search_image=PhotoImage(file='img/searchbar.png')
myimage=Label (image=Search_image, bg='#57adff')
myimage.place(x=270, y=115)

weat_image=PhotoImage(file='img/Layer7.png')
weatherimage=Label (root, image=weat_image, bg='#203243')
weatherimage.place(x=290,y=120)

textfield=tk.Entry(root, justify='center',width=15,font=('poppins',25, 'bold' ),bg='#203243',border=0,fg='white')
textfield.place(x=370, y=130)
textfield.focus()

Search_icon=PhotoImage(file='img/search_icon.png')
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor='hand2' , bg='#203243', command=getWeather)
myimage_icon.place(x=645,y=130)

##Bottom box
frame=Frame (root, width=900, height=180,bg='#212120')
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file='img/rounded_rectangle_1.png')
secondbox=PhotoImage(file='img/rounded_rectangle_1_copy.png')

Label(frame, image=firstbox, bg='#212120') .place(x=30, y=20)

Label(frame, image=secondbox, bg='#212120') .place(x=300, y=30)
Label(frame, image=secondbox, bg='#212120') .place(x=400, y=30)
Label(frame, image=secondbox, bg='#212120') .place(x=500, y=30)
Label(frame, image=secondbox, bg='#212120') .place(x=600, y=30)
Label(frame, image=secondbox, bg='#212120') .place(x=700, y=30)
Label(frame, image=secondbox, bg='#212120') .place(x=800, y=30)

#clock / here we will place current time

clock=Label(root, font=('Helvetica',30, 'bold'),fg='white',bg='#57adff')
clock.place (x=30,y=20)

#timezone
timezone=Label (root, font=('Helvetica',20),fg='white', bg='#57adff')
timezone. place(x=650, y=20)

long_lat=Label(root, font=('Helvetica',10),fg='white', bg='#57adff')
long_lat.place(x=700,y=50)

#thpwd

#thpwd / setting temp,hum,press,wind and desc style and allign them
t=Label(root, font=("Helvetica",11),fg="white", bg="#203243")
t.place(x=150, y=120)
h=Label (root, font=("Helvetica",11),fg="white", bg="#203243")
h.place(x=150, y=140)
p=Label (root, font=("Helvetica",11),fg="white", bg="#203243")
p.place(x=150,y=160)
w=Label (root, font=("Helvetica",11),fg="white", bg="#203243")
w.place(x=150, y=180)
d=Label(root, font=("Helvetica",11),fg="white", bg="#203243")
d.place(x=150, y=200)

#first cell / todays card
firstframe=Frame(root,width=215,height=125,bg="#282829")
firstframe.place(x=35,y=315)
day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=0,y=0)
firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=-5,y=45)
day1temp=Label(firstframe,bg="#282829",font="arial 15 bold", fg="#57adff")
day1temp.place(x=120,y=25)

#second cell
secondframe=Frame (root ,width=75,height=120,bg="#282829")
secondframe.place(x=305,y=325)
day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=9,y=0)
secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)
day2temp=Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=10,y=60)

#third cell
thirdframe=Frame(root,width=75,height=120,bg="#282829")
thirdframe.place(x=405,y=325)
day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=9,y=0)
thrirdimage=Label(thirdframe,bg="#282829")
thrirdimage.place(x=7,y=20)
day3temp=Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=10,y=60)

#fourth cell
fourthframe=Frame (root ,width=75,height=120,bg="#282829")
fourthframe.place(x=505,y=325)
day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=9,y=0)
fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)
day4temp=Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=10,y=60)

#fifth cell
fifthframe=Frame(root,width=75,height=120,bg="#282829")
fifthframe.place(x=605,y=325)
day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=9,y=0)
fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)
day5temp=Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=10,y=60)

#sixth cell
sixthframe=Frame(root,width=75,height=120,bg="#282829")
sixthframe.place(x=705, y=325)
day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=9,y=0)
sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)
day6temp=Label(sixthframe,bg="#282829",fg="#fff")
day6temp.place(x=10,y=60)

#seventh cell
seventhframe=Frame (root ,width=75,height=120, bg="#282829")
seventhframe.place(x=805,y=325)
day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=9,y=0)
seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)
day7temp=Label(seventhframe,bg="#282829",fg="#fff")
day7temp.place(x=10,y=60)


root.mainloop()