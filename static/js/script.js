// Example POST method implementation:
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST", headers: {
        "Content-Type": "application/json",
      }, body: JSON.stringify(data),
    });
    return response.json();
  }

sendButton.addEventListener("click", async ()=>{
    questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput;

    // Get the answer and populate it!
    let result = await postData("/api", {"question": questionInput})
    let string = String(result.answer)
    let ind = 1;
    const typing = () => {
      solution.innerHTML =  string.slice(0, ind)
      ind++;
      setTimeout(() => typing(), 30)
    }

    typing()
    // solution.innerHTML = result.answer
})


function reload(){
  let reload = document.querySelector('.reload');
  reload.addEventListener('click', () => {
    window.location.reload();
})
}


let developer = "Developed by:- Kunal Gurjar, Shashank Mandloi and Vasundhara Patil"
let developed = document.querySelector('.developed')
    let ind = 1;
    const typing2 = () => {
      developed.innerHTML =  developer.slice(0, ind)
      ind > developer.length ? ind = 1 : ind++
      setTimeout(() => typing2(), 50)
    }

    typing2()