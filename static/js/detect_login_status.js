$(function (){
    $.get(
        '/user/detect_session/',
        function (data){
            if(data['status']==='000'){
                fill_show="登录/注册"
            }else{
                fill_show=data['msg']
            }
            $('.top').find('a').html(fill_show)
        }
    )
})