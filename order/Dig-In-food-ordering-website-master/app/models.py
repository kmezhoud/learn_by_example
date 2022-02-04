from datetime import datetime
from app import db

class Customer(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(250), nullable=False)
    cmail = db.Column(db.String(250), unique=True, nullable=False)
    cmobile = db.Column(db.Integer, unique=True, nullable=False)
    caddress = db.Column(db.String(250), nullable=False)
    cpassword = db.Column(db.String(250), nullable=False)

    # def __init__(self, cid, cname, cmail,cmobile,cpassword):
    # self.cid = cid
    # self.cname = cname
    # self.cmail = cmail
    # self.cmobile = cmobile
    # self.cpassword = cpassword
    
    # def __repr__(self):
    #     return "customer('{self.cid}')"


class Restadmin(db.Model):
    rid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rname = db.Column(db.String(250), nullable=False)
    rmail = db.Column(db.String(250), unique=True, nullable=False)
    rmobile = db.Column(db.Integer,unique=True, nullable=False)
    raddress = db.Column(db.String(250), nullable=False)
    rpassword = db.Column(db.String(250), nullable=False)
    

class Diginadmin(db.Model):
    amail = db.Column(db.String(250), primary_key=True) 
    apassword = db.Column(db.String(250), nullable=False)
    

class Items(db.Model):
    iid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    iname = db.Column(db.String(250), nullable=False)
    iprice = db.Column(db.Integer, nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('restadmin.rid'), nullable=False)
    


class Orders(db.Model):
    ohash = db.Column(db.Integer,primary_key=True, autoincrement=True)
    cid = db.Column(db.Integer, db.ForeignKey('customer.cid'), nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('restadmin.rid'), nullable=False)
    items = db.Column(db.String(250), nullable=False)
    tprice=db.Column(db.Integer, nullable=False)
    ostatus = db.Column(db.String(20), nullable=False)
    



db.create_all()
