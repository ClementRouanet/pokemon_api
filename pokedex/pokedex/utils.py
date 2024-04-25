import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .models import User


def generate_jwt_token(user_id):
    """
    Génère un jeton JWT pour un utilisateur avec un ID donné.
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)  # Expiration dans 1 jour
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def authenticate_user(username, password):
    """
    Authentifie un utilisateur à partir du nom d'utilisateur et du mot de passe.
    Retourne None si l'authentification échoue.
    """
    try:
        user = User.objects.get(pseudo=username)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        pass
    return None
