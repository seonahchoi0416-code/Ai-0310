console.log("javascript -- running")
$(()=>{ //ready 이벤트 작동
    //console.log($("h1"))

   $("li").on("mouseover",function(){
        const img_path="/static/images/"
        const img_style=`style="width:50vw;max-height:67vh"`
        const img_tag=`<img  ${img_style} src="${img_path}${$(this).attr("im")}">`
        console.log(img_tag)
        $("#main_img").html(img_tag)
    })
    $("li").on("click",function(){
       $("#send_service").attr("info",this.id)
      $("#content_container").css("display","block")
    })
    $("#send_service").on("click",async function(){
        const form_data = new FormData();
        form_data.append("user_img",$("#file_input").get(0).files[0])
        const pending =await fetch(`/option/${$(this).attr("info")}`,{
            method:"post",
            body:form_data
        })
        const result = await pending.json()
        console.log(result)
        $("#result").append(`
            <div style="text=align:center;width:12rem;float:left">
            <img style="width:11em;height:11em" src="data:image/png;base64,${result.timg}"/>
            <p style="matgin:1rem">${result.yrat}확률로 ${result.yred}로 예측</p>
            </div>
        `)
    })

})
 $("#close").on("click",()=>{$("#content_container").css("display","none")})