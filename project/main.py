import tkinter as tk
from tkinter import filedialog
import verify
import os
import pandas as pd
from tkinter import  messagebox
from PIL import Image
import uuid


# function for to save data that user have inputed
def save_data():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    hometown = hometown_entry.get()
    class_name = class_entry.get()
    image_path = image_label.cget("text")  # Get the image path from the label
    
    if name and age and gender and hometown and class_name and image_path != "No Image Selected":
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
                df = pd.read_excel('data.xlsx')
            except FileNotFoundError:
                df = pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Hometown', 'Class', 'Image'])

            # Add new data to DataFrame
            new_data = pd.DataFrame([[name, age, gender, hometown, class_name, image_save_path]],
                                    columns=['Name', 'Age', 'Gender', 'Hometown', 'Class', 'Image'])
            df = pd.concat([df, new_data], ignore_index=True)

            # Save updated data to Excel
            df.to_excel('data.xlsx', index=False)

            messagebox.showinfo("Success", "Data has been saved successfully!")
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving data: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields and select an image.")

# Function to clear the input fields

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    hometown_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    gender_var.set(None)
    image_label.config(text="No Image Selected")

# Function to select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        image_label.config(text=file_path)

# Create main window
window = tk.Tk()
window.title("Student Data Entry Form")
window.geometry("500x600")

# Titile of form 
def header_frame():
    
# Header Frame (using grid instead of pack)
    header_frame = tk.Frame(window, bg="#4CAF50", bd=0, relief="flat")
    header_frame.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

    header_label = tk.Label(header_frame, text="Student Data Entry", font=("Helvetica", 18, "bold"))
    header_label.grid(row=10, column=10, padx=150, pady=10)

# Create labels and entry fields (with modern look)
font_style = ("Arial", 12)

# Function for input name
def name_input():
    # Name Entry
    name_label = tk.Label(window, text="Name:", font=font_style, bg="#f0f0f0")
    name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    global name_entry
    name_entry = tk.Entry(window, font=font_style, bd=2, relief="solid")
    name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Function for input age
def age_input():
    # Age Entry
    age_label = tk.Label(window, text="Age:", font=font_style, bg="#f0f0f0")
    age_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    global age_entry
    age_entry = tk.Entry(window, font=font_style, bd=2, relief="solid")
    age_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

# Function for choose Gender
def gender_input():
    # Gender Options
    gender_label = tk.Label(window, text="Gender:", font=font_style, bg="#f0f0f0")
    gender_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    global gender_var
    gender_var = tk.StringVar(value=None)
    male_rb = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", font=font_style, bg="#f0f0f0")
    male_rb.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    female_rb = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", font=font_style, bg="#f0f0f0")
    female_rb.grid(row=3, column=2, padx=10, pady=5, sticky="w")

# Function for input Hometown
def hometown_input():
    # Hometown Entry
    hometown_label = tk.Label(window, text="Hometown:", font=font_style, bg="#f0f0f0")
    hometown_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
    global hometown_entry
    hometown_entry = tk.Entry(window, font=font_style, bd=2, relief="solid")
    hometown_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

# Function for input classroom
def class_input():
    # Class Entry
    class_label = tk.Label(window, text="Class:", font=font_style, bg="#f0f0f0")
    class_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
    global class_entry
    class_entry = tk.Entry(window, font=font_style, bd=2, relief="solid")
    class_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

# Function for input image
def image_input():
        # Image selection
    global image_label
    image_label = tk.Label(window, text="No Image Selected", width=30, relief="solid", font=("Arial", 10), bg="#f0f0f0")
    image_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="w")
    
    select_image_button = tk.Button(window, text="Select Image", command=select_image, font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat")
    select_image_button.grid(row=6, column=2, padx=10, pady=10)

# Function calls to render the UI
header_frame()
name_input()
age_input()
gender_input()
hometown_input()
class_input()
image_input()

# Function for verify Data image with your face and show your data by webcam
def verifyData():
    print( verify.verifydata())
    
# Submit Button
submit_button = tk.Button(window, text="Submit Data", command= save_data, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat")
submit_button.grid(row=7, column=0, columnspan=3, pady=20)
# Verify Data
verify_button = tk.Button(window, text="Verify Data", command= verifyData, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat")
verify_button.grid(row=14, column=0, columnspan=6, pady=40)

# Run the application
window.mainloop()

