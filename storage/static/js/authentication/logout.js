function logout_user() {

    const logout_userss = fetchWithAuth('http://localhost:8000/accounts/api/logout', {method: 'GET'})
    logout_userss.then(re => {
        document.cookie = 'access' + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
        document.cookie = 'refresh' + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
        location.replace('/')
    }).catch(er=>{
        console.log(er)
    })


}