from .import views
from django.urls import path
# import pdfkit 
urlpatterns = [
path('', views.coustmer_front, name='front'),
path('signup/', views.coustmer_signup, name='signup'),
path('login/', views.coustmer_login, name='login'),
path('logout/', views.coustmer_logout, name='logout'),
path('coustmerpreview/<int:id>', views.coustmer_preview, name='coustmerpreview'),
path('aftercreate/<int:id>/', views.coustmer_after_create, name='aftercreate'),
path('createproposal/<int:id>/',views.create_proposal,name='createproposal'),
path('editproposal/<int:id>/', views.edit_proposal, name='editproposal'),
path('deleteproposal/<int:id>/', views.delete_proposal, name='deleteproposal'),
path('showimage/', views.coustmer_proposal_image, name='showimage'),
]