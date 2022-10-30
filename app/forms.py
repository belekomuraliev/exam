from datetime import date
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, \
     validators, ValidationError, DateField

from .models import Position, Employee

class PositionForm(FlaskForm):

    name = StringField(label='Должность', validators=[validators.DataRequired()])
    department = StringField(label='Отдел', validators=[validators.DataRequired()])
    wage = IntegerField(label='Зарплата', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить')

    def validate_wage(self, wage):
        if wage.data > 0:
            raise ValidationError('Зарплата  не может быть отрицательным.')

class EmployeeForm(FlaskForm):
    name = StringField(label='ФИО',  validators=[validators.DataRequired()])
    birth_date = DateField('Дата рождения')
    position_id = SelectField(label='Что купил')
    submit = SubmitField(label='Сохранить')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for position in Position.query.all():
            result.append((position.id, position.name))
        self.position_id.choices = result

