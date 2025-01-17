function addToOrderForLadder(advertising) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('advertise', advertising)
    const data = fetchWithAuth(`http://localhost:8000/payment/api/ladder/payment`, {
        method: 'POST',
        body: form,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    })

    data.then(response => {

        Swal.fire({
            icon: 'success',
            title: 'Success',
            text: response.message,
            confirmButtonText: 'OK'
        });
    })
        .catch(error => {

            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: error.message,
                confirmButtonText: 'OK'
            });
        });
}