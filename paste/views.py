

from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, View, DeleteView
from django.views.decorators.csrf import csrf_exempt
import json


# from .forms import CommentForm, PasteForm
# from .models import Comment, PasteFile
from .forms import  PasteForm
from .models import PasteFile


class Index(CreateView):
    model = PasteFile
    form_class = PasteForm

# @csrf_exempt
from django.utils.decorators import method_decorator 

# @method_decorator(csrf_exempt, name='dispatch')
class Detail(DetailView):
    template_name = "paste/detail.html"
    model = PasteFile

    def get(self, request, slug):
        paste_obj = get_object_or_404(PasteFile, slug=slug)
        context = dict(
            object=paste_obj,
            slug=slug,
        )
        # print(context)
        return render(request, self.template_name, context)

class RawContent(DetailView):
    model = PasteFile

    def get(self, request, slug):
        paste_obj = get_object_or_404(PasteFile, slug=slug)
        context = paste_obj.content
        return HttpResponse(json.dumps(context), content_type='application/json')


class find_url(DetailView):
    # model = PasteFile
    def get(self, request, content, title):
        # slug = slug
        get_url = get_object_or_404(PasteFile, content=content, title=title)
        print(get_url)
        return HttpResponse(json.dumps(get_url.get_absolute_url()), content_type='application/json')
        # return HttpResponse(json.dumps(get_url.slug), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class CreateNewPaste(View):
    def post(self, request):
        data = json.loads(request.body)
        title, content = data['title'], data['content']
        pastefile = PasteFile(content=content, title=title)
        pastefile.save()
        return HttpResponse(json.dumps(pastefile.get_absolute_url()), content_type='application/json')


# @method_decorator(csrf_exempt, name='dispatch')
class GetRawPaste(View):
    def get(self, request):
        data = json.loads(request.body)
        slug = data['slug']
        pastefile = PasteFile.objects.get(slug=slug)
        return HttpResponse(json.dumps(pastefile.content), content_type='application/json')


# from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class GetUrl(View):
    def post(self, request):
        data = json.loads(request.body)
        title, content = data['title'], data['content']
        if request.method == "POST":
            try:
                pastefile = PasteFile.objects.filter(content=content, title=title).first()
            except:
                pastefile = PasteFile(content=content, title=title)
                pastefile.save()
            
            return HttpResponse(pastefile.get_absolute_url())

@method_decorator(csrf_exempt, name='dispatch')
# @action(methods=['delete'], detail=False)
class deleteUrl(View):
     def get(self, request):
        data = json.loads(request.body)
        slug = data['slug']
        # pastefile = PasteFile.objects.filter(slug=slug).first()
        record = PasteFile.objects.get(slug=slug)
        record.delete()
        # success_url = reverse_lazy(pastefile)  
        response = json.dumps({'message': "deleted"})
        return HttpResponse(response, content_type='application/json')
