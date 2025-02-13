import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import pyperclip  # For copying to clipboard
from PIL import Image, ImageTk  # For displaying the logo

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    try:
        with open(file_path, "rb") as file:
            hash_obj = hashlib.new(hash_algorithm)
            while chunk := file.read(8192):
                hash_obj.update(chunk)
            return hash_obj.hexdigest()
    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return f"Error: Unsupported hash algorithm '{hash_algorithm}'."

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def compute_hash():
    file_path = file_entry.get()
    hash_algorithm = algorithm_var.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return
    result = calculate_file_hash(file_path, hash_algorithm)
    result_label.config(text=f"Hash ({hash_algorithm}): {result}")
    copy_button.config(state=tk.NORMAL)  # Enable the copy button

def copy_hash():
    hash_value = result_label.cget("text").split(": ")[1]  # Extract hash value
    pyperclip.copy(hash_value)
    messagebox.showinfo("Copied", "Hash value copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("File Hash Calculator")

try:
    logo_image = Image.open("logo.png")  
    logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)  # Resize for GUI
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.grid(row=0, column=1, pady=10)
except FileNotFoundError:
    print("Logo not found. Make sure 'logo.png' is in the same directory.")

# File selection section
tk.Label(root, text="Select File:").grid(row=1, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Algorithm selection section
tk.Label(root, text="Algorithm:").grid(row=2, column=0, padx=10, pady=10)
algorithm_var = tk.StringVar(value="sha256")
algorithm_menu = tk.OptionMenu(root, algorithm_var, "sha256", "md5", "sha1")
algorithm_menu.grid(row=2, column=1, padx=10, pady=10)

# Compute button
compute_button = tk.Button(root, text="Compute Hash", command=compute_hash)
compute_button.grid(row=3, column=1, pady=20)

# Result label
result_label = tk.Label(root, text="", wraplength=400)
result_label.grid(row=4, columnspan=3, padx=10)

# Copy button
copy_button = tk.Button(root, text="Copy Hash", command=copy_hash, state=tk.DISABLED)
copy_button.grid(row=5, column=1, pady=10)

# Footer section
footer_text = "Made with ❤️by Jonathan DeLeon | MIT License"
footer_label = tk.Label(
    root,
    text=footer_text,
    font=("Arial", 10),
    fg="gray"
)
footer_label.grid(row=6, columnspan=3, pady=(20, 5))

# Run the application
root.mainloop()