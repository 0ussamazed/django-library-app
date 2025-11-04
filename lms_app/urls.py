from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    # path('delete',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('best-selling-days/', views.best_selling_days, name='best_selling_days'),
    path('clients/', views.clients_info, name='clients_info'),

]