function FormUserProfile() {
    cntextCommentsEL.innerHTML=``
    contexAdminPanelEL.innerHTML = ''
    contexAdminPanelEL.innerHTML = `<form action="" id="formUpdateUserProfile" class="gap-3 mx-40">
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">First name</span>

            </div>
            <input type="text" name="first_name" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Last name</span>

            </div>
            <input type="text" name="last_name" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Phone</span>

            </div>
            <input type="number" name="phone" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Age</span>

            </div>
            <input type="number" name="age" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Address</span>

            </div>
            <input type="text" name="address" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>

        </label>


        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">gender</span>

            </div>
            <select class="select select-bordered" name="gender">


                <option value="" selected="">--------</option>


                <option value="FEMALE">female</option>


                <option value="MALE">male</option>


                <option value="OTHER">other</option>


            </select>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Official photo</span>

            </div>
            <input type="file" name="image_Official_photo" class="file-input file-input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">letter of commitment</span>

            </div>
            <input type="file" name="image_letter_of_commitment"
                   class="file-input file-input-bordered w-full max-w-xs"/>

        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">ID Card</span>

            </div>
            <input type="file" name="image_idcard" class="file-input file-input-bordered w-full max-w-xs"/>

        </label>

        <button type="button" onclick="sendUserProfile(${userId})" class="btn btn-ghost">Accepted</button>
    </form>`
}

function sendUserProfile(user_id) {
    const form = document.querySelector('#formUpdateUserProfile')
    const csrfTokens = getCookie('csrftoken')
    let forms = new FormData(form)
    forms.append('id', user_id)
    console.log(user_id)

    const data = fetchWithAuth(`http://localhost:${domainPort}/accounts/api/update/user/${user_id}`, {
        method: 'PUT',

        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: forms,
    })
    data.then(response=>{
        swal({
            title: "Accepted",
            text: response.massage,
            icon: "accepted",
            button: "accept",
        });
        get_user(userId)


    }).catch(error => {
        swal({
            title: "Error!",
            text: "error",
            icon: "warning",
            button: "accept",
        });

    })

}