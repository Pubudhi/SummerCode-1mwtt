// Week 05 Day 02

// General frequencies of music nodes
   // A          220
   // A#         233.082
   // B          246.942
   // C          261.626
   // C#         277.183
   // D          293.665
   // D#         311.127
   // E          329.628
   // F          349.228
   // F#         369.994
   // G          391.995
   // G#         415.305
   // A          440
// Music A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz Calculate and console.
// log the frequency each of the 12 notes between A and A' Hint: the notes are NOT in a linear scale, but in a geometric scale
// * all values are in the Hz
// One simple mechanism is to start with some note, say A-220, and multiply it by the 12-th root of two to get the next note. 
// If we do this 12 times, we will have multiplied by two, thus arriving at the note one octave up, A-440. 
// The 12-th root of two is 1.0594631
   
   // var A = 440;
   // var A# = 440 * 1.0594631; // A * ((12-th root of two)
   

   var val = 0;
   var i = 0;
   var result = 0;
   var musicNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A'"];
   var notesValues = [];

   for ( i = 0; i < 12; i++) { 
      if( i == 0){
         val = 440;
         notesValues.push(val);
      }else{
         val = val  * 1.0594631;
         notesValues.push(val);
      } 
   }

   for (var i = 0;i < notesValues.length; i++) {
      console.log( musicNotes[i] + " : "+ notesValues[i])
   }

// Planets Calculate and console log how many 'minutes' the Moon travels in a day. 
// Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during 
// its daily rotation.

// degrees in a circle  = 360
   var circleDegrees = 360; 
// circular orbit for one round  = 27.3 days
   var oneRound = 27.3;
// calculation per day degrees = 360/27.3 = 13.2
   var perDayDegrees = 360 / 27.3;
// since 1 degree = 60 minutes
   var perDayMinutes = perDayDegrees * 60;
   console.log( "The Moon travels in a day : " + perDayDegrees + " minutes." );