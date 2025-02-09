
let form = document.getElementById("userForm")

form.addEventListener("submit",async function(e){
  e.preventDefault()
  console.log("This FAR")
  const email = document.getElementById("userEmail")
  const password = document.getElementById("userPassword")

  const json = await login(email.value,password.value)
  console.log(json)
  }
)

async function login(email,password){

  try{
    const res = await fetch("http://127.0.0.1:5000/login",{
      method:"POST",
      headers:{ 'Content-Type': 'application/json' },
      body:JSON.stringify({email:email,password:password})
      }
    )

    if(!res.ok){
      throw new Error(`Response status: ${res.status}`)
    }
    const data = await res.json();  // Await the JSON response
    console.log(data);  // Logs actual response data

    return data

  }catch (err){
    console.log(err)
  }
}