from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Position, Employee
from .forms import PositionForm, EmployeeForm


def index():
    title = 'Список сотрудников'
    employee = Employee.query.all()
    return render_template('index.html', employees=employee, title=title)



def position_create():
    title = 'Позиция'
    form = PositionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'Позиция {position.name} успешно добавлено', 'success')
            return redirect(url_for('employee'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
    return render_template('position_form.html', form=form, title=title)

def position_delete(position_id):
    form = PositionForm(request.form)
    position = Position.query.filter_by(id=position_id).first()
    if request.method == 'GET':
        return render_template('position_delete.html', position=position, form=form)
    if request.method == 'POST':
        db.session.delete(position)
        db.session.commit()
        flash(f'Категория "{position.name}" успешно удален', 'warning')
        return redirect(url_for('employee'))

def position_update(position_id):

    position = Position.query.filter_by(id=position_id).first()
    form = PositionForm(request.form, obj=position)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(position)
            db.session.commit()
            flash(f'Позиция  "{position.name}" № {position.id} успешно обнавлен', 'success' )
        return redirect(url_for('employee', position_id=position.id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в  поле {field} текст ошибки {error}', 'danger')
    return render_template('position_form.html', form=form, position=position)




def employee_create():
    title = 'Новый сотрудник'
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'Новый  сотрудник {employee.name} успешно добавлен', 'success')
            return redirect(url_for('employee'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
    return render_template('employee_form.html', form=form, title=title)

def employee_detail(employee_id):
    form = EmployeeForm(request.form)
    employee = Employee.query.filter_by(id=employee_id).first()
    return render_template('employee_detail.html', employee=employee, form=form)

def employee_delete(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    form = Employee()
    if request.method == 'GET':
        return render_template('employee_delete.html', employee=employee, form=form)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        flash(f'Сотрудник {employee.name} № {employee.id} успешно удалено.')
        return redirect(url_for('employee', employee_id=employee.id))

def employee_update(employee_id):

    employee = Employee.query.filter_by(id=employee_id).first()
    form = EmployeeForm(request.form, obj=employee)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.commit()
            flash(f'Данные сотрудник  "{employee.name}" успешно обнавлен', 'success' )
        return redirect(url_for('employee_detail', employee_id=employee.id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в  поле {field} текст ошибки {error}', 'danger')
    return render_template('employee_form.html', form=form, employee=employee)