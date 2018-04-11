# -*- encoding=UTF-8 -*-


from updateinfo import app, db
from flask_script import Manager
from updateinfo.models import Info

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()