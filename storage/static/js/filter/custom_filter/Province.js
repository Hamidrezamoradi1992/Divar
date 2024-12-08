// function getProvince() {
//     let ProvinceEL = document.querySelector('#getProvince')
//     ProvinceEL.innerHTML = ""
//
//     fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/state`, {
//         method: 'GET'
//     }).then(response => {
//         const category = response.json()
//         category.then(data => {
//             ProvinceEL.innerHTML = `<option value="None">Province</option>`
//             let el = ``
//             data.forEach(cat => {
//                 el += `<option  onclick="getCity(${cat.id})" value="${cat.id}">${cat.title}</option>`
//
//             })
//             ProvinceEL.innerHTML += el
//         })
//
//     }).catch()
//
//
// }

function getProvince() {
    let ProvinceEL = document.querySelector('#getProvince');
    ProvinceEL.innerHTML = ""; // حذف محتوای قبلی

    fetch(`http://localhost:${domainPort}/advertising/api/add/advertise/state`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        // افزودن گزینه پیش‌فرض
        ProvinceEL.innerHTML = `<option value="None">Province</option>`;
        let el = ``;
        data.forEach(cat => {
            el += `<option value="${cat.id}">${cat.title}</option>`;
        });
        ProvinceEL.innerHTML += el;

        // افزودن رویداد onchange برای انتخاب استان
        ProvinceEL.onchange = function () {
            const selectedProvinceId = this.value;
            if (selectedProvinceId !== "None") {
                getCity(selectedProvinceId); // صدا زدن تابع getCity با آی‌دی استان
            }
        };
    })
    .catch(error => {
        console.error("Error fetching provinces:", error);
    });
}