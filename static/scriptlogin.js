const navbar = document.getElementsByClassName("navbar")[0];
const navbarBox = document.getElementsByClassName("navbar-box")[0];
const emailBox = document.getElementById("email");
const passwordBox = document.getElementById("pw");
const registerForm = document.getElementById("formlogin");
const sendButton = document.getElementById("sendbutton");

const warningText = document.createElement("p");
const node = document.createTextNode("Invalid email address");
warningText.appendChild(node);
warningText.style.color="red", warningText.style.padding="5px 0";


let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
var isEmailValid = false, isPwValid = false;

function checkValidity(){
    if(isEmailValid && isPwValid){
        return true;
    }
    return false;
}

sendButton.addEventListener("click", () => {
    if(checkValidity()){
        registerForm.submit()
    }
});
emailBox.addEventListener("blur", function () {
  if (emailBox.value.match(validRegex)) {
   	  emailBox.style.borderColor="green";
   	  isEmailValid = true;
  } else {
      emailBox.style.borderColor="red";
      isEmailValid = false;
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

navbar.addEventListener("click",function(){
    if(navbarBox.style.display=="block"){
        navbarBox.style.display="none";
    }else{
        navbarBox.style.display="block";
    }
});

userPageSettingButton.addEventListener("click",function(){
    if(addLink.style.display=="block"){
        addLink.style.display="none";
    }
    if(userPageSetting.style.display=="block"){
        userPageSetting.style.display="none";
    }else{
        userPageSetting.style.display="block";
    }
});
addLinkButton.addEventListener("click",function(){
    if(userPageSetting.style.display=="block"){
        userPageSetting.style.display="none";
    }
    if(addLink.style.display=="block"){
        addLink.style.display="none";
    }else{
        addLink.style.display="block";
    }
});