from django.http import JsonResponse
from .models import Move

def get_move_identifier(request, move_id):
    try:
        move = Move.objects.get(id=move_id)
        identifier  = move.identifier
        return JsonResponse({'identifier ': identifier })
    
    except Move.DoesNotExist:
        return JsonResponse({'error': 'Move not found'}, status=404)
