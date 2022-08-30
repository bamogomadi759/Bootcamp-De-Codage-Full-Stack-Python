// Exercice 1 :

// En utilisant ce tableau :

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

// Supprimez Banana de la baie.
fruits.splice(0,1)
// ['Banana'] : l'élément supprimé

// Triez le tableau par ordre alphabétique.
fruits.sort()
// ['Apples', 'Blueberries', 'Oranges']

// Ajoutez "Kiwi" à la fin du tableau.
fruits.splice(3, 0, "Kiwi")

// Supprimez "Apples" du tableau.
fruits.shift() 
// 'Apples' : l'élément supprimé

// Triez le tableau dans l'ordre inverse. 
fruits.reverse()
// ['Kiwi', 'Oranges', 'Blueberries']




// Exercice 2 :

// En utilisant ce tableau :

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

moreFruits[1][1]
['Oranges']
console.log(moreFruits[1][1])
// ['Oranges']