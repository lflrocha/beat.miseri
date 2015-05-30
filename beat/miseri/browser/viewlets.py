from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
    
class MenuViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/menu.pt')    
    
class LogoViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/logo.pt')        