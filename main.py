import pygame
import random
import words

# Initialiser Pygame
pygame.init()

# Définir les variables de base
largeur = 800
hauteur = 600
couleur_fond = (255, 255, 255)
couleur_texte = (0, 0, 0)
font = pygame.font.SysFont(None, 48)
mot_secret = ""
lettres_invalides = []
lettres_trouvees = ""
erreurs = 0
win = False

imgs = [
    "========      ",
    " ||/       |  ",
    " ||        0  ",
    " ||       /|\ ",
    " ||       / \ ",
    "/||           ",
    "=============="
]

mots = words.liste_en_lane

# Choisir un mot au hasard
mot_secret = random.choice(mots)

fenetre = pygame.display.set_mode((largeur, hauteur))

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            exit()

        if erreurs < len(imgs) and not win:
            if evenement.type == pygame.KEYDOWN and evenement.unicode.isalpha():
                lettre = evenement.unicode.lower()
                if lettre in mot_secret:
                    lettres_trouvees += lettre
                else:
                    if lettre not in lettres_invalides:
                        lettres_invalides.append(lettre)
                        erreurs += 1

        else:
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_RETURN:
                mot_secret = random.choice(mots)
                lettres_invalides = []
                lettres_trouvees = ""
                erreurs = 0
                win = False

    fenetre.fill(couleur_fond)

    mot_affiche = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    texte_mot = font.render(mot_affiche, True, couleur_texte)
    fenetre.blit(texte_mot, (50, 50))

    texte_lettres = font.render("Lettres utilisées : " + ", ".join(lettres_invalides), True, couleur_texte)
    fenetre.blit(texte_lettres, (50, 150))

    # afficher les états en fonction des erreurs
    for erreur in range(erreurs):
        surface_texte = font.render(imgs[erreur], True, couleur_texte)
        fenetre.blit(surface_texte, (64, 200+(32*erreur)))

    if "_" not in mot_affiche:
        win = True

    if win:
        texte_message = font.render("Gagné", True, couleur_texte)
        fenetre.blit(texte_message, (50, 500))
        fenetre.blit(font.render("Appuyer sur Entrée pour relancer", True, couleur_texte), (50, 540))

    elif erreurs > 6:
        texte_message = font.render("Perdu - le mot était : " + mot_secret, True, couleur_texte)
        fenetre.blit(texte_message, (50, 480))
        fenetre.blit(font.render("Appuyer sur Entrée pour relancer", True, couleur_texte), (50, 540))

    pygame.display.flip()
