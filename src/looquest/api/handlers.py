from piston.handler import BaseHandler, AnonymousBaseHandler
from loos.models import Loo, LooSpot
from loos.forms import LooSpotForm
from piston.utils import validate, rc

from operator import methodcaller

class LooHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Loo
    
    
    def read(self, request):
        """ Returns all known loos, or the closest if closest is a var with a latlon """
        base = Loo.objects
        loos = base.all()
        
        location = request.GET.get('closest_to', None)
        if location:
            lat, lon = location.split(',')
            loo_list = [x for x in loos]
            receeding_loos = sorted(loo_list, 
                                    key=methodcaller('distance_from', 
                                                     float(lat), 
                                                     float(lon)))   
            return receeding_loos[0] 
        else:
            return loos
        
class LooSpotHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = LooSpot
    is_anonymous = True
    
    def read(self, request):
        return LooSpot.objects.all()
    
    #Given that we allow anonymous writes we'd better throttle this
    @validate(LooSpotForm)
    def create(self, request):
        request.form.save()
        return rc.CREATED