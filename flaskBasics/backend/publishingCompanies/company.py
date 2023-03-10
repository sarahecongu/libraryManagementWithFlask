from backend.db import db;

class PublishingCompany(db.Model):
    __tablename__ = "publishing_companies"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    user_id =db.Column(db.Integer,db.ForeignKey('users.id'))
    


#function call
def __init__(self,id,name,contact,address):
    self.id = id
    self.name=name
    self.contact = contact
    self.address = address


    


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