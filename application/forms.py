from flask_wtf import FlaskForm
from models import Users
from wtforms import Form, StringField, PasswordField, IntegerField, RadioField
from wtforms.validators import InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "User Name"})
	password = PasswordField('password',validators=[InputRequired()], render_kw={"placeholder": "Password"})

class RegisterForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(max=20)], render_kw={"placeholder": "Create User Name"})
	password = PasswordField('password',validators=[InputRequired(),Length(min=3,max=20, message="Password length MUST between 3-20"), EqualTo('confirm', message='Passwords must match')], render_kw={"placeholder": "Create Password"})
	confirm = PasswordField('password',validators=[InputRequired(), Length(min=3,max=20)], render_kw={"placeholder": "Confirm Password"})


class UploadForm(FlaskForm):
	product = StringField('product', validators=[InputRequired()], render_kw={"placeholder": "Enter product name"})
	price = IntegerField('price',validators=[InputRequired()], render_kw={"placeholder": "Price(Must be numbers)"})
	address = StringField('address',validators=[InputRequired()], render_kw={"placeholder": "Grocery store's address"})
	price_type = RadioField(choices=[('Regular','Regular'),('Special','Special')],default='Regular')


class SearchForm(FlaskForm):
	product = StringField('product', validators=[InputRequired()], render_kw={"placeholder": "Enter a name"})
