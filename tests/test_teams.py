from PatrowlManagerSDK.api import PatrowlArsenalApi
import random
import string

api = PatrowlArsenalApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Assets
print(api.get_teams())
print(api.get_team_by_id(1))

rand_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
new_team = api.add_team(name=rand_name, is_active=False)
print(new_team)
print(api.delete_team(new_team['id']))
