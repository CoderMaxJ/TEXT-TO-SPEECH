var box=document.getElementById('storage');
var textarea=document.getElementById('text');
var btn=document.querySelector('.button1');
var button1=document.getElementById("button1");

setTimeout(function(){
    box.style.display='block';
    box.style.opacity=1;
    box.style.marginTop='200px';
    
    textarea.style.opacity='50%';
    textarea.style.display='none';
    textarea.style.pointerEvents='none';
    btn.style.pointerEvents='none';
    btn.style.opacity='50%';
    button1.style.display='none';


},33000)

function autoclick(){
    setTimeout(function(){
button1.click();
    },1000)
}

autoclick(); 




const output = document.getElementById('text');
const text = "HI' MY NAME IS JEL. I AM AI THAT CONVERT TEXT INTO VOICE. I WAS DESIGN TO ASSIST MUTE PEOPLE IN ORDER THEM TO SPEAK USING COMPUTER, I WAS DEVELOP BY 3 COMPUTER SCIENTIST NAMELY  JOHNSEN, PHILIP, LOVELYN. I WOULD LIKE YOU TO REMIND THAT I WAS FOR ONE PURPOSE AND THAT IS TO ASSIST. AVOID INPUTTING TEXT THAT CONTAINS  INAPPROPRIATE WORDS OTHERWISE YOUR TEXT WILL BE REJECTED";

let i = 0;
function simulateTyping() {
  if (i < text.length) {
    output.value += text.charAt(i);
    i++;
    setTimeout(simulateTyping, 78);
  }
}

// // input.value = text;
simulateTyping();

const message=new SpeechSynthesisUtterance("HI, MY NAME IS JELL. I AM AI THAT CONVERT TEXT INTO VOICE. I WAS DESIGN TO ASSIST MUTE PEOPLE IN ORDER THEM TO SPEAK USING COMPUTER, I WAS DEVELOP BY 3 COMPUTER SCIENTIST NAMELY  JOHNSEN  , PHILIP , LOVELYN. I WOULD LIKE YOU TO REMIND THAT I WAS FOR ONE PURPOSE AND THAT IS TO ASSIST. AVOID INPUTTING TEXT THAT CONTAINS  INAPPROPRIATE WORDS OTHERWISE YOUR TEXT WILL BE REJECTED");

message.lang='en-US';
message.volume=1;
message.rate=0.80;
message.pitch=1;

window.addEventListener('load',()=>{
  speechSynthesis.speak(message);
})

