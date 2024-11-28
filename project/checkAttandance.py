import customtkinter as ctk

# Import modules for Check In and Check Out
try:
    import checkInVerify
    import checkOutverify
except ImportError as e:
    print(f"Error importing module: {e}")

# Function to handle Check In
def verify_data_checkin():
    result = checkInVerify.verifydata_checkin()
    update_feedback(f"Check In: {result}", "green")

# Function to handle Check Out
def verify_data_checkout():
    result = checkOutverify.verifydata_checkout()
    update_feedback(f"Check Out: {result}", "red")

# Function to update feedback label
def update_feedback(message, color):
    feedback_label.configure(text=message, text_color=color)

# Function to create the header section
def create_header_section(frame):
    header_label = ctk.CTkLabel(frame, text="Technology Company", font=("Helvetica", 24, "bold"), width=600, height=100)
    header_label.grid(row=0, column=0, columnspan=7, pady=(30, 10))

    header = ctk.CTkLabel(frame, text="Hello my beloved staff. Welcome to my company❤️", font=("Helvetica", 16, "bold"))
    header.grid(row=1, column=0, columnspan=7, pady=(10, 5))

    header = ctk.CTkLabel(frame, text="You want to check in / check out?", font=("Helvetica", 16, "bold"))
    header.grid(row=2, column=0, columnspan=7, pady=(5, 20))

# Function to create the button section
def create_button_section(frame):
    # Check In Button
    checkin_button = ctk.CTkButton(frame, text="Check In Now", command=verify_data_checkin, fg_color="blue", hover_color="black", width=200, height=50)
    checkin_button.grid(row=3, column=1, padx=32, pady=16)

    # Check Out Button
    checkout_button = ctk.CTkButton(frame, text="Check Out Now", command=verify_data_checkout, fg_color="red", hover_color="black", width=200, height=50)
    checkout_button.grid(row=3, column=4, padx=32, pady=16)

    # Exit Button
    exit_button = ctk.CTkButton(frame, text="Exit", command=window.destroy, fg_color="gray", hover_color="black", width=200, height=50)
    exit_button.grid(row=4, column=2, pady=(16, 16))

# Function to create the feedback label
def create_feedback_label(frame):
    global feedback_label
    feedback_label = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"))
    feedback_label.grid(row=5, column=0, columnspan=7, pady=10)

# Function to initialize the app window
def initialize_window():
    global window
    window = ctk.CTk()
    window.title("Face Detection Application")
    window.geometry("1440x1024")  # Set the window size to 1440x1024
    ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
    ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"
    return window

# Function to create the main interface
def create_main_interface(window):
    frame = ctk.CTkFrame(window, fg_color="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    
    create_header_section(frame)
    create_button_section(frame)
    create_feedback_label(frame)

# Main function to run the app
def main():
    window = initialize_window()
    create_main_interface(window)
    window.mainloop()


