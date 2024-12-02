import tkinter as tk
from tkinter import messagebox
import math
PI = math.pi

def cylinder(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and Height must be positive and not equal to zero.")
    if str(radius) or str(height):
        raise ValueError("Please enter a number")
    volume = PI * height * (radius**2)
    surface_area = 2 * PI * radius * (radius + height)
    return volume, surface_area

def cone(height, radius):
    def calc_surface_area(height, radius): 
        slant_length = (height**2) + (radius**2)
        slant_length = math.sqrt(slant_length)
        base_area = (radius**2) * PI 
        lateral_surface_area  = radius * slant_length * PI 
        return base_area + lateral_surface_area
    
    def calc_volume(height, radius): 
        volume = (1/3) * PI * (radius**2) * height 
        return volume

    if radius <= 0 or height <= 0:
        raise ValueError("Radius and Height must be positive and not equal to zero.")
    if str(radius) or str(height):
        raise ValueError("Please enter a number")

    surface_area = round(calc_surface_area(height, radius),2)
    volume = round(calc_volume(height, radius),2)
    
    return volume, surface_area 

def sphere(radius):
    checking_input = True
    while checking_input:
        if radius <= 0:
            raise ValueError ("Radius must be positive and not equal to zero.")
        elif str(radius):
            raise ValueError("Please enter a number")
        else:
            checking_input = False
    volume = (4/3) * PI * (radius**2)
    surface_area = 4 * PI * (radius**2) 
    return volume, surface_area

def cuboid(width, length, height):
    if width <= 0 or length <= 0 or height <= 0:
        raise ValueError("Width, length and height must all be positive and not equal to zero.")
    if str(width) or str(height) or str(length):
        raise ValueError("Please enter a number")
    volume = width * length * height
    surface_area = 2 * ((length * width) + (width * height) + (length * height))
    return volume, surface_area
    
def calculate():
    shape = shape_var.get()
    try:
        # Get inputs based on selected shape
        if shape == "Cylinder":
            radius = float(param1_entry.get())
            height = float(param2_entry.get())
            volume, surface_area = cylinder(radius, height)
        elif shape == "Sphere":
            radius = float(param1_entry.get())
            volume, surface_area = sphere(radius)
        elif shape == "Cuboid":
            length = float(param1_entry.get())
            width = float(param2_entry.get())
            height = float(param3_entry.get())
            volume, surface_area = cuboid(width, length, height)
        elif shape == "Cone":
            radius = float(param1_entry.get())
            height = float(param2_entry.get())
            volume, surface_area = cone(height,radius)
        else:
            raise ValueError("Invalid shape selected.")
        
        # Format volume and surface area in scientific notation/standard form if necessary
        def format_number(num):
            if num >= 1e6 or num <= 1e-2:
                return f"{num:.2e}"
            else:
                return f"{num:.2f}"
        
        # Apply formatting to volume and surface_area
        formatted_volume = format_number(volume)
        formatted_surface_area = format_number(surface_area)

        # Display formatted results
        result_label.config(text=f"Volume: {formatted_volume}\nSurface Area: {formatted_surface_area}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def update_parameters(*args):
    shape = shape_var.get()
    # Reset parameter fields
    param1_label.config(text="")
    param2_label.config(text="")
    param3_label.config(text="")
    param1_entry.grid_remove()
    param2_entry.grid_remove()
    param3_entry.grid_remove()

    param1_entry.delete(0, tk.END)
    param2_entry.delete(0, tk.END)
    param3_entry.delete(0, tk.END)
    result_label.config(text="")

    if shape == "Cylinder":
        param1_label.config(text="Radius:")
        param2_label.config(text="Height:")
        param1_entry.grid(row=2, column=1)
        param2_entry.grid(row=3, column=1)
    elif shape == "Sphere":
        param1_label.config(text="Radius:")
        param1_entry.grid(row=2, column=1)
    elif shape == "Cuboid":
        param1_label.config(text="Length:")
        param2_label.config(text="Width:")
        param3_label.config(text="Height:")
        param1_entry.grid(row=2, column=1)
        param2_entry.grid(row=3, column=1)
        param3_entry.grid(row=4, column=1)
    elif shape == "Cone":
        param1_label.config(text="Radius:")
        param2_label.config(text="Height:")
        param1_entry.grid(row=2, column=1)
        param2_entry.grid(row=3, column=1)

# Create the main window
root = tk.Tk()
root.title("Shape Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Shape selection
tk.Label(root, text="Select Shape:", font=("Arial", 12)).grid(row=0, column=0, pady=10, sticky="e")
shape_var = tk.StringVar(value="Cylinder")
shape_dropdown = tk.OptionMenu(root, shape_var, "Cylinder", "Sphere", "Cuboid", "Cone", command=update_parameters)
shape_dropdown.grid(row=0, column=1)

# Parameter inputs
param1_label = tk.Label(root, text="", font=("Arial", 12))
param1_label.grid(row=2, column=0, sticky="e")
param1_entry = tk.Entry(root, font=("Arial", 12))

param2_label = tk.Label(root, text="", font=("Arial", 12))
param2_label.grid(row=3, column=0, sticky="e")
param2_entry = tk.Entry(root, font=("Arial", 12))

param3_label = tk.Label(root, text="", font=("Arial", 12))
param3_label.grid(row=4, column=0, sticky="e")
param3_entry = tk.Entry(root, font=("Arial", 12))

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate)
calculate_button.grid(row=5, column=1, pady=20)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=6, column=0, columnspan=2)

# Initialize parameters for the default shape
update_parameters()

# Run the application
root.mainloop()
