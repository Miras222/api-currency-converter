import customtkinter
from tkinter import *
import requests

# Barvy
main_color = "#350a34"

# Okno
window = Tk()
window.title("Převodník měn")
window = Canvas(window, width=450, height=350)
window.pack()

window.config(bg=main_color)

# Seznam měn
currency_list = ["AUD", "BRL", "CHF", "CNY", "CZK", "EUR", "GBP", "HKD", "PHP", "PLN", "USD"]


# Funkce
def count():
    try:
        currency_from = var1.get()
        currency_to = var2.get()
        amount = float(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "NvjfMH6ZUrVPk3WI2SeojIsxDlMjsBls"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.config(text = round(data_result['result'], 2))
        notification_label.config(text="")
    except:
        notification_label.config(text="Zadejte prosím částku")

def reset():
    user_input.delete(0, END)

# Obrázek a jeho vizualizace v aplikaci
my_img = PhotoImage(file="money.png")
window.create_image(160,0, anchor= NW, image = my_img)


# Uživatelský vstup
user_input = customtkinter.CTkEntry(window, width=370, font=("Verdana", 20, "bold"), text_color="#000", justify=CENTER, fg_color="#fff", border_color="#fff")
user_input.insert(0, "0")
user_input.place(x=40, y=180)

# Nastavení prázdných výchozích hodnot v roletce
var1 = StringVar()
var2 = StringVar()

# Roletka - z jaké měny
drop_down_from = customtkinter.CTkComboBox(window, variable=var1, values=currency_list, font=("Verdana", 12, "bold"), dropdown_font=("Verdana", 12, "bold"), fg_color="#fff", text_color="#000", button_color="#ffa77c", button_hover_color="#ff9b6b", border_color="#fff", dropdown_hover_color="#ffd4c0", dropdown_text_color="#888")
drop_down_from.place(x=40, y=140)

# Roletka - na jakou měnu
drop_down_to = customtkinter.CTkComboBox(window, variable=var2, values=currency_list, font=("Verdana", 12, "bold"), dropdown_font=("Verdana", 12, "bold"), fg_color="#fff", text_color="#000", button_color="#ffa77c", button_hover_color="#ff9b6b", border_color="#fff", dropdown_hover_color="#ffd4c0", dropdown_text_color="#888")
drop_down_to.place(x=270, y=140)

# Tlačítko přepočtu
convert_button = customtkinter.CTkButton(window, text="Přepočítat", font=("Arial", 20, "bold"), text_color="#fff", fg_color="#9d001d", hover_color="#bf0023", command=count)
convert_button.place(x=77, y=225)

# Tlačítko na vyresetování
reset_button = customtkinter.CTkButton(window, text="Reset", font=("Arial", 20, "bold"), text_color="#fff", fg_color="#d14400", hover_color="#e24900", command=reset)
reset_button.place(x=227, y=225)

# Výsledný Label
result_label = Label(bg=main_color, fg="white", font=("Arial", 18, "bold"))
result_label.place(x=185, y=270)

# Upozorňující label
notification_label = Label(bg=main_color, fg="white", font=("Arial", 18, "bold"))
notification_label.place(x=100, y=270)

# Hlavní cyklus
window.mainloop()