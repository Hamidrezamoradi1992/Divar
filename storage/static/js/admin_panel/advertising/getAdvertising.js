function getAdvertising() {
    cntextCommentsEL.innerHTML=``
    contexAdminPanelEL.innerHTML=''
    contexAdminPanelEL.innerHTML = `
        <div class="max-w-[100vw] m-auto my-12">
            <div role="tablist" class="tabs tabs-lifted tabs-lg max-w-[40vw] m-auto">
                <button class="w-auto tab btn btn-ghost" onclick="getPublishedAdvertising()">Published</button>
                <button class=" tab btn " onclick="getReadyToPayment()">Ready for payment</button>
                <button class=" w-auto tab btn btn-ghost" onclick="getExpAdvertising()">All Advertising</button>
            </div>

        </div>
        <div id="advertise" class="m-auto !hidden">
            <div class="overflow-x-auto">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <th>advertise</th>
        <th>description</th>
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
        <th>description</th>
        <th></th>
        <th></th>
      </tr>
    </tfoot>
  </table>
</div>
        </divid>
`
}

function getPublishedAdvertising() {
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/adminpanel/advertising`, {
        method: 'GET',

    })

    let advertiseEl = document.querySelector('#advertise')
    advertiseEl.classList.remove('!hidden')
    let advertiseItemEl = document.querySelector('#itemAdvertise')
    advertiseItemEl.innerHTML=""
    data.then(response => {
        console.log(response)
        response.forEach(advertisingPublisher => {
            const date = new Date(advertisingPublisher.expires_at);
            const formattedDate = date.toLocaleDateString();
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const result = `${formattedDate} ${hours}:${minutes}`;
            advertiseItemEl.innerHTML += `
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
          <button type="submit" class="btn btn-ghost btn-xs" onclick="">deactive</button>
          <button type="submit" class="btn btn-ghost btn-xs" onclick="addToOrderForLadder(${advertisingPublisher.id})">ladder</button>
        </th>
      </tr>
`
        })
    })
}


function getExpAdvertising(){

     const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/adminpanel/all/advertising`, {
        method: 'GET',

    })

    let advertiseEl = document.querySelector('#advertise')
    advertiseEl.classList.remove('!hidden')
    let advertiseItemEl = document.querySelector('#itemAdvertise')
    advertiseItemEl.innerHTML=""
    data.then(response => {
        console.log(response)
        response.forEach(advertisingPublisher => {
            const date = new Date(advertisingPublisher.expires_at);
            const formattedDate = date.toLocaleDateString();
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const result = `${formattedDate} ${hours}:${minutes}`;
            advertiseItemEl.innerHTML += `
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
          <button class="btn btn-ghost btn-xs">details</button>
        </th>
      </tr>
`
        })
    })

}