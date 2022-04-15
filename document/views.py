from django.shortcuts import render, redirect

# Create your views here.
from .models import Document, Priority


def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title').strip()
        content = request.POST.get('content', '').strip()
        priority = request.POST.get('priority').strip()

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.priority = Priority.objects.get(id=priority)
            document.save()

            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content, priority=Priority.objects.get(id=priority))

            return redirect('/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    priorities = Priority.objects.all()
    context = {
        'docid': docid,
        'documents': documents,
        'document': document,
        'priorities': priorities
    }

    return render(request, 'editor.html', context)


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')
