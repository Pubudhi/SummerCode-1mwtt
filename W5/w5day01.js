// Hours in a year. How many hours are in a year?
	var hours = 24 * 30 * 12;
	console.log("Hours in a year : " + hours);

// Minutes in a decade. How many minutes are in a decade?
	var minutes = 60 * 1 * 24 * 30 * 12 * 10;
	console.log("Minutes in a decade : " + minutes);

//Your age in seconds. How many seconds old are you?
	var seconds = 60 * 60 * 1 * 24 *30 * 12 * 25;
	console.log("My age in seconds : " + seconds);

// Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? 
	var cristinaAge = 60 * 60 * 60 * 1 * 24 *30 * 12 * 32;
	console.log("Cristina's age in milliseconds : " + cristinaAge);

//How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
	var int32 = Math.pow(2,31) - 1;
	var tmeout32 = int32/(24*60*60);
	console.log("it takes "+ tmeout32 +" days from 2018.08.22");

//How about a 64-bit system?
	var int64 = Math.pow(2,63) - 1;
	var tmeout64 = int64/(24*60*60);
	console.log("it takes "+ tmeout64 +" days from 2018.08.22");

// Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) 
// 	Assumption : born time 02.51 am
	// born day 
	var bornday = new Date(1993, 4, 4, 2, 51, 00, 00);
	//diff between current time and born time in milliseconds
	var ageDiffMs = Date.now() - bornday.getTime()
	// convert to Date 
	var ageDate = new Date(ageDiffMs);

	var years = Math.abs(ageDate.getUTCFullYear() - 1970);
	var months = Math.abs(ageDate.getMonth());
	var days = Math.abs(ageDate.getDate());
	var hours = Math.abs(ageDate.getHours());
	var minutes = Math.abs(ageDate.getMinutes());
	var seconds = Math.abs(ageDate.getSeconds());
	
	console.log("I am " + years + " years " + months + " months " + days + " days " + hours + " minutes and " + seconds + " seconds old now. !!!")
