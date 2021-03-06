from django.shortcuts import render
from .models import Message
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    message_list = Message.objects.all().order_by('-create_date')
    context = {
        'message_list': message_list,
    }
    return render(request, 'leave_message/index.html', context)

def add(request):
    print('test add func')
    name = request.POST['user']
    content = request.POST['content']
    m = Message(user_name=name, message_text=content, create_date=timezone.now())
    m.save()
    return HttpResponseRedirect(reverse('message:index'))