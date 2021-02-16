import math
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    end_page = math.ceil(paginator.count/10)
    try:
        rooms = paginator.page(int(page))
        if int(page) % 5 == 0:
            start = (int(int(page) / 5) * 5) - 5
            end = int(page)
            paginator_range = paginator.page_range[start:end]
        else:
            start = (int(int(page) / 5) * 5)
            end = (math.ceil(int(page) / 5) * 5)
            paginator_range = paginator.page_range[start:end]
    except EmptyPage:
        return redirect("/")

    return render(request, "rooms/home.html", {"page": rooms, "paginator_range":paginator_range})