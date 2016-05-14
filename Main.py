from tkinter import *
from random import *
from time import *
import random

def Main():
    Launcher.destroy() #Quand on clique, le bouton disparait
    Chat.config(state = NORMAL)
    Ligne = float(Chat.index('end'))-1.0
    Chat.insert(END, "Le jeu commence ! \n \n")
    Chat.tag_add("start", Ligne, Ligne + 0.17)
    Chat.tag_config("start", foreground="#008000", font=("Arial", 20)) #, "bold"

    

    if Joueur == 'LoupGarou':
        PictureBox.create_image(75, 75, image=ImgLoupGarou)
        Chat.insert(END, RoleLG + '\n')
        Chat.insert(END, "Utilisez la commande '.kill + nom', pour éliminer un joueur." + '\n')
    elif Joueur == 'Chasseur':
        PictureBox.create_image(75, 75, image=ImgChasseur)
        Chat.insert(END, RoleChassou + '\n')
        Chat.insert(END, """Utilisez la commande '.revenge + nom', pour éliminer quelqu'un lorsque
vous mourrez.""" + '\n')
    elif Joueur == 'Cupidon':
        PictureBox.create_image(75, 75, image=ImgCupidon)
        Chat.insert(END, RoleCupi + '\n')
        Chat.insert(END, "Utilisez la commande '.love + nom' pour vous unir avec un joueur." + '\n')
    else:
        PictureBox.create_image(75, 75, image=ImgSorciere)
        Chat.insert(END, RoleSoso + '\n')
        Chat.insert(END, "Utilisez la commande '.poison + nom' pour éliminer un joueur." + '\n')

    Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
    Chat.insert(END, Night + '\n')
    Chat.config(state = DISABLED)
    TimerNuit()

        
    
def TimerNuit():
    global secNuit, isNuit, CanPlayLG, CanPlaySoso, CanPlayCupi, CanPlayChassou, AlreadyPlayedCupi, AlreadyPlayedSoso, AlreadyPlayedChassou, finish
    BackGround.create_image(400, 230, image=FondNuit)
    if secNuit == 55:
        if AlreadyPlayedCupi != True:
            Chat.config(state = NORMAL)
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, ActionCupi + '\n')
            Chat.tag_add("CupiText", Ligne, Ligne + 0.41)
            Chat.tag_config("CupiText", foreground="#FF8000", font=("Arial", 12, "bold")) 
            if Joueur == 'Cupidon':
                CanPlayCupi = True
                Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
            else:
                while finish is False:
                    random.shuffle(PlayerList)
                    Lover = random.choice(PlayerList)
                    if Lover != 'Cupidon':
                        print(Lover)
                        Love(Lover)
                        finish = True
                    else:
                        finish = False
                
            finish = False
            Chat.config(state = DISABLED)

    if secNuit == 40:
        Chat.config(state = NORMAL)
        Ligne = float(Chat.index('end'))-1.0
        Chat.insert(END, ActionLG + '\n')
        Chat.tag_add("LGText", Ligne, Ligne + 0.47)
        Chat.tag_config("LGText", foreground="#FF8000", font=("Arial", 12, "bold")) 
        if Joueur == 'LoupGarou':
            CanPlayLG = True
            Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
        else:
            while finish is False:
                random.shuffle(PlayerList)
                Victime = random.choice(PlayerList)
                if Victime != 'LoupGarou':
                    Kill(Victime)
                    finish = True
                else:
                    finish = False

        AlreadyPlayedLG = True
        finish = False
        Chat.config(state = DISABLED)
        

    if secNuit == 30:
        if AlreadyPlayedSoso != True:
            Chat.config(state = NORMAL)
            
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, ActionSoso + '\n')
            Chat.tag_add("SosoText", Ligne, Ligne + 0.43)
            Chat.tag_config("SosoText", foreground="#FF8000", font=("Arial", 12, "bold")) 
            if Joueur == 'Sorciere':
                CanPlaySoso = True
                Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
            else:
                while finish is False:
                    random.shuffle(PlayerList)
                    Poisonned = random.choice(PlayerList)
                    if Poisonned != 'Sorciere':
                        Kill(Poisonned)
                        finish = True
                    else:
                        finish = False
            AlreadyPlayedSoso = True
                    
            finish = False
            Chat.config(state = DISABLED)
    

    # Ordre : ActionCupi / ActionLG / ActionSoso 
    if secNuit != 0:
        isNuit = True
        secNuit -= 1
        TimerBox['text'] = 'Nuit :\n' + 'Temps restant : ' + str(secNuit)
        TimerBox.after(1000, TimerNuit)
    elif secNuit == 0:
        AlreadyPlayedLG = False
        Chat.config(state = NORMAL)
        Chat.insert(END, DeadList)
        if Joueur not in PlayerList:
            Chat.insert(END, "- Joueur" + "(" + Joueur + ")" +'\n' +'\n')
        if Ordi1 not in PlayerList:
            Chat.insert(END, "- Ordi1" + "(" + Ordi1 + ")" + '\n' +'\n')
        if Ordi2 not in PlayerList:
            Chat.insert(END, "- Ordi2" + "(" + Ordi2 + ")" + '\n' +'\n')
        if Ordi3 not in PlayerList:
            Chat.insert(END, "- Ordi3" + "(" + Ordi3 + ")" + '\n' +'\n')
        if Ordi4 not in PlayerList:
            Chat.insert(END, "- Ordi4" + "(" + Ordi4 + ")" + '\n' +'\n')

        if 'Chasseur' not in PlayerList:
            if AlreadyPlayedChassou != True:
                Chat.config(state = NORMAL)
            
                Ligne = float(Chat.index('end'))-1.0
                Chat.insert(END, ChoixChassou + '\n')
                Chat.tag_add("ChassouText", Ligne, Ligne + 0.61)
                Chat.tag_config("ChassouText", foreground="#008000", font=("Arial", 12, "bold")) 
                if Joueur == 'Chasseur':
                    CanPlayChassou = True
                    Chat.insert(END, '[Privé] Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
                else:
                    random.shuffle(PlayerList)
                    Killed = random.choice(PlayerList)
                    Kill(Killed)
                AlreadyPlayedChassou = True
            


        Chat.insert(END, Vote + '\n' + '\n')
        
        if Ordi1 in PlayerList:
            Choix = random.choice(PlayerList)
            print(Choix)
            Vote(Choix)
        if Ordi2 in PlayerList:
            Choix = random.choice(PlayerList)
            print(Choix)
            Vote(Choix)
        if Ordi3 in PlayerList:
            Choice = random.choice(PlayerList)
            print(Choice)
            Vote(Choice)
        if Ordi4 in PlayerList:
            Choice = random.choice(PlayerList)
            print(Choice)
            Vote(Choice)



        Chat.config(state = DISABLED)
        Chat.yview(END)

            
        TimerBox['text'] = ''
        isNuit = False
        TimerJour()
        secNuit += 60
        

def TimerJour():
    global secJour, isJour
    BackGround.create_image(400, 230, image=FondJour)
    if secJour != 0:
        isJour = True
        secJour -= 1
        TimerBox['text'] = 'Jour :\n' +'Temps restant : ' + str(secJour)
        TimerBox.after(1000, TimerJour)
    else:
        #Gestion de la mort du voté ici
        Chat.config(state = NORMAL)
        if JoueurIsVoted > Ordi1IsVoted and JoueurIsVoted > Ordi2IsVoted and JoueurIsVoted > Ordi3IsVoted and JoueurIsVoted > Ordi4IsVoted:
            PlayerList.remove(Joueur)
            Chat.insert(END, "Le village a décidé d'éliminer Joueur qui était" + Joueur + ".")
        elif Ordi1IsVoted > JoueurIsVoted and Ordi1IsVoted > Ordi2IsVoted and Ordi1IsVoted > Ordi3IsVoted and Ordi1IsVoted > Ordi4IsVoted:
            PlayerList.remove(Ordi1)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi1 qui était" + Ordi1 + ".")

        elif Ordi2IsVoted > JoueurIsVoted and Ordi2IsVoted > Ordi1IsVoted and Ordi2IsVoted > Ordi3IsVoted and Ordi2IsVoted > Ordi4IsVoted:
            PlayerList.remove(Ordi2)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi2 qui était" + Ordi2 + ".")

        elif Ordi3IsVoted > JoueurIsVoted and Ordi3IsVoted > Ordi1IsVoted and Ordi3IsVoted > Ordi2IsVoted and Ordi3IsVoted > Ordi4IsVoted:
            PlayerList.remove(Ordi3)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi3 qui était" + Ordi3 + ".")

        elif Ordi4IsVoted > JoueurIsVoted and Ordi4IsVoted > Ordi1IsVoted and Ordi4IsVoted > Ordi2IsVoted and Ordi4IsVoted > Ordi3IsVoted:
            PlayerList.remove(Ordi4)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi4 qui était" + Ordi4 + ".")

        Chat.config(state = DISABLED)
            
        TimerBox['text'] = ''
        isJour = False
        TimerNuit()
        secJour += 60


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


#A simplifier
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
                if isNuit == True:
                    EntryText = ''
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

            elif EntryText[:6] == '.kill ':#Commande .kill
                if Joueur == 'LoupGarou':
                    if isJour == True:
                        EntryText = ''
                    if CanPlayLG == False:
                        EntryText = ''

                    if Joueur not in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".kill ", '')
                        if EntryText in PlayerList:
                            if AlreadyPlayedLG != True:
                                Kill(EntryText)

                                KillMessage = "Vous avez décidé de tuer " + EntryText + '.\n Il ne se reveillera pas demain. \n'
                                Chat.config(state=NORMAL)
                                if Chat.index('end') != None:
                                    Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                                    Chat.insert(END, KillMessage + '\n') #On l'insert dans le Chat
                                    Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                                    Chat.tag_config('Start', foreground="#ED0000", font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                                    Chat.config(state=DISABLED)#Et on 'ferme' le chat
                                    Chat.yview(END)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''

            elif EntryText[:9] == '.revenge ':#Commande .revenge (chasseur)
                if Joueur == 'Chasseur':
                    if isJour == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = ''
                    if CanPlayChassou == False:
                        EntryText = ''
                    EntryText = EntryText.replace("\n", '') 
                    EntryText = EntryText.replace(".revenge ", '')
                    if EntryText in PlayerList:
                        Kill(EntryText)

                        RevengeMessage = "Dans un élan d'éffort, vous tirez sur " + EntryText + '.'
                        Chat.config(state=NORMAL)
                        if Chat.index('end') != None:
                            Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                            Chat.insert(END, RevengeMessage + '\n') #On l'insere dans le Chat
                            Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                            Chat.tag_config('Start', font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                            Chat.config(state=DISABLED)#Et on 'ferme' le chat
                            Chat.yview(END)
                    else:
                        EntryText = ''
                else:
                    EntryText = ''

            elif EntryText[:6] == '.love ':
                if Joueur == 'Cupidon':
                    if isJour == True:
                        EntryText = ''
                    if CanPlayCupi == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".love ", '')
                        if EntryText in PlayerList:
                            Love(EntryText)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''

            elif EntryText[:8] == '.poison ':
                if Joueur == 'Sorciere':
                    if isJour == True:
                        EntryText = ''
                    if CanPlaySoso == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".poison ", '')
                        if EntryText in PlayerList:
                            if AlreadyPlayedSoso != True:
                                Kill(EntryText)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    
                


            if EntryText[:5] == '.info':
                Chat.config(state = NORMAL)
                Chat.insert(END, PlayerList)
                Chat.insert(END, '\n')
                Chat.config(state = DISABLED)
                        
            else:
                if isNuit == True:
                    EntryText = ''
                else:
                    FinalMessage(Chat, EntryText) #Si ce n'est pas une commande connue, on envoie le message tel quel
        else:
            if isNuit == True:
                EntryText = ''
            else:
                FinalMessage(Chat, EntryText) # Si le message ne commence pas par un point, on l'envoie normalement


def Vote(Target):
    global JoueurIsVoted,Ordi1IsVoted,Ordi2IsVoted,Ordi3IsVoted,Ordi4IsVoted
    if Target == Joueur:
        JoueurIsVoted += 1
    elif Target == Ordi1:
        Ordi1IsVoted += 1
    elif Target == Ordi2:
        Ordi2IsVoted += 1
    elif Target == Ordi3:
        Ordi3IsVoted += 1
    elif Target == Ordi4:
        Ordi4IsVoted += 1

def Love(Target):
    global JoueurIsLove,Ordi1IsLove,Ordi2IsLove,Ordi3IsLove,Ordi4IsLove,AlreadyPlayedCupi
    AlreadyPlayedCupi = True
    #for Player in PlayerList:

    if Joueur == 'Cupidon':
        JoueurIsLove = True
            
        if Target == Ordi1:
            Ordi1IsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, """[Privé] Vous êtes amoureux de Ordi1 ! Si l'un de vous vient à mourir, l'autre ne
pourra supporter cette souffrance et se suiciedera immédiatement..""" + '\n')
            Chat.config(state = DISABLED)
                
        elif Target == Ordi2:
            Ordi2IsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, """[Privé] Vous êtes amoureux de Ordi1 ! Si l'un de vous vient à mourir, l'autre ne
pourra supporter cette souffrance et se suiciedera immédiatement..""" + '\n')
            Chat.config(state = DISABLED)
            
        elif Target == Ordi3:
            Ordi3IsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, """[Privé] Vous êtes amoureux de Ordi1 ! Si l'un de vous vient à mourir, l'autre ne
pourra supporter cette souffrance et se suiciedera immédiatement..""" + '\n')
            Chat.config(state = DISABLED)
            
        elif Target == Ordi4:
            Ordi4IsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, """[Privé] Vous êtes amoureux de Ordi1 ! Si l'un de vous vient à mourir, l'autre ne
pourra supporter cette souffrance et se suiciedera immédiatement..""" + '\n')
            Chat.config(state = DISABLED)


    elif Ordi1 == 'Cupidon':
        Ordi1IsLove = True
        print('debug Ordi1')
            
        if Target == Joueur:
            print("Joueur",Target)
            JoueurIsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, "[Privé] Vous êtes amoureux de Ordi1 ! Si l'un de vous vient à mourir, l'autre ne pourra supporter cette souffrance et se suiciedera immédiatement.." + '\n')
            Chat.config(state = DISABLED)
        elif Target == Ordi2:
            print("Ordi2",Target)
            Ordi2IsLove = True
        elif Target == Ordi3:
            print("Ordi3",Target)
            Ordi3IsLove = True
        elif Target == Ordi4:
            print("Ordi4",Target)
            Ordi4IsLove = True

            

    elif Ordi2 == 'Cupidon':
        Ordi2IsLove = True
        print('debug Ordi2')

        if Target == Joueur:
            print("Ordi2",Target)
            JoueurIsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, "[Privé] Vous êtes amoureux de Ordi2 ! Si l'un de vous vient à mourir, l'autre ne pourra supporter cette souffrance et se suiciedera immédiatement.." + '\n')
            Chat.config(state = DISABLED)
        elif Target == Ordi1:
            print("Ordi1",Target)
            Ordi1IsLove = True
        elif Target == Ordi3:
            print("Ordi3",Target)
            Ordi3IsLove = True
        elif Target == Ordi4:
            print("Ordi4",Target)
            Ordi4IsLove = True

    elif Ordi3 == 'Cupidon':
        Ordi3IsLove = True
        print('debug Ordi3')

        if Target == Joueur:
            print("Ord3",Target)
            JoueurIsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, "[Privé] Vous êtes amoureux de Ordi3 ! Si l'un de vous vient à mourir, l'autre ne pourra supporter cette souffrance et se suiciedera immédiatement.." + '\n')
            Chat.config(state = DISABLED)
        elif Target == Ordi1:
            print("Ordi1",Target)
            Ordi1IsLove = True
        elif Target == Ordi2:
            print("Ordi2",Target)
            Ordi2IsLove = True
        elif Target == Ordi4:
            print("Ordi4",Target)
            Ordi4IsLove = True

    elif Ordi4 == 'Cupidon':
        Ordi4IsLove = True
        print('debug Ordi4')

        if Target == Joueur:
            print("Ordi4",Target)
            JoueurIsLove = True
            Chat.config(state = NORMAL)
            Chat.insert(END, "[Privé] Vous êtes amoureux de Ordi4 ! Si l'un de vous vient à mourir, l'autre ne pourra supporter cette souffrance et se suiciedera immédiatement.." + '\n')
            Chat.config(state = DISABLED)
        elif Target == Ordi1:
            print("Ordi1",Target)
            Ordi1IsLove = True
        elif Target == Ordi2:
            print("Ordi2",Target)
            Ordi2IsLove = True
        elif Target == Ordi3:
            print("Ordi3",Target)
            Ordi3IsLove = True
    
    

def Kill(Target):
    global JoueurIsLove, Ordi1IsLove,Ordi2IsLove,Ordi3IsLove,Ordi4IsLove
    print(Target)
    if Target in PlayerList:
        PlayerList.remove(Target)

    if JoueurIsLove == True:
        if Joueur not in PlayerList:
            if Ordi1IsLove == True:
                if Ordi1 in PlayerList:
                    PlayerList.remove(Ordi1)
            elif Ordi2IsLove == True:
                if Ordi2 in PlayerList:
                    PlayerList.remove(Ordi2)
            elif Ordi3IsLove == True:
                if Ordi3 in PlayerList:
                    PlayerList.remove(Ordi3)
            elif Ordi4IsLove == True:
                if Ordi4 in PlayerList:
                    PlayerList.remove(Ordi4)

    elif Ordi1IsLove == True:
        if Ordi1 not in PlayerList:
            if JoueurIsLove == True:
                if Joueur in PlayerList:
                    PlayerList.remove(Joueur)
            elif Ordi2IsLove == True:
                if Ordi2 in PlayerList:
                    PlayerList.remove(Ordi2)
            elif Ordi3IsLove == True:
                if Ordi3 in PlayerList:
                    PlayerList.remove(Ordi3)
            elif Ordi4IsLove == True:
                if Ordi4 in PlayerList:
                    PlayerList.remove(Ordi4)
                
            
    elif Ordi2IsLove == True:
        if Ordi2 not in PlayerList:
            if JoueurIsLove == True:
                if Joueur in PlayerList:
                    PlayerList.remove(Player)
            elif Ordi1IsLove == True:
                if Ordi1 in PlayerList:
                    PlayerList.remove(Ordi1)
            elif Ordi3IsLove == True:
                if Ordi3 in PlayerList:
                    PlayerList.remove(Ordi3)
            elif Ordi4IsLove == True:
                if Ordi4 in PlayerList:
                    PlayerList.remove(Ordi4)

    elif Ordi3IsLove == True:
        if Ordi3 not in PlayerList:
            if JoueurIsLove == True:
                if Joueur in PlayerList:
                    PlayerList.remove(Joueur)
            elif Ordi1IsLove == True:
                if Ordi1 in PlayerList:
                    PlayerList.remove(Ordi1)
            elif Ordi2IsLove == True:
                if Ordi2 in PlayerList:
                    PlayerList.remove(Ordi2)
            elif Ordi4IsLove == True:
                if Ordi4 in PlayerList:
                    PlayerList.remove(Ordi4)
        
    elif Ordi4IsLove == True:
        if Ordi4 not in PlayerList:
            if JoueurIsLove == True:
                if Joueur in PlayerList:
                    PlayerList.remove(Joueur)
            elif Ordi1IsLove == True:
                if Ordi1 in PlayerList:
                    PlayerList.remove(Ordi1)
            elif Ordi2IsLove == True:
                if Ordi2 in PlayerList:
                    PlayerList.remove(Ordi2)
            elif Ordi3IsLove == True:
                if Ordi3 in PlayerList:
                    PlayerList.remove(Ordi3)


#---------------------------------------------------#
#----------------GESTION DU GRAPHISME---------------#
#---------------------------------------------------#

root = Tk() #On définit notre fenêtre
root.title('LGame') #On définit notre nom, ici LGame
root.geometry("800x460") # On définit sa taille
root.resizable(width=FALSE, height=FALSE) # On dit que la fenêtre ne peut pas être redimensionnée

BackGround = Canvas(root, width=800, height=460)
BackGround.pack()

#Fenêtre du Chat
Chat = Text(root, bd=0, bg="white", height="8", width="50", font="Arial") #Customisation de la fenêtre de chat
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n") #On insère du texte
Chat.config(state=DISABLED) #Une fenêtre où ne peut pas écrire, sinon wtf

#Fenetre Image
PictureBox = Canvas(root, width=200, height=200)

#Fenetre Joueurs
PlayerBox = Text(root, bd=0, height="8", width = "25", font = 'Arial')
texte = """Joueurs restants :\n"""
PlayerBox.insert("0.0", texte, "texte")
PlayerBox.config(state = DISABLED)

#Fenetre timer
TimerBox = Label(root)

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
scrollbar.place(x=559,y=6, height=386) #La Barre de Scroll
Chat.place(x=6,y=6, height=386, width=570) #Le cadre du Chat
ChatBox.place(x=128, y=401, height=50, width=500) #Le cadre de la boite à message (lol)
BoutonEnvoi.place(x=6, y=401, height=50) #Le cadre du bouton
Launcher.place(x=650, y=401, height=50 ) #Le cadre du bouton
PictureBox.place(x=645, y=5)
PlayerBox.place(x= 645, y= 215)
TimerBox.place(x= 655, y= 165)


#Images
ImgLoupGarou = PhotoImage(file ='lg.gif')
ImgCupidon = PhotoImage(file ='cupi.gif')
ImgChasseur = PhotoImage(file ='chassou.gif')
ImgSorciere = PhotoImage(file ='soso.gif')
FondJour = PhotoImage(file ='FondJour.gif')
FondNuit = PhotoImage(file ='FondNuit.gif')


#---------------------------------------------------#
#----------------GESTION DES DONNEES----------------#
#---------------------------------------------------#

RoleList = ['LoupGarou','LoupGarou','Cupidon','Sorciere','Chasseur']

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

PlayerList = [Joueur, Ordi1, Ordi2, Ordi3, Ordi4]

secNuit = 60
isNuit = False
secJour = 60
isJour = False


JoueurIsVoted = 0
Ordi1IsVoted = 0
Ordi2IsVoted = 0
Ordi3IsVoted = 0
Ordi4IsVoted = 0

JoueurIsLove = False
Ordi1IsLove = False
Ordi2IsLove = False
Ordi3IsLove = False
Ordi4IsLove = False

CanPlayLG = False
CanPlaySoso = False
CanPlayCupi = False
CanPlayChassou = False
AlreadyPlayedLG = False
AlreadyPlayedSoso = False
AlreadyPlayedCupi = False
AlreadyPlayedChassou = False
finish = False
#---------------------------------------------------#
#----------------     DIALOGUES     ----------------#
#---------------------------------------------------#

DeadList = "Liste des morts : \n"

RoleLG = """[Privé] Vous êtes Loup-Garou. Votre objectif est d'éliminer tous les innocents.
Chaque nuit, vous vous réunissez entre Loups pour décider d'une victime
à éliminer... Bon jeu et... Bonne chance !"""

RoleSoso = """[Privé] Vous êtes Sorcière. Votre objectif est d'éliminer tous les Loups-Garous.
Vous disposez d'une potion de mort pour assassiner quelqu'un...
Bon jeu et... Bonne chance !"""

RoleChassou = """[Privé] Vous êtes Chasseur. Votre objectif est d'éliminer tous les Loups-Garous.
A votre mort, vous pourrez éliminer un joueur en utilisant votre dernier souffle...
Bon jeu et... Bonne chance !"""

RoleCupi = """[Privé] Vous êtes Cupidon. Votre objectif est d'éliminer tous les Loups-Garous.
Dès le début de la partie, vous pourrez former un couple entre deux joueurs.
Leur objectif sera de survivre ensemble, car si l'un d'eux meurt,
l'autre se suicidera... Bon jeu et... bonne chance !"""

Death = "[Privé] Vous êtes mort."


ActionLG = "Les loups vont décider d'une victime à éliminer."
Dévorer = "[Joueur] vote pour dévorer [Joueur]"
VictimeLG = "Les loups on décidé d'éliminer [Joueur]"


ActionCupi = "Cupidon va pouvoir désigner deux amoureux."
ChoixLove = "[Privé] Grâce à vos deux flèches d'amour, vous rendez [joueur] et [joueur] amoureux à tout jamais..."
PvLove = "[Privé] Vous êtes amoureux de [joueur]! Si l'un de vous vient à mourir, l'autre ne pourra supporter cette souffrance et se suiciedera immédiatement.."

ActionSoso = "La sorcière va pouvoir utiliser ses potions."
VictimeSoso = "[Privé] Avec vos subtiles potions vous arrivez à empoisonner [Joueur]. Il ne se reveillera pas demain..."

ChoixChassou = "Le chasseur dispose de 30 secondes pour éliminer sa cible !"
Pan = "PAN ! [Joueur]([Rôle]) a été tué par le chasseur."

Vote = """Une fois par jour, le village décide d'éliminer un joueur qu'il croit Loup-Garou.
Pour voter contre quelqu'un, vous devez utiliser la commande '.vote ' + nom."""
ChoixVillage = "Le village a décidé d'éliminer [Joueur] qui était [Rôle]."

Night = "La nuit tombe sur le village de Thiercelieux..."


RipAll = "Tout le monde est mort !"
GgLg = "Les LOUPS-GAROUS ont gagné !"
GgVillage = "Les VILLAGEOIS ont gagné !"
GgLove = "Les AMOUREUX on gagné !"
