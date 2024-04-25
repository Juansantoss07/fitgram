# utils/context_processors.py
from customUser.models import Usuario

def user_data(request):
    user_profile = None
    
    if request.user.is_authenticated:
        try:
            user_profile = Usuario.objects.get(id=request.user.id)
        except Usuario.DoesNotExist:
            pass
    
    return {'user_profile': user_profile}
