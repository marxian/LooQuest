from django.db import models
from datetime import datetime

from math import sin, cos, radians, acos

# http://en.wikipedia.org/wiki/Earth_radius
# """For Earth, the mean radius is 6,371.009 km """
EARTH_RADIUS_IN_MILES = 3958.761

def calc_dist(lat_a, long_a, lat_b, long_b):
    """all angles in degrees, result in miles"""
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    delta_long = radians(long_a - long_b)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES

class Loo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    
    def distance_from(self, lat, lon):
        return calc_dist(lat, lon, self.lat, self.lon)
    
    def __unicode__(self):
        return '%s (%s, %s)' % (self.name, self.lat, self.lon)

class LooSpot(models.Model):
    name = models.CharField(max_length=100, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    spot_time = models.DateTimeField('date spotted', default=datetime.now, editable=False)
    open = models.BooleanField()
    
    def distance_from(self, lat, lon):
        return calc_dist(lat, lon, self.lat, self.lon)
    
    def __unicode__(self):
        return '%s (%s, %s)' % (self.spot_time, self.lat, self.lon)
