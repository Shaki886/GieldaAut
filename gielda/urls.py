from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gielda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'', include('index.urls')),
	url(r'^index.html/', include('index.urls')),
	url(r'^faq/', include('faq.urls')),
	url(r'^pomoc/', include('pomoc.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
