from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.dates import YearArchiveView
from .models import Youtube ,YoutubeLink

# Create your views here.
class HomeView(ListView):
    model = Youtube
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context["top_rated"] = Youtube.objects.filter(status='TR')
        context["most_watched"] = Youtube.objects.filter(status='MW')
        context["recently_added"] = Youtube.objects.filter(status='RA')
        return context


class YoutubeList(ListView):
    model = Youtube
    paginate_by = 2
    template_name = "blog/youtube_list.html"




class YoutubeDetail(DetailView):
    model = Youtube
    

    def get_object(self):
        object = super(YoutubeDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object


    def get_context_data(self, **kwargs):
        context = super(YoutubeDetail,self).get_context_data(**kwargs)
        context["links"] = YoutubeLink.objects.filter(youtube=self.get_object())
        context["related_youtubes"] = Youtube.objects.filter(category=self.get_object().category)
        return context
    template_name = "blog/youtube_detail.html"

class YoutubeCategory(ListView):
    model = Youtube
    paginate_by = 2
    template_name = "blog/youtube_list.html"

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Youtube.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(YoutubeCategory,self).get_context_data(**kwargs)
        context["youtube_category"] = self.category
        return context
    
    

class YoutubeLanguage(ListView):
    model = Youtube
    paginate_by = 2
    template_name = "blog/youtube_list.html"

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Youtube.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(YoutubeLanguage,self).get_context_data(**kwargs)
        context["youtube_language"] = self.language
        return context



class YoutubeSearch(ListView):
    model = Youtube
    paginate_by = 2
    template_name = "blog/youtube_list.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()

        return object_list


class YoutubeYear(YearArchiveView):
    queryset = Youtube.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
    template_name = "blog/youtube_archive_year.html"