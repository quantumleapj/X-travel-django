from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from . import views
import analysis.views
# import album.views

urlpatterns = [
  path('',views.index,name='index'),
  path('login',
    auth_views.LoginView.as_view(template_name = 'login.html'),
    name = 'login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name = 'logout'),
  path('signup/', views.signup, name = 'signup'),
  path('album/',views.index,name='album'),
  path('upload/',views.upload,name='upload'),
  path('detail/<int:photo_id>',views.detail,name='detail'),
  # path('test/',views.test, name='test')  ,
#태그 
  path('detail/add_tag/',views.add_tag,name='add_tag'),
  path('detect_tag/',views.detect_tag,name='detect_tag'),
# 검색 페이지,
  path('search/', views.search_by_tag,name='search_by_tag'),
  path('search/detail/<int:photo_id>',views.detail,name='detail'),
# 분석 페이지
  path('analysis/', views.analysis, name='analysis'),
  path('analysis/analysisPlace',analysis.views.analysisPlace,name='analysisPlace'),
  path('analysis/analysisTime',analysis.views.analysisTime,name='analysisTime'),
  path('analysis/a_search', analysis.views.analysisSearch, name='a_search'),   

# app api 
  path('app_login/', views.AppLoginView.as_view(), name='AppLogin'),
  path('app_upload/', views.UploadView.as_view(), name="AppUpload"),
  path('app_index/',views.IndexView.as_view(), name='AppIndex'),
  path('app_profile/',views.ProfileView.as_view(), name='AppProfile'),
  path('app_detail/',views.UploadDetailView.as_view(), name='AppDetail'),
  path('app_analysis/',views.AnalysisView.as_view(), name='AppAnalysis'),
  path('app_index/search/',views.SearchView.as_view(),name='search_by_tag'),
  path('app_index/detail/add_tag/',views.add_tag,name='add_tag'),
  path('app_index/detect_tag/',views.detect_tag,name='detect_tag'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

