from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Lista de post / list post
class BlogList(ListView):
    model = Post
    template_name = 'BlogPost/listpost.html'

# Detalle de post / detail post
class BlogDetail(DetailView):
    model = Post
    template_name = 'BlogPost/detailpost.html'

# Crear post / create post
class BlogCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('listpost')
    fields = ['title', 'subtitle', 'content', 'image']
    # Asigna el usuario que crea el post (autor) / assign user that creates the post (author)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Actualizar post / update post
class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('listpost')
    fields = ['title', 'subtitle', 'content', 'image']
    # Valida si el usuario es el autor del post / validate if the user is the author of the post
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )
    
# Eliminar post / delete post
class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('listpost')
    fields = ['title', 'subtitle', 'content', 'image']

# Buscar post por titulo / search post by title
def search(request):
    if request.GET["title"]:
        title = request.GET["title"]
        post = Post.objects.filter(title__icontains=title)
        return render(request, 'BlogPost/resultsearch.html', {"post":post})
    else:
        response="Please enter the title of the post"
    return render(request, 'BlogPost/listpost.html', {"response":response})