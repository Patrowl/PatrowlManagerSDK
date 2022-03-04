from PatrowlManagerSDK.api import PatrowlArsenalApi
import time


api = PatrowlArsenalApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Scan definitions
print(api.add_scan_definition(
    engine_policy=1,
    engine_id=1,
    title="PatrowlManagerSDK single test scan ({})".format(time.time()),
    description="PatrowlManagerSDK test scan",
    scan_type="single",
    every=None,
    period=None,
    scheduled_at=None,
    start_scan="now",
    assets=[1, 1284],
    assetgroups=None
    # assetgroups=[7]
))
print(api.get_scan_definitions())
print(api.get_scan_definition_by_id(1))

# Scans
print(api.get_scan_by_id(1))
print(api.get_scans(limit=10))
print(api.get_scans(limit=10, status="finished"))
