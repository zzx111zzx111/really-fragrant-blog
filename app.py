from flask import render_template

from user.models import db
from __init__ import create_app, create_manager, reg_bp, db_config, create_migrate, init_db, set_secret_key

app = create_app()
manager = create_manager(app)
reg_bp(app)
db_config(app)
init_db(db, app)
create_migrate(manager, app, db)
set_secret_key(app)

# hello world 视图函数
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
