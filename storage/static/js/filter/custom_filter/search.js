function search() {
    let formSearchEL = document.querySelector('#formSearch')
    const data = new FormData(formSearchEL)
    const csrfTokens = getCookie('csrftoken')
    fetch('http://localhost:8000/advertising/api/add/advertise/filter', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: data,


    }).then(async res=>{
        const response = await res.json();
                console.log(response);
                let El = '';

                response.forEach(data => {
                    console.log('dasdasd',data);
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
    })

}