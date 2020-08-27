from flask import Blueprint, render_template, request, session

from blog.blog_logic.blog_cls import BlogCls
from user.user_logic.account_cls import AccountCls
from blog.models import db, Blog

blog_bp = Blueprint('blog_bp', __name__, url_prefix='/blog')
blog_bp.template_folder = './templates'
blog_bp.static_folder = './static'


@blog_bp.route('/')
def hello_blog():
    return 'hello blog'


@blog_bp.route('/to_my_blog/')
def to_my_blog():
    # # 找到登录用户
    account_name = session.get('account_name')
    account = AccountCls(account_name).check_account_name()
    blogs = account.blog
    print(type(blogs))

    return render_template('my_blog.html',blogs=blogs)


@blog_bp.route('/pub_comment/', methods=['post', 'get'])
def pub_comment():
    # 获取微博内容
    sentence = request.form.get('sentence')

    # 找到登录用户
    account_name = session.get('account_name')
    account = AccountCls(account_name).check_account_name()

    # 通过登录用户添加微博实例
    blog = BlogCls(account=account, sentence=sentence).add_blog()
    # 向数据库里提交
    db.session.add(blog)
    db.session.commit()
    return "添加成功"
