from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from imager_images.forms import (PhotoUploadForm,
                                 PhotoEditForm,
                                 NewAlbumForm
                                 )
from .models import Photo, Album
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class PhotoView(DetailView):
    template_name = 'imager_images/photo.html'
    model = Photo


class AlbumDetailView(DetailView):
    template_name = 'imager_images/album.html'
    model = Album

    def get_context_data(self, **kwargs):
        """
        Override of the builtin get_context_data function.
        """
        context = super(DetailView, self).get_context_data(**kwargs)
        photo_queryset = self.object.photos.all()
        photo_paginator = Paginator(photo_queryset, 4)
        page = self.request.GET.get('page')
        try:
            photos = photo_paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            photos = photo_paginator.page(1)
        except EmptyPage:
            photos = photo_paginator.page(photo_paginator.num_pages)
        context['photos'] = photos
        return context


class NewAlbumView(CreateView):
    template_name = 'imager_images/album_new.html'
    form_class = NewAlbumForm
    model = Album

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.user = self.request.user
        return super(NewAlbumView, self).form_valid(form)

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('library_view')
        return url


class UploadPhotoView(CreateView):
    template_name = 'imager_images/create_photo.html'
    form_class = PhotoUploadForm
    model = Photo

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('library_view')
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


class PhotoEditView(UpdateView):
    model = Photo
    # fields = ['caption', 'camera', 'published_status', 'albums']
    template_name_suffix = '_edit'
    form_class = PhotoEditForm

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('library_view')
        return url

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.user = self.request.user
        return super(PhotoEditView, self).form_valid(form)
