#end point file
#registsering a user
from flask import jsonify,request,Blueprint
#from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend .users.model import User,db

users = Blueprint('users',__name__,url_prefix='/users')

#get all users
@users.route('/')
def all_users():
    users = User.query.all()
    results = [
        {
            "name":k.name,
            "email":k.email,
            "contact":k.contact
        } for k in users
    ]

    return {"count":len(results),"users":results}

#creating a user
@users.route("/create",methods =['POST','GET'])
def create_user():
    user_name = request.json['name']
    email = request.json['email']
    contact = request.json['contact']
    address = request.json['address']
    password = request.json['password']
    usertype = 'author'
    hashed_password = generate_password_hash(password)

#Validation
    if not user_name:
        return jsonify({'message':'Username is required'}),400
    
    if not email:
        return jsonify({'message':'Email is required'}),400
    
    if not address:
        return jsonify({'message':'Address is required'}),400
    
    if not contact:
        return jsonify({'message':'contact is required'}),400
    
    if not password:
        return jsonify({'message':'password is required'}),400

    if len(password) <7:
        return jsonify({'message':'password must be greater than 7 characters'})
    
    #query 1st parameter is column constraits
    if User.query.filter_by(contact = contact).first():
        pass

    existing_contact = User.query.filter_by(contact = contact).first(),409
    if existing_contact:
        return jsonify({'message':'Already existing'})
    
    # constraits for email
    existing_email = User.query.filter_by(email = email).first(),409
    if existing_email:
        return jsonify({'message':'Already existing'})
#storing a new user
    new_user = User(user_name=user_name,contact = contact,email = email,address=address,password=hashed_password,usertype=usertype)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success':True,'message':'you have successfully registered','data':new_user}),201