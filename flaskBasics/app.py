from backend import create_app,db
from flask_migrate import Migrate
from backend.users.model import User
from backend.books.books import Book 
from backend.publishingCompanies.company import PublishingCompany





app = create_app('development')
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Book=Book,company=PublishingCompany)