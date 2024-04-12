API_HOST = 'https://api.iot.yandex.net'

API_RESOURCES = {
    'user_info': ('GET', '/v1.0/user/info'),
    'device_state': ('GET', '/v1.0/devices/{device_id}'),
    'device_actions': ('POST', '/v1.0/devices/actions'),
    # 'group_state': ('GET', '/v1.0/groups/{group_id}'),
    # 'group_actions': ('POST', '/v1.0/groups/{group_id}/actions'),
    # 'scenario_actions': ('POST', '/v1.0/scenarios/{scenario_id}/actions'),
    # 'delete_device': ('DELETE', '/v1.0/devices/{device_id}')
}
