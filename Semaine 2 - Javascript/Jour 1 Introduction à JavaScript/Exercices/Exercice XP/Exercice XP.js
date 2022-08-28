// Exercice 1 : Votre Plat Préféré

// La commande qui permet de stocker mon plat préféré dans une variable

var favorite_food = " Riz soumbala";

// La commande qui permet de stocker mon repas préférée dans une variable
var favorite_meal = " Dinner";


// La commande qui permet d'affiche le résultat
console.log("I eat " + favorite_food + "at every " + favorite_meal)
// le rendu : I eat  Riz soumbalaat every  Dinner


// Exercice 2: Série

// Première Partie


let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
// Commande qui permet d'affiche le nombre de séries dans le tableau

myWatchedSeriesLength= myWatchedSeries.length // 3

// Commande qui permet de stocker une pharse dans une variable
myWatchedSeriesSentence= "black mirror, money heist, and the big bang theory ";

// Console.log une phrase utilisant les deux variables créées ci-dessus
console.log("I wtched", myWatchedSeriesLength, "seires : ", myWatchedSeriesSentence)
// le rendu : I wtched 3 seires :  black mirror, money heist, and the big bang theory 


// Deuxième Partie
// Remplacez la série « the big bang theory » par « friends ».

myWatchedSeries.splice(2, 1, "friends")
['the big bang theory'] // l'élément supprimé
// Le resultat
console.log(myWatchedSeries)
// ['black mirror', 'money heist', 'friends']

// Ajoutez, à la fin du tableau, le nom d'une autre série que vous avez regardée.

myWatchedSeries.splice(3, 1, "Blacklist")
[]
console.log(myWatchedSeries)
// ['black mirror', 'money heist', 'friends', 'Blacklist']

//Ajoutez, au début du tableau, le nom de votre série préférée.
myWatchedSeries.splice(0, 0, "Suits");
[]
console.log(myWatchedSeries)
// ['Suits', 'black mirror', 'money heist', 'friends', 'Blacklist']


// Supprimer la série « miroir noir ».

myWatchedSeries.splice(1, 1,)
['black mirror']
console.log(myWatchedSeries)
// ['Suits', 'money heist', 'friends', 'Blacklist']



// Exercice 3 : Le Convertisseur De Température
// Stocker une température Celsius dans une variable.
let tempCelsius = "32";

// Convertissez-le en fahrenheit

let tempFahrenheit = ((Number(tempCelsius)/5)*9 +32);

// La commande qui permet d'affiche le résultat 

console.log(tempCelsius, "°C", "is", tempFahrenheit, "°F")
// 32 °C is 89.6 °F


// Exercise 4 : Devinez Les Réponses #1

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:It will output 55, because 34 and 21 are numbers
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:It will output 23, because 2 and 21 are numbers
    // Actual: 23

    // c est indéfinie
    // Analysons le code ci-dessous et donnons le résultat 
    console.log(3 + 4 + '5');   
// 3 et 4 sont des nombres par contre '5' est une chaine de caractère par conséquent le résltat final sera 75 


// Exercice 5 : Devinez Les Réponses #2


typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: number
// Actual: number

typeof(NaN)
// Prediction: number
// Actual: number

typeof("hello")
// Prediction: string
// Actual: string

typeof(true)
// Prediction: boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers
// Actual: hamburgers

"hamburgers" - "s"
// Prediction:hamburger
// Actual:NaN

"1" + "3"
// Prediction: 13
// Actual: 13

"1" - "3"
// Prediction: -2
// Actual: -2

"johnny" + 5
// Prediction: johnny5
// Actual: johnny5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction: NaN
// Actual: NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: true
// Actual:true

1 === "1"
// Prediction: false
// Actual: false


// Exercice 6 : Devinez Les Réponses #3

5 + "34"
// Prediction: 534
// Actual:534

5 - "4"
// Prediction:1
// Actual: 1

10 % 5
// Prediction: 0
// Actual:0

5 % 10
// Prediction: 5
// Actual: 5

"Java" + "Script"
// Prediction: JavaScript
// Actual: JavaScript

" " + " "
// Prediction: '  '
// Actual: '  '

" " + 0
// Prediction: ' 0'
// Actual: ' 0'

true + true
// Prediction: truetrue
// Actual:2

true + false
// Prediction:truefalse
// Actual:1

false + true
// Prediction:falsetrue
// Actual:1

false - true
// Prediction: NaN
// Actual:-1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction: -1
// Actual:-1

"Bob" - "bill"
// Prediction: NaN
// Actual:NaN