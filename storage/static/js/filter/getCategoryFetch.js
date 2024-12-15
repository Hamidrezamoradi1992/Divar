function getCategoryFetch(id_category = null) {
    console.log('hamid22')
    categoryViewEL.innerHTML = ''
    if (id_category) {
        fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/${id_category}`, {
            method: 'GET',

        }).then(res => {
            const data = res.json()

            data.then(dats => {
                console.log(dats)
                categoryViewEL.innerHTML = ""
                let el = '';
                dats.forEach(category => {
                    el += `
                    <div class="relative inline-block mx-[10px]">
                        <button class="btn btn-accent"
                                onClick="getCategoryFetch(${category.id})">${category.title}</button>
                        <div class="avatar absolute top-[-30px] right-[-10px]">
                            <div class="mask mask-hexagon w-11">
                                <img src="${category.image}"/>
                            </div>
                        </div>
                    </div>`
                });

                if (id_category) {
                    el += `<button class="btn btn-outline btn-error mx-3" onclick="getCategoryFetch()">back</button>`;
                }
                console.log(dats.length)
                if (dats.length === 0) {
                    location.assign(`http://localhost:8000//advertising/view/filter/${id_category}`)
                }
                categoryViewEL.innerHTML = el;
            }).catch(error => {
                console.error('Error:', error);
            });
        })
    } else {

        fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/all_category/`, {
            method: 'GET',

        }).then(res => {
            const data = res.json()
                console.log(data)
            data.then(dats => {
                console.log(dats)
                categoryViewEL.innerHTML = ""
                let el = '';
                dats.forEach(category => {
                    el += `
                    <div class="relative inline-block mx-[10px]">
                        <button class="btn btn-accent"
                                onClick="getCategoryFetch(${category.id})">${category.title}</button>
                        <div class="avatar absolute top-[-30px] right-[-10px]">
                            <div class="mask mask-hexagon w-11">
                                <img src="${category.image}"/>
                            </div>
                        </div>
                    </div>
                        `
                    ;
                });

                categoryViewEL.innerHTML = el;
            })
        }).catch(error => {
            console.error('Error:', error);
        });

    }

}

