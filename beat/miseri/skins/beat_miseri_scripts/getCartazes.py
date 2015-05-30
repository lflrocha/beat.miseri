## Script (Python) "getCartazes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

catalogo = context.portal_catalog
path={'query' : '/miseri/espetaculos','depth':2}
cartazes = catalogo.searchResults(path=path, id='cartaz.jpg')

return cartazes