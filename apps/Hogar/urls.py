from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.Hogar.views import *

from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^prevencion/',prevencion,name='baseprevencion'),

]
