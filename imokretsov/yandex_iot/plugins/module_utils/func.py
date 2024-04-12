import requests
from ansible_collections.imokretsov.yandex_iot.plugins.module_utils.vars import API_HOST, API_RESOURCES


def make_api_request(resource_name, token, resource_params=None, json=None):
    if resource_name not in API_RESOURCES:
        raise ValueError(f'Unknown resource: {resource_name}')

    method, path = API_RESOURCES[resource_name]
    url = f'{API_HOST}{path.format(**resource_params)}' if resource_params else f'{API_HOST}{path}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.request(method, url, headers=headers, json=json)

    return response


def make_json(resource_name, device_id, action, instance, value):
    if resource_name == 'device_actions':
        return {
            'devices': [
                {
                    'id': device_id,
                    'actions': [
                        {
                            'type': f'devices.capabilities.{action}',
                            'state': {
                                'instance': instance,
                                'value': value
                            }
                        }
                    ]
                }
            ]
        }
    return None
