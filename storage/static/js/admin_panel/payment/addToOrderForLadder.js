function addToOrderForLadder(advertising) {
    let form = new FormData()
    const csrfTokens = getCookie('csrftoken')
    form.append('advertising', advertising)
    const data = fetchWithAuth(``, {
        method: 'POST',
        body: form,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    })

}