import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.conf import settings

from .models import User



# Génère un jeton JWT pour un utilisateur avec un ID donné
def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=30)  # Expiration dans 30 minutes
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token



# Authentifie un utilisateur à partir du nom d'utilisateur et du mot de passe
def authenticate_user(username, password):
    try:
        user = User.objects.get(pseudo=username)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        pass
    return None



# Vérifie si le token de la requête est correcte
def token_validation(request) :
    # Récupérer l'en-tête Authorization de la requête
    authorization_header = request.headers.get('Authorization')
    
    # Vérifier si l'en-tête Authorization est présent et commence par "Bearer "
    if authorization_header and authorization_header.startswith('Bearer ') :
        # Extraire le token de l'en-tête Authorization
        token = authorization_header.split(' ')[1]

        try :
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

            expiration_timestamp = payload.get('exp')
            if expiration_timestamp is None or expiration_timestamp < datetime.utcnow().timestamp() :
                return JsonResponse({'error': 'Expired Token'}, status=401), None
        
            user_id = payload.get('user_id')
            return True, user_id

        # Le token a expiré 
        except jwt.ExpiredSignatureError :
            return JsonResponse({'error': 'Expired Token'}, status=401), None
        
        # Le token est invalide
        except jwt.InvalidTokenError :
            return JsonResponse({'error': 'Invalide Token'}, status=401), None

    else :
        # L'en-tête Authorization n'est pas présent ou ne commence pas par "Bearer "
        return JsonResponse({'error': 'Authentication required'}, status=401), None
    


# Vérifie si l'utilisateur est admin ou non
def is_admin(user_id) :
    user = User.objects.get(id=user_id)
    return user.role == 'admin'
