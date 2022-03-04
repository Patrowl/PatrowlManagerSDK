from PatrowlManagerSDK.api import PatrowlArsenalApi
import random
import string

api = PatrowlArsenalApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Assets groups
print(api.get_assetgroups())

rand = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
new_assetgroup = api.add_assetgroup(
    name="Test AssetGroup via PatrowlManagerSDK ({})".format(rand), description="n/a", criticity="low",
    assets=[1, 1314], tags=["patrowl", "demo"]
)
print(new_assetgroup)
print(api.delete_assetgroup(new_assetgroup['id']))
