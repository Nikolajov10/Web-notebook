function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/notebook";
  });
}

dna=[]
dna_len=0
last_time=-1
$(document).ready(function() {
    $("#password").keyup(function() {
        let password = document.getElementById("password").value;
        let today=new Date();
        let time=today.getHours()*3600000 + today.getMinutes()*60000 +
        today.getSeconds()*1000 + today.getMilliseconds();
        if (dna_len==0){
            last_time=time;
            dna.push(0)
            dna_len++;
        }
        else {
            while(password.length>dna_len){
                dna.push(time-last_time);
                dna_len++;
            }
            while(password.length<dna_len){
                dna.pop();
                dna_len--;
            }
        }
        last_time=time;
    });
});

function regDna() {
    let user_name=document.getElementById("name").value;
    let password1 = document.getElementById("password").value;
    let email=document.getElementById("email").value;
    let password2 = document.getElementById("password2").value;
    fetch("/register", {
    method: "POST",
    body: JSON.stringify({ DNA: dna,name:user_name,password1:password1,email:email,password2:password2 }),
  }).then((_res) => {
    window.location.href = "/reg-wrapper";
  });
}

function sendDna() {
    let user_name=document.getElementById("name").value;
    let password = document.getElementById("password").value;
    fetch("/login", {
    method: "POST",
    body: JSON.stringify({ DNA: dna,name:user_name,password:password }),
  }).then((_res) => {
    window.location.href = "/login-wrapper";
  });
}