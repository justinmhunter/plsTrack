from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class PlsForm(Form):
    pls_nick = StringField('pls_nick', validators = [Required()], default='nickname')
    pls_link = StringField('pls_link', validators = [Required()], default='url pls')
