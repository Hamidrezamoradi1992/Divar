function setImage(advertising) {
    formView.innerHTML = ""
    categoryKey.innerHTML = `
                <button class="btn btn-outline btn-error mx-3" onclick="getCategory()">back</button>
                <button class="btn btn-active btn-neutral" onclick="addFieldImageInput()">add image field</button>
            `;
    formView.innerHTML = `
        <form action="" id="form_input_images" class="flex flex-col gap-4">
            <div id="images">
            <input type="file" name="image" class="file-input file-input-bordered file-input-info w-full max-w-xs m-5" />
          </div>
          <button class="btn btn-ghost" type="button" onclick="send_image()">accept</button>
          </form>
    `
}

let imageInputCount = 0

function addFieldImageInput() {
    let images = document.querySelector("#images")
    if (imageInputCount < 5) {
        imageInputCount++;
        console.log(formView.length);
        images.innerHTML += `  
            <input type="file" name="image" class="file-input file-input-bordered file-input-info w-full max-w-xs m-5"  />  
        `;
    } else {
        swal({
            title: "خطا!",
            text: "حداکثر 6 فیلد ورودی تصویر مجاز است.",
            icon: "warning",
            button: "باشه",
        });
    }
}


function send_image() {
    const csrfTokens = getCookie('csrftoken')
    const formImages = document.querySelector("#form_input_images")
    data = new FormData(formImages)
    data.append('advertising', parseInt(advertiseId))
    const advertise_iamge_send = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/image/`, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: data,

    })

    advertise_iamge_send.then(response => {

        swal({
            title: "Accepted",
            text: response.massage,
            icon: "accepted",
            button: "accept",
        });
        getFieldAdvertising()


    }).catch(error => {
        console.error('Error:', error);
        swal({
            title: "Error!",
            text: "error",
            icon: "warning",
            button: "accept",
        });
    });
}
