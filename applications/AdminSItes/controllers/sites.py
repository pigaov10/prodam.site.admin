### SITE PLONE
import os, sys
@auth.requires_membership('admin')
def add():
	"""
	MÉTODO RESPONSÁVEL POR GERAR O SKELETON DE UM SITE PLONE
	@dir /sites/prodam.gerenciador.<project_name>/src/prodam/gerenciador/<project_name>/
	"""

	if request.post_vars.site:
		site = request.post_vars.site
		folders = ['sites','/viewlets','/browser','/src','/templates']
		try:
			project_name = "prodam.gerenciador."+str(site)
			path   = folders[0]
			path  += "/"+str(project_name)
			os.mkdir(path, 0755 ); # plone name site
			path  += folders[3]
			os.mkdir(path, 0755 ); # directory src

			directories = project_name.split(".")
			for directory in directories:
				path += "/"+directory
				os.mkdir(path, 0755 );
			# browser
			profiles = path
			os.mkdir(profiles+"/profiles", 0755);

			path += folders[2]
			os.mkdir(path, 0755);
			# viewlets
			path += folders[1]
			os.mkdir(path, 0755);
			# zcml file
			add_configure_file(path)
			# python file
			add_viewlets_file(path)
			# templates
			path += folders[4]
			os.mkdir(path, 0755);
			# pt file 
			add_template_file(path)
		except:
			raise HTTP(500, T('Erro ao criar o diretório'))
	else:
		site = None
	lista = os.listdir("sites/")
	return dict(lista=lista,site=site)

def add_configure_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O ARQUIVO ZCML 
	"""

	file_name = "configure.zcml"
	file = open(path+"/"+file_name,"a+")
	text = """<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:browser="http://namespaces.zope.org/browser"
    i18n_domain="prodam.portal">

  <browser:viewlet
      name="prodam.prefeitura.alertas"
      manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
      class=".viewlets.DefaultViewlet"
      layer="prodam.portal.interfaces.IProdamPortal"
      template="templates/alerta.pt"
      permission="zope2.View"
      />
</configure>
			"""
	file.write(text)
	file.close()
	return True

def add_template_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O TEMPLATE alerta.pt 
	"""

	file_name = "alerta.pt"
	file = open(path+"/"+file_name,"a+")
	file.close()
	return True

def add_viewlets_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O viewlets.py 
	"""

	file_name = "viewlets.py"
	file = open(path+"/"+file_name,"a+")
	file.close()
	return True
