# import "packages" from flask
import requests, json

from tkinter import *

from flask import Flask, render_template, request
from flask import Blueprint, render_template
from image import image_data
from pathlib import Path

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html

# The code below creates the default pages that we have hidden from view on our website

@app.route('/')
def mainpage():
    return render_template("main_page.html")


@app.route('/game')
def gamepage():
    return render_template("game.html")


# The code below creates the custom about me pages for each team member

@app.route('/jakub/')
def jakub():
    response = requests.get("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key"
                            "=4E07A0ABAE258C00B17B9EBDEE265FE0&steamid=76561198988285392")
    text = response.json()
    game1 = text['response']['games'][0]['name']
    game1time = str(round(text['response']['games'][0]['playtime_2weeks']/60, 1))
    game1timeTotal = str(round(text['response']['games'][0]['playtime_forever']/60, 1))
    game1img = text['response']['games'][0]['img_logo_url']
    game1ID = text['response']['games'][0]['appid']
    game2 = text['response']['games'][1]['name']
    game2time = str(round(text['response']['games'][1]['playtime_2weeks']/60, 1))
    game2timeTotal = str(round(text['response']['games'][1]['playtime_forever']/60, 1))
    game2img = text['response']['games'][1]['img_logo_url']
    game2ID = text['response']['games'][1]['appid']
    game3 = text['response']['games'][2]['name']
    game3time = str(round(text['response']['games'][2]['playtime_2weeks']/60, 1))
    game3timeTotal = str(round(text['response']['games'][2]['playtime_forever']/60, 1))
    game3img = text['response']['games'][2]['img_logo_url']
    game3ID = text['response']['games'][2]['appid']
    return render_template("about_us/jakub.html", text=text, g1=game1, g1t=game1time, g1img=game1img,
                           g1tT=game1timeTotal, g1ID=game1ID, g2=game2, g2t=game2time, g2tT=game2timeTotal,
                           g2ID=game2ID, g2img=game2img, g3=game3, g3t=game3time, g3tT=game3timeTotal,
                           g3ID=game3ID, g3img=game3img)


@app.route('/kevin/', methods=['GET', 'POST'])
def kevin():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    payload = "{\"key1\": \"value\",\"key2\": \"value\"}"
    headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': "7c1d894378mshb7e7e6c6ecac61bp1f2fcbjsn264b46c0ce80"
    }

    response = requests.request("POST", url, headers=headers)

    text = response.text
    return render_template("about_us/kevin.html", text=text)


@app.route('/tristan/', methods=['GET', 'POST'])
def tristan():
    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "deb5e7f2d3mshad8ffd0c6263400p144918jsnd5cede3b7ac9"
    }

    response = requests.request("GET", url, headers=headers)
    text = response.text
    return render_template("about_us/tristan.html", text=text)


@app.route('/sreeja/', methods=['GET', 'POST'])
def sreeja():
    url = "https://brooklyn-nine-nine-quotes.p.rapidapi.com/api/v1/quotes/random"

    headers = {
        'x-rapidapi-host': "brooklyn-nine-nine-quotes.p.rapidapi.com",
        'x-rapidapi-key': "05cd5ecb69msh65f30850019e80dp124961jsn1cec22cef625"
    }
    response = requests.request("GET", url, headers=headers)

    text = response.text
    return render_template("about_us/sreeja.html", text=text)


@app.route('/hamza/', methods=['GET', 'POST'])
def hamza():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = "{\"key1\": \"value\",\"key2\": \"value\"}"
    headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
    'x-rapidapi-key': "6aa5930ddamsh4e21c56a3045ce9p1aaf49jsn2e14280f30bb"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    text = response.text
    return render_template("about_us/hamza.html", text=text)

# The code below creates the lab pages

@app.route('/lab1/', methods=['GET', 'POST'])
def greet5():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab1.html", name=name)
    # starting and empty input default
    return render_template("our_work/lab1.html", name="World")


@app.route('/lab2/')
def lab2():
    return render_template("our_work/lab2.html")


@app.route('/lab3/', methods=['GET', 'POST'])
def lab3():
    path = Path(app.root_path) / "static" / "assets"
    return render_template("our_work/lab3.html", images=image_data(path))


@app.route('/lab4/', methods={'GET', 'POST'})
def lab4():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab4.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/lab4.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/lab4_colorCode/', methods={'GET', 'POST'})
def lab4_colorcode():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab4_colorCode.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/lab4_colorCode.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=24)


@app.route('/lab4_unsignedAdd/')
def lab4_unsignedadd():
    return render_template("our_work/lab4_unsignedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/lab4_signedAdd/')
def lab4_signedadd():
    return render_template("our_work/lab4_signedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/tpts/')
def tpts():
    return render_template("our_work/tpts.html")


@app.route('/hackathontt3/', methods={'GET', 'POST'})
def tt3():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/hackathontt3.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/hackathontt3.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/wireframe/')
def wireframe():
    return render_template("our_work/wireframe.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.method == "POST":
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


# The code below creates the weather pages

@app.route('/weather1/')
def weather1():
    return render_template("weather_info/weather1.html")


@app.route('/weather2/')
def weather2():
    return render_template("weather_info/weather2.html")


@app.route('/weather3/')
def weather3():
    return render_template("weather_info/weather3.html")


@app.route('/weather4/')
def weather4():
    return render_template("weather_info/weather4.html")


@app.route('/wtd1/')
def wtd1():
    return render_template("weather_info/wtd1.html")


@app.route('/wtd2/')
def wtd2():
    return render_template("weather_info/wtd2.html")


@app.route('/wtd3/')
def wtd3():
    return render_template("weather_info/wtd3.html")


@app.route('/weather_checks/')
def wchecks():
    return render_template("weather_info/weather_checks.html", background='linear-gradient(-45deg, #f3feed, #5c8be4, '
                                                                          '#fbb73a)')

""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, password="", phone=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(password) > 0:
            self.password = password
        if len(phone) > 0:
            self.phone = phone
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='123toby', phone="1111111111")
    u2 = Users(name='Nicholas Tesla', email='ntesla@example.com', password='123niko', phone="1111112222")
    u3 = Users(name='Alexander Graham Bell', email='agbell@example.com', password='123lex', phone="1111113333")
    u4 = Users(name='Eli Whitney', email='eliw@example.com', password='123whit', phone="1111114444")
    u5 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="8587754956")
    u6 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8587754956")
    # U7 intended to fail as duplicate key
    u7 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8586791294")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()

"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests

from crud.model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def users_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Users.query.all()]


def users_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.filter((Users.name.ilike(term)) | (Users.email.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def user_by_id(userid):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userid).first()


# User extraction from SQL
def user_by_email(email):
    """finds User in table matching email """
    return Users.query.filter_by(email=email).first()


""" app route section """


# Default URL
@app_crud.route('/')
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())


# CRUD create/add
@app_crud.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('crud.crud'))


# CRUD read
@app_crud.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@app_crud.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("search.html")


# Search request and response
@app_crud.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response


""" API routes section """


class UsersAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, email, password, phone):
            po = Users(name, email, password, phone)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {email} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return users_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return users_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, email, name):
            po = user_by_email(email)
            if po is None:
                return {'message': f"{email} is not found"}, 210
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, email, name, password, phone):
            po = user_by_email(email)
            if po is None:
                return {'message': f"{email} is not found"}, 210
            po.update(name, password, phone)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:email>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:email>/<string:name>/<string:password>/<string:phone>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/crud'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/delete/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
