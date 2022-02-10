from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, View, DeleteView
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from datetime import timedelta
from accounts.models import User
from  django.contrib.auth.hashers import check_password
# from .forms import CommentForm, PasteForm
# from .models import Comment, PasteFile
from .forms import  PasteForm
from .models import PasteFile
import jwt
from django.conf import settings

# https://medium.com/@sebastianojeda/user-authentication-with-django-rest-framework-and-json-web-tokens-747ea4d84b9f
# https://stackoverflow.com/questions/47407536/how-to-store-jwt-token-in-db-with-django-rest-framework
def get_user_for_token(token):
        try:
            data = jwt.decode(token, settings.SECRET_KEY)
        except jwt.DecodeError:
            # if(data==None):
                raise Exception("Invalid token")

        user = User.objects.get(pk=data['id'])
        if(user==None):
            raise Exception("Invalide token")

        else:
            return user    
        # model_cls = get_user_model()

            # try:
                # except (User.DoesNotExist, KeyError):
                #     raise Exception("Invalid token")
                # else:
                #     return user

def generate_jwt_token(username, email,password):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        user = User.objects.filter(email=email, username=username).first()
        if(user==None):
            raise Exception("User doesn't exists")
        encoded = user.password
        flag = check_password(password,encoded)
        if(flag==False):
            raise Exception("wrong Password")
        dt = datetime.now() + timedelta(days=60)

        data = {
        'id': str(user.id),
        }
        
        return jwt.encode(data, settings.SECRET_KEY).decode()
        # token = jwt.encode({
        #     'id': user.pk,
        #     'exp': dt.utcfromtimestamp(dt.timestamp())
        # }, settings.SECRET_KEY, algorithm='HS256')
        # return token

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

class GetUser(View):
    def get(self, request):
        data = json.loads(request.body)
        token = data['token']
        # data = json.loads(request.body)
        # token = request.body
        user = get_user_for_token(token)
        return HttpResponse(json.dumps(user.username), content_type='application/json')

class GetToken(View):
    def get(self, request):
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        # data = json.loads(request.body)
        # token = request.body
        token = generate_jwt_token(username,email,password)
        return HttpResponse(json.dumps(token), content_type='application/json')

# from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class GetUrl(View):
    def post(self, request):
        data = json.loads(request.body)
        title, content = data['title'], data['content']
        if 'custom_url' in data:
            custom_url = data['custom_url']
        if request.method == "POST":
            try:
                pastefile = PasteFile.objects.filter(content=content, title=title).first()
            except:
                pastefile = PasteFile(content=content, title=title, slug=custom_url)
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


class AllPastes(DetailView):
    def get(self, request):
        pastes = PasteFile.objects.all()
        pastes_list = []
        for paste in pastes:
            paste_dict = {}
            paste_dict['title'] = paste.title
            paste_dict['content'] = paste.content
            paste_dict['url'] = request.build_absolute_uri(paste.get_absolute_url())
            paste_dict['date_time'] = paste.date_time.strftime('%Y-%m-%dT%H:%M:%S.%f')
            pastes_list.append(paste_dict)
        return HttpResponse(json.dumps(pastes_list), content_type="application/json")
