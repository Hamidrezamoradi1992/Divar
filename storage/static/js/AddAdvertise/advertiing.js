function get_state(category_id) {
    categoryId=category_id
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/state`, {
        method: 'GET',
    })
    data.then(dats => {
        categoryKey.innerHTML = ""
        let el = '';
        dats.forEach(state => {
            el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="get_city(${state.id})">${state.title}</button>`;
        });
        el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory()">back</button>`;
        categoryKey.innerHTML = el;
    })

}

function get_city(state_id) {
    stateId=state_id
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/city/${stateId}`, {
        method: 'GET',
    })
    data.then(dats => {
        categoryKey.innerHTML = ""
        let el = '';
        dats.forEach(city => {
            el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="formAdvertise(${city.id})">${city.title}</button>`;
        });
        el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory()">back</button>`;
        categoryKey.innerHTML = el;
    })
}