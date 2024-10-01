from django.contrib import admin
from django.urls import path
from todos.views import home, todo_list, todo_list_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página inicial (home.html)
    path('todos/', todo_list),  # Página com a lista de alunos
    path('todos_db/', todo_list_db),  # Página com a lista de tarefas do BD
]
