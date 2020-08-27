$(function () {
    $('input[type="submit"]').click(function () {
        account_name = $('input[name="account_name"]').val()
        password = $('input[name="password"]').val()
        password2 = $('input[name="password2"]').val()
        // console.log(account_name,password)
        if (account_name === "" || password === "") {
            alert('必填项不能为空')
        } else if (password !== password2) {
            alert('两次输入的密码不一致')
        } else {
            $.post(
                '/user/exe_reg/',
                {
                    'account_name': account_name,
                    'password': password,
                },
                function (data) {

                    alert(data['msg'])
                    if (data['status'] === '200') {
                        window.location.href = '/user/to_login/'
                    }
                }
            )
        }
    })
})