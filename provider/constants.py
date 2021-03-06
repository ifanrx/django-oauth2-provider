from datetime import timedelta
from django.conf import settings

CONFIDENTIAL = 0
PUBLIC = 1
INSECURE = 2

SOCIALBASE_CLIENTS = [CONFIDENTIAL, PUBLIC, INSECURE]

SSO_ENDUSER_CONFIDENTIAL = 3
SSO_ENDUSER_PUBLIC = 4
SSO_ENDUSER_INSECURE = 4
SSO_HYDROGEN_OPENAPI = 5

SSO_CLIENTS = [
    SSO_ENDUSER_PUBLIC, SSO_ENDUSER_INSECURE, SSO_ENDUSER_CONFIDENTIAL]

CLIENT_TYPES = (
    (CONFIDENTIAL, "Confidential (Web applications)"),
    (PUBLIC, "Public (Native and JS applications)"),
    (INSECURE, "Insecure applications"),
    (SSO_ENDUSER_CONFIDENTIAL, "SSO end-user application Confidential (Web applications)"),
    (SSO_ENDUSER_PUBLIC, "SSO end-user application Public (Native and JS applications)"),
    (SSO_ENDUSER_INSECURE, "SSO end-user application Insecure applications"),
)

RESPONSE_TYPE_CHOICES = getattr(settings, 'OAUTH_RESPONSE_TYPE_CHOICES', ("code", "token"))

TOKEN_TYPE = 'Bearer'

READ = 1 << 1
WRITE = 1 << 2
ADMIN = 1 << 3
READ_WRITE = READ | WRITE
READ_WRITE_ADMIN = READ | WRITE | ADMIN

DEFAULT_SCOPES = (
    (READ, 'read'),
    (WRITE, 'write'),
    (READ_WRITE, 'read+write'),
    (READ_WRITE_ADMIN, 'read+write+admin'),
)

SCOPES = getattr(settings, 'OAUTH_SCOPES', DEFAULT_SCOPES)

EXPIRE_DELTA = getattr(settings, 'OAUTH_EXPIRE_DELTA', timedelta(days=365))

# Expiry delta for public clients (which typically have shorter lived tokens)
EXPIRE_DELTA_PUBLIC = getattr(settings, 'OAUTH_EXPIRE_DELTA_PUBLIC', timedelta(days=30))

EXPIRE_CODE_DELTA = getattr(settings, 'OAUTH_EXPIRE_CODE_DELTA', timedelta(seconds=10 * 60))

# Remove expired tokens immediately instead of letting them persist.
DELETE_EXPIRED = getattr(settings, 'OAUTH_DELETE_EXPIRED', False)

ENFORCE_SECURE = getattr(settings, 'OAUTH_ENFORCE_SECURE', False)
ENFORCE_CLIENT_SECURE = getattr(settings, 'OAUTH_ENFORCE_CLIENT_SECURE', True)

SESSION_KEY = getattr(settings, 'OAUTH_SESSION_KEY', 'oauth')

SINGLE_ACCESS_TOKEN = getattr(settings, 'OAUTH_SINGLE_ACCESS_TOKEN', False)
