# Exercice 1 : Bonjour Le Monde
print("Hello world");
print("Hello world");
print("Hello world");
print("Hello world");


# Exercice 2 : Quelques Maths
# Ecrivons un code qui calcule le résultat de : (99^3) * 8(99 à la puissance 3 fois 8)

x = 99**3*8;
print(f"x = {x}")

# Exercice 3 : Quelle Est La Sortie ?

# Prédisons le résultat des extraits de code suivants :

5 < 3 # False
3 == 3 # True
3 == "3" # False
#"3" > 3 # TypeError
"Hello" == "hello" # Talse


# 🌟 Exercice 4 : Votre Marque D'ordinateur

# Créons une variable appelée computer_branddont la valeur est le nom de marque de votre ordinateur.

computer_brand = "hp ProBook";
print(f"I have a {computer_brand} computer")



# 🌟 Exercice 5 : Vos Informations

# Créons une variable appelée name et définissons sa valeur sur notre nom.
name = "BAMOGO Madi";
#Créons une variable appelée age et définissons sa valeur sur notre âge.
age = 27;
# Créons une variable appelée shoe_size et définissons sa valeur sur notre pointure.
shoe_size = 44;
# Créons une variable appelée info et définissons sa valeur sur une phrase intéressante sur nous-même. La phrase doit contenir toutes les variables créées dans les parties 1, 2 et 3.
info = f"Je me Monsieur {name}, j'ai {age} ans et ma pointure est {shoe_size} ";
# Demandons à notre code d'imprimer le message info.
print(info)


# 🌟 Exercice 6 : A & B
# Créons deux variables, a et b.
a = 54;
b = 38 ;
if a > b:
    print("Hello World.")
else:
    print(f"{a} est plus petit que {b}")


# Exercice 7 : Pair Ou Impair
# Écrivons un code qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impair.
nombre =int(input("Veuillez saisir un nombre : "));
if nombre % 2 == 0 :
    print(f"{nombre} est pair ")
else:
    print(f"{nombre} est impair ")



# 🌟 Exercice 8 : Comment T'appelles-Tu ?
# Écrivons un code qui demande à l'utilisateur son nom et détermine si vous avez le même nom ou non, imprimez un message amusant en fonction du résultat.
nom = input("Comment T'appelles-Tu ?")
mon_nom = "BAMOGO Madi"
if nom == mon_nom :
    print(f"Salut mon Homo ")
else :
    print(f"Salut {nom} soyez la bienvenue ! ")



# 🌟 Exercice 9 : Assez Grand Pour Faire Des Montagnes Russes
# Écrivons un code qui demandera à l'utilisateur sa taille en pouces.
taille = float(input("Veuillez entrer votre taille en pouce : "))
if taille > 145 :
    print(f"Vous etes assez grand pour rouler ")
else :
    print(f"Vous devez grandir un peu plus pour rouler.")