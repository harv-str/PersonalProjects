import requests
import customtkinter as ctk



def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data



def get_city(name):
    #name = "London"
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'LOquvAa7Kl94P7v2X0sXTQ==hhUWmTwbeqtwE7dV'})
    if response.status_code == requests.codes.ok:
        #print(response.text)
        data = response.json()
        longitude = data[0]['longitude']
        latitude = data[0]['latitude']
        return [latitude,longitude]

        
    else:
        print("Error:", response.status_code, response.text)



def send_weather_update(name):
    #for new york city
    #name = input("Name of your city?")
    x = get_city(name)
    latitude = x[0]
    longitude = x[1]

    # print(latitude)

    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]


    weather_info = (
        f"Good morning!\n"
        f"Current Weather in {name}:\n"
        f"Temperature: {temperature_celsius}°C\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind speed: {wind_speed} m/s"
        ) 

        #Greeting = "Good Morning Harvey"

    
    #print(weather_info)
    label = ctk.CTkLabel(scrollable_frame, text = weather_info)
    label.pack()

def add_name():
    name = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text = name, font= Underline_font)
    label.pack()
    entry.delete(0, ctk.END)
    send_weather_update(name)

root = ctk.CTk()
root.geometry("750x450")
root.title("Weather app")

Underline_font_Title = ctk.CTkFont( family = "bahnschrift semilight",size = 50, weight = "bold" )
Underline_font_Title.configure(underline = "True")

Underline_font = ctk.CTkFont( family = "bahnschrift semilight", weight = "bold" )
Underline_font.configure(underline = "True")
greeting_label = ctk.CTkLabel(root, text="Hourly weather check",font = Underline_font_Title)

#
# greeting_label = ctk.CTkLabel(root, text="Hourly weather check", font=ctk.CTkFont(size=30, weight ="bold", "bahnschrift semilight underline"))
greeting_label.pack(padx=20, pady =(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()



entry = ctk.CTkEntry(scrollable_frame, placeholder_text="City")
entry.pack(fill = "x")

confirm_city_button = ctk.CTkButton(root, text="Confirm", width = 500, command = add_name)
confirm_city_button.pack(pady = 20)

root.mainloop()



    





#def main():
    #send_weather_update()
    #send_weather_update()
    
  




#if __name__ == "__main__":
    #main()
