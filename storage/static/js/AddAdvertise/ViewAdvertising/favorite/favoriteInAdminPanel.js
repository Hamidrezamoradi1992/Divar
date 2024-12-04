function viewFavoriteAdmin() {
    cntextCommentsEL.innerHTML=``
    contexAdminPanelEL.innerHTML = ''
    contexAdminPanelEL.innerHTML = `
        <div id="Favorite" class="m-auto">
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
                        <th>Name</th>
                        <th>Job</th>
                        <th>Favorite Color</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody id="itemFavorite">
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
                        <th>description</th>
                        <th></th>
                        <th></th>
                    </tr>
                    </tfoot>
                </table>
            </div>
        </divid>`
    getFavorite()
}

function getFavorite() {
    let itemMassageEl = document.querySelector('#itemFavorite')
    const datas = fetchWithAuth(`http://localhost:8000/advertising/api/adminpanel/favorite/advertising`, {
        method: 'GET'
    })
    datas.then(response => {
        console.log(response)
        response.forEach(advertisingPublisher => {
            const date = new Date(advertisingPublisher.expires_at);
            const formattedDate = date.toLocaleDateString();
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const result = `${formattedDate} ${hours}:${minutes}`;
            itemMassageEl.innerHTML += `
                      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="skeleton mask mask-squircle h-12 w-12">
              <a href="http://localhost:8000/advertising/view/add/advertise/${advertisingPublisher.id}">
                <img
                  src="${advertisingPublisher.image.file}"
                  alt="${advertisingPublisher.image.alt}" />
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
          <br />
          <span class="badge badge-ghost badge-sm">active: ${advertisingPublisher.is_active}</span>
        </td>
        <td>${result}</td>
        <th>
          <button type="submit" class="btn btn-ghost btn-xs" onclick="favoriteRemove(${advertisingPublisher.id})">details</button>
        </th>
      </tr>
`
        })
    })

}
function favoriteRemove(advertising_id) {
    Swal.fire({
        icon: 'question',
        title: 'Are you sure?',
        text: 'Do you want to remove this advertisement from your favorites?',
        showCancelButton: true,
        confirmButtonText: 'Yes, remove it!',
        cancelButtonText: 'No, cancel',
    }).then((result) => {
        if (result.isConfirmed) {
                favoriteAddAndRemove(advertising_id);


            Swal.fire({
                icon: 'info',
                title: 'Processing...',
                text: 'Please wait a moment...',
                timer: 500,
                showConfirmButton: false,
            });

        } else {

            Swal.fire({
                icon: 'info',
                title: 'Action Canceled',
                text: 'The advertisement was not removed from your favorites.',
            });
        }
    });
    setTimeout(30)
    viewFavoriteAdmin();
}
