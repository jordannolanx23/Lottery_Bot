import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from lotbot import lotbot

# create lotbot as global #
bot = lotbot()

### methods to make lotbot calls and display to gui ###

# will call and display lotbot random algorithim #
def random():
	bot.randomGuess()
	text = bot.send()
	# example to place text first #
	#txt_edit.insert(0.0, str(text))
	txt_edit.insert(tk.END, str(text))
	txt_edit.insert(tk.END, ',')
	#txt_edit.insert(tk.END, "")

# will save Data to a file #
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
	

## to create world ##
window = tk.Tk()
window.title("LotBot")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

txt_edit = tk.Text(window)
#entry = tk.Entry(window)
#entry2 = tk.Entry(window)

## Click buttons to run algorthims ##
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_random = tk.Button(fr_buttons, text="Randomize", command=random)
btn_save = tk.Button(fr_buttons, text="Export", command=save_file)

## button location in window ##
btn_random.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

## set up the window buttons on left text box on right ##
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")



window.mainloop()

