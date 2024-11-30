function ExitAdvertising(advertise_id) {
    console.log('exit', advertise_id)
    let datas = new FormData()
    const csrfTokens = getCookie('csrftoken')
    datas.append('advertising', advertise_id)
    const data = fetchWithAuth(`http://localhost:${domainPort}/advertising/api/destroy`, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body:datas,

    })

    location.reload()


}