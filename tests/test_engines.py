from PatrowlManagerSDK.api import PatrowlManagerApi

api = PatrowlManagerApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Engine instances
print(api.get_engines())
print(api.get_engine_by_id(1))
print(api.get_engine_instances())
print(api.get_engine_instance_by_id(1))

# Engine policies
print(api.get_engine_policies())
print(api.get_engine_policy(1))