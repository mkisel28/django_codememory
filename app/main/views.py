from django.shortcuts import render
from users.models import MemoryPage
# Create your views here.
def index(request):
    avatars = MemoryPage.objects.filter(avatar__isnull=False).order_by('-id')[:5]
    print(avatars)
    return render(request, 'main/index.html', context={"title": "Главная страница", "avatars": avatars})