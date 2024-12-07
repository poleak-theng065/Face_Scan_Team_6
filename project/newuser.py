import customtkinter as ctk
# got back to page welcome
def back():
    import main
    main.create_main_window()

# Function to open the student data form
def open_form():
    import inputData
    inputData.create_student_data_form()
print(open_form(),"It's working now")

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
    # Get Started button
    start_button = ctk.CTkButton(
        frame,
        text="Get Started",
        command=open_form,
        width=200,
        height=50,
        corner_radius=10,
        fg_color="#4CAF50",
        hover_color="#45A049",
        font=("Helvetica", 16)
    )
    start_button.place(relx=0.5, rely=0.7, anchor="center")

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
    back_button = ctk.CTkButton(
        window,
        text="Go Back",
        command=back,
        width=100,
        fg_color="#D9534F",
        hover_color="#C9302C",
        font=("Helvetica", 14)
    )
    back_button.place(relx=0.9, rely=0.05, anchor="center")

# Main function to create the welcome screen
def create_welcome_screen():
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



