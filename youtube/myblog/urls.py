
from django.urls import path
from .views import YoutubeList , YoutubeDetail , YoutubeCategory , YoutubeLanguage , YoutubeSearch , YoutubeYear
app_name = 'myblog'

urlpatterns = [
    path('', YoutubeList.as_view(), name='youtube_list'),
    path('category/<str:category>', YoutubeCategory.as_view(), name='youtube_category'),
    path('language/<str:lang>', YoutubeLanguage.as_view(), name='youtube_language'),
    path('search/', YoutubeSearch.as_view(), name='youtube_search'),
    path('<int:pk>', YoutubeDetail.as_view(), name='youtube_detail'),
    path('<slug:slug>', YoutubeDetail.as_view() , name='youtube_detail'),
    path('year/<int:year>', YoutubeYear.as_view() , name='youtube_year'),
    
]
