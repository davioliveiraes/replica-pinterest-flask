from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validatores import DataRequired, Email, Equalto, Length, ValidationError
class FormLogin(FlaskForm):
   email = StringField("Email", validators=[DataRequired(), Email()])
   senha = PasswordField("Senha", validatores=[DataRequired()])
   botao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
   email = StringField("Email", validators=[DataRequired(), Email()])
   username = StringField("Nome do usuário", validators=[DataRequired()])
   senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
   confirmacao_senha = PasswordField("Confirmacao de Senha", validators=[DataRequired(), Equalto("senha")])
   botao_confirmacao = SubmitField("Criar Conta")

   def validate_email(self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
         return ValidationError("Email já cadastrado, faça o login novamente para continuar.")
