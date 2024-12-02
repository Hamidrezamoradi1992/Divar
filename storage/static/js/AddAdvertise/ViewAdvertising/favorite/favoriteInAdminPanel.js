function viewFavoriteAdmin() {
    contexAdminPanelEL.innerHTML = ''
    contexAdminPanelEL.innerHTML =`
        <div id="Favorite" class="m-auto !hidden">
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
}       getFavorite()

function getFavorite(){
    let itemMassageEl=document.querySelector('#itemMassage')
    const datas=fetchWithAuth(``,{
        method:'GET'
    })
}