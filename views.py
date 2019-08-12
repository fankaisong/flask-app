from app import *
from models import Users, Ppa
from flask import session, render_template, request, redirect
from forms import LoginForm, Upload, Search


@app.route('/')
def home():
	if not session.get('logged_in'):
		return login()
	return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
	error=None
	form = LoginForm()

	if form.validate_on_submit():
		user = Users.query.filter_by(user_name=form.username.data).first()
		if user and user.password==form.password.data:	
			session['logged_in'] = True
			session['username'] = form.username.data
			return render_template('home.html',error = None)
		elif user:
			return render_template('login.html',error = "Wrong Password",form=form)
		else:
			return render_template('login.html',error = "Wrong User Name",form=form)
		
	return render_template('login.html',error=None,form=form)


@app.route('/upload',methods = ['POST','GET'])
def upload():
	info = []		
	form = Upload()
	if form.validate_on_submit():
		info.append(form.product.data)
		info.append(form.price.data)
		info.append(form.address.data)
		info.append(form.price_type.data)
		data = Ppa(user_name=session['username'], product=info[0], price=info[1], address=info[2], price_type=info[3])
		db.session.add(data)
		db.session.commit()

	return render_template('upload.html', info=info, form=form)

@app.route('/search',methods = ['POST','GET'])
def search():
	info = []
	form = Search()
	if form.validate_on_submit():
		search = "%{}%".format(form.product.data)
		res = Ppa.query.filter(Ppa.product.like(search)).all()
		if res:
			for r in res:
				info.append({'price_type':r.price_type,'price':r.price,'address':r.address})
		
	return render_template('search.html', info = info, form=form)



@app.route('/account',methods = ['POST','GET'])
def account():
	if request.method == 'POST':
		Ppa.query.filter_by(id=request.form['del']).delete()
		db.session.commit()

	info = []
	res = Ppa.query.filter_by(user_name=session['username']).all()
	if res:
		for r in res:
			info.append({'id':r.id, 'product':r.product, 'price_type':r.price_type,'price':r.price,'address':r.address})

	return render_template('account.html', info = info)

	

@app.route("/logout")
def logout():
	session['logged_in'] = False
	session.clear()
	return home()	

@app.route('/about')
def about():
    return render_template('about.html')
