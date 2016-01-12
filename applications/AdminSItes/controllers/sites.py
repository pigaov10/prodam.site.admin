### SITE PLONE
import os, sys
import xml.etree.cElementTree as tree_element_first

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

			#split do nome do site separado por .
			directories = project_name.split(".")
			for directory in directories:
				path += "/"+directory
				os.mkdir(path, 0755 );
			
			# profiles
			profiles = path
			os.mkdir(profiles+"/profiles", 0755);
			os.mkdir(profiles+"/profiles/default/", 0755);
			add_profile_file(path)

			#browser
			path += folders[2]
			os.mkdir(path, 0755);
			
			# viewlets
			path += folders[1]
			os.mkdir(path, 0755);
			
			# zcml file
			add_configure_file(path,project_name)
			
			# python file configure
			add_viewlets_file(path)
			
			# templates
			path += folders[4]
			os.mkdir(path, 0755);
			# pt file 
			add_template_file(path)
		except:
			raise HTTP(500, T('Ocorreu um erro...'))
	else:
		site = None
	lista = os.listdir("sites/")
	return dict(lista=lista,site=site)


def add_configure_file(path,project_name,param1='IPortalHeader',param2='IProdamPortal'):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O ARQUIVO ZCML 
	"""

	#seta nó para configuração dos namespaces
	configure = tree_element_first.Element('configure')
	configure.set('xmlns','http://namespaces.zope.org/zope')
	configure.set('xmlns:browser','http://namespaces.zope.org/browser')
	configure.set('i18n_domain','prodam.portal')

	#seta nó para configuração das Viewlets do Plone
	browser = tree_element_first.SubElement(configure,"browser:viewlet")
	browser.set("name","plone.logo")
	browser.set("manager","plone.app.layout.viewlets.interfaces."+param1)
	browser.set("class",".logo.LogoViewlet")
	browser.set("permission","zope2.View")
	browser.set("layer",project_name+".interfaces."+param2)

	tree = tree_element_first.ElementTree(configure)
	configure_name = "/configure.zcml"
	indent(configure)
	tree.write(path+configure_name,encoding="utf-8")


def add_template_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O TEMPLATE alerta.pt 
	"""
	text = open('sites/components/alerta.pt','r').read()
	file_name = "alerta.pt"
	file = open(path+"/"+file_name,"a+")
	file.write(text)
	file.close()

def add_profile_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O PROFILE CONFIGURAÇÃO VIEWLET viewlets.xml
	"""
	#seta nó para configuração dos namespaces
	xml_object = tree_element_first.Element('object')

	tree = tree_element_first.ElementTree(xml_object)
	configure_name = "/profiles/default/viewlets.xml"
	indent(xml_object)
	tree.write(path+configure_name,encoding="utf-8")


def add_viewlets_file(path):
	"""
	MÉTODO RESPONSÁVEL POR GERAR O viewlets.py 
	"""

	file_name = "viewlets.py"
	file = open(path+"/"+file_name,"a+")
	file.close()

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

def testando():
	users = db(db.t_tbl_components).select()
	return dict(users=users)