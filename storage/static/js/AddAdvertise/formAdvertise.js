function formAdvertise(city_id) {
    cityId = city_id
    formView.innerHTML = ''
    categoryKey.innerHTML = `<button class="btn btn-outline btn-error mx-3" onclick="getCategory()">back</button>`;
    formView.innerHTML = `
        <form action="" id="form_input" class="flex flex-col gap-4">
            <div class="flex gap-4">
                <input type="text" name="title" placeholder="title" class="input input-bordered w-full max-w-xs"/>
                <input type="number" name="price" placeholder="price" class="input input-bordered w-full max-w-xs"/>
            </div>
            <textarea name="description" class="textarea textarea-bordered" placeholder="Bio"></textarea>
            <button class="btn btn-ghost" type="button" onclick="send_form()">accept</button>
        </form>`


}

function send_form() {
    const form_advertise = document.querySelector('#form_input')
    let data = new FormData(form_advertise)
    data.append('category', parseInt(categoryId))
    data.append('state', parseInt(stateId))
    data.append('city', parseInt(cityId))
    data.append('user', parseInt(userId))
    const csrfTokens = getCookie('csrftoken')


    const advertise_send = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/`, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: data,

    })

    advertise_send.then(response => {
        console.log('re', response)
        console.log(response.status)

        advertiseId = response.advertise
        setImage(response.advertise)


    }).catch(error => {
        console.error('Error:', error);
    });

}