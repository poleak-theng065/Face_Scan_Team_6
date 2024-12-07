import customtkinter as ctk

# Import modules for Check In and Check Out
try:
    import newuser
    import Interface_check
except ImportError as e:
    print(f"Error importing module: {e}")

# Function to handle Check In
def newCustomer():
    result = newuser.create_welcome_screen()
    update_feedback(f"Check In: {result}", "green")

# Function to handle Check Out
def oldCustomer():
    result = Interface_check.create_check_window()
    update_feedback(f"Check Out: {result}", "red")

# Function to update feedback label
def update_feedback(message, color):
    feedback_label.configure(text=message, text_color=color)

# Function to create the feedback label
def create_feedback_label(frame):
    global feedback_label
    feedback_label = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"))
    feedback_label.grid(row=5, column=0, columnspan=7, pady=10)


# Function to open the student data form
def open_form():
    import inputData
    inputData.create_student_data_form()

# Function to toggle between light and dark modes
def toggle_appearance_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Light"
    ctk.set_appearance_mode(new_mode)

# Function to add welcome labels
def add_welcome_labels(frame):
    # Add welcome message
    label = ctk.CTkLabel(
        frame,
        text="Welcome to my Face Detection Smart System",
        font=("Helvetica", 24, "bold"),
        text_color="#333"
    )
    label.place(relx=0.5, rely=0.35, anchor="center")

    # Add description
    description = ctk.CTkLabel(
        frame,
        text="A system to streamline attendance with advanced face detection.",
        font=("Helvetica", 16),
        text_color="#555"
    )
    description.place(relx=0.5, rely=0.5, anchor="center")

# Function to add buttons to the screen
def add_buttons(window, frame):
   # Create the Check In button
    olduser_button = ctk.CTkButton(
        frame,
        text="Old User",
        command=oldCustomer,
        width=200,
        height=50,
        corner_radius=10,
        fg_color="#00FF00",  # Corrected color formatting
        hover_color="#003366",
        font=("Helvetica", 16)
    )
    olduser_button.place(relx=0.3, rely=0.7, anchor="center")

    # Create the Check Out button
    newuser_button = ctk.CTkButton(
        frame,
        text="New User",
        command=newCustomer,
        width=200,
        height=50,
        corner_radius=10,
        fg_color="#FF0000",  # Corrected color formatting
        hover_color="#000000",
        font=("Helvetica", 16)
    )
    newuser_button.place(relx=0.7, rely=0.7, anchor="center")

    # Toggle Theme button
    toggle_button = ctk.CTkButton(
        window,
        text="Toggle Theme",
        command=toggle_appearance_mode,
        width=150,
        fg_color="#008CBA",
        hover_color="#0078A0",
        font=("Helvetica", 14)
    )
    toggle_button.place(relx=0.1, rely=0.05, anchor="center")

    # Exit button
    exit_button = ctk.CTkButton(
        window,
        text="Exit",
        command=window.destroy,
        width=100,
        fg_color="#D9534F",
        hover_color="#C9302C",
        font=("Helvetica", 14)
    )
    exit_button.place(relx=0.9, rely=0.05, anchor="center")

# Main function to create the welcome screen
def create_main_window():
    # Initialize the main window
    window = ctk.CTk()
    window.title("Welcome Screen")
    window.geometry("1440x1024")  # Set the window size

    # Set appearance and color theme
    ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
    ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

    # Create a welcome frame with specified width and height
    welcome_frame = ctk.CTkFrame(
        window, fg_color="white", corner_radius=20, width=800, height=500
    )
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

    add_welcome_labels(welcome_frame)
    add_buttons(window, welcome_frame)

    # Run the application
    window.mainloop()

# Run the main window
if __name__ == "__main__":
    create_main_window()