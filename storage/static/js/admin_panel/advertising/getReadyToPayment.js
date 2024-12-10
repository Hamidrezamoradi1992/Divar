function getReadyToPayment() {
    let itemAdvertiseEl = document.querySelector("#itemAdvertise")
    let advertiseEl = document.querySelector('#advertise')
    let button_viewEL = document.querySelector('#button_view')
    button_viewEL.innerHTML=``
    advertiseEl.classList.remove('!hidden')

    itemAdvertiseEl.innerHTML = ''
    const get_data = fetchWithAuth(`http://localhost:8000/advertising/api/adminpanel/forpayment/advertising`, {
        method: 'GET'
    })
    get_data.then(response => {

        response.datas.forEach(advertisingPublisher => {
            const date = new Date(advertisingPublisher.expires_at);
            const formattedDate = date.toLocaleDateString();
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const result = `${formattedDate} ${hours}:${minutes}`;
            itemAdvertiseEl.innerHTML += `
                <tr>
                    <th>
                        <label>
                            <input type="checkbox" class="checkbox"/>
                        </label>
                    </th>
                    <td>
                        <div class="flex items-center gap-3">
                            <div class="avatar">
                                <div class="skeleton mask mask-squircle h-12 w-12">
                                    <a href="http://localhost:8000/advertising/view/add/advertise/${advertisingPublisher.id}">
                                        <img
                                            src="${advertisingPublisher.image.file}"
                                            alt="${advertisingPublisher.image.alt}"/>
                                    </a>
                                </div>
                            </div>
                            <div>
                                <div class="font-bold">${advertisingPublisher.title}</div>
                                <!--              <div class="text-sm opacity-50">United States</div>-->
                            </div>
                        </div>
                    </td>
                    <td>
                        ${advertisingPublisher.description}
                        <br/>
                        <span class="badge badge-ghost badge-sm">active: ${advertisingPublisher.is_active}</span>
                    </td>
                    <td>${result}</td>
                    <th>
 
                    </th>
                </tr>
`
        })

        console.log(response.order)
        console.log(response.total)
        button_viewEL.innerHTML =
            `
            <div class=" grid grid-cols-2 w-[500px] m-auto ">
                <section class="btn w-22 mr-2">
                    <h1>Total Price</h1>
                    ${response.total}$
                </section>
                <div>
                    <button type="button" class="btn btn-success w-20" onclick="postPayment(${response.order})">pay</button>
                    <button type="button" class="btn btn-warning w-20">cancel</button>
                </div>
            </div>
            `
    })
}

function postPayment(orderID) {
    let form = new FormData();
    form.append('order_id', orderID);
    const csrfTokens = getCookie('csrftoken');
    const data = fetchWithAuth('http://localhost:8000/payment/api/pay', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: form,
    })
    data.then(response => {
        console.log(response.status)
        if (response.status === 200) {
            Swal.fire({
                title: 'Success!',
                text: 'Payment posted successfully.',
                icon: 'success',
                confirmButtonText: 'OK'
            });
        } else if (response.status === 400) {
            Swal.fire({
                title: 'Error!',
                text: 'Failed to post payment. Please check the details and try again.',
                icon: 'error',
                confirmButtonText: 'Retry'
            });
        }
    })
        .catch(error => {

            Swal.fire({
                title: 'Error!',
                text: 'An unexpected error occurred. Please try again later.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        });
    let itemAdvertiseEl = document.querySelector("#itemAdvertise").innerHTML=``
    let advertiseEl = document.querySelector('#advertise').innerHTML=``
    let button_viewEL = document.querySelector('#button_view').innerHTML=``
}