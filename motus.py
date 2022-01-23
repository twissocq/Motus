###Jeu python motus

import numpy as np
import matplotlib.pyplot as plt
nombre_essai = 6



class Motus():

    def __init__(self, fichier_dico):

        self.fichier_dico = fichier_dico
        self.liste_mots = self.read_fichier_mots()
        self.mot_a_trouver = self.generer_mot()
        self.longueur_choisie = 0
        self.nombre_essai = 6
        self.solution_courante = self.mot_a_trouver[0] + '_'*(self.longueur_choisie-1)
        self.historique = ['']*self.nombre_essai    
        self.nombre_essai_restants = 6
        
        self.generer_mot()
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
        return mot_choisi
    
    def entree_user(self):
        self.mot_courant = input().upper()
    
    
    def afficher_grille(self):
        #code couleur : 0 : non trouvé, 2 : bonne lettre, 1 : lettre existante dans le mot
        
        fig, ax = plt.subplots()
        Z = []
        for ligne in range(0, self.nombre_essai):
            liste_temp =  ['2'] + [0]*(self.longueur_choisie-1)
            Z.append(liste_temp)
        c = ax.pcolor(Z, edgecolors='k', linewidths=4)
        fig.tight_layout()
        plt.show()
        return 1
    
    def jouer(self):
               
        for i in range(0,nombre_essai+1):
            print(self.historique)
            mot = input().upper()
            
            if len(mot) != self.longueur_choisie:
                print('Le mot n\' est pas de la bonne longueur! Reessayez:')
                mot = input()
            if not(mot in self.liste_mots):
                print()
            #cas de figure :
                #Mot n'existe pas
                #mot de mauvaise longueur
                #Tester les lettres. Attention à ne pas donner trop d'infos (lettres triples ou doubles!)
                #Mot correct
    
Jeu = Motus('littre.txt')

        