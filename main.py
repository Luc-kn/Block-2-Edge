import tkinter as tk
import json
import os
from tkinter import messagebox

# Declare global variables for username and password entry fields
signup_username_entry = None
signup_password_entry = None



# Function to check if the JSON file exists, and create it if not
def create_json_file_if_not_exists():
    if not os.path.exists('user_data.json'):
        with open('user_data.json', 'w') as file:
            json.dump([], file)

# Create a function to check the credentials
def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    # You can replace this logic with your own authentication method
    if username == "user" and password == "password":
        messagebox.showinfo("Login successful", "Welcome, " + username + "!")
        root.deiconify()  # Show the login page upon successful login
        signup_window.destroy()  # Close the sign-up window if it's open
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

def open_signup():
    global signup_username_entry, signup_password_entry, signup_window  # Ensure the variables are accessed globally
    root.withdraw()  # Close the login page upon opening the sign-up page
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("400x300")  # Set the size of the sign-up window

    # Create and pack the username and password input fields for sign up
    signup_username_label = tk.Label(signup_window, text="New Username")
    signup_username_label.pack()
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.pack()

    signup_password_label = tk.Label(signup_window, text="New Password")
    signup_password_label.pack()
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.pack()

    # Create and pack the sign up button for the sign up window
    signup_button = tk.Button(signup_window, text="Sign Up", command=lambda: perform_signup(signup_username_entry.get(), signup_password_entry.get(), signup_window))
    signup_button.pack()

    return signup_window  # Return the signup_window

# Create a function to handle sign up button click in the sign up window
# Create a function to handle sign up button click in the sign up window
def perform_signup(new_username, new_password, signup_window):
    global signup_username_entry, signup_password_entry  # Access the global variables
    new_user_data = {"username": new_username, "password": new_password}
    with open('user_data.json', 'a+') as file:
        data = json.load(file) if os.path.getsize('user_data.json') > 0 else []
        data.append(new_user_data)
        file.seek(0)
        json.dump(data, file)

    messagebox.showinfo("Sign Up successful", "Welcome, " + new_username + "!")
    signup_window.destroy()  # Close the sign-up window
    root.deiconify()  # Show the login page after sign-up is successful

# Main function to initialize the GUI
def main():
    create_json_file_if_not_exists()  # Check and create the JSON file if it doesn't exist

    # Create the main window and set its size
    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")  # Set the initial size of the window

    # Create and pack the username and password input fields
    global username_entry, password_entry
    username_label = tk.Label(root, text="Username")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Create and pack the login button
    login_button = tk.Button(root, text="Login", command=check_credentials)
    login_button.pack()

    # Create and pack the sign up button
    signup_button = tk.Button(root, text="Sign Up", command=open_signup)
    signup_button.pack()

    # Run the main loop
    root.mainloop()

# Call the main function to start the program
if __name__ == "__main__":
    main()