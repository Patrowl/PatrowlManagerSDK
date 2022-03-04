from PatrowlManagerSDK.api import PatrowlArsenalApi

api = PatrowlArsenalApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Alerting rules
print(api.get_alerting_rules())
print(api.get_alerting_rule(3))
# print(api.delete_alerting_rule(1))
print(api.duplicate_alerting_rule(3))