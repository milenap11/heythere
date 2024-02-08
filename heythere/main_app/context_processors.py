from .models import Employee
def show_user(request):
    if request.user.is_superuser:
        current_user = 'superuser'
    elif not request.user.is_anonymous:
        current_user = Employee.objects.get(employee_email=request.user.email)
    else:
        current_user = 'guest'
    return {'current_user': current_user}