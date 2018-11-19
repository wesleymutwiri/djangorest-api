from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
import json 
from django.core.serializers import serialize

# Create your views here.
# def detail_view(request):
	# return HttpResponse(get_template(), render())

# def update_model_detail_view(request):
# 	data = {
# 		"count":1000,
# 		"content": "Some new Content  "
# 	}
# 	return JsonResponse(data)

class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
		"count":1000,
		"content": "Some new Content  "
		}
		return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
		"count":1000,
		"content": "Some new Content  "
		}
		return self.render_to_json_response(data)


class SerializedDetailView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		data = serialize("json", [obj,], fields = ('user', 'content'))
		print(data)
		json_data = data 
		# data = {
		# "user": obj.user.username,
		# "content": obj.content
		# }
		# json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all()
		data = serialize("json", qs, fields = ('user', 'content'))
		print(data)
		# data = {
		# "user": obj.user.username,
		# "content": obj.content
		# }
		# json_data = json.dumps(data)
		json_data = data
		return HttpResponse(json_data, content_type='application/json')