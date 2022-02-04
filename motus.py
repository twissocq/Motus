###Jeu python motus

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import unidecode
from PIL import Image
import copy


nombre_essai = 6



class Motus():

    def __init__(self, fichier_dico):

        self.fichier_dico = fichier_dico
        self.liste_mots = self.read_fichier_mots()
        self.mot_a_trouver = self.generer_mot()
        self.nombre_essai = 6
        self.solution_courante = self.mot_a_trouver[0] + '_'*(self.longueur_choisie-1)
        self.historique = ['']*self.nombre_essai    
        self.nombre_essai_restants = 6
        
        self.generer_mot()
        
        self.longueur_choisie = len(self.mot_a_trouver)
        # self.colortable = self.genere_colortable_ini()
        
   
        
        
    def read_fichier_mots(self):
        #Renvoie 
        fichier = self.fichier_dico
        liste_mots = []
        f = open(fichier, encoding = 'UTF-8')
        ligne = f.readline()
        while(ligne != ''):
            liste_mots.append(ligne.strip())
            ligne = f.readline()
        return liste_mots
    
    def generer_mot(self):
        #Genere un mot de nombre de lettre dans le dictionnaire
        liste_mots = self.read_fichier_mots()
        longueur = [5,6,7,8]
        self.longueur_choisie = np.random.choice(longueur)
    
        liste_mots_bonne_taille = []
        for mot in liste_mots:
            if len(mot) == self.longueur_choisie:
                liste_mots_bonne_taille.append(mot)
        
        mot_choisi = np.random.choice(liste_mots_bonne_taille)
        mot_choisi = mot_choisi.replace('é','e').replace('è','e').replace('â','a').replace('ê','e')
        return unidecode.unidecode(mot_choisi)
    
    def entree_user(self):
        self.mot_courant = input().upper()
    
    
    def afficher_grille(self, data, liste_mots_input):
        #code couleur : 0 : non trouvé, 2 : bonne lettre, 1 : lettre existante dans le mot, 3 : blanc
        '''
        data = liste de liste de int. Traduction des lettres trouvées ou non
        liste_mots_input = liste de mots rentrés
        Prototype :
        '''
        print(data, liste_mots_input)
        name = 'grille_' + str(self.nombre_essai-self.nombre_essai_restants) + '.png'
        fig, ax = plt.subplots()
        cmap = colors.ListedColormap(['red', 'blue', 'orange'])
        im = ax.imshow(data, cmap)
        
        for x in range(self.longueur_choisie):
            ax.axvline(x+0.5)
            
            
        for mot in range(len(liste_mots_input)):
            for lettre in range(len(liste_mots_input[mot].upper())):
                text = ax.text(lettre, mot, liste_mots_input[mot][lettre].upper(),
                   ha="center", va="center", color="black", fontsize = 20)
        fig.savefig(name)
        img = Image.open(name)
        img.show()
        
        return 1
    
    def jouer(self):
        print("Le mot à trouver possède ", len(self.mot_a_trouver), " lettres.")
        print("Bonne chance!")
        
        found = False
        tofind = self.mot_a_trouver
        essai = 0
        self.nombre_essai_restants = self.nombre_essai
        code_couleur = [[2] + [0 for p in range(len(self.mot_a_trouver)-1)]]
        data = copy.deepcopy(code_couleur)
        code_couleur_temp=copy.deepcopy(data[0])
        
        couleur_neutre = code_couleur[0]
        
        liste_mots_input = [tofind[0] + ' '*(len(self.mot_a_trouver)-1)]
        
        
        
        self.afficher_grille(data, liste_mots_input)
        
        
        while (not found) and (self.nombre_essai_restants>0):
            essai +=1
            self.nombre_essai_restants -=1
            print("Essai N°", str(essai))
            guessed = tofind[0] + input(" " + tofind[0])
            guessed = guessed.upper()
            while len(guessed) != len(tofind):
                print("Le mot n'est pas de la bonne longueur, rentrez un autre mot")
                guessed = tofind[0] + input(" " + tofind[0])

            assert(len(guessed) == len(tofind))
            
            liste_mots_input[essai-1] = guessed
            liste_mots_input.append(tofind[0] + ' '*(len(self.mot_a_trouver)-1))
            
            guessed_list = [guessed[i] for i in range(len(guessed))]
            tofind_list = [tofind[i] for i in range(len(tofind))]
            result = ['-' for i in range(len(tofind))]
        
            for il, letter in enumerate(tofind):
        
                if guessed_list[il] == tofind[il]:
                    result[il] = 'o'
                    guessed_list[il] = '?'
                    tofind_list[il] = '?'
        
                else:
                    for il_guessed in range(len(guessed_list)):
                        if guessed_list[il_guessed] == tofind_list[il]:
                            result[il_guessed] = 'x'
                            guessed_list[il_guessed] = '?'
                            tofind_list[il] = '?'
        
        
            display = ''
            for i in range(len(result)):
                display += result[i]
            print(display)
            print(result)
            
            for idx, lettre in enumerate(result):
                if lettre == 'o':
                    code_couleur_temp[idx] = 2
                elif lettre == 'x':
                    code_couleur_temp[idx] = 1
                else:
                    code_couleur_temp[idx] = 0
            data[essai-1] = code_couleur_temp
            data.append(couleur_neutre)
            
            
            self.afficher_grille(data, liste_mots_input)
            
            if guessed == tofind :
                found = True
                print (" Bien joué !")
                return 1
            
        return 'Pas de chance'

        # for i in range(0,nombre_essai+1):
        #     print(self.historique)
        #     mot = input().upper()
            
        #     if len(mot) != self.longueur_choisie:
        #         print('Le mot n\' est pas de la bonne longueur! Reessayez:')
        #         mot = input()
        #     if not(mot in self.liste_mots):
        #         print()
            #cas de figure :
                #Mot n'existe pas
                #mot de mauvaise longueur
                #Tester les lettres. Attention à ne pas donner trop d'infos (lettres triples ou doubles!)
                #Mot correct
    
Jeu = Motus('littre.txt')
print(Jeu.mot_a_trouver)
Jeu.jouer()
# Jeu.jouer()
        