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

	import xml.etree.cElementTree as tree_element_first
	#seta nó para configuração dos namespaces
	configure = tree_element_first.Element('configure')
	configure.set('xmlns','http://namespaces.zope.org/zope')
	configure.set('xmlns:browser','http://namespaces.zope.org/browser')
	configure.set('i18n_domain','prodam.portal')

	#seta nó para configuração das Viewlets do Plone
	browser = tree_element_first.SubElement(configure,"browser:viewlet")
	browser.set("name","plone.logo")
	browser.set("manager","plone.app.layout.viewlets.interfaces.IPortalHeader")
	browser.set("class",".logo.LogoViewlet")
	browser.set("permission","zope2.View")
	browser.set("layer","prodam.portal.interfaces.IProdamPortal")

	tree = tree_element_first.ElementTree(configure)
	configure_name = "/configure.zcml"
	indent(configure)
	tree.write(path+configure_name,encoding="utf-8")
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

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i