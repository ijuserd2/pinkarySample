const navbar = document.getElementsByClassName("navbar")[0];
const navbarBox = document.getElementsByClassName("navbar-box")[0];
const emailBox = document.getElementById("email");
const nameBox = document.getElementById("name");
const userNameBox = document.getElementById("username");
const passwordBox = document.getElementById("pw");
const passwordConfirmBox = document.getElementById("cpw");
const registerForm = document.getElementById("registerform");
const sendButton = document.getElementById("sendbutton");


const warningText = document.createElement("p");
const node = document.createTextNode("Invalid email address");
warningText.appendChild(node);
warningText.style.color="red", warningText.style.padding="5px 0";


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
var isEmailValid = false, isNameValid=false, isUserNameValid = false, isPwValid = false, isCPwValid= false;
var isReady=false;

function checkValidity(){
    if(isEmailValid && isNameValid && isUserNameValid && isPwValid && isCPwValid){
        return true;
    }
    return false;
}


registerForm.addEventListener("change", () => {
    if(!checkValidity()){
        registerForm.disable=true;
    }else{
        registerForm.disable=false;
    }
});


emailBox.addEventListener("blur", function () {
  if (emailBox.value.match(validRegex)) {
   	  emailBox.style.borderColor="rgba(0,0,0,0.2)";
   	  isEmailValid = true;
  } else {
      emailBox.style.borderColor="red";
      isEmailValid = false;
  }
});

nameBox.addEventListener("blur", function () {
    if(nameBox.value.length>3){
        nameBox.style.borderColor="green";
        isNameValid = true;
    } else {
        nameBox.style.borderColor="red";
        isNameValid = false;
    }
});
userNameBox.addEventListener("blur", function () {
    if(userNameBox.value.length>3){
        userNameBox.style.borderColor="green";
        isUserNameValid = true;
    } else {
        userNameBox.style.borderColor="red";
        isUserNameValid = false;
    }

});
passwordBox.addEventListener("blur", function () {
    if(passwordBox.value.length>8){
        passwordBox.style.borderColor="green";
        isPwValid = true;
    } else {
        passwordBox.style.borderColor="red";
        isPwValid = false;
    }

});
passwordConfirmBox.addEventListener("blur", function () {
    if(isPwValid==true){
        if(passwordConfirmBox.value == passwordBox.value) {
            passwordConfirmBox.style.borderColor="green";
            isCPwValid = true;
        }else{
            passwordConfirmBox.style.borderColor="red";
            isCPwValid = false;
        }

    } else {
        passwordConfirmBox.style.borderColor="red";
        isCPwValid = false;
    }
});

navbar.addEventListener("click",function(){
    if(navbarBox.style.display=="block"){
        navbarBox.style.display="none";
    }else{
        navbarBox.style.display="block";
    }
});