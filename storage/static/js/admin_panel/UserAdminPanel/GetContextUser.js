function get_user(user_id) {

    const data = fetchWithAuth(`http://localhost:${domainPort}/accounts/api/user/${user_id}`, {
        method: 'GET',
    })

    data.then(response => {
            console.log(response)
            console.log(`${response.image_Official_photo && response.image_Official_photo.length > 0 ? response.image_Official_photo.url : " "}`)
            formContextEl.innerHTML = `
                <div class=" avatar my-5">
                   <div class="skeleton mask mask-hexagon w-52">
                       <img src="${response.image_Official_photo}"
                                        alt="imageUser"  class="max-w-[95vw] max-h-[95vh] "/>
                    </div>
                 </div>
                    
                </div>

                   
                  
          
            <div>
                <h1 class="font-sans  italic capitalize m-auto ">first name : ${response.first_name}</h1>
                <h1 class="font-sans  italic capitalize m-auto ">last name : ${response.last_name}</h1>
                <h1 class="font-sans  italic capitalize m-auto ">age : ${response.age}</h1>
                <h1 class="font-sans  italic capitalize m-auto ">email : ${response.email}</h1>
                <h1 class="font-sans  italic capitalize m-auto ">gender : ${response.gender}</h1>
                <h1 class="font-sans italic capitalize m-auto ">phone : ${response.phone}</h1>
                <h1 class="font-sans  capitalize m-auto ">address : ${response.address}</h1>
                
            </div>
            <div>
                <h1 class="font-sans  italic capitalize m-auto ">kyc :  ${response.is_kyc} </h1>
                <h1 class="font-sans  italic capitalize m-auto flex justift-center gap-2 ">is active :${response.is_active}  </h1>
              
                
            </div>
            <div>
                <div class=" avatar my-5">
                    <div class="skeleton mask mask-hexagon w-44">
                        <img src="${response.image_idcard}" alt="idcard" class="max-w-[95vw] max-h-[95vh] "/>
                    </div>
                </div>
                <div class=" avatar my-5">
                    <div class="skeleton mask mask-hexagon w-44">
                        <img src="${response.image_letter_of_commitment}" alt="letter of commitment" class="max-w-[95vw] max-h-[95vh] "/>
                    </div>
                </div>

            </div>
            `
        }
    )


}