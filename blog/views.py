from flask import Blueprint, render_template

blog_bp=Blueprint('blog_bp',__name__,url_prefix='/blog')
blog_bp.template_folder='./templates'
blog_bp.static_folder='./static'

@blog_bp.route('/')
def hello_blog():
    return 'hello blog'
@blog_bp.route('/to_my_blog/')
def to_my_blog():
    return render_template('my_blog.html')