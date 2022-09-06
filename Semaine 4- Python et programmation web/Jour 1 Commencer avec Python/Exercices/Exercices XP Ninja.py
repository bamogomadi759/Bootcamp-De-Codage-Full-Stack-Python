# Exercice 3 : Sorties
# Prédisons le résultat des extraits de code suivants :

3 <= 3 < 9 # True
3 == 3 == 3 # True
bool(0) # False
bool(5 == "5") # False
bool(4 == 4) == bool("4" == "4") # True
bool(bool(None)) # False
x = (1 == True) 
y = (1 == False) 
a = True + 4 
b = False + 10 

print("x is", x) # x is True
print("y is", y) # y is False
print("a:", a) # a : 5
print("b:", b) # b: 10



#  Exercice 4 : Combien De Caractères Dans Une Phrase ?
# Utilisons python pour connaître le nombre de caractères dans le texte suivant, utilisez une seule ligne de code (au-delà de l'établissement de votre my_textvariable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)) # 445




#  Exercice 5 : Mot Le Plus Long Sans Caractère Spécifique
# Continuons à demander à l'utilisateur de saisir la phrase la plus longue possible sans le caractère "A".
phrase = input("Veuillez saisir la phrase la plus longue possible sans le caractère 'A' : ")
for i in range(len(phrase)):
    if phrase[i] =="a" :
        print(f"Votre phrase : {phrase} contient le caractère 'A' ")
        break
    else :
        print(f"Bravo vous avez reçu !!!")