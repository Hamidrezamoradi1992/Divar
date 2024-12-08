function getGeneralCategory(id_category) {
    let GeneralCategoriesEL = document.querySelector('#getGeneralCategories')
    GeneralCategoriesEL.innerHTML = ""

    fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/`, {
        method: 'GET'
    }).then(response => {
        const category = response.json()
        category.then(data => {
            GeneralCategoriesEL.innerHTML =`
                <option value="">----------------</option>
                <option value="${id_category}">this</option>
                `
            let el = ``
            data.forEach(cat => {
                el += `<option value="${cat.id}">${cat.title}</option>`

            })
            GeneralCategoriesEL.innerHTML += el
        })

    }).catch()


}