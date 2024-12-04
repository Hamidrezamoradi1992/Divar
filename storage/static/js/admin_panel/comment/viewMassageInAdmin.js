function viewMassageAdmin() {
    const datas = fetchWithAuth(`http://localhost:8000/comment/api/discussionforum`, {
        method: 'GET'
    })
    datas.then(data => {
        console.log(data)
        contexAdminPanelEL.innerHTML = ''
        data.comments.forEach(datas => {

            contexAdminPanelEL.innerHTML +=
                `
                <div class="indicator" onclick="">
                        <button type="button" onclick="getAllComments(${datas[2]})">
                            <span class="indicator-item badge badge-primary"></span>
                            <div class="bg-base-300 grid h-32 w-32 place-items-center">${datas[1]}</div>
                        </button>
                </div>
               
                `
        })
    })
}

function getAllComments(discussionForum) {
    let form = new FormData()
    form.append('discussion', discussionForum)
    console.log(form)
    const datas = fetchWithAuth(`http://localhost:8000/comment/api/list`, {
        method: 'POST',
        body: form
    })
    let to_user1 = 0
    let to_user2 = 0
    let to_users = 0
    let cntextCommentsEl = document.querySelector('#cntextComments')
    datas.then(data => {
        let el = ''
        data.forEach(comments => {

            if (userId === comments.user.id) {
                to_user1=comments.to_user
                el += `
                    <div class="chat chat-end">
                        <div class="chat-image avatar">
                            <div class="w-10 rounded-full skeleton">
                                <img
                                    alt="image_user"
                                    src="${comments.user.image_Official_photo}"/>
                            </div>
                        </div>
                        <div class="chat-bubble">${comments.massage}</div>
                    </div>
                    `

            } else {
                    to_user2=comments.to_user
                el += `
                    <div class="chat chat-start">
                        <div class="chat-image avatar">
                            <div class="w-10 rounded-full skeleton">
                                <img
                                    alt="image_user"
                                    src="${comments.user.image_Official_photo}"/>
                            </div>
                        </div>
                        <div class="chat-bubble">${comments.massage}</div>
                    </div>
                    `

            }


        })
        if (to_user1 !== 0) {
            to_users = to_user1
        } else {
            to_users = to_user2
        }

        el += `<form action="" id="massageForm" class="m-auto mt-3">
            <input type="text" name="massage" placeholder="Type here" class="input input-bordered w-full max-w-xs"/>
            <button type='button' onclick="sendMassageAdmin(${to_users},${discussionForum})" class="btn">send</button>
        </form>`

        cntextCommentsEl.innerHTML = ''
        cntextCommentsEl.innerHTML = el
        cntextCommentsEl.classList.remove('!hidden')

    })


}

// <div className="chat chat-start">
//     <div className="chat-bubble">
//         It's over Anakin,
//         <br/>
//         I have the high ground.
//     </div>
// </div>
// <div className="chat chat-end">
//     <div className="chat-bubble">You underestimate my power!</div>
// </div>
