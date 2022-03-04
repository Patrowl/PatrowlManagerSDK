from PatrowlManagerSDK.api import PatrowlManagerApi


api = PatrowlManagerApi(
    url='http://localhost:8004',
    auth_token='78854fc93308b0cc49542d838e220aabb5351501'
)

# Findings
print(api.get_findings())
print(api.get_findings(status="new"))
print(api.get_findings(title="Nmap", severity="info"))
print(api.get_findings(severity="high", limit=1))
print(api.get_finding(1))
print(api.ack_finding(1))
