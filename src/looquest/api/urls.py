from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import LooHandler, LooSpotHandler

loo_handler = Resource(LooHandler)
loospot_handler = Resource(LooSpotHandler)


urlpatterns = patterns('',
   url(r'^loos/', loo_handler),                    
   url(r'^loospots/', loospot_handler),
)
