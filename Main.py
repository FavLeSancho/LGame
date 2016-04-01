#Projet LG by Fav/Shirotani/user3

from tkinter import *
from random import *
import random

def Main():
    Launcher.destroy() #Quand on clique, le bouton disparait

    Joueur = random.choice(RoleList)
    RoleList.remove(Joueur)
    #------------#
    Ordi1 = random.choice(RoleList)
    RoleList.remove(Ordi1)
    #------------#
    Ordi2 = random.choice(RoleList)
    RoleList.remove(Ordi2)
    #------------#
    Ordi3 = random.choice(RoleList)
    RoleList.remove(Ordi3)
    #------------#
    Ordi4 = random.choice(RoleList)
    RoleList.remove(Ordi4)

    if Joueur == 'LoupGarou':
        PictureBox.create_image(70, 70, image=ImgLoupGarou)
    elif Joueur == 'Chasseur':
        ''
    elif Joueur == 'Cupidon':
        ''
    else:
        ''
        

    

    


def FinalMessage(Chat, EntryText):
    if EntryText != '':
        Chat.config(state=NORMAL)
        if Chat.index('end') != None:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Vous: " + EntryText)
            Chat.tag_add("Vous", Ligne, Ligne+0.4)
            Chat.tag_config("Vous", foreground="#FF8000", font=("Arial", 12, "bold")) #Police, couleur...
            Chat.config(state=DISABLED)
            Chat.yview(END)


#A supprimer
def Filtration(EntryText): #Permet de filtrer les messages (EntryText)
    DoneFilter = '' #On initialise la variable qu'on va renvoyer
    for i in range(len(EntryText)-1,-1,-1): #On va regarder dans notre message (step = -1)
        if EntryText[i]!='\n': #Si le message n'est pas "vide"
            DoneFilter = EntryText[0:i+1] #On remplit la varible avec le message (i+1 = limite du message)
            break #Et on sort de la boucle for
    for i in range(0,len(DoneFilter), 1): #On va regarder notre message "filtré"
        if DoneFilter[i] != "\n": #Si il n'est pas "vide"
            return DoneFilter[i:]+'\n' #On le 'renvoie', avec un '\n' pour sauter une ligne
        return '' #Si le message est vide, on ne 'renvoie' rien

def ClicAction():
    #On envoie le texte dans le fonction Filtration
    EntryText = Filtration(ChatBox.get("0.0",END))
    #Puis on l'envoie dans la fonction Command, pour regarder si il y a une éventuelle commande
    Command(EntryText)
    #FinalMessage(Chat, EntryText)
    #Scroll du message
    Chat.yview(END)
    #Supprimer le message de la ChatBox après envoi
    ChatBox.delete("0.0",END)

def ReleaseEnter(event):
    ChatBox.config(state=NORMAL) #Après avoir relaché ENTER, on re-initialise la ChatBox (de nouveau dispo)
    ClicAction() #Et on utilise la fonction ClicAction

def StopChat(event):
    #Permet de désactiver le chat quand on appuie sur ENTER (pour eviter de sauter un espace en écrivant)
    ChatBox.config(state=DISABLED)




#---------------------------------------------------#
#---------------GESTION DES COMMANDES---------------#
#---------------------------------------------------#

def Command(EntryText):
    if EntryText != None: #Si le texte n'est vide
        if EntryText[0] == '.': #Si le texte commence par un point, on le considère comme une commande (si elle existe)
            #Début des commandes#
            
            if EntryText[:6] == '.vote ':#Commande .vote
                EntryText = EntryText.replace("\n", '') #On enlève le retour à la ligne (fixage de bugs)
                EntryText = EntryText.replace(".vote ", '') #On enlève le '.vote ' pour ne reccuperer que le pseudo
                if EntryText in PlayerList: #Si le pseudo fait partie de la liste de Joueurs
                    Vote(EntryText)
                    
            #Début du message Chat
                    VotedMessage = "Vous avez voté contre " + EntryText + '.' #Le message à envoyer
                    Chat.config(state=NORMAL) # On 'ouvre' le chat
                    if Chat.index('end') != None:
                        Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                        Chat.insert(END, VotedMessage + '\n') #On l'insert dans le Chat
                        Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                        Chat.tag_config('Start', foreground="#713070", font=("Arial", 15, "bold")) #On lui donne une couleur, taille
                        Chat.config(state=DISABLED)#Et on 'ferme' le chat
                        Chat.yview(END)
            #Fin du Message Chat
                        
                else: #Sinon, on ne revoie rien
                    EntryText = ''
            else:
                FinalMessage(Chat, EntryText) #Si ce n'est pas une commande connue, on envoie le message tel quel
        else:
            FinalMessage(Chat, EntryText) # Si le message ne commence pas par un point, on l'envoie normalement



def Vote(Player):
    global JoueurIsVoted,Ordi1IsVoted,Ordi2IsVoted,Ordi3IsVoted,Ordi4IsVoted
    for Player in PlayerList:
        if Player == 'Joueur':
            JoueurIsVoted += 1
        if Player == 'Ordi1':
            Ordi1IsVoted += 1
        if Player == 'Ordi2':
            Ordi2IsVoted += 1
        if Player == 'Ordi3':
            Ordi3IsVoted += 1
        if Player == 'Ordi4':
            Ordi4IsVoted += 1

#---------------------------------------------------#
#----------------GESTION DU GRAPHISME---------------#
#---------------------------------------------------#

root = Tk() #On définit notre fenêtre
root.title('LGame') #On définit notre nom, ici LGame
root.geometry("800x460") # On définit sa taille
root.resizable(width=FALSE, height=FALSE) # On dit que la fenêtre ne peut pas être redimensionnée

#Fenêtre du Chat
Chat = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",) #Customisation de la fenêtre de chat
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n") #On insère du texte
Chat.config(state=DISABLED) #Une fenêtre où ne peut pas écrire, sinon wtf

PictureBox = Canvas(root, width=200, height=200)

#Barre de Scrolling
scrollbar = Scrollbar(root, command=Chat.yview)
Chat['yscrollcommand'] = scrollbar.set

#Le Bouton "Envoyer"
BoutonEnvoi = Button(root, font=30, text="Envoyer", width='12', height='5', #Customisation du Bouton
bd=0, bg="#FFBF00", activebackground="#FACC2E", #Customisation du Bouton
command=ClicAction) #Quand on clique, ça lance la fonction "ClicAction"

#Le Bouton "Lancer la partie"
Launcher = Button(root, font=30, text="Lancer la partie", width='12', height='5',
bd=0, bg="#FFBF00", activebackground="#FACC2E",
command=Main)

#L'espace où taper son message
ChatBox = Text(root, bd=0, bg="white",width='29', height='5', font="Arial") # Customisation de la ChatBox (Taille/police/fond)
ChatBox.bind("<Return>", StopChat) #Quand on appuie sur Enter, Utiliser la fonction StopChat
ChatBox.bind("<KeyRelease-Return>", ReleaseEnter) #Quand on relache Enter, Utiliser la fonction ReleaseEnter

#Placer les différents tools sur l'interface
scrollbar.place(x=376,y=6, height=386) #La Barre de Scroll
Chat.place(x=6,y=6, height=386, width=370) #Le cadre du Chat
ChatBox.place(x=128, y=401, height=50, width=500) #Le cadre de la boite à message (lol)
BoutonEnvoi.place(x=6, y=401, height=50) #Le cadre du bouton
Launcher.place(x=650, y=401, height=50 ) #Le cadre du bouton
PictureBox.place(x=650, y=10)


#Images
ImgLoupGarou = PhotoImage(file ='')
ImgCupidon = PhotoImage(file ='')
ImgChasseur = PhotoImage(file ='')
ImgSorciere = PhotoImage(file ='')


#---------------------------------------------------#
#----------------GESTION DES PLAYERS----------------#
#---------------------------------------------------#



PlayerList = ['Player','Ordi1','Ordi2','Ordi3','Ordi4']
RoleList = ['LoupGarou','LoupGarou','Cupidon','Sorciere','Chasseur']
JoueurIsVoted = 0
Ordi1IsVoted = 0
Ordi2IsVoted = 0
Ordi3IsVoted = 0
Ordi4IsVoted = 0
