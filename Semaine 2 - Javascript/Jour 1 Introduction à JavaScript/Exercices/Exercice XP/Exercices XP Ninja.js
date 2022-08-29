// Exercice 1 : Évaluation

5 >= 1 // true

0 === 1 // false

4 <= 1 // false

1 != 1 // false

"A" > "B" // false

"B" < "C" // true

"a" > "A" // true

"b" < "A" // false

true === false // false

true != true //  false


// Exercice 2 : Demander Des Nombres

function addition(x, y) {
    if (typeof x !== "number" || typeof y !== "number") {
        return "Erreur : veuillez entrer deux nombres!";
    }
    return x + y;
}


// Exercice 3 : Trouver Nemo

// Demandez à l'utilisateur de vous donner une phrase contenant le mot "Nemo".
let phrase = prompt("Donner une phrase contenant le mot Nemo");

// Trouver le mot "Nemo"
Phrase = phrase.indexOf("Nemo");

console.log( "I found Nemo at ", Phrase)
// I found Nemo at  23



// Exercice 4 : Boum

 //saisie du numéro par l'utilisateur
 let num = Number(prompt("Entrez un numéro"));
 //2
 let chaine = "b";
 if (num < 2) {
     chaine = "boum";
     if ((num%2) == 0){//Si le nombre donné est divisible par 2, ajoutez un point d'exclamation à la fin.
         console.log("divisible par 2" , chaine + "!");
     } else if ((num%5) == 0){//Si le nombre donné est divisible par 5, renvoyez la chaîne en MAJUSCULES.
         console.log("divisible par 5" , chaine.toUpperCase() + "!");
     } else if ((num%5) && (num%2) == 0){//Si le nombre donné est divisible à la fois par 2 et 5, renvoyez la chaîne en MAJUSCULES et ajoutez un point d'exclamation à la fin.
         console.log(chaine.toUpperCase() + "!");
     } else {
         console.log("Ni divisible par 2, ni par 5  ", chaine);
     }
 } else {//si sup. à 2
     for (var i = 1; i <= num ; i++) {//num est égale au nombre de zéro de boom
         chaine=chaine+"o";
     }
     chaine=chaine+"u";
     chaine=chaine+"m";
     if ((num%2) == 0){
         console.log("divisible par 2" , chaine + "!");
     } else if ((num%5) == 0){
         console.log("divisible par 5" , chaine.toUpperCase() + "!");
     } else if ((num%5) && (num%2) == 0){
         console.log(chaine.toUpperCase() + "!");
     } else {
         console.log("Ni divisible par 2, ni par 5  ", chaine);
     }
 } 