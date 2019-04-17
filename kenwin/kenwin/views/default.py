from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from ..services.user import UserService
from .security import check_password


@view_config(route_name='home',
             renderer='kenwin:templates/login_index.jinja2')
def index_page(request):
    return {}


@view_config(route_name='auth', match_param='action=in', renderer='string',
             request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    username = request.POST.get('username')
    if username:
        user = UserService.by_name(username, request=request)
        if user and check_password(request.POST.get('password'), user.password):
            headers = remember(request, user.name)
        else:
            headers = forget(request)
    else:
        headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)
