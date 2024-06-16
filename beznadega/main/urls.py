from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cours', views.about, name='about'),
    path('openedu', views.pyti, name='pyti'),
    path('openedu.urfu', views.pyti1, name='pyti1'),
    path('learnonline.hse.ru', views.pyti2, name='pyti2'),
    path('lxp.utmn.ru', views.pyti3, name='pyti3'),
    path('ULEARN.ME', views.pyti4, name='pyti4'),
    path('ELEARN.URFU.RU', views.pyti5, name='pyti5'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('course', views.course, name='course'),
    path('URFU', views.course1, name='course1'),
    path('ITMO', views.course2, name='course2'),
    path('MGY', views.course3, name='course3'),
    path('MISIS', views.course4, name='course4'),
    path('MIFI', views.course5, name='course5'),
    path('MFTI', views.course6, name='course6'),
    path('NIY', views.course7, name='course7'),
    path('POLITEH', views.course8, name='course8'),
    path('SPB', views.course9, name='course9'),
    path('TGY', views.course10, name='course10'),
    path('TUMGY', views.course11, name='course11'),
]