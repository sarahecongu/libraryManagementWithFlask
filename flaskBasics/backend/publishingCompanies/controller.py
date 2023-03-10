from flask import jsonify,request,Blueprint,db

from backend.publishingCompanies.company import PublishingCompany

publishing_company = Blueprint('publishingCompany',__name__,url_prefix='/publishingCompany')

@publishing_company.route('/')
def get_companies():
    publishing_company = PublishingCompany.query.all()
    results = [
        {
            "name":p.name,
            "address":p.email,
            "contact":p.contact
        } for p in publishing_company
    ]

    return {"count":len(results),"publishing company":results}


#creating a company
@publishing_company.route("/create",methods =['POST','GET'])
def create_company():
    name = request.json['name']
    contact = request.json['contact']
    address = request.json['address']


#Validation
    if not name:
        return jsonify({'message':'Username is required'}),400
     
    if not address:
        return jsonify({'message':'Address is required'}),400
    
    if not contact:
        return jsonify({'message':'contact is required'}),400
    
    if not address:
        return jsonify({'message':'address is required'}),400
    
    #query 1st parameter is column constraits
    if PublishingCompany.query.filter_by(contact = contact).first():
        pass

    existing_contact = PublishingCompany.query.filter_by(contact = contact).first(),409
    if existing_contact:
        return jsonify({'message':'Already existing'})
    
#storing a new user
    new_publishingcompany = PublishingCompany(name=name,contact = contact,address=address)
    db.session(new_publishingcompany)
    db.session.commit()
    return jsonify({'success':True,'message':'you have successfully registered','data':new_publishingcompany}),201