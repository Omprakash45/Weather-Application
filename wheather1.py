from tkinter import *
from tkinter import ttk
import requests
from datetime import datetime, timezone, timedelta

def data_get():
    city = city_name.get()
    api_key = "d015882c85b689b31f57312ef4f94015"  # Your API key
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    
    # Print the fetched data for debugging
    print(data)
    
    # Convert temperatures from Kelvin to Celsius
    temperature = data["main"]["temp"] - 273.15
    feels_like = data["main"]["feels_like"] - 273.15
    temp_min = data["main"]["temp_min"] - 273.15
    temp_max = data["main"]["temp_max"] - 273.15
    
    # Convert sunrise and sunset times to local time in India
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"], tz=timezone.utc) + timedelta(seconds=data["timezone"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"], tz=timezone.utc) + timedelta(seconds=data["timezone"])
    
    # Update the labels with the fetched data
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp1.config(text=f"{temperature:.2f} °C")
    temp_min1.config(text=f"{temp_min:.2f} °C")
    temp_max1.config(text=f"{temp_max:.2f} °C")
    feels_like1.config(text=f"{feels_like:.2f} °C")
    per1.config(text=f"{data['main']['pressure']} hPa")
    hum1.config(text=f"{data['main']['humidity']} %")
    wind_speed1.config(text=f"{data['wind']['speed']} m/s")
    visibility1.config(text=f"{data['visibility']} m")
    sunrise1.config(text=sunrise.strftime("%H:%M:%S"))
    sunset1.config(text=sunset.strftime("%H:%M:%S"))

def filter_cities(event):
    typed = search_var.get()
    if typed == '':
        filtered_list = list_name
    else:
        filtered_list = [city for city in list_name if typed.lower() in city.lower()]
    
    com['values'] = filtered_list

win = Tk()
win.title("Weather")
win.config(bg="#330867")
win.geometry("600x900")

name_label = Label(win, text="WEATHER APP", font=("Times New Roman", 40, "bold"))
name_label.place(x=65, y=50, height=50, width=450)

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
             "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
             "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
             "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
             "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
             "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
             "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry", "Agra", "Ahmedabad", "Aizawl", "Ajmer", "Aligarh", "Allahabad", "Alleppey", "Amritsar",
             "Amravati", "Anantapur", "Aurangabad", "Ayodhya",
             "Badrinath", "Bangalore", "Bareilly", "Belgaum", "Bhagalpur", "Bharatpur", "Bhavnagar",
             "Bhopal", "Bhubaneswar", "Bhuj", "Bikaner",
             "Bilaspur", "Bodh Gaya", "Calicut", "Chandigarh", "Chennai", "Cherrapunji", "Chikmagalur",
             "Chittoor", "Coimbatore", "Coonoor",
             "Cuttack", "Darjeeling", "Dehradun", "Delhi", "Dhanbad", "Dharamshala", "Dibrugarh",
             "Dimapur", "Dindigul", "Diu",
             "Durgapur", "Ernakulam", "Erode", "Faridabad", "Fatehpur Sikri", "Gandhinagar",
             "Gangotri","gangapur", "Gangtok", "Gaya", "Ghaziabad", "Goa",
             "Gorakhpur", "Greater Noida", "Gulbarga", "Guntur", "Gurgaon", "Guwahati",
             "Gwalior", "Haldwani", "Haridwar", "Hassan", "Hissar",
             "Hosur", "Hubli", "Hyderabad", "Imphal", "Indore", "Itanagar", "Jabalpur", "Jaipur",
             "Jaisalmer", "Jalandhar", "Jalgaon",
             "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Junagadh", "Kadapa",
             "Kakinada", "Kalimpong", "Kanchipuram", "Kanpur",
             "Kanyakumari", "Karimnagar", "Karnal", "Karur", "Kashmir", "Katni", "Kavaratti",
             "Khajuraho", "Kharagpur", "Kochi", "Kodaikanal",
             "Kohima", "Kolar", "Kolhapur", "Kolkata", "Kollam", "Korba", "Kota", "Kottayam",
             "Kozhikode", "Kumbakonam", "Kurnool",
             "Kurukshetra", "Leh", "Lonavala", "Lucknow", "Ludhiana", "Madurai", "Mahabalipuram",
             "Malappuram", "Manali", "Mandya", "Mangalore",
             "Mathura", "Meerut", "Mohali", "Moradabad", "Mount Abu", "Mumbai", "Munnar",
             "Mysore", "Nagpur", "Nainital", "Nashik",
             "Navi Mumbai", "Noida", "Ooty", "Pali", "Panaji", "Patiala", "Patna", "Pondicherry",
             "Porbandar", "Port Blair", "Prayagraj",
             "Pune", "Puri", "Pushkar", "Raipur", "Rajahmundry", "Rajkot", "Rameswaram",
             "Ranchi", "Ratlam", "Rishikesh", "Rohtak",
             "Rourkela", "Sagar", "Salem", "Sambalpur", "Sangli", "Saputara", "Satna",
             "Secunderabad", "Shillong", "Shimla", "Sikar",
             "Silchar", "Siliguri", "Solapur", "Sonipat", "Srinagar", "Surat", "Tawang",
             "Tezpur", "Thane", "Thanjavur", "Thiruvananthapuram",
             "Thrissur", "Tiruchirappalli", "Tirupati", "Tirunelveli", "Tiruvannamalai",
             "Udaipur", "Ujjain", "Vadodara", "Varanasi", "Vellore",
             "Vijayawada", "Visakhapatnam", "Vrindavan", "Warangal"]

search_var = StringVar()
search_bar = Entry(win, textvariable=search_var, font=("Times New Roman", 20))
search_bar.place(x=65, y=120, height=50, width=450)
search_bar.bind("<KeyRelease>", filter_cities)

city_name = StringVar()
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=65, y=190, height=50, width=450)

done_button = Button(win, text="CHECK", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=260, height=50, width=100)

w_label = Label(win, text="WEATHER CLIMATE:", font=("Times New Roman", 10))
w_label.place(x=160, y=330, height=50, width=200)
w_label1 = Label(win, text="T", font=("Times New Roman", 10))
w_label1.place(x=370, y=330, height=50, width=200)

wb_label = Label(win, text="WEATHER DESCRIPTION:", font=("Times New Roman", 10))
wb_label.place(x=160, y=400, height=50, width=200)
wb_label1 = Label(win, text="T", font=("Times New Roman", 10))
wb_label1.place(x=370, y=400, height=50, width=200)

temp_label = Label(win, text="TEMPERATURE:", font=("Times New Roman", 10))
temp_label.place(x=160, y=430, height=50, width=200)
temp1 = Label(win, text="T", font=("Times New Roman", 10))
temp1.place(x=370, y=430, height=50, width=200)

temp_min_label = Label(win, text="TEMP MIN:", font=("Times New Roman", 10))
temp_min_label.place(x=160, y=460, height=50, width=200)
temp_min1 = Label(win, text="T", font=("Times New Roman", 10))
temp_min1.place(x=370, y=460, height=50, width=200)

temp_max_label = Label(win, text="TEMP MAX:", font=("Times New Roman", 10))
temp_max_label.place(x=160, y=490, height=50, width=200)
temp_max1 = Label(win, text="T", font=("Times New Roman", 10))
temp_max1.place(x=370, y=490, height=50, width=200)

feels_like_label = Label(win, text="FEELS LIKE:", font=("Times New Roman", 10))
feels_like_label.place(x=160, y=520, height=50, width=200)
feels_like1 = Label(win, text="T", font=("Times New Roman", 10))
feels_like1.place(x=370, y=520, height=50, width=200)

per = Label(win, text="PRESSURE:", font=("Times New Roman", 10))
per.place(x=160, y=550, height=50, width=200)
per1 = Label(win, text="T", font=("Times New Roman", 10))
per1.place(x=370, y=550, height=50, width=200)

hum = Label(win, text="HUMIDITY:", font=("Times New Roman", 10))
hum.place(x=160, y=580, height=50, width=200)
hum1 = Label(win, text="T", font=("Times New Roman", 10))
hum1.place(x=370, y=580, height=50, width=200)

wind_speed_label = Label(win, text="WIND SPEED:", font=("Times New Roman", 10))
wind_speed_label.place(x=160, y=610, height=50, width=200)
wind_speed1 = Label(win, text="T", font=("Times New Roman", 10))
wind_speed1.place(x=370, y=610, height=50, width=200)

visibility_label = Label(win, text="VISIBILITY:", font=("Times New Roman", 10))
visibility_label.place(x=160, y=640, height=50, width=200)
visibility1 = Label(win, text="T", font=("Times New Roman", 10))
visibility1.place(x=370, y=640, height=50, width=200)

sunrise_label = Label(win, text="SUNRISE:", font=("Times New Roman", 10))
sunrise_label.place(x=160, y=670, height=50, width=200)
sunrise1 = Label(win, text="T", font=("Times New Roman", 10))
sunrise1.place(x=370, y=670, height=50, width=200)

sunset_label = Label(win, text="SUNSET:", font=("Times New Roman", 10))
sunset_label.place(x=160, y=700, height=50, width=200)
sunset1 = Label(win, text="T", font=("Times New Roman", 10))
sunset1.place(x=370, y=700, height=50, width=200)

win.mainloop()
