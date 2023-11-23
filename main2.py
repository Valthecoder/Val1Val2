import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_apples():
    try:
        money = float(entry_money.get())
        apple_price = float(entry_apple_price.get())
        if money < 0 or apple_price <= 0:
            raise ValueError("Please enter valid positive numbers.")
        num_apples = int(money / apple_price)
        remaining_money = money % apple_price
        result_str = f"You can buy {num_apples} apples.\nRemaining money: ₱{remaining_money:.2f}"
        show_result(result_str)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
def show_result(result_str):
    result_window = tk.Toplevel(window)
    result_window.title("Results")
    result_window.geometry("300x200")
    result_window.configure(bg="#E0E0E0")
    result_frame = tk.Frame(result_window, bg="#E0E0E0")
    result_frame.pack(expand=True, fill="both")
    result_label = tk.Label(result_frame, text=result_str, font=("Times", 14), bg="#E0E0E0")
    result_label.pack(pady=10)
    if apple_icon:
        resized_image = apple_image.resize((80, 80))
        resized_icon = ImageTk.PhotoImage(resized_image)
        apple_label = tk.Label(result_frame, image=resized_icon, bg="#E0E0E0")
        apple_label.image = resized_icon
        apple_label.pack(pady=10)
window = tk.Tk()
window.title("Apple Purchase Calculator")
window.geometry("400x300")
apple_icon_path = "Apple Icon.png"
try:
    apple_image = Image.open(apple_icon_path)
    apple_icon = ImageTk.PhotoImage(apple_image)
except FileNotFoundError:
    apple_icon = None
label_money = tk.Label(window, text="Enter your money (₱):", font=("Times", 12))
label_money.pack(pady=10)
entry_money = tk.Entry(window, font=("Times", 12))
entry_money.pack(pady=5)
label_apple_price = tk.Label(window, text="Enter the price of an apple (₱):", font=("Times", 12))
label_apple_price.pack(pady=10)
entry_apple_price = tk.Entry(window, font=("Times", 12))
entry_apple_price.pack(pady=5)
button_calculate = tk.Button(window, text="Calculate", command=calculate_apples, font=("Times", 12))
button_calculate.pack(pady=20)
if apple_icon:
    window.iconphoto(True, apple_icon)

window.mainloop()
