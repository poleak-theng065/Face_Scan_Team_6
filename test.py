import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import sqlite3
import os

# Directory to save face images
FACE_IMAGES_DIR = 'face_images'
os.makedirs(FACE_IMAGES_DIR, exist_ok=True)

# Function to store data in the database
def store_data(name, age, weight, height, hometown, face_image_path):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO users (name, age, weight, height, hometown, face_image_path)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, age, weight, height, hometown, face_image_path))
    conn.commit()
    conn.close()

# Function to start the webcam feed
def start_webcam():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read each frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Capture the face image
            face_image = frame[y:y+h, x:x+w]

            # Save the face image to a file
            global face_image_path
            face_image_path = os.path.join(FACE_IMAGES_DIR, f'{name}_{x}_{y}.jpg')
            cv2.imwrite(face_image_path, face_image)

            # Store data in the database
            store_data(name, age, weight, height, hometown, face_image_path)

            # Add text near each detected face
            text = f"Name: {name}, Age: {age}, Weight: {weight}kg, Height: {height}cm, Hometown: {hometown}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        # Display the frame with detected faces and text
        cv2.imshow("Face Detection", frame)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def submit_form():
    global name, age, weight, height, hometown
    name = name_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    hometown = hometown_entry.get()

    # Print the entered details
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")
    print(f"Hometown: {hometown}")

    # Show a message box with the entered details
    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nWeight: {weight}\nHeight: {height}\nHometown: {hometown}")

    # Start webcam feed in a separate thread
    threading.Thread(target=start_webcam).start()

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create the main window
root = tk.Tk()
root.title("User Information Form")

# Create and place the labels and entries for each field
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Height (cm):").grid(row=3, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Hometown:").grid(row=4, column=0, padx=10, pady=5)
hometown_entry = tk.Entry(root)
hometown_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
