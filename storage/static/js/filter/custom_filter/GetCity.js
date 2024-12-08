function getCity(stateId) {
    let CityEL = document.querySelector('#getCity')
    CityEL.innerHTML = ""

    fetch( `http://localhost:${domainPort}/advertising/api/add/advertise/city/${stateId}`, {
        method: 'GET'
    }).then(response => {
        const category = response.json()
        category.then(data => {
            CityEL.innerHTML = `<option value="None">City</option>`
            let el = ``
            data.forEach(cat => {
                el += `<option value="${cat.id}">${cat.title}</option>`

            })
            CityEL.innerHTML += el
        })

    }).catch()


}