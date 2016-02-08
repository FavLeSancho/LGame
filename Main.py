#Projet LG by Fav/Shirotani/user3
from tkinter import *

def LoadEntry(Chat, EntryText):
    if EntryText != '':
        Chat.config(state=NORMAL)
        if Chat.index('end') != None:
            LineNumber = float(Chat.index('end'))-1.0
            Chat.insert(END, "Vous: " + EntryText)
            Chat.tag_add("Vous", LineNumber, LineNumber+0.4)
            Chat.tag_config("Vous", foreground="#FF8000", font=("Arial", 12, "bold")) #Police, couleur...
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
    #On envoie le texte dans la fonction LoadEntry, pour ressortir l'effet stylisé, avec le Vous: "message"
    LoadEntry(Chat, EntryText)

    #Scroll du message
    Chat.yview(END)

    #Supprimer le message de la ChatBox après envoi
    ChatBox.delete("0.0",END)

def PressAction(event):
	ChatBox.config(state=NORMAL) #Après avoir envoyé un message, on re-initialise la ChatBox
	ClickAction() #Et on utilise la fonction ClickAction
	
def DisableEntry(event):
	#Permet de désactiver le chat quand on appuie sur ENTER (pour eviter de sauter un espace en écrivant)
	ChatBox.config(state=DISABLED)


root = Tk() #On définit notre fenêtre
root.title('LGame') #On définit notre nom, ici LGame
root.geometry("800x460") # On définit sa taille
root.resizable(width=FALSE, height=FALSE) # On dit que la fenêtre ne peut pas être redimensionnée

#Fenêtre du Chat
Chat = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",) #Customisation de la fenêtre de chat
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n") #On insère du texte
Chat.config(state=DISABLED) #Une fenêtre où ne peut pas écrire, sinon wtf

#Barre de Scrolling
scrollbar = Scrollbar(root, command=Chat.yview)
Chat['yscrollcommand'] = scrollbar.set

#Le Bouton "Envoyer"
SendButton = Button(root, font=30, text="Envoyer", width="12", height=5, #Customisation du Bouton
                    bd=0, bg="#FFBF00", activebackground="#FACC2E", #Customisation du Bouton
                    command=ClickAction) #Quand on clique, ça lance la fonction "ClicAction"

#L'espace où taper son message
ChatBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial") # Customisation de la ChatBox
ChatBox.bind("<Return>", DisableEntry) #Quand on appuie sur Enter, Utiliser la fonction DisableEntry
ChatBox.bind("<KeyRelease-Return>", PressAction)  #Quand on relache Enter, Utiliser la fonction PressAction

#Placer les différents tools sur l'interface
scrollbar.place(x=376,y=6, height=386) #La Barre de Scroll
Chat.place(x=6,y=6, height=386, width=370) #Le cadre du Chat
ChatBox.place(x=128, y=401, height=50, width=500) #Le cadre de la boite à message (lol)
SendButton.place(x=6, y=401, height=50) #Le cadre du bouton

