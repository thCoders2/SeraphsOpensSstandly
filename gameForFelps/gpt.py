from tkinter import *

root = Tk()
lilClicks = []
bigClicks = []

def addBigOne():
    click = Label(root, text='1 big Clicão!!', background='lightblue')
    click.pack()
    bigClicks.append(click)

def upgradeClicksSistem():
    if len(lilClicks) > 5:
        for labelzin in lilClicks[-5:]:
            labelzin.destroy()
        addBigOne()
        lilClicks.pop()
        lilClicks.pop()
        lilClicks.pop()
        lilClicks.pop()
        lilClicks.pop()
    root.after(1000, upgradeClicksSistem)

btnUpg1 = Button(root, text='upgrade 15 clicks!', state=DISABLED, command=upgradeClicksSistem)
def generateBtnUpgrade():
    btnUpg1.pack(side=LEFT)    

def checkClicks():
    curCli = len(lilClicks)
    if curCli > 5:
        generateBtnUpgrade()
    if curCli >= 5:
        btnUpg1.config(state='active')
    print(curCli)
    
def addOne():
    checkClicks()
    clickzin = Label(root, text='1 clickzin')
    clickzin.pack()
    lilClicks.append(clickzin)


greetings = Label(root, text='Clicker idle test!!')
greetings.pack()
btnAdd = Button(root, text='dê uma clicada ai vai!', command=addOne)
btnAdd.pack()

root.mainloop()
