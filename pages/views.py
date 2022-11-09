from django.http import HttpResponse
from instagram_private_api import Client, ClientCompatPatch

user_name = "USUARIO_INSTAGRAM"
password = "SENHA_INSTAGRAM"
api = Client(user_name, password)

results = api.feed_timeline()
items = [item for item in results.get("feed_items", []) if item.get("media_or_ad")]

def homePageView(request):
    return HttpResponse(items)