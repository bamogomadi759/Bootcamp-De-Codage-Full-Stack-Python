#  🌟 Exercice 1 : Set
# Créons un ensemble appelé my_fav_numbers avec tous nos numéros favoris.
my_fav_numbers ={12, 24, 67, 90}

# Ajoutons deux nouveaux numéros à l'ensemble.
my_fav_numbers.update([17, 78])

# Supprimons le dernier numéro.
my_fav_numbers.remove(90)

# Créons un ensemble appelé friend_fav_numbers avec les numéros favoris de votre ami.
friend_fav_numbers = {77, 68, 34, 76}

# Concaténons my_fav_numbers et friend_fav_numbers à une nouvelle variable appelée our_fav_numbers.
our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)




#  🌟 Exercice 2 : Tuple
# Étant donné un tuple dont la valeur est un entier, il n'est pas possible d'ajouter plus d'entiers au tuple car les tuple on ne peut pas les modifier une fois qu'ils ont été créés.



#  🌟 Exercice 3 : Liste

#  Utilisation de cette liste
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Supprimons "Banane" de la liste
basket.remove("Banana")

# Supprimons « Myrtilles » de la liste.
# Erreur car « Myrtilles » n'est pas dans la liste

# Ajoutons "Kiwi" à la fin de la liste.
basket.append("Kiwi")

# Ajoutons « Pommes » au début de la liste.
basket.insert(0, "Pommes")

# Comptons le nombre de pommes dans le panier.
count = 0;
for element in basket:
    if element== "Pommes":
        count += 1
        print(f"The total number of Pommes in the basket: {count} ")

# Vidons le panier.
basket.clear()
print(basket)



# 🌟 Exercice 4 : Flotteurs

# Qu'est-ce que le type float ?
"""Le type float (flottant)
Le type float (flottant)
Ce type est utilisé pour stocker des nombres à virgule flottante, désignés en anglais par l'expression floating point numbers.
Un entier est un nombre sans virgule tandis qu'un flottant est un nombre à virgule. 
"""

# Créons une liste contenant la séquence suivante 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (ne codez pas la séquence en dur).
for nombre in range(1, 6) :
    print(f"{nombre + 0.5}");



# 🌟 Exercice 5 : Boucle For
# Utilisons une forboucle pour imprimer tous les nombres de 1 à 20 inclus.
for nombre in range(1, 20) :
    print(f"{nombre}")

# En utilisant une forboucle, qui boucle de 1 à 20 (inclus), imprimez chaque élément qui a un index pair.
for nombre in range(2, 20,2) :
    print(f"{nombre}")



#  🌟 Exercice 6 : Boucle While

# Écrivons une boucle while qui demandera continuellement à l'utilisateur son nom, à moins que l'entrée ne soit égale à votre nom.
nom = input("Veuillez saisir votre nom : ")
mon_nom = "BAMOGO"
while nom != mon_nom :
    nom = input("Veuillez saisir votre nom : ")


# 🌟 Exercice 7 : Fruits Préférés
# Demandons à l'utilisateur de saisir son/ses fruit(s) préféré(s) (un ou plusieurs fruits).
fruit = input("Veuillez saisir son/ses fruit(s) préféré(s) (un ou plusieurs fruits) : ")
"""while fruit != " " :
    fruit = input("Veuillez saisir son/ses fruit(s) préféré(s) (un ou plusieurs fruits) : ")
    fruits = fruit"""
print(fruit)

# Stocker le(s) fruit(s) préféré(s) dans une liste (convertir la chaîne de mots en une liste de mots).
liste = fruit.split()

# Demandons à l'utilisateur d'entrer le nom de n'importe quel fruit

fruit_favoris =input("Veuillez saisir le nom de n'importe quel fruit : ")
for i in liste :
    if fruit_favoris in liste :
        print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
    else :
        print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")



# Exercice 8 : Qui A Commandé Une Pizza ?
pizza = input("Veuillez saisir une série de garniture de pizza");
garnitures_pizza = " ";

while pizza != "quitter" :
    pizza = input("Veuillez saisir une série de garniture de pizza");
    garnitures_pizza = pizza
    compteur = 0;
    for i in garnitures_pizza :
        if i == pizza :
            compteur += 1
        print(f"vous ajouterez cette garniture à leur pizza.")
print(f"{garnitures_pizza} le prix total est : {(10+2.5)*compteur} ")



# Exercice 9 : Cinémax

