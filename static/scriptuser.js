const addLinkButton = document.getElementsByClassName("setting-1")[0];
const addLink = document.getElementsByClassName("setting-new-link")[0];
const userPageSettingButton = document.getElementsByClassName("setting-2")[0];
const userPageSetting = document.getElementsByClassName("setting-userpage")[0];
const linkForm = document.getElementById("form-new-link");
const descriptionInput = document.getElementById("description");
const linkInput = document.getElementById("url");
const sendLink = document.getElementById("sendLink");
const cancelbutton = document.getElementsByClassName("cancel-button");

const validRegex = /^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?\/?$/gm;
var isLinkFormValid = false, isSettingFormValid = false;

sendLink.addEventListener("click", () => {
    if(isLinkFormValid){
        linkForm.submit()
    }
});
descriptionInput.addEventListener("blur", function () {
  if (descriptionInput.value.length>5) {
   	  descriptionInput.style.borderColor="green";
   	  isLinkFormValid = true;
  } else {
      descriptionInput.style.borderColor="red";
      isLinkFormValid = false;
  }
});

linkInput.addEventListener("blur", function () {
  if (linkInput.value.match(validRegex)) {
   	  linkInput.style.borderColor="green";
   	  isLinkFormValid = true;
  } else {
      linkInput.style.borderColor="red";
      isLinkFormValid = false;
  }
});


function hideUserPageSetting(){
    userPageSetting.style.display="none";
}
function hideLinkSetting(){
    addLink.style.display="none";
}

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