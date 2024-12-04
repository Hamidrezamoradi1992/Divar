function sendMassageAdmin(to_user, discussion_forum) {
    let massageFormEl = document.querySelector('#massageForm')
    let data = new FormData(massageFormEl)
    data.append('to_user', to_user)
    data.append('discussion_forum', discussion_forum)
    const csrfTokens = getCookie('csrftoken')
    const send = fetchWithAuth(`http://localhost:8000/comment/api/replay`, {
        method: 'POST',
        body: data,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    })

    send.then(data=>{
        getAllComments(discussion_forum)
    })
}