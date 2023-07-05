"""
URL configuration for triovet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from triovet.apps.users.views import sign_up, sign_in, sign_out
from triovet.apps.schedule.views import appointments, new_appointment, \
    delete_appointment, approve_appointment
from triovet.apps.core.views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("new_appointment/", new_appointment, name="new_appointment"),
    path("appointments/", appointments, name="appointments"),
    path("appointments/delete/<int:appointment_id>/", delete_appointment, name="delete_appointment"),
    path("appointments/approve/<int:appointment_id>/", approve_appointment, name="confirm_appointment"),
    path("sign_up/", sign_up, name="sign_up"),
    path("sign_in/", sign_in, name="sign_in"),
    path("sign_out/", sign_out, name="sign_out")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
