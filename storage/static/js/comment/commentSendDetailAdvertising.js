function viewMassage() {
    viewMassageEl.classList.remove('!hidden')
}

function sendMassage() {
    console.log(userId)
    console.log(IdAdvertising)
    console.log(idUserAdvertising)
    let massageFormEl = document.querySelector('#massageForm')
    let data = new FormData(massageFormEl)
    data.append('to_user', idUserAdvertising)
    data.append('advertised', IdAdvertising)
    const send = fetchWithAuth(`http://localhost:8000/comment/api/send`, {
        method: 'POST',
        body: data
    })

}