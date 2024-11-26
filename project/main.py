import customtkinter as ctk
import inputData
import verify


# Function for Verify Data
def verify_data():
    print(verify.verifydata())
# Function for Input Data
def input_your_data():
    print(inputData.create_student_data_form())
# Main window setup
window = ctk.CTk()
window.title("Face Detection Application")
window.geometry("1440x1024")  # Set the window size to 1440x1024

# Set appearance and color theme
ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

# Create a frame for the buttons (Centering purposes)
button_frame = ctk.CTkFrame(window,width=1440,height=1024,fg_color="white")
button_frame.place(relx=0.5, rely=0.5, anchor="center")

header_label = ctk.CTkLabel(button_frame, text="Welcome to my Face Detection Application", font=("Helvetica", 24, "bold"))
header_label.grid(row=0, column=0, columnspan=3, pady=20)

header = ctk.CTkLabel(button_frame, text="Please enjoys with my App. Happy with your day.", font=("Helvetica", 16, "bold"))
header.grid(row=1, column=0, columnspan=3, pady=20)

# Create the Input Data button
input_button = ctk.CTkButton(button_frame, text="Input Data", command=input_your_data,width=300,height=50)
input_button.grid(row=2, column=1, padx=20, pady=10)

# Create the Verify Data button
verify_button = ctk.CTkButton(button_frame, text="Verify Data", command=verify_data)
verify_button.grid(row=3, column=1, padx=20, pady=10)

# Run the application
window.mainloop()
