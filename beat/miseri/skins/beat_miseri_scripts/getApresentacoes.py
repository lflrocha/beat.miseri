## Script (Python) "getUltimasNoticias"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

catalogo = context.portal_catalog
path={'query' : '/miseri/espetaculos'}
end={'query': context.ZopeTime(), 'range': 'min'}

apresentacoes = catalogo.searchResults(path=path, \
                                       Type='Event', \
                                       end=end, \
                                       sort_on='start', \
                                       limit=5, \
                                       review_state='published')

return apresentacoes