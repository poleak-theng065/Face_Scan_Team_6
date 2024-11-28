import customtkinter as ctk
import newuser
import oldUser

# Function to toggle between light and dark modes
def toggle_appearance_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Light"
    ctk.set_appearance_mode(new_mode)


# Function for Verify Data check In
def new_customer():
    print(newuser.create_welcome_screen())
# Function for Verify Data Check Out
def old_customer():
    print(oldUser.create_main_window())
# Main window setup
window = ctk.CTk()
window.title("Face Detection Application")
window.geometry("1440x1024")  # Set the window size to 1440x1024

# Set appearance and color theme
ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

# Create a frame for the buttons (Centering purposes)
frame = ctk.CTkFrame(window,fg_color="white",corner_radius=20, width=800, height=500)
frame.place(relx=0.5, rely=0.5, anchor="center")

header_label = ctk.CTkLabel(frame, text="Welcome to my Face Detection Application", font=("Helvetica", 24, "bold"),width=600,height=20,  text_color="#555")
header_label.grid(row=0, column=0, columnspan=7, pady=20)
# header_label.place(relx=0.3,rely=0.5,anchor="center")

header = ctk.CTkLabel(frame, text="Enjoys with my smart system.", font=("Helvetica", 16, "bold") , text_color="#555")
header.grid(row=1, column=0, columnspan=7, pady=20)
header = ctk.CTkLabel(frame, text="Are you a New stuff or stuff?", font=("Helvetica", 16, "bold"),  text_color="#555")
header.grid(row=2, column=0, columnspan=7, pady=20)

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


# Create the Verify Data button
checkin_button = ctk.CTkButton(window, text="New Stuff", command=new_customer,fg_color="blue",hover_color="black",width=200,height=50)
checkin_button.grid(row=3, column=1, padx=32, pady=16)
checkin_button.place(relx=0.3,rely=0.75,anchor="center")
# Create the Verify Data button
checkout_button = ctk.CTkButton(window, text="Stuff", command=old_customer,fg_color="red",hover_color="black",width=200,height=50)
checkout_button.grid(row=3, column=2, padx=32, pady=16)
checkout_button.place(relx=0.7,rely=0.75,anchor="center")

# Run the application
window.mainloop()
