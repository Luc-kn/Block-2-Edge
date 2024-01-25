import tkinter as tk
import json
import os
import random
from tkinter import messagebox

def create_json_file_if_not_exists():
    if not os.path.exists('user_data.json'):
        with open('user_data.json', 'w') as file:
            json.dump([], file)

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []

    return data

def generate_random_event():
    events = ["Attend a seminar", "Meet with a mentor", "Complete a coding challenge", "Network with professionals", "Participate in a hackathon"]
    return random.choice(events)

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    data = load_user_data()

    for user_data in data:
        if user_data["username"] == username and user_data["password"] == password:
            messagebox.showinfo("Login successful", "Welcome, " + username + "!")
            open_main_page(username)
            return

    messagebox.showerror("Login failed", "Invalid username or password")

def open_signup():
    root.withdraw()
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("400x300")

    signup_username_label = tk.Label(signup_window, text="New Username")
    signup_username_label.pack()
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.pack()

    signup_password_label = tk.Label(signup_window, text="New Password")
    signup_password_label.pack()
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.pack()

    signup_button = tk.Button(signup_window, text="Sign Up", command=lambda: perform_signup(signup_username_entry.get(), signup_password_entry.get(), signup_window))
    signup_button.pack()

def perform_signup(new_username, new_password, signup_window):
    new_user_data = {"username": new_username, "password": new_password}

    data = load_user_data()
    data.append(new_user_data)

    with open('user_data.json', 'w') as file:
        json.dump(data, file)

    messagebox.showinfo("Sign Up successful", "Welcome, " + new_username + "!")
    signup_window.destroy()
    root.deiconify()

def open_main_page(username):
    root.withdraw()
    main_page = tk.Toplevel()
    main_page.title("Main Page")
    main_page.geometry("400x200")

    welcome_label = tk.Label(main_page, text="Welcome, " + username + "!")
    welcome_label.pack()

    # Display a random event on the main page
    event_label = tk.Label(main_page, text="Today's Event: " + generate_random_event())
    event_label.pack()

    # Add additional components or functionality for the main page here

def main():
    create_json_file_if_not_exists()

    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")

    global username_entry, password_entry
    username_label = tk.Label(root, text="Username")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login", command=check_credentials)
    login_button.pack()

    signup_button = tk.Button(root, text="Sign Up", command=open_signup)
    signup_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
