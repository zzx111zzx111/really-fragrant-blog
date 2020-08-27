from flask import Blueprint, render_template, request, g, redirect, url_for, make_response, session

from user.user_logic.account_operation import AccountCls
from user.user_logic.password_encrypt import sha512_encrypt

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')
user_bp.template_folder = './templates'
user_bp.static_folder = './static'


@user_bp.route('/')
def hello_user():
    return 'hello user!'


@user_bp.route('/to_login/')
def to_login():
    return render_template('login.html')


@user_bp.route('/to_reg/')
def to_reg():
    return render_template('register.html')


@user_bp.route('/exe_reg/', methods=['GET', 'POST'])
def exe_reg():
    # 获取前端数据
    account_name = request.form.get('account_name')
    password = request.form.get('password')

    # 密码加密
    encrypt_passwrod = sha512_encrypt(password)
    # 往数据库里添加数据
    try:
        AccountCls(account_name, encrypt_passwrod).account_register()
    except:
        g.status = '000'
        g.msg = '用户名已被占用,请换一个用户名'
    else:
        g.status = '200'
        g.msg = '注册成功'
    data = {
        'status': g.status,
        'msg': g.msg
    }
    return data
@user_bp.route('/exe_login/')
def exe_login():
    print('-----------------------------------------已连接服务器')
    account_name=request.args.get('account_name')
    password=request.args.get('password')
    print(account_name,password)
    #在数据库中查找用户名
    try:
        account=AccountCls(account_name).check_account_name()
    except:
        g.msg='用户名不存在'
        g.status='000'
    else:
    #密码加密
        encrypt_password=sha512_encrypt(password)
    #查询用户名的密码是否输入正确
        if account.password!=encrypt_password:
            g.msg='密码输入错误,请重新输入'
            g.status='000'
        # 如果全部正确则将用户名存储在session中
        else:
            session['account_name']=account_name
            g.status='200'
            g.msg='登陆成功'
    data={
        'status':g.status,
        'msg':g.msg
    }
    return data

@user_bp.route('/detect_session/')
def detect_session():
    account_name=session.get('account_name')
    if account_name==None:
        g.status='000'
    else:
        g.status='200'
    data={
        'status':g.status,
        'msg':account_name
    }
    return data