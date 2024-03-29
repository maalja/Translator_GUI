from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Translator')
root.iconbitmap('C:/Users/mahrh/PycharmProjects/pythonProject/translator_icon.ico')
root.geometry("880x300")
root.configure(background="dark green")

def translate_it():
	# Delete Any Previous Translations
	translated_text.delete(1.0, END)

	try:
		# Get Languages From Dictionary Keys
		# Get the From Langauage Key
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		# Get the To Language Key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		# Turn Original Text into a TextBlob
		words = textblob.TextBlob(original_text.get(1.0, END))

		# Translate Text
		words = words.translate(from_lang=from_language_key , to=to_language_key)

		# Output translated text to screen
		translated_text.insert(1.0, words)

	except Exception as e:
		messagebox.showerror("Translator", e)

def clear():
	# Clear the text boxes
	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)


# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())
# Text Boxes
original_text = Text(root,height=10, width=40)
original_text.grid(row=0, column=0, pady=40, padx=20)
translate_button = Button(root, text="Translate!", fg="white", bg="black",font=("Helvetica", 20), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=40, padx=20)

# Combo boxes
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

# Clear button
clear_button = Button(root, text="Clear",fg="white", bg="red", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()