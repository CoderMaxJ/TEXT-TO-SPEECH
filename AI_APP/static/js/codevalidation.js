var email=document.getElementById("email")
var code=document.getElementById("code")

var btn=document.getElementById("btnclear");

btn.addEventListener("click",()=>{
    email.value="";
    code.value="";
})