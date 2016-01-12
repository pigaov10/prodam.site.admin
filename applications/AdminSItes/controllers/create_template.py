"""
"""

def a():
	return dict()

def b():
	post = request.post_vars.nome
	if not post:
		post = None
	return dict(post=post)