# Exercice 1 : Hello World-J'aime Python
print(f"Hello world");
print(f"Hello world");
print(f"Hello world");
print(f"Hello world");

print(f"I love python");
print(f"I love python");
print(f"I love python");
print(f"I love python");


#  Exercice 2 : Quelle Est La Saison ?
# Demandons à l'utilisateur de saisir un mois (1 à 12).
mois = int(input("Veuillez saisir un mois (1 à 12) : "));
if mois < 1 or mois > 12 :
    print(f"Nous avons douze mois dans l'année veuillez revoir votre saisi !")
else :
    if 3<= mois <=5 :
        print(f"C'est le printemps ")
    elif 6<= mois <=8 :
        print(f"C'est l'été")
    elif 9<= mois <=11 :
        print(f"C'est l'automne")
    else :
        print(f"C'est l'hiver")