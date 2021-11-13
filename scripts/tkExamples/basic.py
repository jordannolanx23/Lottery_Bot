import tkinter as tk

class gui:
# constructor #
	def __init__(self):
		self.name = ""
		

	def start(self):
		window = tk.Tk()
		window.title("LotBot")

		# to display text labels#
		label = tk.Label(text="LotBot")
		label.pack()

		# to get single line text form user #
		entry = tk.Entry()
		entry.pack()
		text = entry.get()

		# to make a text box for larger text #
		text_box = tk.Text()
		text_box.pack()

		frame_a = tk.Frame()
		frame_b = tk.Frame()

		label_a = tk.Label(master=frame_a, text="I'm in Frame A")
		label_a.pack()

		label_b = tk.Label(master=frame_b, text="I'm in Frame B")
		label_b.pack()

		frame_a.pack()
		frame_b.pack()

		def handle_click(event):
			print("The button was clicked!")

		button = tk.Button(text="Click me!")

		button.bind("<Button-1>", handle_click)


		window.mainloop()
