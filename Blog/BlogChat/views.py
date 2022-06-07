from .models import Chat
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Lista chat / list chat
class ChatList(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'BlogChat/global.html'

class ChatCreate(LoginRequiredMixin, CreateView):
    model = Chat
    success_url = reverse_lazy('listchat')
    fields = ['text']
    # Asigna el usuario que envia el mensaje de chat / Assign user that sends the chat message
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
