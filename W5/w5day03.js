
// A Few Things to Try

//  01.Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
// Finally, it should greet the person using their full name.

var fname = prompt("What's your first name ? ");
var midname = prompt("What's your middle name ?");
var lname = prompt("What's your second name ? ");
console.log("Hello " + fname + " " + midname + " " + lname +" , You'r mostly welcome to 1MWTT...!!!");

// 02.Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
// Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

var input  = prompt("Hello there what's your favourite number ?");

function favouriteNumber(number){
	number  = parseInt(number);
	if((number + 1) > 100){
		return "Wo-oh! It's a big number !!! "
	}else{
		return "Great! Good number!!!"
	}
}
console.log(favouriteNumber(parseInt(input)));

// 03.Angry boss. Write an angry boss program that rudely asks what you want. 
// Whatever you answer, the angry boss should yell it back to you and then fire you. 
// For example, if you type in I want a raise, it should yell back like this:
// "WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!""

var name  = prompt("What's your name ? ");
var askFromBoss = prompt("What do tou want to ask from the boss ? ");

console.log( name.toUpperCase() + " MEAN " + askFromBoss.toUpperCase() + " ?!? YOU'RE FIRED!!");

// ===Optional ====
// 01.
// Research how to generate a random number with JavaScript. 
// (Math.random() will output a random number from 0 up to but not including 1)

// Generate a random number
// between 1 and 10
console.log("between 1 and 10 : ");
for(var i = 0; i < 10; i++){
	console.log(parseInt(Math.random() * 10 + 1));
}

// between 1 and 100
console.log("between 1 and 100 : ");
for (var i = 0; i < 10; i++) {
	console.log(parseInt(Math.random() * 100 + 1));
}

// between 1930 and 1950
console.log("between 1930 and 1950 : ");

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

for (var i = 0; i < 10; i++) {
	console.log(getRndInteger(1930, 1950));
}

// 02.
// Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:

// oooXXXoo
// oooXoXoo
// XXXooXoo

// o = water ; x = land
var counter = "";

for (var i = 0; i < 11; i++) {
	for (var j = 0; j < 11; j++) {
		var random = Math.floor(Math.random() * (3 - 1) + 1);
		if( random == 1){
			counter = counter + "o"
		}else{
			counter = counter + "x"
		}	
	}
	console.log(counter);
	counter = "";
}


