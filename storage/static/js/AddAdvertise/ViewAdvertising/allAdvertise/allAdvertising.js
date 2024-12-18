function AllAdvertising(url = null) {
    console.log("Current URL:", url);
    var urlUser = `http://localhost:${domainPort}/advertising/api/all/advertising`;
    if (url) {
        urlUser = url;
    }

    fetch(urlUser, {
        method: 'GET',
    })
        .then(async (rs) => {
            const response = await rs.json();
            console.log(response);
            let El = '';

            // مقداردهی به دکمه‌ها
            const nextButton = document.getElementById("next");
            const previousButton = document.getElementById("previous");

            nextButton.value = response.next || '';
            previousButton.value = response.previous || '';

            // غیرفعال کردن دکمه‌ها بر اساس وضعیت
            if (!response.next) {
                nextButton.disabled = true;
            } else {
                nextButton.disabled = false;
            }

            if (!response.previous) {
                previousButton.disabled = true;
            } else {
                previousButton.disabled = false;
            }

            // رندر داده‌ها
            response.results.forEach((data) => {
                console.log(data);
                const el = `
                <div class="card card-side bg-base-100 shadow-xl max-w-[450px] max-h-[230px]">
                    <figure class="max-w-[160px] max-h-[230px]">
                        <img
                            src="${data.image.file}"
                            alt="${data.image.alt}" />
                    </figure>
                    <div class="card-body">
                        ${
                            userId
                                ? `
                            <label class="swap">
                                <input type="checkbox" />
                                ${
                                    data.favorite
                                        ? `<div class="swap-on" onclick="favoriteAddAndRemove(${data.id})">😍</div>`
                                        : `<div class="swap-off" onclick="favoriteAddAndRemove(${data.id})">🤍</div>`
                                }
                            </label>
                        `
                                : ''
                        }
                        <h2 class="card-title">${data.title}</h2>
                        <p>${data.price}</p>
                        <div class="card-actions justify-end">
                           <a href="http://localhost:8000/advertising/view/add/advertise/${data.id}">
                               <button type="button" class="btn btn-primary">Watch</button>
                           </a>
                        </div>
                    </div>
                </div>`;
                El += el;
            });

            maineViewEl.innerHTML = El;
        })
        .catch((error) => {
            console.error('Error fetching advertising data:', error);
        });
}

// function AllAdvertising(url = NaN) {
//     console.log(url)
//     var urlUser = `http://localhost:${domainPort}/advertising/api/all/advertising`
//     if (url) {
//         urlUser = url
//     }
//
//     fetch(`${urlUser}`, {
//         method: 'GET',
//     }).then(async rs => {
//         const response = await rs.json();
//         console.log(response);
//         let El = '';
//         console.log(response.next);
//         console.log(response.previous);
//         document.getElementById("next").value = response.next;
//         document.getElementById("previous").value = response.previous;
//         response.results.forEach(data => {
//             console.log(data);
//             const el = `
//                 <div class="card card-side bg-base-100 shadow-xl max-w-[450px] max-h-[230px]">
//                     <figure class="max-w-[160px] max-h-[230px]">
//                         <img
//                             src="${data.image.file}"
//                             alt="${data.image.alt}" />
//                     </figure>
//                     <div class="card-body">
//                         ${userId ? `
//                             <label class="swap">
//                                 <input type="checkbox" />
//                                         ${data.favorite === true ? `
//                                             <div class="swap-on" onclick="favoriteAddAndRemove(${data.id})">😍</div> ` :
//                 ` <div class="swap-off" onclick="favoriteAddAndRemove(${data.id})">🤍</div> `}
//
//
//                             </label>
//                         ` : ""}
//                         <h2 class="card-title">${data.title}</h2>
//                         <p>${data.price}</p>
//                         <div class="card-actions justify-end">
//                            <a href="http://localhost:8000/advertising/view/add/advertise/${data.id}"><button type="button" class="btn btn-primary">Watch</button>  </a>
//
//                         </div>
//                     </div>
//                 </div>`;
//             El += el;
//         });
//
//         maineViewEl.innerHTML = El;
//     }).catch(error => {
//         console.error('Error fetching advertising data:', error);
//     });
//
//
// }