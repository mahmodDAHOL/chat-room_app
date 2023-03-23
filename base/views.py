from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # icontains represent type of filter (i) for case insensetive and contain for match with part of the string
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | # get the attr (name) of object (topic) by __
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ) 
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {"rooms": rooms, 'topics': topics, 'room_count': room_count}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}

    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})

