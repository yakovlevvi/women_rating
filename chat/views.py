from django.shortcuts import render

 
def chat_page(request, *args, **kwargs):
    context = {}
    return render(request, "chat.html", context)
