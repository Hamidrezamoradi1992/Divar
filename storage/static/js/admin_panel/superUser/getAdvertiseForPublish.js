function getAdvertisingAccepted() {
    cntextCommentsEL.innerHTML = ``
    contexAdminPanelEL.innerHTML = ''
    contexAdminPanelEL.innerHTML =
        `
        <div id="advertise" class="m-auto">
            <div class="overflow-x-auto">
                <table class="table">
                    <!-- head -->
                    <thead>
                    <tr>
                        <th>
                            <label>
                                <input type="checkbox" class="checkbox"/>
                            </label>
                        </th>
                        <th>advertise</th>
                        <th>category</th>
                        <th></th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody id="itemAdvertise">
                    <!-- row 1 -->

                    <!-- row 2 -->

                    <!-- row 3 -->

                    <!-- row 4 -->

                    </tbody>
                    <!-- foot -->
                    <tfoot>
                    <tr>
                        <th></th>
                        <th>advertise</th>
                        <th>category</th>
                        <th></th>
                        <th></th>
                    </tr>
                    </tfoot>
                </table>
            </div>
        </divid>
        `
    getAdvertiseForPublish()
}

function getAdvertiseForPublish() {
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/accepted/`, {
        method: 'GET',

    })
    let advertiseItemEl = document.querySelector('#itemAdvertise')
    advertiseItemEl.innerHTML = ""
    data.then(response => {
        console.log(response)
        response.forEach(advertisingPublisher => {
            advertiseItemEl.innerHTML += `
                <tr class="min-h-[150px]">
                    <th>
                        <label>
                            <input type="checkbox" class="checkbox"/>
                        </label>
                    </th>
                    <td>
                        <div class="flex items-center gap-3">
                            <div class="avatar">
                                <div class="skeleton mask mask-squircle h-12 w-12">
                                    <a href="http://localhost:8000/advertising/view/add/advertise/test/${advertisingPublisher.id}">
                                        <img
                                            src="${advertisingPublisher.image.file}"
                                            alt="${advertisingPublisher.image.alt}"/>
                                    </a>
                                </div>
                            </div>
                            <div>
                                <div class="font-bold">${advertisingPublisher.title}</div>
                                              <div class="text-sm opacity-50">state : ${advertisingPublisher.state.title}</div>
                                              <div class="text-sm opacity-50">city : ${advertisingPublisher.city.title}</div>
                                              <div class="text-sm opacity-50">price : ${advertisingPublisher.price}</div>
                          
                            </div>
                        </div>
                    </td>
                    <td>
                        ${advertisingPublisher.category.title}
                        <br/>
                        <span class="badge badge-ghost badge-sm">free: ${advertisingPublisher.category.free}</span>
                        <br/>
                        <span class="badge badge-ghost badge-sm">price: ${advertisingPublisher.category.price}</span>
                    </td>
                    <td>
                        <span class="badge badge-ghost badge-sm">user email: ${advertisingPublisher.user.email}</span>
                         <br/>
                        <span class="badge badge-ghost badge-sm">user firs name: ${advertisingPublisher.user.first_name}</span>
                        <br/>
                        <span class="badge badge-ghost badge-sm">user address: ${advertisingPublisher.user.address}</span>
</td>
                    <th>
                        <button type="submit" class="btn btn-ghost btn-xs" onclick="removeAdvertiseForPublish(${advertisingPublisher.id},${advertisingPublisher.user.id})">rejected</button>
                        <button type="submit" class="btn btn-ghost btn-xs"
                                onclick="acceptedAdvertiseForPublish(${advertisingPublisher.id},${advertisingPublisher.user.id})">accepted
                        </button>
                    </th>
                </tr>
`
        })
    })
}

function removeAdvertiseForPublish(Advertising, user) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('advertise', Advertising)
    form.append('user', user)
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/accepted/`, {
        method: 'POST',

        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: form,
    })

    getAdvertisingAccepted()
}

function acceptedAdvertiseForPublish(Advertising, user) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('advertise', Advertising)
    form.append('user', user)
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/accepted/`, {
        method: 'PUT',

        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: form,
    })
    getAdvertisingAccepted()
}