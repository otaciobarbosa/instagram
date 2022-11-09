from instagram_private_api import Client, ClientCompatPatch

user_name = "USUARIO_INSTAGRAM"
password = "USENHA_INSTAGRAM"
api = Client(user_name, password)

results = api.feed_timeline()
items = [item for item in results.get("feed_items", []) if item.get("media_or_ad")]
for item in items:
    ClientCompatPatch.media(item["media_or_ad"])
    print(item["media_or_ad"]["code"])