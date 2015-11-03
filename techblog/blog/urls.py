__author__ = 'jiasir'

from django.conf.urls import *
from techblog.blog.views import archive

urlpatterns = patterns('',
                       url(r'^$', archive))
