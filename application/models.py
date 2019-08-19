from app import db 

class Users(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))



class Ppa(db.Model):
	__tablename__ = 'ppa'
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(20))
	product = db.Column(db.String(20))
	price = db.Column(db.DECIMAL(10,4))
	address = db.Column(db.String(50))
	price_type = db.Column(db.String(20))







