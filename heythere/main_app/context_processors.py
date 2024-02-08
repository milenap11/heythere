from .models import Employee
def show_user(request):
    current_user = Employee.objects.get(employee_email=request.user.email)
    return {'current_user': current_user}