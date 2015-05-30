## Script (Python) "getUltimasNoticias"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

catalogo = context.portal_catalog
path={'query' : '/miseri/imprensa'}
noticias = catalogo.searchResults(path=path, \
                                  Type='News Item', \
                                  sort_on='created', \
                                  review_state='published')[:2]

return noticias