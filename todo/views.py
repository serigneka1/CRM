from django.shortcuts import render

# Create your views here.
todo=["aller à Paris", "Visiter Strasbourg", "Aller voir des amis à Toulouse"]
def todo_list(request):

    return render(request, "todo_list.html", {"todos": todo})