from django.shortcuts import redirect, render

from video.models import Chat



def index(request):
    
    if request.method == 'POST':
        room = request.POST.get('room')
        get_room = Chat.objects.filter(room=room)
        if get_room:
            get_room = get_room[0]
            number = get_room.allowed_users

            if number < 2:
                number = 2
                return redirect(f'/video/{room}/join/')
        else: 
            create = Chat.objects.create(room=room, allowed_users=1)
            if create:
                return redirect(f'/video/{room}/created/')

    return render(request, 'index.html')


def video(request, room, created):
    return render(request, 'video.html', {'room': room, 'created': created})