import tkinter as tk
from tkinter import messagebox
import math

def compute_ugde(lat_err, lon_err, lat_ref, mode='MAE'):
    if mode.upper() == 'RMSE':
        factor = math.sqrt(2 / math.pi)
        lat_err *= factor
        lon_err *= factor

    lat_km = lat_err * 111
    lon_km = lon_err * 111 * math.cos(math.radians(lat_ref))
    ugde = math.sqrt(lat_km**2 + lon_km**2)
    return lat_km, lon_km, ugde

def on_calculate():
    try:
        lat_err = float(entry_lat.get())
        lon_err = float(entry_lon.get())
        lat_ref = float(entry_ref.get())
        mode = var_mode.get()

        lat_km, lon_km, ugde = compute_ugde(lat_err, lon_err, lat_ref, mode)

        result = (
            f"Latitude error: {lat_km:.2f} km\n"
            f"Longitude error: {lon_km:.2f} km\n"
            f"UGDE: {ugde:.2f} km"
        )
        messagebox.showinfo("Result", result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("UGDE Calculator")
root.geometry("350x250")

# Mode selection
var_mode = tk.StringVar(value="MAE")
tk.Label(root, text="Error type:").pack(pady=4)
tk.Radiobutton(root, text="MAE", variable=var_mode, value="MAE").pack()
tk.Radiobutton(root, text="RMSE", variable=var_mode, value="RMSE").pack()

# Input fields
tk.Label(root, text="Latitude error (°):").pack()
entry_lat = tk.Entry(root)
entry_lat.pack()

tk.Label(root, text="Longitude error (°):").pack()
entry_lon = tk.Entry(root)
entry_lon.pack()

tk.Label(root, text="Reference latitude (°):").pack()
entry_ref = tk.Entry(root)
entry_ref.pack()

# Calculate button
tk.Button(root, text="Calculate UGDE", command=on_calculate).pack(pady=10)

# Start GUI loop
root.mainloop()
