from django.views.generic import TemplateView
# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


class ProfileView(TemplateView):

    """This view handles requests for the user profile view"""

    template_name = 'imager_profile/profile.html'

    def get_context_data(self, **kwargs):
        """
        This function overrides the included generic TemplateView function and
        provides a custom context
        """
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        context['full_name'] = self.request.user.get_full_name()
        context['photo_count'] = self.request.user.photo.count()
        context['album_count'] = self.request.user.album.count()
        return context
