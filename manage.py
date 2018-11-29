# encoding: utf-8
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from run import app
from exts import db
from models import User

manager = Manager(app)

#bound  app and db from Migrate
migrate = Migrate(app,db)

#add migration script cmd in manager
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()