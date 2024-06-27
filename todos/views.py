from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .todo import todos

def index(request):
    return render(request, 'index.html')

@require_http_methods(['POST'])
def search(request):
    found_todos = []
    search_term = request.POST.get('search')
    if len(search_term) == 0:
        return render(request, 'todo.html', {'todos': []})
    for todo in todos:
        if search_term in todo['title']:
            found_todos.append(todo)
    return render(request, 'todo.html', {'todos': found_todos})
