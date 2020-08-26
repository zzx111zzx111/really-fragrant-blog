$(function (){
    $('input[type="submit"]').click(function (){
        account_name=$('input[name="account_name"]').val()
        password=$('input[name="password"]').val()
        $.get(
            '/user/exe_login/',
            {
                'account_name':account_name,
                'password':password,
            },
            function (data){
                alert(data["msg"])
                window.location.href='/'
            }
        )
    })
})