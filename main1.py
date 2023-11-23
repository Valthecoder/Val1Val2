import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def calculate_total():
    try:
        apples = int(apple_entry.get())
        oranges = int(orange_entry.get())
        apple_price = 20
        orange_price = 25
        total_amount = (apples * apple_price) + (oranges * orange_price)
        result_window = tk.Toplevel(root)
        result_window.title("Result")
        tk.Label(result_window, text="Result", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(result_window, text=f"Total Amount: {total_amount} pesos", font=("Helvetica", 14)).pack(pady=5)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid quantities for apples and oranges.")


root = tk.Tk()
root.title("Fruit Shop")
root.configure(bg="#F5F5F5")
apple_icon_path = "Apple Icon.png"  # Replace with the actual path to your apple icon
orange_icon_path = "Orange Icon.png"  # Replace with the actual path to your orange icon
apple_icon = Image.open(apple_icon_path).resize((30, 30))
apple_icon = ImageTk.PhotoImage(apple_icon)
orange_icon = Image.open(orange_icon_path).resize((40, 30))
orange_icon = ImageTk.PhotoImage(orange_icon)
tk.Label(root, text="Fruit Shop", font=("Helvetica", 16), bg="#F5F5F5").pack(pady=10)
tk.Label(root, text="How many apples do you want?", font=("Hobo Std", 12), bg="#F5F5F5").pack()
apple_entry = tk.Entry(root, font=("Helvetica", 12))
apple_entry.pack()
tk.Label(root, image=apple_icon, bg="#F5F5F5").pack()
tk.Label(root, text="How many oranges do you want?", font=("Helvetica", 12), bg="#F5F5F5").pack()
orange_entry = tk.Entry(root, font=("Helvetica", 12))
orange_entry.pack()
tk.Label(root, image=orange_icon, bg="#F5F5F5").pack()
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
calculate_button.pack(pady=20)
root.mainloop()
