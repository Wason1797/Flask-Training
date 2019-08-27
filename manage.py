from app.main import create_app
from app.settings import Config
from app.main.plugins import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import unittest

from app.main.models import Order, OrderDetail, Ingredient, Size

flask_app = create_app(Config)


flask_app.app_context().push()

manager = Manager(flask_app)

migrate = Migrate(flask_app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    flask_app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
