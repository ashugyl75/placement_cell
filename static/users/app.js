const signInLink = document.querySelector("#signInLink");
const signUpLink = document.querySelector("#signUpLink");
const signUpForm = document.querySelector(".signUp"); // Corrected selector for the sign-up form
const signInForm = document.querySelector(".signIn"); // Corrected selector for the sign-in form

signInLink.addEventListener('click', () => {
    signUpForm.classList.add("dontdisplay");
    signInForm.classList.remove("dontdisplay");
});

signUpLink.addEventListener('click', () => {
    signUpForm.classList.remove("dontdisplay");
    signInForm.classList.add("dontdisplay");
});



// signUpForm.addEventListener('submit', function(event) {
//     var password1 = document.getElementById('password1').value;
//     var password2 = document.getElementById('password2').value;

//     if (password1 !== password2) {
//         // Prevent form submission
//         event.preventDefault();

//         // Display an error message or perform any desired action
//         alert('Passwords do not match. Please re-enter.');

//         // Clear the password fields for re-entry (optional)
//         document.getElementById('password1').value = '';
//         document.getElementById('password2').value = '';
//     }
// });

function checkPassword(form) { 
    password1 = form.password1.value; 
    password2 = form.password2.value; 

    // // If password not entered 
    // if (password1 == '') 
    //     alert ("Please enter Password"); 
          
    // // If confirm password not entered 
    // else if (password2 == '') 
    //     alert ("Please enter confirm password"); 
          
    // If Not same return False.     
    if (password1 != password2) { 
        alert ("\nPassword did not match: Please try again...") 
        return false; 
    } 

    // If same return True. 
    else{ 
        // alert("Password Match: Welcome to GeeksforGeeks!") 
        return true; 
    } 
}