const navbar = document.getElementsByClassName("navbar")[0];
const navbarbox = document.getElementsByClassName("navbar-box")[0];
navbar.addEventListener("click",function(){
    if(navbarbox.style.display=="block"){
        navbarbox.style.display="none";
    }else{
        navbarbox.style.display="block";
    }
})