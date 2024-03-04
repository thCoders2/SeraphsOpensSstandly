import tkinter as tk
from databases import karms, fearArr, lilFearArr

def initialize_character_selection():
    possiblesPerson = [karms, fearArr, lilFearArr]
    names = ['karms', 'fear', 'lilFear']
    current = 0
    currentSpeed = 300
    maxSpeed = 400
    nameCur = 'karms'

    def updateChar():
        nonlocal current
        next_item = possiblesPerson[current].pop(0)
        canvas.itemconfig(char, text=next_item)
        possiblesPerson[current].append(next_item)
        root.after(currentSpeed, updateChar)

    def changeSpeed():
        from random import random
        nonlocal currentSpeed
        currentSpeed = int(random() * maxSpeed)

    def openNoteCreator():
        window = tk.Tk()
        window.title("New Window")

        nameCur_label = tk.Label(window, text="name: " + nameCur)
        nameCur_label.pack()

        title_entry = tk.Entry(window)
        title_entry.pack()

        note_text = tk.Text(window, width=8, height=4)
        note_text.pack()

        def save_content():
            import os
            title = title_entry.get()
            note = f"{note_text.get('1.0', tk.END)}"
            file_path = os.path.join("content", title)
            with open(file_path, "w") as file:
                file.write(f"Note: {note}")

        confirm_button = tk.Button(window, text="Confirm", command=save_content)
        confirm_button.pack()

        window.mainloop()

    root = tk.Tk()
    root.title("Character Selection")

    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()

    char = canvas.create_text(150, 100, text=possiblesPerson[current][0], font=("Courier", 32), fill="blue")
    name = canvas.create_text(150, 150, text=names[current], font=("Courier", 16), fill="black")

    button2 = tk.Button(root, text='change speed', command=changeSpeed)
    button2.pack()

    btnNote = tk.Button(root, text='create a Note', command=openNoteCreator)
    btnNote.pack()

    updateChar()
    root.mainloop()

# Call the function to initialize the character selection interface
initialize_character_selection()
