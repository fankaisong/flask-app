from flask import Flask
from flask_sqlalchemy import SQLAlchemy

  

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)




from views import * 

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)


