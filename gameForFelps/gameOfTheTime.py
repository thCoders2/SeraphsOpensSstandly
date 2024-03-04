from tkinter import *

root = Tk()
lilClicks = []
bigClicks = []

def addBigOne():
    click = Label(root, text='1 big Clicão!!', background='lightblue').pack()
    bigClicks.append(click)

def upgradeClicksSistem():
    if len(lilClicks) > 5:
        for labelzin in lilClicks[0:5]:
            labelzin.labels.pop()
            labelzin.destroy()
        addBigOne()
    root.after(1000, upgradeClicksSistem)

btnUpg1 = Button(root, text='upgrade 15 clicks!', state=DISABLED, command=upgradeClicksSistem)
def generateBtnUpgrade():
    btnUpg1.pack(side=LEFT)    

def checkClicks():
    curCli = len(lilClicks)
    if curCli > 5:
        generateBtnUpgrade()
    if curCli >= 15:
        btnUpg1.config(state='active')
    print(curCli)
    
def addOne():
    checkClicks()
    clickzin = Label(root, text='1 clickzin').pack()
    lilClicks.append(clickzin)
    addOne()


greetings = Label(root, text='Clicker idle test!!').pack()
btnAdd = Button(root, text='dê uma clicada ai vai!', command=addOne).pack()

root.mainloop()