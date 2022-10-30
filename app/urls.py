

from .views import app, index, position_create, position_delete, position_update, \
    employee_create,employee_delete,employee_detail,employee_update

app.add_url_rule('/', view_func=index, methods=['GET','POST'], endpoint='employee')
app.add_url_rule('/position/create', view_func=position_create, methods=['GET', 'POST'], endpoint='position_create')
app.add_url_rule('/position/<int:position_id>/delete', view_func=position_delete, methods=['GET', 'POST'], endpoint='position_delete')
app.add_url_rule('/position/<int:position_id>/update', view_func=position_update, methods=['GET', 'POST'], endpoint='position_update')


app.add_url_rule('/employee/create', view_func=employee_create, methods=['GET', 'POST'], endpoint='employee_create')
app.add_url_rule('/employee/<int:employee_id>', view_func=employee_detail, methods=['GET', 'POST'], endpoint='employee_detail')
app.add_url_rule('/employee/<int:employee_id>/delete', view_func=employee_delete, methods=['GET', 'POST'], endpoint='employee_delete')
app.add_url_rule('/employee/<int:employee_id>/update', view_func=employee_update, methods=['GET', 'POST'], endpoint='employee_update')

