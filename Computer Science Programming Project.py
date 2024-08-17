import tkinter as tk
from tkinter import filedialog
import time

loggedin = False
start_time = time.time()
start_of_month = time.time()  # Initialize the start time for the month

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("FirstCall")
    new_window.configure(bg="#7BC8F6")
    label = tk.Label(new_window, text="Hello Agent!")
    label.grid()

def open_calendar_window():
    def import_file():
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            # Process the file or display its content as needed
            print(f"File selected: {file_path}")

    calendar_window = tk.Toplevel(root)
    calendar_window.title("CALENDAR")
    
    calendar_window.geometry("400x200")  # Adjust dimensions as needed
    calendar_window.configure(bg="#7BC8F6")

    # Button to import a file
        
    rota_button = tk.Button(calendar_window, text="Import Rota", command=import_file)
    rota_button.grid(row=0, column=0, padx=10, pady=10)
    

def open_leaderboards_window():
    leaderboards_window = tk.Toplevel(root)
    leaderboards_window.title("LEADERBOARDS AND STATISTICS")
    leaderboards_window.geometry("400x400")  
    leaderboards_window.configure(bg="#7BC8F6")

    # Labels and entry boxes for entering name and stats
    name_label = tk.Label(leaderboards_window, text="Enter Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    name_entry = tk.Entry(leaderboards_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    stats_label = tk.Label(leaderboards_window, text="Enter Stats:")
    stats_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    stats_entry = tk.Entry(leaderboards_window)
    stats_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)


    # Function to add user to the leaderboard
    def add_to_leaderboard():
        try:
            new_name = name_entry.get()
            new_stats = int(stats_entry.get())

            # Add the new entry to the leaderboard data
            sample_leaderboard_data.append({"name": new_name, "stats": new_stats})

            # Update the leaderboard display
            update_leaderboard()
        except ValueError:
            # Handle invalid input (non-numeric stats)
            tk.messagebox.showerror("Error", "Invalid input. Please enter a numeric value for stats.")

    # Button to add user to the leaderboard
    add_button = tk.Button(leaderboards_window, text="Add to Leaderboard", command=add_to_leaderboard)
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    add_button.configure(bg="white")

    # Function to update the leaderboard display
    def update_leaderboard():
        # Sort the leaderboard data based on stats in descending order
        sorted_leaderboard = sorted(sample_leaderboard_data, key=lambda x: x["stats"], reverse=True)

        # Clear existing labels in the leaderboard window
        for widget in leaderboards_window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        # Display the leaderboard entries
        for idx, entry in enumerate(sorted_leaderboard):
            label_text = f"{idx + 1}. {entry['name']}: {entry['stats']} stats"
            label = tk.Label(leaderboards_window, text=label_text)
            label.grid(row=idx + 3, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

    # Display the initial leaderboard
    update_leaderboard()

def open_payment_window():
    payment_window = tk.Toplevel(root)
    payment_window.title("PAYMENT")
    payment_window.geometry("400x200")  # Adjust dimensions as needed
    payment_window.configure(bg="#7BC8F6")

    # Label for the top two boxes
    top_label = tk.Label(payment_window, text="Please enter the monthly hours and hourly wage:")
    top_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    # Creating four input boxes for the top two values
    input_box1 = tk.Entry(payment_window)
    input_box1.grid(row=1, column=1, padx=5, pady=5)

    input_box2 = tk.Entry(payment_window)
    input_box2.grid(row=1, column=2, padx=5, pady=5)

    # Label for the bottom two boxes
    bottom_label = tk.Label(payment_window, text="Enter the hours done (all time) and the hourly wage:")
    bottom_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    # Creating four input boxes for the bottom two values
    input_box3 = tk.Entry(payment_window)
    input_box3.grid(row=3, column=1, padx=5, pady=5)

    input_box4 = tk.Entry(payment_window)
    input_box4.grid(row=3, column=2, padx=5, pady=5)

    # Labels for displaying results
    result_label1 = tk.Label(payment_window, text="Payment due (Month):")
    result_label1.grid(row=5, column=0, padx=5, pady=5)

    result_label2 = tk.Label(payment_window, text="Payments recieved (All time):")
    result_label2.grid(row=5, column=1, padx=5, pady=5)

    # Function to calculate the product and update the result labels
    def calculate_product():
        try:
            value1 = float(input_box1.get())
            value2 = float(input_box2.get())
            value3 = float(input_box3.get())
            value4 = float(input_box4.get())

            result_top_two = value1 * value2
            result_bottom_two = value3 * value4

            # Display the results in the labels
            result_label1.config(text=f"Result (Top Two): {result_top_two}")
            result_label2.config(text=f"Result (Bottom Two): {result_bottom_two}")
        except ValueError:
            result_label1.config(text="Invalid input. Please enter numeric values.")
            result_label2.config(text="Invalid input. Please enter numeric values.")

    # Button to trigger the calculation
    calculate_button = tk.Button(payment_window, text="Calculate", command=calculate_product)
    calculate_button.grid(row=5, column=2, padx=5, pady=5)
    calculate_button.configure(bg="white")


def open_user_window():
    user_window = tk.Toplevel(root)
    user_window.title("USER")
    user_window.geometry("1920x1080")
    user_window.configure(bg="#7BC8F6")

def open_hours_window():
    hours_window = tk.Toplevel(root)
    hours_window.title("HOURS")
    hours_window.geometry("1920x1080")
    hours_window.configure(bg="#7BC8F6")

    time_label = tk.Label(hours_window, text="Time Completed (All Time):")
    time_label.grid(row=0, column=0, padx=5, pady=5)

    time_box = tk.Text(hours_window, height=5, width=20, bd=2, relief=tk.SOLID)
    time_box.grid(row=0, column=1, padx=5, pady=5)
    time_box.configure(bg="white", fg="black")

    logged_out_time_label = tk.Label(hours_window, text="Time Completed (This Month):")
    logged_out_time_label.grid(row=1, column=0, padx=5, pady=5)

    global logged_out_time_box
    logged_out_time_box = tk.Text(hours_window, height=5, width=20, bd=2, relief=tk.SOLID)
    logged_out_time_box.grid(row=1, column=1, padx=5, pady=5)
    logged_out_time_box.configure(bg="white", fg="black")

    time_box.insert(tk.END, "00:00:00")
    logged_out_time_box.insert(tk.END, "00:00:00")

    def start_timer(time_box, is_logged_out_time):
        global start_of_month

        if is_logged_out_time:
            elapsed_time = int(time.time() - start_of_month)
        else:
            elapsed_time = int(time.time() - start_time)

        if elapsed_time < 0:
            elapsed_time = 0

        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = (elapsed_time % 3600) % 60
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

        time_box.delete(1.0, tk.END)
        time_box.insert(tk.END, time_str)

        if is_logged_out_time:
            hours_window.after(1000, lambda: start_timer(logged_out_time_box, True))
        else:
            hours_window.after(1000, lambda: start_timer(time_box, False))

    start_timer(time_box, False)  # Timer for time_box
    start_timer(logged_out_time_box, True)  # Timer for logged_out_time_box

    def reset_time():
        global start_of_month
        start_of_month = time.time()
        logged_out_time_box.delete(1.0, tk.END)
        logged_out_time_box.insert(tk.END, "00:00:00")

    reset_button = tk.Button(hours_window, text="Reset", command=reset_time)
    reset_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    reset_button.configure(bg="white")

# setting up all of the buttons on the main window and positioning them correctly
def submit():
    global loggedin, start_time
    username = username_entry.get()
    password = password_entry.get()
    if username == "adam.jennings" and password == "Password1":
        loggedin = True
        start_time = time.time()
        open_new_window()
        window = tk.Tk()

        window.geometry("1920x1080")
        window.configure(bg="#7BC8F6")

        pay_button = tk.Button(window, text="PAYMENT", width=25, height=20, command=open_payment_window)
        pay_button.grid(row=0, column=0, padx=35, pady=70, sticky=tk.W+tk.E+tk.N+tk.S)
        pay_button.configure(bg="white")

        clndr_button = tk.Button(window, text="CALENDAR", width=25, height=20, command=open_calendar_window)
        clndr_button.grid(row=0, column=1, padx=35, pady=70, sticky=tk.W+tk.E+tk.N+tk.S)
        clndr_button.configure(bg="white")

        ldrbrd_button = tk.Button(window, text="LEADERBOARDS", width=25, height=20, command=open_leaderboards_window)
        ldrbrd_button.grid(row=0, column=2, padx=35, pady=70, sticky=tk.W+tk.E+tk.N+tk.S)
        ldrbrd_button.configure(bg="white")

        hourlog_button = tk.Button(window, text="HOURS", width=25, height=20, command=open_hours_window)
        hourlog_button.grid(row=0, column=3, padx=35, pady=70, sticky=tk.W+tk.E+tk.N+tk.S)
        hourlog_button.configure(bg="white")

        user_button = tk.Button(window, text="USER", width=25, height=20, command=open_user_window)
        user_button.grid(row=0, column=4, padx=35, pady=70, sticky=tk.W+tk.E+tk.N+tk.S)
        user_button.configure(bg="white")

        time_box = tk.Text(window, height=5, width=15, bd=2, relief=tk.SOLID)
        time_box.grid(row=65, column=0, rowspan=1, columnspan=2, padx=1, pady=1)
        time_box.configure(bg="white", fg="black")

        def start_timer():
            elapsed_time = int(time.time() - start_time)
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = (elapsed_time % 3600) % 60
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            time_box.delete(1.0, tk.END)
            time_box.insert(tk.END, time_str)
            window.after(1000, start_timer)

        start_timer()

        def msg_of_day():
            msg_of_day = entry.get()
            print("Message of the day! - ", msg_of_day)
            text_box = tk.Text(window, height=12, width=80)
            text_box.grid(row=20, column=12, rowspan=5, columnspan=5)

        greeting = tk.Label(text="Hello Agent!")
        greeting.grid()

        # Add an outlined text box for user input
        input_text_box = tk.Text(window, height=10, width=50, bd=2, relief=tk.SOLID)
        input_text_box.grid(row=65, column=0, rowspan=2, columnspan=5, padx=1, pady=1)

        window.mainloop()
    else:
        error_label.config(text="Incorrect username or password")

root = tk.Tk()
root.title("Login")
root.configure(bg="#7BC8F6")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)
username_label.configure(bg="white")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)
password_label.configure(bg="white")

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
submit_button.configure(bg="white")

error_label = tk.Label(root, fg="red", bg="#7BC8F6")
error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
