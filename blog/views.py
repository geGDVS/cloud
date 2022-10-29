from django.shortcuts import render
import secrets, os
def begin(request):
    if request.method == "POST":
        File = request.FILES.get("myfile", None)
        save = request.POST.get("save")
        if File is None:
            return render(request, 'fail.html')
        else:
          if str(os.getcwd()) == '/home/runner/cloud':
            os.chdir('file')
          elif str(os.getcwd()) != '/home/runner/cloud/file':
            os.chdir(os.path.pardir)
          if save:
            dir = secrets.token_urlsafe(16)
            os.mkdir(dir)
            os.chdir(dir)
            os.mknod(File.name)
            with open("%s" % File, 'wb+') as f:
              for chunk in File.chunks():
                  f.write(chunk)
            return render(request, 'success.html', {'save':True, 'url': dir, 'name': File.name})
          else:
            name = secrets.token_urlsafe(32)
            ext = File.name.split('.')[-1]
            fName = name + '.' + ext
            os.mknod(fName)
            with open("%s" % fName, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            return render(request, 'success.html', {'save':False, 'url': fName})
    else:
        return render(request, 'upload.html')

  