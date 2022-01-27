from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse

from paste.models import PasteFile
from paste.api.serializers import PasteFileSerializer

@api_view(['GET'])
def api_detail_paste_view(request):
    data = json.loads(request.body)
    slug = data['slug']
    pastefile = PasteFile.objects.get(slug=slug)
    serializer = PasteFileSerializer(pastefile)
    return Response(serializer.data)
    # return HttpResponse(json.dumps(pastefile.content), content_type='application/json')

