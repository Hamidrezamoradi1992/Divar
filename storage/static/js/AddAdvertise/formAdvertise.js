function formAdvertise(city_id) {
    cityId = city_id
    formView.innerHTML = ''
    categoryKey.innerHTML = `<button class="btn btn-outline mx-3 btn-secondary" onclick="getCategory()">back</button>`;
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
    let data=FormData()
    const advertise_send = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/`, {
        method: 'POST',
            headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfTokens
                },

    })

}