function getCategory(id_category = null) {

    if (id_category) {
        console.log('hamid22')
        const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/${id_category}`, {
            method: 'GET',

        })

        data.then(dats => {
            categoryKey.innerHTML = ""
            let el = '';
            dats.forEach(category => {
                el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory(${category.id})">${category.title}</button>`;
            });

            if (id_category) {
                el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory()">back</button>`;
            }
            console.log(dats.length)
            if (dats.length === 0) {
                get_state(id_category)
            }
            categoryKey.innerHTML = el;
        }).catch(error => {
            console.error('Error:', error);
        });

    } else {

        const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/`, {
            method: 'GET',

        })

        data.then(dats => {
            categoryKey.innerHTML = ""
            let el = '';
            dats.forEach(category => {
                console.log(category);
                el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory(${category.id})">${category.title}</button>`;
            });

            categoryKey.innerHTML = el;
        }).catch(error => {
            console.error('Error:', error);
        });

    }

}

