function favoriteAddAndRemove(id_advertising) {
    let csrfTokens = getCookie('csrftoken')
    let data=new FormData()
    data.append('user',userId)
    data.append('advertising',id_advertising)
    const sendFavorite = fetchWithAuth(`http://localhost:${domainPort}/favorite/add/favorite`, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
        body: data,

    })

}