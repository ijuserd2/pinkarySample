const navbar = document.getElementsByClassName("navbar")[0];
const navbarBox = document.getElementsByClassName("navbar-box")[0];
const addLinkButton = document.getElementsByClassName("setting-1")[0];
const addLink = document.getElementsByClassName("setting-new-link")[0];
const userPageSettingButton = document.getElementsByClassName("setting-2")[0];
const userPageSetting = document.getElementsByClassName("setting-userpage")[0];
navbar.addEventListener("click",function(){
    if(navbarBox.style.display=="block"){
        navbarBox.style.display="none";
    }else{
        navbarBox.style.display="block";
    }
})

userPageSettingButton.addEventListener("click",function(){
    if(addLink.style.display=="block"){
        addLink.style.display="none";
    }
    if(userPageSetting.style.display=="block"){
        userPageSetting.style.display="none";
    }else{
        userPageSetting.style.display="block";
    }
})
addLinkButton.addEventListener("click",function(){
    if(userPageSetting.style.display=="block"){
        userPageSetting.style.display="none";
    }
    if(addLink.style.display=="block"){
        addLink.style.display="none";
    }else{
        addLink.style.display="block";
    }
})