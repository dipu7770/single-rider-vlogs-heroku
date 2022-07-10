from .models import Youtube


def slider_youtubes(request):
    youtubes = Youtube.objects.all().order_by('created')[0:3]
    # movies = Movie.objects.last()
    return {'slider_youtube' : youtubes}