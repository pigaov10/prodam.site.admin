### SITE PLONE
@auth.requires_membership('admin')
def add():
	import os, sys
	if request.post_vars.site:
		site = request.post_vars.site
		path = str("sites/prodam.gerenciador.")+str(site)
		try:
			os.mkdir( path, 0755 );
			path = str("sites/prodam.gerenciador.")+str(site)+str('/src')
			os.mkdir( path, 0755 );
			path = str("sites/prodam.gerenciador.")+str(site)+str('/src/prodam')
			os.mkdir( path, 0755 );
			path = str("sites/prodam.gerenciador.")+str(site)+str('/src/prodam/gerenciador')
			os.mkdir( path, 0755 );
			path = str("sites/prodam.gerenciador.")+str(site)+str('/src/prodam/gerenciador/')+str(site)
			os.mkdir( path, 0755 );
		except:
			raise HTTP(500, T('Erro ao criar o diretório'))
	else:
		site = None
	lista = os.listdir("sites/")
	return dict(lista=lista,site=site)



