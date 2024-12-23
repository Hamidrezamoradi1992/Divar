function AllAdvertisingCategoryID(categoryID) {
    let token = getCookie('refresh');
    if (token) {
        const datas = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/advertise/filter/category/${categoryID}`, {
            method: 'GET',
        })
        datas.then(response => {
            let El = '';

            response.forEach(data => {

                const el = `  
                <div class="card card-side bg-base-100 shadow-xl max-w-[450px] max-h-[230px]">  
                    <figure class="max-w-[160px] max-h-[230px]">  
                        <img  
                            src="${data.image.file}"  
                            alt="${data.image.alt}" />  
                    </figure>  
                    <div class="card-body">  
                        ${userId ? ` 
                             
                            <label class="swap">  
                                <input type="checkbox" /> 
                            ${data.favorite === true ? `
                            <div class="swap-on" onclick="favoriteAddAndRemove(${data.id})">❤</div> ` : ` 
                            <div class="swap-off" onclick="favoriteAddAndRemove(${data.id})">🤍</div> `} 
                       
                            </label>  
                        ` : ""}  
                        <h2 class="card-title">${data.title}</h2>  
                        <p>${data.price}</p>  
                        <div class="card-actions justify-end">  
                        <a href="http://localhost:8000/advertising/view/add/advertise/${data.id}"><button type="button" class="btn btn-primary">Watch</button>  </a>

                        </div>  
                    </div>  
                </div>`;
                El += el;
            });

            maineViewEl.innerHTML = El;
        }).catch(error => {
            console.error('Error fetching advertising data:', error);
        });


    }


    token = getCookie('access');
    if (!token) {
        const refresh = getCookie('refresh');
        if (!refresh) {
            fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/filter/category/${categoryID}`, {
                method: 'GET',
            }).then(async rs => {
                const response = await rs.json();
                console.log(response);
                let El = '';

                response.forEach(data => {
                    console.log(data);
                    const el = `  
                <div class="card card-side bg-base-100 shadow-xl max-w-[450px] max-h-[230px]">  
                    <figure class="max-w-[160px] max-h-[230px]">  
                        <img  
                            src="${data.image.file}"  
                            alt="${data.image.alt}" />  
                    </figure>  
                    <div class="card-body">  
                        ${userId ? `  
                            <label class="swap">  
                                <input type="checkbox" /> 
                                        ${data.favorite === true ? `
                                            <div class="swap-on" onclick="favoriteAddAndRemove(${data.id})">😍</div> ` :
                        ` <div class="swap-off" onclick="favoriteAddAndRemove(${data.id})">🤍</div> `} 
                                 
                                
                            </label>  
                        ` : ""}  
                        <h2 class="card-title">${data.title}</h2>  
                        <p>${data.price}</p>  
                        <div class="card-actions justify-end">  
                           <a href="http://localhost:8000/advertising/view/add/advertise/${data.id}"><button type="button" class="btn btn-primary">Watch</button>  </a>

                        </div>  
                    </div>  
                </div>`;
                    El += el;
                });

                maineViewEl.innerHTML = El;
            }).catch(error => {
                console.error('Error fetching advertising data:', error);
            });
        }
    }

}