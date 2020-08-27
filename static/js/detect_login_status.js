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
    // #我的微博点击事件
    $('.to_my_blog').click(function (){
        // #检测top 下的 a的值
        account_name=$('.top').find('a').html()
        if(account_name==='登录/注册'){
            alert('您还未登录,请登录后再查看我的微博')
        }else{
            window.location.href="/blog/to_my_blog/"
        }
    })

})