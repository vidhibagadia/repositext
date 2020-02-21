from django.shortcuts import render
from django.views import View
from apps.repo.models import Folder


class IndexView(View):
    def get(self, request):
        root_folder = Folder.objects.get(name='ROOT')
        child_folders = Folder.objects.filter(parent=root_folder)
        return render(
            request,
            'docweb/index.html',
            {
                'root_folder': root_folder,
                'child_folders': child_folders,
            }
        )
