from backend.db import db;



class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    isbn = db.Column(db.String(100))
    price = db.Column(db.String(100))
    description = db.Column(db.String(100))
    copies = db.Column(db.String(100),unique=True)
    publishing_company_id =db.Column(db.Integer,db.ForeignKey('publishing_companies.id'))
    user_id =db.Column(db.Integer,db.ForeignKey('users.id'))

    


#function call
def __init__(self,id,name,price,copies,description,isbn):
    self.id = id
    self.name=name
    self.price = price
    self.copies = copies
    self.description=description
    self.isbn=isbn


def __repr__(self):
    return f"<Book{self.name}>"


#save a new instance
def save(self):
    db.session.add(self)
    db.session.commit()

# delete the item
def delete(self):
    db.session.delete(self)
    db.session.commit()