def create_jwt(request):
    
    """
    the above token need to be saved in database, and a one-to-one
    relation should exist with the username/user_pk
    """

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    expiry = datetime.date.today() + timedelta(days=50)
    token = jws.sign({'username': user.username, 'expiry':expiry}, 'seKre8', algorithm='HS256')

return HttpResponse(token)



class JWTAuthentication(object):
    
    """
    Simple token based authentication.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:
    Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    def authenticate(self, request):
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'token':
        return None

    try:
        token = auth[1].decode()
    except UnicodeError:
        msg = _('Invalid token header. Token string should not contain invalid characters.')
        raise exceptions.AuthenticationFailed(msg)

    return self.authenticate_credentials(token)

    def authenticate_credentials(self, payload):

    decoded_dict = jws.verify(payload, 'seKre8', algorithms=['HS256'])

    username = decoded_dict.get('username', None)
    expiry = decoded_dict.get('expiry', None)

    try:
        usr = User.objects.get(username=username)
    except model.DoesNotExist:
        raise exceptions.AuthenticationFailed(_('Invalid token.'))

    if not usr.is_active:
        raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

    if expiry < datetime.date.today():
        raise exceptions.AuthenticationFailed(_('Token Expired.'))

    return (usr, payload)

    def authenticate_header(self, request):
    return 'Token'