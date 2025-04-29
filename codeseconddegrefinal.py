from math import *

fin="Fin du programme, veuillez le relancer"

def relancer():
    reponse = input("Voulez-vous relancer le programme ? ('oui'/'non') : ").lower()
    if reponse=="oui":
        seconddegre()
        return
    if reponse=="non":
        print(fin)
        return
    else:
        print("La réponse donnée n'est pas comprise dans les réponses, réesayez.")
        relancer()
        
def premierdegre():
    # Demande à l'utilisateur les variables b et c pour trouver X
    b=float(input("Combien sera b : "))
    if b==0:
        print("Le calcul ne possède pas d'inconnu")
        print(fin)
        return
    c=float(input("Combien sera c : "))
    resultatpremierdegre=-c/b
    print("L'inconnu X est égal à : ",resultatpremierdegre)
    relancer()
    return

def seconddegre():
    # L'utilisateur définie les trois variables ou peut décaler vers le premier degré.
    a=float(input("Combien sera a : "))
    if a==0:
        print("Impossible d'effectuer du second degré, ceci est un calcul du premier degré.")
        premierdegre()
    b=float(input("Combien sera b : "))
    c=float(input("Combien sera c : "))

    # Calcul de la variable Delta (discriminant)
    delta=b*b-4*a*c
    print("Delta est égal à : ",delta)
    
    def racines():
        # Dans le cas où Delta est supérieur à zéro.
        if delta>0:
            print("Il y a deux racines")
            x1=(-b-sqrt(delta))/(2*a)
            x2=(-b+sqrt(delta))/(2*a)
            print("x1 = ",x1,"    x2 = ",x2)
            relancer()
            return
        # Dans le cas où Delta est égal à zéro.
        if delta==0:
            x=-b/(2*a)
            print(x)
            relancer()
            return
        # Dans le cas où Delta est inférieur à zéro.
        else:
            print("Aucune racine réelle trouvée, car Delta est négatif.")
            relancer()
            return
    racines()
seconddegre()
# Appel de(s) définition(s).
# 𓆝 𓆟 𓆞 𓆝 𓆟