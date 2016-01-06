from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Gerenciador de portais Plone'
settings.subtitle = 'powered by prodam'
settings.author = 'prodam'
settings.author_email = 'prodam@example.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '549aacc2-3f87-4be3-bff4-5604dbe6db98'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
