import json
import requests

# payload = '{"end_device_ids":{"device_id":"eui-24e124785d121612","application_ids":{"application_id":"upvdisca-mlsght-em320-th-app"},"dev_eui":"24E124785D121612","join_eui":"0000000000000000","dev_addr":"260BC73B"},"correlation_ids":["gs:uplink:01JHE741F4AH1V73QJ8FHXKM69"],"received_at":"2025-01-12T21:36:04.273514267Z","uplink_message":{"session_key_id":"AZNVYE3g2ofBO/U26X+htQ==","f_port":84,"f_cnt":36783,"frm_payload":"AXVeA2eDAARoeg==","decoded_payload":{"battery":94,"humidity":61,"temperature":13.1},"rx_metadata":[{"gateway_ids":{"gateway_id":"eui-ac1f09fffe0cb0b5","eui":"AC1F09FFFE0CB0B5"},"time":"2025-01-12T21:36:03.281315088Z","timestamp":3158337901,"rssi":-99,"channel_rssi":-99,"snr":10.75,"uplink_token":"CiIKIAoUZXVpLWFjMWYwOWZmZmUwY2IwYjUSCKwfCf/+DLC1EO3SgeILGgsIxOuQvAYQkNKtICDIo+/c9evLAQ==","received_at":"2025-01-12T21:36:04.014752938Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7,"coding_rate":"4/5"}},"frequency":"868100000","timestamp":3158337901,"time":"2025-01-12T21:36:03.281315088Z"},"received_at":"2025-01-12T21:36:04.068670081Z","consumed_airtime":"0.061696s","version_ids":{"brand_id":"milesight-iot","model_id":"em320-th","hardware_version":"V1.0","firmware_version":"1.02","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","ns_id":"EC656E0000000181","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}'
# loaded = json.loads(payload)
# print(loaded)
# print("##")

# print(loaded["uplink_message"]["decoded_payload"])
# a = loaded["uplink_message"]["decoded_payload"]
# print(type(a))

payload = {"temperature":25.2}
url = "http://eu.thingsboard.cloud/api/v1/oety0i8xlql7dqcrxsan/telemetry"
response = requests.post(url, json=payload)
print(response)
print(response.status_code)