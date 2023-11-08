import tkinter as tk
import random

def shuffle_names(names, total_roll, shuffle_number_var):
    current_shuffle = 1
    while current_shuffle <= total_roll:
        random.shuffle(names)
        text_widget.delete('1.0', tk.END)
        for name in names:
            text_widget.insert(tk.END, name + '\n')
        shuffle_number_var.set(current_shuffle)
        window.update()
        current_shuffle += 1
        window.after(200)  # Delay for animation effect

def roll_dice_and_randomize():
    # Simulate rolling two 6-sided dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total_roll = dice1 + dice2
    result_label.config(text=f'Dice Result: Dice 1: {dice1}, Dice 2: {dice2}, Total: {total_roll}')

    # Get the list of names from the text widget and filter out empty lines
    names_text = text_widget.get('1.0', tk.END)  # Read all text
    names = [name for name in names_text.split('\n') if name.strip()]  # Exclude empty lines

    if total_roll > 4:
        shuffle_number_var.set(0)
        shuffle_names(names, total_roll, shuffle_number_var)

def copy_selected():
    # Programmatically select the text
    text_widget.tag_add("sel", "1.0", "end")
    text_widget.event_generate('<<Copy>>')  # Simulate Ctrl+C to copy selected text
    copied_label.config(text="Text has been copied")
    window.after(3000, clear_copied_message)  # Hide the message after 3 seconds

def clear_copied_message():
    copied_label.config(text="")  # Clear the message

# Create the main window
window = tk.Tk()
window.title('JNE Dice Roll and Name Randomizer')

# Configure rows and columns to expand dynamically
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Create and configure widgets
roll_button = tk.Button(window, text='Roll Dice and Randomize Names', command=roll_dice_and_randomize)
text_label = tk.Label(window, text='Enter names, each on a new line:')
text_widget = tk.Text(window)
result_label = tk.Label(window, text='')
shuffle_number_var = tk.StringVar()
shuffle_number_label = tk.Label(window, textvariable=shuffle_number_var)

copy_button = tk.Button(window, text='Copy Selected', command=copy_selected)
copied_label = tk.Label(window, text="")

# Add widgets to the grid
roll_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
text_label.grid(row=1, column=0, columnspan=2, sticky="nsew")
text_widget.grid(row=2, column=0, columnspan=2, sticky="nsew")
result_label.grid(row=3, column=0, columnspan=2, sticky="nsew")
shuffle_number_label.grid(row=4, column=0, columnspan=2, sticky="nsew")
copy_button.grid(row=5, column=0, columnspan=2, sticky="nsew")
copied_label.grid(row=6, column=0, columnspan=2, sticky="nsew")

# Start the GUI event loop
window.mainloop()
