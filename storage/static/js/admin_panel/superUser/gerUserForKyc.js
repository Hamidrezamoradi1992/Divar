function getUser() {
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
                        <th>User</th>
                        <th>Image</th>
                        <th>Image</th>
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
                        <th>Image</th>
                        <th>Image</th>
                        <th></th>
                    </tr>
                    </tfoot>
                </table>
            </div>
        </divid>
        `
    getUserForKyc()
}

function getUserForKyc() {
    const data = fetchWithAuth(`http://localhost:${domainPort}/accounts/api/get/image/user`, {
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
                                    <a href="http://localhost:8000/+++++++++++++++++++++++++++++++++${advertisingPublisher.id}">
                                        <img
                                            src="${advertisingPublisher.image_Official_photo}"
                                            alt="image_Official_photo"/>
                                    </a>
                                </div>
                            </div>
                            <div>
                                <div class="font-bold">${advertisingPublisher.email}</div>
                                              <div class="text-sm opacity-50">user firs name: : ${advertisingPublisher.first_name}</div>
                                              <div class="text-sm opacity-50">user firs name: : ${advertisingPublisher.last_name}</div>
                                              <div class="text-sm opacity-50">price : ${advertisingPublisher.price}</div>
                          
                            </div>
                        </div>
                    </td>
                    <td>
                       <div class="avatar" >
                       <div class="skeleton mask mask-squircle h-60 w-60">
                                        <img
                                            src="${advertisingPublisher.image_letter_of_commitment}"
                                            alt="image letter of commitment"/>
                                </div>
                            </div>
                    </td>
                    <td>
                        
                       <div class="avatar ">
                                <div class="skeleton mask mask-squircle h-60 w-60">
                                    
                                        <img
                                            src="${advertisingPublisher.image_idcard}"
                                            alt="image idcard"/>
                                    
                                </div>
                            </div>
</td>
                    <th>
                        <button type="submit" class="btn btn-ghost btn-xs" onclick="removeImageForKyc(${advertisingPublisher.id})">rejected</button>
                        <button type="submit" class="btn btn-ghost btn-xs"
                                onclick="acceptedImageForKyc(${advertisingPublisher.id})">accepted
                        </button>
                    </th>
                </tr>
`
        })
    })
}

function removeImageForKyc( user) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('user', user)
    const data = fetchWithAuth(`http://localhost:${domainPort}/accounts/api/get/image/user`, {
        method: 'POST',

        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: form,
    })

    getUser()
}

function acceptedImageForKyc(user) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('user', user)
    const data = fetchWithAuth(`http://localhost:${domainPort}/accounts/api/get/image/user`, {
        method: 'PUT',

        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: form,
    })
    getUser()
}