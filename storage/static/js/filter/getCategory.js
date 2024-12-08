function getCategory(id_category = null) {
    console.log('hamid22')
    categoryViewEL.innerHTML = ''
    if (id_category) {
        const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/${id_category}`, {
            method: 'GET',

        })

        data.then(dats => {
            console.log(dats)
            categoryViewEL.innerHTML = ""
            let el = '';
            dats.forEach(category => {
                el +=`
                    <div class="relative inline-block mx-[10px]">
                        <button class="btn btn-accent"
                                onClick="getCategory(${category.id})">${category.title}</button>
                        <div class="avatar absolute top-[-30px] right-[-10px]">
                            <div class="mask mask-hexagon w-11">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"/>
                            </div>
                        </div>
                    </div>`
            });

            if (id_category) {
                el += `<button class="btn btn-outline btn-error mx-3" onclick="getCategory()">back</button>`;
            }
            console.log(dats.length)
            if (dats.length === 0) {
                location.assign(`http://localhost:8000//advertising/view/filter/${id_category}`)
            }
            categoryViewEL.innerHTML = el;
        }).catch(error => {
            console.error('Error:', error);
        });

    } else {

        const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/`, {
            method: 'GET',

        })

        data.then(dats => {
            categoryViewEL.innerHTML = ""
            let el = '';
            dats.forEach(category => {
                el +=`
                    <div class="relative inline-block mx-[10px]">
                        <button class="btn btn-accent"
                                onClick="getCategory(${category.id})">${category.title}</button>
                        <div class="avatar absolute top-[-30px] right-[-10px]">
                            <div class="mask mask-hexagon w-11">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"/>
                            </div>
                        </div>
                    </div>
`
                ;
            });

            categoryViewEL.innerHTML = el;
        }).catch(error => {
            console.error('Error:', error);
        });

    }

}

