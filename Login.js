//Importing The Readline Module
const readline = require('readline-sync');

let S_Username, S_Password;

// Welcome to the Login Screen
console.log('Welcome to The Login Page!');

// Giving the User Login Options
console.log('\nWhat would you like to do?');

console.log('\n\n(1). Sign Up');
console.log('(2). Sign In');

// User chooses from Options
let Login_Options = readline.question('\nConsole: ');

// Converting User Input from Str to Int
Login_Options = parseInt(Login_Options);


// User chooses their Login Information
if (Login_Options === 1) {

    let S_Username = readline.question('\nWhat do you want your Username to be?: ');
    let S_Password = readline.question('\nWhat do you want your Password to be?: ');

    console.log('\nThanks for Signing Up!')
    
    Login_Options = 2;

// User Provides their Login Information
}

if (Login_Options === 2) {

    let L_Username = readline.question('\nWhat is your Username?: ');
    let L_Password = readline.question('\nWhat is your Password?: ');

// If User Info is Correct print Access Granted
    if (L_Username == S_Username && L_Password == S_Password) {
        console.log('\n[ACCESS GRANTED]')
        
// Else Statement if User Info is Invalid
    } else {

        console.log('\n[ACCESS DENIED]')
    }
}