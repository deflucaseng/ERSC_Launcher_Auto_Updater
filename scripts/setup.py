
# Check if first time exists, if so, remove it, then download the latest release
# Queue the prompter for entering the coop session password, which should be done in flask. 
from auto_updater import autoUpdater
import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
from resource_path_getter import resource_path
class setup:

	def get_coop_password(self):
		def get_input():
			user_input = entry.get()
			with open(os.path.join("text_resources", "cooppassword"), "w") as cooppasswordfile:
				cooppasswordfile.write(user_input)
			root.destroy()

		root = tk.Tk()
		root.title("Co-Op Password Entry")

		# Load and resize the background image
		original_image = Image.open(os.path.join("assets", "soyjack.png"))
		width, height = original_image.size
		new_width, new_height = width // 4, height // 4
		bg_image = original_image.resize((new_width, new_height), Image.LANCZOS)
		bg_photo = ImageTk.PhotoImage(bg_image)

		# Set the window size to match the resized image
		root.geometry(f"{new_width}x{new_height}")

		# Create a label with the image
		bg_label = tk.Label(root, image=bg_photo)
		bg_label.place(x=25, y=105, relwidth=1, relheight=1)

		# Create a frame for other widgets
		frame = tk.Frame(root, bg='#F7F7F7', bd=5)
		frame.place(relx=0.5, rely=0.5, anchor='center')

		# Style configuration
		style = ttk.Style()
		style.theme_use('clam')
		style.configure("TEntry", fieldbackground="white", foreground="black")
		style.configure("TButton", background="#5E5E5E", foreground="white")

		# Create and place the label
		label = tk.Label(frame, text="Enter your Co-Op password", font=("Segoe UI", 10), bg='#F7F7F7')
		label.pack(pady=(10,5))

		# Create and place the Entry widget
		entry = ttk.Entry(frame, width=25, font=("Segoe UI", 8), style="TEntry")
		entry.pack(pady=5)

		# Create and place a button to submit the input
		submit_button = ttk.Button(frame, text="Submit", command=get_input, style="TButton")
		submit_button.pack(pady=10)

		# Start the Tkinter event loop
		root.mainloop()


	def do_setup(self):
		self.get_coop_password()


