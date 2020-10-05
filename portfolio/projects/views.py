from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):
    # Get all objects
    projects = Project.objects.all()
    # Create context dict
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_details(request, id):
    # query id of project
    project = Project.objects.get(pk=id)

    # Create cotext dict
    context = {"project": project}

    return render(request, "project_details.html", context)
