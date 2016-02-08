#Projet LG by Fav/user2/user3
from tkinter import *

def LoadEntry(Chat, EntryText):
    if EntryText != '':
        Chat.config(state=NORMAL)
        if Chat.index('end') != None:
            LineNumber = float(Chat.index('end'))-1.0
            Chat.insert(END, "Vous: " + EntryText)
            Chat.tag_add("Vous", LineNumber, LineNumber+0.4)
            Chat.tag_config("Vous", foreground="#FF8000", font=("Arial", 12, "bold"))
            Chat.config(state=DISABLED)
            Chat.yview(END)


def FilteredMessage(EntryText):
    EndFiltered = ''
    for i in range(len(EntryText)-1,-1,-1):
        if EntryText[i]!='\n':
            EndFiltered = EntryText[0:i+1]
            break
    for i in range(0,len(EndFiltered), 1):
            if EndFiltered[i] != "\n":
                    return EndFiltered[i:]+'\n'
    return ''

def ClickAction():
    #Ecrire un message
    EntryText = FilteredMessage(ChatBox.get("0.0",END))
    LoadEntry(Chat, EntryText)

    #Scroll
    Chat.yview(END)

    #Supprimer un message
    ChatBox.delete("0.0",END)

def PressAction(event):
	ChatBox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	ChatBox.config(state=DISABLED)


root = Tk()
root.title('LGame')
root.geometry("800x460")
root.resizable(width=FALSE, height=FALSE)

#Fenêtre du Chat
Chat = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n")
Chat.config(state=DISABLED)

#Barre de Scrolling
scrollbar = Scrollbar(root, command=Chat.yview)
Chat['yscrollcommand'] = scrollbar.set

#Le Bouton "Envoyer"
SendButton = Button(root, font=30, text="Envoyer", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

#L'espace où taper son message
ChatBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")
ChatBox.bind("<Return>", DisableEntry)
ChatBox.bind("<KeyRelease-Return>", PressAction)

#Placer les différents tools sur l'interface
scrollbar.place(x=376,y=6, height=386)
Chat.place(x=6,y=6, height=386, width=370)
ChatBox.place(x=128, y=401, height=50, width=500)
SendButton.place(x=6, y=401, height=50)

