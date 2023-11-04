# context_processors.py
def is_user_admin(request):
    return {'is_admin': request.user.groups.filter(name='Admin').exists()}
