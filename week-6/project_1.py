import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

def calculate_charge():
    def process():
        try:
            location = location_var.get().strip()
            weight_text = weight_entry.get().strip()

            if not location:
                result_var.set("Please pick a location!")
                return

            weight = float(weight_text)
            result_var.set("Calculating...")  # Simulate processing

            time.sleep(0.8)  # Simulate delay

            if location == "Ibeju-Lekki":
                charge = 5000 if weight >= 10 else 3500
            elif location == "Epe":
                charge = 10000 if weight >= 10 else 5000
            else:
                result_var.set("Hmm... unknown location?")
                return

            result_var.set(f"Charge: ₦{charge:,} for {weight}kg to {location}")
        except ValueError:
            result_var.set("Please enter a valid number for weight.")

    threading.Thread(target=process).start()

# GUI Setup
root = tk.Tk()
root.title("Simi Services - Delivery Estimator")
root.geometry("420x270")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

location_var = tk.StringVar()
result_var = tk.StringVar()

# UI Elements
tk.Label(root, text="Where are we delivering to?", font=("Segoe UI", 11), bg="#f4f4f4").pack(pady=6)
location_menu = ttk.Combobox(root, textvariable=location_var, values=["Ibeju-Lekki", "Epe"], state="readonly", width=30)
location_menu.pack()

tk.Label(root, text="How much does it weigh (kg)?", font=("Segoe UI", 11), bg="#f4f4f4").pack(pady=6)
weight_entry = tk.Entry(root, width=33)
weight_entry.insert(0, "e.g. 7.5")  # Hint
weight_entry.pack()

tk.Button(root, text="Tell me the price", command=calculate_charge, bg="#2d7d46", fg="white", width=20).pack(pady=12)

tk.Label(root, textvariable=result_var, font=("Segoe UI", 12, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

root.mainloop()