from django.shortcuts import render

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
#Now, replace the code you have in project/urls.py with the following code. This will handle the chatbox name stated in the browser (http://127.0.0.1:8002/chat/**chatboxname**/).

from django.contrib import admin
from django.urls import path
from app.views import chat_box

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
]