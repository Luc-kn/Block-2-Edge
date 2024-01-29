import tkinter as tk
import json
import os
from tkinter import messagebox
import datetime
import time

def create_json_file_if_not_exists():
    if not os.path.exists('user_data.json'):
        with open('user_data.json', 'w') as file:
            json.dump([], file)

def create_event_file_if_not_exists():
    if not os.path.exists('event_data.json'):
        with open('event_data.json', 'w') as file:
            json.dump({"all_events": []}, file)

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

    view_all_events_label = tk.Label(main_page, text="All Events:", bg="black", fg="white")
    view_all_events_label.pack()

    data = load_event_data()
    global all_events_list
    all_events_list = tk.Listbox(main_page, bg="black", fg="white")
    for event in data.get("all_events", []):
        all_events_list.insert(tk.END, event)
    all_events_list.pack()

    all_events_list.bind("<Double-Button-1>", lambda event: view_event_details(all_events_list.get(tk.ACTIVE)))

    change_event_button = tk.Button(main_page, text="Change Event", command=change_event, bg="black", fg="white",
                                    relief=tk.RIDGE)
    change_event_button.pack()

    add_event_button = tk.Button(main_page, text="Add Event", command=add_event, bg="black", fg="white",
                                 relief=tk.RIDGE)
    add_event_button.pack()

    delete_event_button = tk.Button(main_page, text="Delete Event", command=delete_event, bg="black", fg="white",
                                    relief=tk.RIDGE)
    delete_event_button.pack()

    logout_button = tk.Button(main_page, text="Logout", command=logout, bg="black", fg="white", relief=tk.RIDGE)
    logout_button.pack()

def logout():
    main_page.destroy()
    root.deiconify()

def view_event_details(selected_event):
    view_details_window = tk.Toplevel()
    view_details_window.title("Event Details")
    view_details_window.geometry("400x300")
    center_window(view_details_window)
    view_details_window.configure(bg="black")

    current_event_label = tk.Label(view_details_window, text="Event Details:", bg="black", fg="white")
    current_event_label.pack()

    data = load_event_data()
    event_details = data.get(selected_event, {})

    time_label = tk.Label(view_details_window, text="Time:", bg="black", fg="white")
    time_label.pack()
    time_entry = tk.Entry(view_details_window, bg="black", fg="white")
    time_entry.insert(0, event_details.get("time", ""))
    time_entry.pack()

    date_label = tk.Label(view_details_window, text="Date:", bg="black", fg="white")
    date_label.pack()
    date_entry = tk.Entry(view_details_window, bg="black", fg="white")
    date_entry.insert(0, event_details.get("date", ""))
    date_entry.pack()

    location_label = tk.Label(view_details_window, text="Location:", bg="black", fg="white")
    location_label.pack()
    location_entry = tk.Entry(view_details_window, bg="black", fg="white")
    location_entry.insert(0, event_details.get("location", ""))
    location_entry.pack()

    major_label = tk.Label(view_details_window, text="Major:", bg="black", fg="white")
    major_label.pack()
    major_entry = tk.Entry(view_details_window, bg="black", fg="white")
    major_entry.insert(0, event_details.get("major", ""))
    major_entry.pack()

    teacher_label = tk.Label(view_details_window, text="Teacher:", bg="black", fg="white")
    teacher_label.pack()
    teacher_entry = tk.Entry(view_details_window, bg="black", fg="white")
    teacher_entry.insert(0, event_details.get("teacher", ""))
    teacher_entry.pack()

    submit_button = tk.Button(view_details_window, text="Submit",
                              command=lambda: save_event_details(selected_event, time_entry.get(),
                                                                   date_entry.get(), location_entry.get(),
                                                                   major_entry.get(), teacher_entry.get(),
                                                                   view_details_window),
                              bg="black", fg="white", relief=tk.RIDGE)
    submit_button.pack()

def save_event_details(selected_event, time, date, location, major, teacher, view_details_window):
    if not (time and date):
        messagebox.showerror("Error", "Please fill in time and date.")
        return

    # Validate time format (HH:MM)
    try:
        time.strptime(time, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
        return

    # Validate date format (YYYY-MM-DD)
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
        return

    data = load_event_data()
    event_details = data.setdefault(selected_event, {})
    event_details["time"] = time
    event_details["date"] = date
    event_details["location"] = location
    event_details["major"] = major
    event_details["teacher"] = teacher

    with open('event_data.json', 'w') as file:
        json.dump(data, file)

    view_details_window.destroy()

def change_event():
    change_event_window = tk.Toplevel()
    change_event_window.title("Change Event")
    change_event_window.geometry("500x300")
    center_window(change_event_window)
    change_event_window.configure(bg="black")  

    current_event_label = tk.Label(change_event_window, text="Select Event:", bg="black", fg="white")  
    current_event_label.pack()

    data = load_event_data()
    selected_event = tk.StringVar(value=data["all_events"][0] if data["all_events"] else "No Event")
    event_dropdown = tk.OptionMenu(change_event_window, selected_event, *data.get("all_events", []))
    event_dropdown.pack()

    edit_event_button = tk.Button(change_event_window, text="Edit Event", command=lambda: edit_event(selected_event.get(), change_event_window), bg="black", fg="white", relief=tk.RIDGE)  
    edit_event_button.pack()

    close_edit_button = tk.Button(change_event_window, text="Close Edit", command=change_event_window.destroy, bg="black", fg="white", relief=tk.RIDGE)  
    close_edit_button.pack()

def edit_event(selected_event, change_event_window):
    edit_event_window = tk.Toplevel()
    edit_event_window.title("Edit Event")
    edit_event_window.geometry("400x200")
    center_window(edit_event_window)
    edit_event_window.configure(bg="black")  

    current_event_label = tk.Label(edit_event_window, text="Edit Event:", bg="black", fg="white")  
    current_event_label.pack()

    edited_event_entry = tk.Entry(edit_event_window, bg="black", fg="white")
    edited_event_entry.insert(0, selected_event)
    edited_event_entry.pack()

    save_edit_button = tk.Button(edit_event_window, text="Save Edit", command=lambda: save_edit(selected_event, edited_event_entry.get(), edit_event_window), bg="black", fg="white", relief=tk.RIDGE)  
    save_edit_button.pack()

def save_edit(selected_event, edited_event, edit_event_window):
    data = load_event_data()
    index = data["all_events"].index(selected_event)
    data["all_events"][index] = edited_event

    with open('event_data.json', 'w') as file:
        json.dump(data, file)

    edit_event_window.destroy()
    update_all_events_list()

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
    update_all_events_list()

def update_all_events(new_event):
    data = load_event_data()
    data.setdefault("all_events", []).append(new_event)
    with open('event_data.json', 'w') as file:
        json.dump(data, file)

def delete_event():
    delete_event_window = tk.Toplevel()
    delete_event_window.title("Delete Event")
    delete_event_window.geometry("400x200")
    center_window(delete_event_window)
    delete_event_window.configure(bg="black")  

    current_event_label = tk.Label(delete_event_window, text="Select Event to Delete:", bg="black", fg="white")  
    current_event_label.pack()

    data = load_event_data()
    selected_event = tk.StringVar(value=data["all_events"][0] if data["all_events"] else "No Event")
    event_dropdown = tk.OptionMenu(delete_event_window, selected_event, *data.get("all_events", []))
    event_dropdown.pack()

    delete_selected_button = tk.Button(delete_event_window, text="Delete Selected Event", command=lambda: delete_selected_event(selected_event.get(), delete_event_window), bg="black", fg="white", relief=tk.RIDGE)  
    delete_selected_button.pack()

def delete_selected_event(selected_event, delete_event_window):
    data = load_event_data()
    data["all_events"].remove(selected_event)

    with open('event_data.json', 'w') as file:
        json.dump(data, file)

    delete_event_window.destroy()
    update_all_events_list()

def update_all_events_list():
    all_events_list.delete(0, tk.END)
    data = load_event_data()
    for event in data.get("all_events", []):
        all_events_list.insert(tk.END, event)

def view_event_details(selected_event):
    view_details_window = tk.Toplevel()
    view_details_window.title("Event Details")
    view_details_window.geometry("400x300")
    center_window(view_details_window)
    view_details_window.configure(bg="black")  

    current_event_label = tk.Label(view_details_window, text="Event Details:", bg="black", fg="white")  
    current_event_label.pack()

    data = load_event_data()
    event_details = data.get(selected_event, {})
    
    time_label = tk.Label(view_details_window, text="Time:", bg="black", fg="white")  
    time_label.pack()
    time_entry = tk.Entry(view_details_window, bg="black", fg="white")  
    time_entry.insert(0, event_details.get("time", ""))
    time_entry.pack()

    date_label = tk.Label(view_details_window, text="Date:", bg="black", fg="white")  
    date_label.pack()
    date_entry = tk.Entry(view_details_window, bg="black", fg="white")  
    date_entry.insert(0, event_details.get("date", ""))
    date_entry.pack()

    location_label = tk.Label(view_details_window, text="Location:", bg="black", fg="white")  
    location_label.pack()
    location_entry = tk.Entry(view_details_window, bg="black", fg="white")  
    location_entry.insert(0, event_details.get("location", ""))
    location_entry.pack()

    major_label = tk.Label(view_details_window, text="Major:", bg="black", fg="white")  
    major_label.pack()
    major_entry = tk.Entry(view_details_window, bg="black", fg="white")  
    major_entry.insert(0, event_details.get("major", ""))
    major_entry.pack()

    teacher_label = tk.Label(view_details_window, text="Teacher:", bg="black", fg="white")  
    teacher_label.pack()
    teacher_entry = tk.Entry(view_details_window, bg="black", fg="white")  
    teacher_entry.insert(0, event_details.get("teacher", ""))
    teacher_entry.pack()

    save_details_button = tk.Button(view_details_window, text="Save Details", command=lambda: save_event_details(selected_event, time_entry.get(), date_entry.get(), location_entry.get(), major_entry.get(), teacher_entry.get(), view_details_window), bg="black", fg="white", relief=tk.RIDGE)  
    save_details_button.pack()

def save_event_details(selected_event, time, date, location, major, teacher, view_details_window):
    data = load_event_data()
    event_details = data.setdefault(selected_event, {})
    event_details["time"] = time
    event_details["date"] = date
    event_details["location"] = location
    event_details["major"] = major
    event_details["teacher"] = teacher

    with open('event_data.json', 'w') as file:
        json.dump(data, file)

    view_details_window.destroy()

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
