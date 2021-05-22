from datetime import datetime
from wsgiref.util import FileWrapper
 
from flask import Flask , render_template ,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bookupdesk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

'''
Sno ,Name ,Email,Message

'''

class Feedback(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80),  nullable=False)
    Email = db.Column(db.String(20),  nullable=False)
    message = db.Column(db.String(500),  nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contactus.html')


@app.route('/genres/')
def genres():
    return render_template('genres.html')

@app.route('/scific/')
def scific():
    return render_template('scific.html')

@app.route('/mystry/')
def mystry():
    return render_template('mystry.html')

@app.route('/romance/')
def romance():
    return render_template('romance.html')

@app.route('/thriller/')
def thriller():
    return render_template('thriller.html')


@app.route('/adventure/')
def adventure():
    return render_template('adventure.html')


@app.route('/horror/')
def horror():
    return render_template('horror.html')


@app.route('/hummmor/')
def hummoor():
    return render_template('hummor.html')



@app.route('/selfhelp/')
def selfhelp():
    return render_template('selfhelp.html')

@app.route('/bio/')
def bio():
    return render_template('bio.html')

@app.route("/feedback/", methods = ['Get' , 'POST'])
def indexfeed():
    if (request.method=='POST'):

        name = request.form.get ('name')
        email = request.form.get ('email')
        message = request.form.get ('message')
        

        entry = Feedback(Name=name ,Email=email , message=message ,date=datetime.now())
        db.session.add(entry)
        db.session.commit()


    return render_template('indexfeed.html')

if __name__=="__main__":
    app.run(debug=True)