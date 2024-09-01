from django.contrib.auth.decorators import login_required
from functools import wraps

from django.shortcuts import render

def has_group(group_name="DIRETOR"):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return render(request, "error.html", {"title": "Permissão negada", "error_code": "403", "message": "Você não tem permissão para executar essa ação, por favor contate o gerenciador do site!"})

        return _wrapped_view
    return decorator
