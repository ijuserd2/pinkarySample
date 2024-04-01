const navbar = document.getElementsByClassName("navbar")[0];
const navbarBox = document.getElementsByClassName("navbar-box")[0];

const updateAccForm = document.getElementById("update_account_form");
const updatePwdForm = document.getElementById("update_pwd");
const fullName = document.getElementById("name");
const userName = document.getElementById("username");
const email = document.getElementById("email");
const bio = document.getElementById("bio");
const saveAcc = document.getElementById("save-acc");
const oldPw = document.getElementById("old_pw");
const newPw = document.getElementById("new_pw");
const cNewPW = document.getElementById("c_new_pw");
const savePass = document.getElementById("change-pw");

let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
var isUpdateAccValid = false, isUpdatePwdValid = false;
var isNameValid = false, isUserNameValid=false, isEmailValid=false, isBioValid=false;
var isOldPwValid = false, isNewPwValid=false, isCNewPwValid=false;


function checkUpdateAccValidity(){
    if(isNameValid && isUserNameValid && isEmailValid && isBioValid){
        return true;
    }
    return false;
}

function checkUpdatePassValidity(){
    if(isOldPwValid && isNewPwValid && isCNewPwValid){
        return true;
    }
    return false;
}


navbar.addEventListener("click",function(){
    if(navbarBox.style.display=="block"){
        navbarBox.style.display="none";
    }else{
        navbarBox.style.display="block";
    }
});

saveAcc.addEventListener("click",function(){
    if(checkUpdateAccValidity()){
        updateAccForm.submit();
    }
});

savePass.addEventListener("click",function(){
    if(checkUpdatePassValidity()){
        updatePwdForm.submit();
    }
});

fullName.addEventListener("blur", function () {
    if(fullName.value.length>3){
        fullName.style.borderColor="green";
        isNameValid = true;
    } else {
        fullName.style.borderColor="red";
        isNameValid = false;
    }
});
userName.addEventListener("blur", function () {
    if(userName.value.length>3){
        userName.style.borderColor="green";
        isUserNameValid = true;
    } else {
        userName.style.borderColor="red";
        isUserNameValid = false;
    }
});
email.addEventListener("blur", function () {
    if(email.value.match(validRegex)){
        email.style.borderColor="green";
        isEmailValid = true;
    } else {
        email.style.borderColor="red";
        isEmailValid = false;
    }

});

bio.addEventListener("blur", function () {
    if(bio.value.length>5){
        bio.style.borderColor="green";
        isBioValid = true;
    } else {
        bio.style.borderColor="red";
        isBioValid = false;
    }

});


oldPw.addEventListener("blur", function () {
    if(oldPw.value.length>8){
        oldPw.style.borderColor="green";
        isOldPwValid = true;
    } else {
        oldPw.style.borderColor="red";
        isOldPwValid = false;
    }

});
newPw.addEventListener("blur", function () {
    if(newPw.value.length>8){
        newPw.style.borderColor="green";
        isNewPwValid = true;
    } else {
        newPw.style.borderColor="red";
        isNewPwValid = false;
    }

});
cNewPW.addEventListener("blur", function () {
    if(isNewPwValid==true){
        if(cNewPW.value == newPw.value) {
            cNewPW.style.borderColor="green";
            isCNewPwValid = true;
        }else{
            cNewPW.style.borderColor="red";
            isCNewPwValid = false;
        }

    } else {
        cNewPW.style.borderColor="red";
        isCNewPwValid = false;
    }
});