function AllAdvertisingView(id_advertising) {
    console.log(id_advertising)
    const product_title = document.querySelector('#product_title');
    const category = document.querySelector('#category');
    const price_product = document.querySelector('#price_product');
    const specifications = document.querySelector('#specifications');
    const description_short = document.querySelector('#description_short');
    const keyImage = document.querySelector('#keyImage');
    const ImageFile = document.querySelector('#ImageFile');
    const addressEl = document.querySelector('#address');
    // address
    var data = ''
    let token = getCookie('access');
    if (!token) {
        const refresh = getCookie('refresh');
        if (!refresh) {
            fetch(`http://localhost:${domainPort}/advertising/api/detail/advertise/${id_advertising}`, {
                method: 'GET',
            }).then(async rs => {
                data = await rs.json()
                addressEl.innerHTML = `${data.address.massage}`

                //     start

                console.log(data)
                product_title.innerHTML = `${data.title}`
                price_product.innerHTML = `${data.price}`
                description_short.innerHTML = `${data.description}`


                let El = ''
                data.vlue_field.forEach(field => {

                    const el = `<li class="flex gap-2">  
                    <h2 class="font-bold capitalize">${field.name_field}</h2> :   
                    <p>${field.field_type === 'bool' ?
                        `${field.value === "1" ? '✅' : '☑'}` : field.value}  
                    </p>  
                </li>`;
                    El += el
                })
                specifications.innerHTML = El
                let count = 0
                El = ''
                console.log('data.image',data.image)
                if (data.image.length>0) {
                    data.image.forEach(image => {
                        count++
                        const el = `<div id="item${count}" class="carousel-item w-full">
                    <img
                            src="${image.file}"
                            alt="${image.alt}"
                            class="w-full"/>
                </div>`
                        El += el

                    })

                    ImageFile.innerHTML = ''
                    ImageFile.innerHTML = El
                    El = ''
                    count = 0
                    data.image.forEach(image => {
                        count++
                        const el = `<a type="button" href="#item${count}" class="btn btn-xs">${count}</a>`
                        El += el
                    })
                    keyImage.innerHTML = ''
                    keyImage.innerHTML = El
                } else {
                    ImageFile.innerHTML = `<div class="skeleton h-full w-full"></div>`

                }

                El = ''

                //     end
            })
        }
    }
    token = getCookie('refresh');
    if (token) {
        const datas = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/detail/advertise/${id_advertising}`, {
            method: 'GET',
        })
        let data2 =
            datas.then(data => {

                console.log(data)
                product_title.innerHTML = `${data.title}`
                price_product.innerHTML = `${data.price}`
                description_short.innerHTML = `${data.description}`
                addressEl.innerHTML = `${data.address[0].address}`
                idUserAdvertising = `${data.address[0].id}`


                let El = ''
                data.vlue_field.forEach(field => {

                    const el = `<li class="flex gap-2">  
                    <h2 class="font-bold capitalize">${field.name_field}</h2> :   
                    <p>${field.field_type === 'bool' ?
                        `${field.value === "1" ? '✅' : '☑'}` : field.value}  
                    </p>  
                </li>`;
                    El += el
                })
                specifications.innerHTML = El
                let count = 0
                El = ''

                if (data.image.length>0) {
                    data.image.forEach(image => {
                        count++
                        const el = `<div id="item${count}" class="carousel-item w-full">
                    <img
                            src="${image.file}"
                            alt="${image.alt}"
                            class="w-full"/>
                </div>`
                        El += el

                    })

                    ImageFile.innerHTML = ''
                    ImageFile.innerHTML = El
                    El = ''
                    count = 0
                    data.image.forEach(image => {
                        count++
                        const el = `<a type="button" href="#item${count}" class="btn btn-xs">${count}</a>`
                        El += el
                    })
                    keyImage.innerHTML = ''
                    keyImage.innerHTML = El
                } else {
                    ImageFile.innerHTML = `<div class="skeleton h-full w-full"></div>`

                }
                El = ''
                buttonDetailEl.innerHTML=`        
                <button class="tab btn" onclick="viewMassage()">massage</button>
                <button class=" w-auto tab btn btn-ghost" onclick="">Update Profile</button>
                <button class=" tab btn">Favorite</button>`

            }).catch()


    }
    // end addressEl


}