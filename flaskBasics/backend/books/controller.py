#end point file
#registsering a book
from flask import jsonify,request,Blueprint,db
from backend.books.books import Book

books = Blueprint('books',__name__,url_prefix='/books')

#get all books
@books.route('/')
def all_books():
    books = Book.query.all()
    results = [
        {
            "name" :y.name,
            "isbn" :y.isbn ,
            "price" : y.price,
             "description" :y.description,
             "copies" :y.copies
        } for y in books
    ]

    return {"count":len(results),"Books":results}

#creating a user
@books.route("/create",methods =['POST','GET'])
def create_user():
    name = request.json['name']
    isbn = request.json['isbn']
    price = request.json['price']
    description = request.json['description']
    copies = request.json['copies']
    

#Validation
    if not name:
        return jsonify({'message':'name is required'}),400
    
    if not isbn:
        return jsonify({'message':'isbn is required'}),400
    
    if not price:
        return jsonify({'message':'Price is required'}),400
    
    if not description:
        return jsonify({'message':'Description is required'}),400
    
    if not copies:
        return jsonify({'message':'specific copy is required is required'}),400

        
    #query 1st parameter is column constraits
    if Book.query.filter_by(name = name).first():
        pass

    existing_name = Book.query.filter_by(name = name).first(),409
    if existing_name:
        return jsonify({'message':'Already existing'})
    
    # constraits for isbn
    existing_isbn = Book.query.filter_by(isbn = isbn).first(),409
    if existing_isbn:
        return jsonify({'message':'Already existing'})
#storing a new book
    new_book = Book(name=name,isbn = isbn,price = price,description=description,copies=copies)
    db.session(new_book)
    db.session.commit()
    return jsonify({'success':True,'message':'you have successfully registered','data':new_book}),201