import os
import sys
import site

site.addsitedir('/home/looquest/venv/lib/python2.6/site-packages')

path = '/home/looquest/LooQuest/src/'
if path not in sys.path:
    sys.path.append(path)

path2 = '/home/looquest/LooQuest/src/looquest/'
if path2 not in sys.path:
    sys.path.append(path2)

os.environ['DJANGO_SETTINGS_MODULE'] = 'looquest.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
