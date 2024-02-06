from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from utils.images.image import get_cropped_image
from .models import MemoryPage


def add_memory_page(request):
    memory_page = MemoryPage.objects.filter(user=request.user).order_by("-id")

    return render(
        request, "users/user_memory.html", context={"memory_page": memory_page}
    )


def edit_memory_page(request, memory_page_id):
    memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)

    return render(request, "users/edit_memory.html", {"memory_page": memory_page})


def create_memory_page(request):
    if request.method == "POST":
        memory_page_avatar = get_cropped_image(request)
        form_data = {
            key: request.POST.get(key) if request.POST.get(key) else None
            for key in [
                "deceased_first_name",
                "deceased_last_name",
                "deceased_middle_name",
                "deceased_birth_date",
                "deceased_death_date",
                "epitaph",
                "biography",
                "awards",
                "family_members",
            ]
            if request.POST.get(key) is not None
        }

        print(form_data)
        print(memory_page_avatar)
        memory_page = MemoryPage.objects.create(
            user=request.user,
            deceased_first_name=form_data["deceased_first_name"],
            deceased_last_name=form_data["deceased_last_name"],
            deceased_middle_name=form_data["deceased_middle_name"],
            deceased_birth_date=form_data["deceased_birth_date"],
            deceased_death_date=form_data["deceased_death_date"],
            epitaph=form_data["epitaph"],
        )
        memory_page.page_avatar = memory_page_avatar
        memory_page.save()
        print(memory_page.get_absolute_url())
        # data = json.loads(request.body)
        # title = data.get('title')
        # content = data.get('content')

        # if not title or not content:
        #     return HttpResponseBadRequest('Title and content are required')

        # MemoryPage.objects.create(
        #     user=request.user,
        #     title=title,
        #     content=content
        # )

        return HttpResponse("Memory page created")
    return render(request, "users/create_memory.html")
