chaine = input("Veuillez saisir une chaine : ") 
if len(chaine) < 10 :
    print(f"chaîne pas assez longue");
elif len(chaine) > 10 :
    print(f"chaîne trop longue")
print(f"{chaine[0]}")
print(f"{chaine[-1]} ")
i=0;
for lettre in chaine :
    i = i+ 1;
    nouvelle_chaine = chaine[:i]
    print(nouvelle_chaine)