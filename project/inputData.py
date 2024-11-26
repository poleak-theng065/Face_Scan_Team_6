import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
from PIL import Image, ImageTk
import uuid
import customtkinter as ctk
import verify
def verify_Data_of_student():
    print(verify.verifydata())

image_path = None
preview_label = None
image_label = None

# Function to select and preview an image
def select_image():
    global image_path, preview_label, image_label

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )

    if file_path:
        image_path = file_path
        image_label.configure(text=file_path)

        try:
            img = Image.open(image_path)
            img.thumbnail((100, 100))  # Resize for preview

            # Convert to CTkImage for proper scaling
            img_ctk = ctk.CTkImage(img, size=(50, 50))

            # Update preview label with CTkImage
            preview_label.configure(image=img_ctk)
            preview_label.image = img_ctk  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
    else:
        messagebox.showwarning("Warning", "No image was selected.")

# Function to create a center frame
def create_center_frame(window):
    center_frame = ctk.CTkFrame(
        window,
        fg_color="white",  # Correct way to set the frame color
    )
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    return center_frame
# Font text of label
# Function to create header label
def create_header(center_frame):
    header_label = ctk.CTkLabel(center_frame, text="Student Data Entry", font=("Helvetica", 32, "bold"))
    header_label.grid(row=0, column=0, columnspan=3, pady=20)

# Function to create and return name input field
def create_name_input(center_frame):
    name_label = ctk.CTkLabel(center_frame, text="Name:", font=("Arial", 16))
    name_label.grid(row=1, column=0, padx=20, pady=10,sticky="e")
    name_entry = ctk.CTkEntry(center_frame, font=("Arial", 16),text_color="blue")
    name_entry.grid(row=1, column=1, padx=20, pady=10,sticky="w")
    return name_entry

# Function to create and return age input field
def create_age_input(center_frame):
    age_label = ctk.CTkLabel(center_frame, text="Age:", font=("Arial", 16))
    age_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
    age_entry = ctk.CTkEntry(center_frame, font=("Arial", 16))
    age_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")
    return age_entry

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    hometown_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    gender_var.set(None)
    image_label.configure(text="No Image Selected")
    preview_label.configure(image="")

# Function to create and return gender input options
def create_gender_input(center_frame):
    gender_label = ctk.CTkLabel(center_frame, text="Gender:", font=("Arial", 16))
    gender_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    gender_var = tk.StringVar(value=None)
    male_rb = ctk.CTkRadioButton(center_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 16))
    male_rb.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    female_rb = ctk.CTkRadioButton(center_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 16))
    female_rb.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    return gender_var

# Function to create and return hometown input field
def create_hometown_input(center_frame):
    hometown_label = ctk.CTkLabel(center_frame, text="Hometown:", font=("Arial", 16))
    hometown_label.grid(row=4, column=0, padx=20, pady=10, sticky="e")
    hometown_entry = ctk.CTkEntry(center_frame, font=("Arial", 16))
    hometown_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")
    return hometown_entry

# Function to create and return class input field
def create_class_input(center_frame):
    class_label = ctk.CTkLabel(center_frame, text="Class:", font=("Arial", 16))
    class_label.grid(row=5, column=0, padx=20, pady=10, sticky="e")
    class_entry = ctk.CTkEntry(center_frame, font=("Arial", 16))
    class_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")
    return class_entry

# Function to create image selection and preview
def create_image_section(center_frame):
    global image_label, preview_label

    image_label = ctk.CTkLabel(center_frame, text="No Image Selected", font=("Arial", 12))
    image_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="w")
    select_image_button = ctk.CTkButton(center_frame, text="Select Image", command=select_image)
    select_image_button.grid(row=6, column=2, padx=10, pady=10)

    preview_label = ctk.CTkLabel(center_frame, text="", width=100, height=100, fg_color="gray")
    preview_label.grid(row=6, column=3, padx=10, pady=10)

def save_data():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    hometown = hometown_entry.get()
    class_name = class_entry.get()
    image_path = image_label.cget("text")  # Get the image path from the label

    # Validation: Check if all fields are filled
    if not name or not age or not gender or not hometown or not class_name or image_path == "No Image Selected":
        messagebox.showwarning("Input Error", "Please fill out all fields and select an image.")
        return

    # Validate age
    if not age.isdigit() or int(age) <= 0:
        messagebox.showwarning("Input Error", "Please enter a valid age greater than 0.")
        return

    try:
        # Create image folder if it doesn't exist
        if not os.path.exists('image'):
            os.makedirs('image')

        # Generate a unique filename for the image
        image_filename = f"{uuid.uuid4().hex}.png"
        image_save_path = os.path.join('image', image_filename)

        # Open and save the image to the 'image' folder
        img = Image.open(image_path)
        img.save(image_save_path)

        # Load the existing Excel file or create a new one if it doesn't exist
        try:
            df = pd.read_excel('dataOfStudent.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Hometown', 'Class', 'Image'])

        # Add new data to DataFrame
        new_data = pd.DataFrame([[name, age, gender, hometown, class_name, image_save_path]],
                                columns=['Name', 'Age', 'Gender', 'Hometown', 'Class', 'Image'])
        df = pd.concat([df, new_data], ignore_index=True)

        # Save updated data to Excel
        df.to_excel('dataOfStudent.xlsx', index=False)

        messagebox.showinfo("Success", "Data has been saved successfully!")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving data: {e}")

# Function to create buttons
def create_buttons(center_frame):
    submit_button = ctk.CTkButton(center_frame, text="Submit Data",
                                                command=save_data, 
                                                fg_color="green", 
                                                hover_color="lightgreen",
                                                width=200,
                                                height=30)
    submit_button.grid(row=7, column=1, pady=10)

    verify_button = ctk.CTkButton(center_frame, text="Verify Data", 
                                                command=verify_Data_of_student, 
                                                fg_color="blue", 
                                                hover_color="lightblue",
                                                width=200,
                                                height=30)
    verify_button.grid(row=8, column=1, pady=10)

# Main function to create the window and form
def create_student_data_form():
    window = ctk.CTk()
    window.title("Student Data Entry Form")
    window.geometry("1440x1024")
    window.config(bg="white")
    # Set modern appearance and theme
    ctk.set_appearance_mode("light")  # Options: "System", "Light", "Dark"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    # Create the center frame
    center_frame = create_center_frame(window)

    # Create header
    create_header(center_frame)

    # Create form fields
    global name_entry, age_entry, gender_var, hometown_entry, class_entry
    name_entry = create_name_input(center_frame)
    age_entry = create_age_input(center_frame)
    gender_var = create_gender_input(center_frame)
    hometown_entry = create_hometown_input(center_frame)
    class_entry = create_class_input(center_frame)

    # Image section
    create_image_section(center_frame)

    # Buttons for submitting and verifying data
    create_buttons(center_frame)
    window.mainloop()

