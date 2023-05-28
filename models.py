from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'Yahoo, {self.email} was successfully added!'

class Dict(db.Model):
    id = db.Column(db.String, primary_key = True)
    word = db.Column(db.String(50))
    meaning = db.Column(db.String(300))
    part_of_speech = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    plural = db.Column(db.String(50))
    present_tense = db.Column(db.String(30))
    past_tense = db.Column(db.String(30))
    past_part = db.Column(db.String(30))
    perfect_aux = db.Column(db.String(10))
    preposition = db.Column(db.String(20))
    case_triggered = db.Column(db.String(15)) 
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,word,meaning,part_of_speech,gender,plural,present_tense,past_tense,past_part,perfect_aux,preposition,case_triggered,user_token, id = ''):
        self.id = self.set_id()
        self.word = word
        self.meaning = meaning 
        self.part_of_speech = part_of_speech 
        self.gender = gender
        self.plural = plural 
        self.present_tense = present_tense 
        self.past_tense = past_tense
        self.past_part = past_part
        self.perfect_aux = perfect_aux 
        self.preposition = preposition
        self.case_triggered = case_triggered
        self.user_token = user_token


    def __repr__(self):
        return f'This word was just added: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class DictSchema(ma.Schema):
    class Meta:
        fields = ['id', 'word', 'meaning', 'part_of_speech', 'gender', 'plural', 'present_tense', 'past_tense', 'past_part', 'perfect_aux', 'preposition', 'case_triggered', ]

dict_schema = DictSchema()
dicts_schema = DictSchema(many=True)