from django.urls import path
from aplications.chemical_sampling import views

urlpatterns = [

path(
    route='',
    view=views.feed_view,
    name='feed'
),

path(
    route='create_sampling/',
    view=views.create_sampling_view,
    name='create_sampling'
),

]