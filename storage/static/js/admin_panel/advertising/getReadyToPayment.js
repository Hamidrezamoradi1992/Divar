function getReadyToPayment() {
    let itemAdvertiseEl = document.querySelector("#itemAdvertise")
    let advertiseEl = document.querySelector('#advertise')
    advertiseEl.classList.remove('!hidden')
    itemAdvertiseEl.innerHTML = ''
    const get_data = fetchWithAuth(`http://localhost:8000/advertising/api/adminpanel/forpayment/advertising`, {
        method: 'GET'
    })
    get_data.then(response => {
        console.log(response)
        response.forEach(advertisingPublisher => {
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
    })
}