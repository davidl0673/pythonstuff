

var pick = window.prompt("pick either rock, paper or scissors!!");
var choices = ["rock", "paper", "scissors"]


var choice = choices[Math.floor(Math.random()*choices.length)];
var computerChoice = Math.random(5);
console.log(choice)

 if (pick === choice){
    console.log("tie!")
} else {
    console.log("try agian")
} 
console.log(computerChoice)