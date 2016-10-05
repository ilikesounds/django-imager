from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from imager_images.forms import PhotoUploadForm
from .models import Photo, Album
# Create your views here.


class PhotoView(DetailView):
    template_name = 'imager_images/photo.html'
    model = Photo


class AlbumView(DetailView):
    pass


class AlbumDetailView(DetailView):
    template_name = 'imager_images/album.html'
    model = Album


class UploadPhotoView(CreateView):
    template_name = 'imager_images/create_photo.html'
    form_class = PhotoUploadForm
    model = Photo

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('library')
        return url

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.user = self.request.user
        return super(UploadPhotoView, self).form_valid(form)


class LibraryView(TemplateView):

    """This class handles the library view. It returns all the photos and
       and albums for a user.
    """
    template_name = 'imager_images/library.html'

    def get_context_data(self, **kwargs):
        """
        Override of the builtin get_context_data function.
        """
        context = super(LibraryView, self).get_context_data(**kwargs)
        context['full_name'] = self.request.user.get_full_name()
        context['photos'] = self.request.user.photo.all()
        context['albums'] = self.request.user.album.all()
        return context
