from functions import arrPrinter, checkSizeLockArr
from databases import karms,fearArr,lilFearArr
import tkinter as tk
# arrPrinter(fearArr, 3)
possiblesPerson = [karms, fearArr, lilFearArr]
names = ['karms', 'fear', 'lilFear']
# global variable to store the current character index
current = 0
currentSpeed = 200
maxSpeed = 400
nameCur = 'karms'
# create the root window
root = tk.Tk()
root.title("Character Selection")

# create the canvas widget
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# create the text object for the character
char = canvas.create_text(150, 100, text=possiblesPerson[current][0], font=("Courier", 32), fill="blue")

# create the text object for the name
name = canvas.create_text(150, 150, text=names[current], font=("Courier", 16), fill="black")

# function to update the character animation
def updateChar():
    global current
    # get the next item in the array
    next_item = possiblesPerson[current].pop(0)
    # update the text object
    canvas.itemconfig(char, text=next_item)
    # append the item back to the array
    possiblesPerson[current].append(next_item)
    # schedule the next update after 200 milliseconds
    root.after(currentSpeed, updateChar)

# function to switch characters
def switchChar():
    global current
    # increment the current index by one modulo the length of the array
    current = (current + 1) % len(possiblesPerson)
    # update the name text object
    canvas.itemconfig(name, text=names[current])

# function to go to fase
def openMap():
    inputsOfMap= {
    'character':possiblesPerson[current],
    'name':names[current],
    'hat':None,
    'onStage': 0,
    }
    # loadTheMap(inputsOfMap)

def changeSpeed():
    from random import random
    global  maxSpeed
    global  currentSpeed
    print(currentSpeed)
    currentSpeed = int(random() * maxSpeed)
    print(currentSpeed)

# create the button widget for switching characters
button = tk.Button(root, text="Next Character", command=switchChar)
button.pack()


#Botão que vai pra fase!!!!
# button = tk.Button(root, text='Lets Plays!', command=openMap)

#Botão que altera velocidade
button2 = tk.Button(root, text='change speed', command=changeSpeed)
button2.pack()

def openNoteCreator():
    # Retrieve the global variable 'name'
    global nameCurCur

    # Create a new window
    window = tk.Tk()

    # Set the title of the window
    window.title("New Window")

    # Create a label for the 'nameCur'
    nameCur_label = tk.Label(window, text="name: " + nameCur)
    nameCur_label.pack()

    # Create an entry widget for the 'title'
    title_entry = tk.Entry(window)
    title_entry.pack()

    # Create a text area for the 'note'
    note_text = tk.Text(window, width=8, height=4)
    note_text.pack()

    # Create a function to save the content to a file
    def save_content():
        title = title_entry.get()
        note = f"""{note_text.get("1.0", tk.END)}""" 
        file_path = os.path.join("content", title)
        with open(file_path, "w") as file:
            file.write(f"Note: {note}")

    # Create a button to save the content
    confirm_button = tk.Button(window, text="Confirm", command=save_content)
    confirm_button.pack()

    # Start the Tkinter event loop
    window.mainloop()
  

btnNote = tk.Button(root, text='create a Note', command=openNoteCreator)
btnNote.pack()


# start the character animation
updateChar()

# start the main loop
root.mainloop()