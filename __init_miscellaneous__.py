from flask import Flask
from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager

from blog.views import blog_bp
from user.views import user_bp
import pymysql


def create_app():
    # # 创建app
    app = Flask(__name__)
    return app


def create_manager(app):
    # 调试模式
    manager = Manager(app)
    return manager


def reg_bp(app):
    # 注册蓝图
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)


def db_config(app):
    # 连接数据库
    pymysql.install_as_MySQLdb()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zzx111:zzx111@localhost:3306/fragrant_blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True


def init_db(db, app):
    # 初始化sqlalchemy第二步
    db.init_app(app)


def create_migrate(manager, app, db):
    # 创建迁移对象
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)


def set_secret_key(app):
    app.config['SECRET_KEY'] = 'dsjfksdfjkdsjfklsdjf'
