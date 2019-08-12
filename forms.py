from flask_wtf import FlaskForm
from models import Users
from wtforms import Form, StringField, PasswordField, SubmitField,RadioField
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "User Name"})
	password = PasswordField('password',validators=[InputRequired()], render_kw={"placeholder": "Password"})



class Upload(FlaskForm):
	product = StringField('product', validators=[InputRequired()], render_kw={"placeholder": "Enter product name"})
	price = StringField('price',validators=[InputRequired()], render_kw={"placeholder": "Price"})
	address = StringField('address',validators=[InputRequired()], render_kw={"placeholder": "Grocery store's address"})
	price_type = RadioField(choices=[('Regular','Regular'),('Special','Special')],default='Regular')


class Search(FlaskForm):
	product = StringField('product', validators=[InputRequired()], render_kw={"placeholder": "Enter a name"})
