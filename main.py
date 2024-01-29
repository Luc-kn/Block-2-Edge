import tkinter as tk
import json
import os
from tkinter import messagebox

def create_json_file_if_not_exists():
    if not os.path.exists('user_data.json'):
        with open('user_data.json', 'w') as file:
            json.dump([], file)

def create_event_file_if_not_exists():
    if not os.path.exists('event_data.json'):
        with open('event_data.json', 'w') as file:
            json.dump({"current_event": "No Event Set", "all_events": []}, file)

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []

    return data

def load_event_data():
    try:
        with open('event_data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        create_event_file_if_not_exists()
        with open('event_data.json', 'r') as file:
            data = json.load(file)

    return data

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
    signup_window.geometry("500x400")
    center_window(signup_window)
    signup_window.configure(bg="black")  

    signup_username_label = tk.Label(signup_window, text="New Username", bg="black", fg="white")  
    signup_username_label.pack()
    signup_username_entry = tk.Entry(signup_window, bg="black", fg="white")  
    signup_username_entry.pack()

    signup_password_label = tk.Label(signup_window, text="New Password", bg="black", fg="white")  
    signup_password_label.pack()
    signup_password_entry = tk.Entry(signup_window, show="*", bg="black", fg="white")  
    signup_password_entry.pack()

    signup_button = tk.Button(signup_window, text="Sign Up", command=lambda: perform_signup(signup_username_entry.get(), signup_password_entry.get(), signup_window), bg="black", fg="white", relief=tk.RIDGE)  
    signup_button.pack()

    back_button = tk.Button(signup_window, text="Back to Login", command=lambda: go_back_to_login(signup_window), bg="black", fg="white", relief=tk.RIDGE)  
    back_button.pack()

def perform_signup(new_username, new_password, signup_window):
    new_user_data = {"username": new_username, "password": new_password}

    data = load_user_data()
    data.append(new_user_data)

    with open('user_data.json', 'w') as file:
        json.dump(data, file)

    messagebox.showinfo("Sign Up successful", "Welcome, " + new_username + "!")
    signup_window.destroy()
    root.deiconify()

def go_back_to_login(signup_window):
    signup_window.destroy()
    root.deiconify()

def open_main_page(username):
    global main_page
    main_page = tk.Toplevel()
    main_page.title("Main Page")
    main_page.geometry("600x500")
    center_window(main_page)
    main_page.configure(bg="black")  

    welcome_label = tk.Label(main_page, text="Welcome, " + username + "!", bg="black", fg="white")  
    welcome_label.pack()

    event_label = tk.Label(main_page, text="Today's Event: " + get_current_event(), bg="black", fg="white")  
    event_label.pack()

    change_event_button = tk.Button(main_page, text="Change Event", command=lambda: change_event(event_label), bg="black", fg="white", relief=tk.RIDGE)  
    change_event_button.pack()

    view_events_button = tk.Button(main_page, text="View All Events", command=view_all_events, bg="black", fg="white", relief=tk.RIDGE)  
    view_events_button.pack()

    add_event_button = tk.Button(main_page, text="Add Event", command=add_event, bg="black", fg="white", relief=tk.RIDGE)  
    add_event_button.pack()

def get_current_event():
    data = load_event_data()
    return data["current_event"]

def change_event(event_label):
    change_event_window = tk.Toplevel()
    change_event_window.title("Change Event")
    change_event_window.geometry("500x300")
    center_window(change_event_window)
    change_event_window.configure(bg="black")  

    current_event_label = tk.Label(change_event_window, text="Current Event:", bg="black", fg="white")  
    current_event_label.pack()

    current_event_entry = tk.Entry(change_event_window, bg="black", fg="white")  
    current_event_entry.insert(0, get_current_event())
    current_event_entry.pack()

    update_event_button = tk.Button(change_event_window, text="Update Event", command=lambda: update_event(event_label, current_event_entry.get(), change_event_window), bg="black", fg="white", relief=tk.RIDGE)  
    update_event_button.pack()

def update_event(event_label, new_event, change_event_window):
    data = load_event_data()
    data["current_event"] = new_event
    update_all_events(new_event)
    with open('event_data.json', 'w') as file:
        json.dump(data, file)

    event_label.config(text="Today's Event: " + new_event)
    change_event_window.destroy()

def update_all_events(new_event):
    data = load_event_data()
    data.setdefault("all_events", []).append(new_event)
    with open('event_data.json', 'w') as file:
        json.dump(data, file)

def view_all_events():
    all_events_window = tk.Toplevel()
    all_events_window.title("All Events")
    all_events_window.geometry("600x400")
    center_window(all_events_window)
    all_events_window.configure(bg="black")  

    all_events_label = tk.Label(all_events_window, text="All Events:", bg="black", fg="white")  
    all_events_label.pack()

    data = load_event_data()
    all_events_list = tk.Listbox(all_events_window, bg="black", fg="white")
    for event in data.get("all_events", []):
        all_events_list.insert(tk.END, event)
    all_events_list.pack()

def add_event():
    add_event_window = tk.Toplevel()
    add_event_window.title("Add Event")
    add_event_window.geometry("500x300")
    center_window(add_event_window)
    add_event_window.configure(bg="black")  

    new_event_label = tk.Label(add_event_window, text="New Event:", bg="black", fg="white")  
    new_event_label.pack()

    new_event_entry = tk.Entry(add_event_window, bg="black", fg="white")  
    new_event_entry.pack()

    save_event_button = tk.Button(add_event_window, text="Save Event", command=lambda: save_event(new_event_entry.get(), add_event_window), bg="black", fg="white", relief=tk.RIDGE)  
    save_event_button.pack()

def save_event(new_event, add_event_window):
    update_all_events(new_event)
    messagebox.showinfo("Event Added", "Event has been added successfully!")
    add_event_window.destroy()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def main():
    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("500x400")
    center_window(root)
    root.configure(bg="black")  

    global username_entry, password_entry
    username_label = tk.Label(root, text="Username", bg="black", fg="white")  
    username_label.pack()
    username_entry = tk.Entry(root, bg="black", fg="white")  
    username_entry.pack()

    password_label = tk.Label(root, text="Password", bg="black", fg="white")  
    password_label.pack()
    password_entry = tk.Entry(root, show="*", bg="black", fg="white")  
    password_entry.pack()

    login_button = tk.Button(root, text="Login", command=check_credentials, bg="black", fg="white", relief=tk.RIDGE)  
    login_button.pack()

    signup_button = tk.Button(root, text="Sign Up", command=open_signup, bg="black", fg="white", relief=tk.RIDGE)  
    signup_button.pack()

    # Run the root main loop
    root.mainloop()

if __name__ == "__main__":
    main()
