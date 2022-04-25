from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="Requerido")])
    email = EmailField("Correo electrónico", validators=[DataRequired(message="Requerido")])
    password = PasswordField("Contraseña", validators=[DataRequired(message="Requerido")])
    submit = SubmitField("Ingresar")