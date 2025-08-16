import tkinter as tk


# --- Function ---
def valorant_vallis():
    result = entry.get().strip()

    if result == 'Vijay':
        message = 'Controller main'
    elif result == 'Gokulnathan':
        message = 'Sentinel main'
    elif result == 'Swami':
        message = 'Ascendent player'
    elif result == 'Sai':
        message = 'Flex player'
    elif result == 'Vishnu':
        message = 'Once in a bluemoon'
    elif result == 'GK':
        message = 'Breach main'
    else:
        message = 'Join Dothraki to get updates'

    # Custom result window
    result_win = tk.Toplevel(root)
    result_win.title("Valorant Result")

    # Window size
    width, height = 400, 200
    screen_w = result_win.winfo_screenwidth()
    screen_h = result_win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    result_win.geometry(f"{width}x{height}+{x}+{y}")
    result_win.configure(bg="#0f1923")  # Valorant dark background

    # Message label
    label = tk.Label(
        result_win,
        text=message,
        font=("Orbitron", 18, "bold"),  # Valorant-style font
        fg="#ff4655",  # Valorant red
        bg="#0f1923",
        wraplength=350,
        justify="center"
    )
    label.pack(expand=True)


# --- Main GUI ---
root = tk.Tk()
root.title("Valorant Vallis")

# Center main window
win_w, win_h = 500, 250
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w // 2) - (win_w // 2)
y = (screen_h // 2) - (win_h // 2)
root.geometry(f"{win_w}x{win_h}+{x}+{y}")
root.configure(bg="#0f1923")  # Valorant background

# Title label
label = tk.Label(
    root,
    text="Welcome to Dothraki!\nWhat is your name?",
    font=("Orbitron", 14, "bold"),
    fg="#ff4655",
    bg="#0f1923"
)
label.pack(pady=20)

# Input field
entry = tk.Entry(root, font=("Arial", 14), bg="#1f2a35", fg="white", insertbackground="white")
entry.pack(pady=10, ipadx=10, ipady=5)

# Button
button = tk.Button(
    root,
    text="Submit",
    command=valorant_vallis,
    font=("Orbitron", 12, "bold"),
    bg="#ff4655",
    fg="white",
    activebackground="#e03e4c",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=5
)
button.pack(pady=15)

root.mainloop()
