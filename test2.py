import tkinter as tk
import json
import os
from tkinter import messagebox

#File to store sales data
SALES_FILE = "sales_data.json"

#dumy login credentials
USER_CREDENTIALS = {"admin": "password123"}

#Load sales data from file
def load_sales():
    if os.path.exists(SALES_FILE):
        with open(SALES_FILE, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict): #ensuring the file contains a dictionary
                    return data
            except json.JSONDecodeError:
                pass # If file is empty/corrupt, ignore and return default         
    return{"Chicken": 0,"Fries-70": 0, "Fries-100": 0, "Smokies": 0, "Smoothies": 0} #default sales

#save sales data to file
def save_sales():
    with open(SALES_FILE, "w") as file:
        json.dump(sales,file)
         
# Initialize sales data
sales = load_sales()

# Function to update sales
def add_sale(item):
    sales[item] += 1
    save_sales() #saves sales after each update
    update_display()
    
# Function to reset sales
def reset_sales():
    global sales
    sales = {"Chicken": 0, "Fries-70": 0, "Fries-100": 0, "Smokies": 0, "Smoothies": 0}
    save_sales()
    update_display()    

# Function to update the display
def update_display():
    total_sales = sum(sales.values())
    display_text.set(
        f"Total Sales: {total_sales}\n"
        f"Sales:\nChicken {sales['Chicken']} \nFries-70: {sales['Fries-70']}\nFries-100: {sales['Fries-100']}\n"
        f"Smokies: {sales['Smokies']}\nSmoothies: {sales['Smoothies']}"
    )

#function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        login_window.destroy() #to hide login window
        open_sales_window()
    else:
        messagebox.showerror("Login Failed", "unaniona matako yako😒username or pass")  
            

# Function to open the sales tracking window
def open_sales_window():
    global display_text
    sales_window = tk.Tk()
    sales_window.title("DESI FRIES SALES")
    sales_window.geometry("400x400")
    sales_window.configure(bg="#1e1e1e")

    display_text = tk.StringVar()
    update_display()
    display_label = tk.Label(sales_window, textvariable=display_text, font=("Helvetica", 14), bg="#f0f0f0", fg="#333333")
    display_label.pack(pady=20)

    for item in sales:
        button = tk.Button(
            sales_window, text=f"Add {item}", font=("Arial", 12), command=lambda item=item: add_sale(item)
        )
        button.pack(pady=5)

    reset_button = tk.Button(
        sales_window, text="Reset Sales", font=("Arial", 12, "bold"), fg="white", bg="red", command=reset_sales
    )
    reset_button.pack(pady=10)
    
    sales_window.mainloop()

#optional logi form destroy
   
#login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.configure(bg="#f0f0f0")

tk.Label(login_window, text="Username:", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", font=("Arial", 12, "bold"), command=login)
login_button.pack(pady=10)

login_window.mainloop()