from app import db;



class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    contact = db.Column(db.String(100),unique = True)
    email = db.Column(db.String(100),unique = True)
    address = db.Column(db.String(100))
    usertype = db.Column(db.String(100))
    password = db.Column(db.String(100),unique=True)
    books=db.relationship('Book', backref ="users")
    publishingCompanies = db.relationship('PublishingCompany',backref='users')


#function call
def __init__(self,id,name,contact,address,usertype,password):
    self.id = id
    self.name=name
    self.contact = contact
    self.address = address
    self.usertype=usertype
    self.password=password

#creating new user













def __repr__(self):
    return f"<user{self.email}>"


#save a new instance
def save(self):
    db.session.add(self)
    db.session.commit()

# delete the item
def delete(self):
    db.session.delete(self)
    db.session.commit()