from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class InventoryModel(db.Model):
    __tablename__ = "mytable"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    quantity = db.Column(db.Integer())
    type = db.Column(db.String(80))
 
    def __init__(self,name,quantity,type):
        self.name = name
        self.quantity = quantity
        self.type = type
 
    def __repr__(self):
        return f"{self.name}:{self.id}"