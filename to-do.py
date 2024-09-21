import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x400")
window.configure(bg="#ADD8E6")  # Light blue background

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def show_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Create widgets with colors
frame = tk.Frame(window, bg="#ADD8E6")
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Arial", 12),
    bg="#F5F5DC",  # Beige background for listbox
    fg="#000000",  # Black font color
    selectbackground="#FFB6C1",  # Light pink selection background
    selectforeground="#000000"  # Black font color on selection
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

task_entry = tk.Entry(
    window,
    font=("Arial", 12),
    bg="#FFFACD",  # Lemon chiffon background
    fg="#000000",  # Black font color
    insertbackground="#000000"  # Cursor color
)
task_entry.pack(pady=10)

add_button = tk.Button(
    window,
    text="Add Task",
    width=20,
    command=add_task,
    bg="#32CD32",  # Lime green background
    fg="#FFFFFF",  # White text
    activebackground="#228B22",  # Forest green on click
    activeforeground="#FFFFFF"  # White text on click
)
add_button.pack(pady=10)

delete_button = tk.Button(
    window,
    text="Delete Task",
    width=20,
    command=delete_task,
    bg="#FF4500",  # Orange red background
    fg="#FFFFFF",  # White text
    activebackground="#B22222",  # Firebrick on click
    activeforeground="#FFFFFF"  # White text on click
)
delete_button.pack(pady=10)

# Run the main loop
window.mainloop()
