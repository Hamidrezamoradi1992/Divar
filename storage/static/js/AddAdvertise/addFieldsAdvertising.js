let fieldsEl = ""

function getFieldAdvertising() {
    categoryKey.innerHTML = `
                <button class="btn btn-outline btn-error mx-3" onclick="getCategory()">exit</button>`;
    formView.innerHTML = ''
    formView.innerHTML = `
         <form action="" id="form_input_fields" class="flex flex-col items-center justify-center m-8"></form>`;
    fieldsEl = ''
    const advertise_get_field = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/field/${categoryId}`, {
        method: 'GET',
    })

    advertise_get_field.then(fields => {
            fields.forEach(field => {
                console.log(field)
                switch (field.type_field) {
                    case 'str':
                        fieldsEl += `
                                    <input type="text" 
                                    name="${field.title}" 
                                    placeholder="${field.title}"
                                    class="file-input file-input-bordered file-input-info w-full max-w-xs m-5"  /> `
                        break;
                    case 'int':
                        fieldsEl += `
                                    <input type="number" 
                                    name="${field.title}" 
                                    placeholder="${field.title}" 
                                    class="file-input file-input-bordered file-input-info w-full max-w-xs m-5"  /> `
                        break;
                    case 'float':
                        fieldsEl += `
                                    <input type="number" 
                                    name="${field.title}" 
                                    placeholder="${field.title}" 
                                    class="file-input file-input-bordered file-input-info w-full max-w-xs m-5"  /> `
                        break;
                    case 'bool':
                        fieldsEl += `
                                    <input type="checkbox" 
                                    name="${field.title}" 
                                    placeholder="${field.title}" 
                                    class="file-input file-input-bordered file-input-info w-full max-w-xs m-5"  /> `
                        break;

                }

            })
            let formField = document.querySelector('#form_input_fields')
            formField.innerHTML = ''
            formField.innerHTML += fieldsEl
            formField.innerHTML += `<button 
                                    class="btn btn-ghost" 
                                    type="button" 
                                    onclick="send_fields()">accept</button>`

        }
    )
}

function send_fields() {
    let formFieldSend = document.querySelector('#form_input_fields')
    data = new FormData(formFieldSend)
    data.append('category', parseInt(categoryId))
    data.append('advertising', parseInt(advertiseId))

    const FieldSend = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/add/field/`, {
        method: 'POST',
        body: data
    })
    FieldSend.then(response => {

        swal({
            title: "Accepted",
            text: response.massage,
            icon: "accepted",
            button: "accept",
        });
        location.replace(`http://localhost:${domainPort}//accounts/adminuser`)


    }).catch(error => {
        console.error('Error:', error);
        swal({
            title: "Error!",
            text: "error",
            icon: "warning",
            button: "accept",
        });
    })
}

