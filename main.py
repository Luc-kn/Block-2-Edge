import tkinter as tk
from tkinter import messagebox

signup_window = None
signup_username_entry = None
signup_password_entry = None

# Create a function to check the credentials
def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    # You can replace this logic with your own authentication method
    if username == "user" and password == "password":
        messagebox.showinfo("Login successful", "Welcome, " + username + "!")
        root.withdraw()  # Close the login page upon successful login
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

# Create a function to handle sign up button click
def open_signup():
    global signup_window, signup_username_entry, signup_password_entry
    global signup_username_entry
    global signup_password_entry
    
    # Create <link>StringVar</link> variables to store the input for sign up
    signup_username = tk.StringVar()
    signup_password = tk.StringVar()
    
    signup_username_entry = tk.Entry(signup_window, textvariable=signup_username)
    signup_username_entry.pack()

    signup_password_entry = tk.Entry(signup_window, show="*", textvariable=signup_password)
    signup_password_entry.pack()

    signup_button = tk.Button(signup_window, text="Sign Up", command=lambda: perform_signup(signup_username_entry, signup_password_entry))
    signup_button.pack()


# Create a function to handle sign up button click in the sign up window
def perform_signup(username_entry, password_entry):
    new_username = username_entry.get()
    new_password = password_entry.get()
    
    new_username = signup_username_entry.get()
    new_password = signup_password_entry.get

    # You can add your sign up logic here, such as adding the new user to a database
    messagebox.showinfo("Sign Up successful", "Welcome, " + new_username + "!")
    root.deiconify()  # Show the login page after sign-up is successful

# Create the main window and set its size
root = tk.Tk()
root.title("Login")
root.geometry("400x200")  # Set the initial size of the window

# Create and pack the username and password input fields
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