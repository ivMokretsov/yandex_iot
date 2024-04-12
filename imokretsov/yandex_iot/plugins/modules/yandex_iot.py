#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.imokretsov.yandex_iot.plugins.module_utils.func import make_api_request, make_json


def main():
    module = AnsibleModule(
        argument_spec=dict(
            resource_name=dict(type='str', required=True),
            token=dict(type='str', required=True),
            resource_params=dict(type='dict', required=False),
            device_id=dict(type='str', required=False),
            action=dict(type='str', required=False),
            instance=dict(type='str', required=False),
            value=dict(type='raw', required=False)
        ),
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(changed=False)

    json_data = make_json(
        resource_name=module.params['resource_name'],
        device_id=module.params['device_id'],
        action=module.params['action'],
        instance=module.params['instance'],
        value=module.params['value']
    )

    response = make_api_request(
        resource_name=module.params['resource_name'],
        token=module.params['token'],
        resource_params=module.params['resource_params'],
        json=json_data
    )

    if response.status_code == 200:
        module.exit_json(changed=True, response=response.json())
    else:
        module.fail_json(
            msg='API request failed',
            status=response.status_code,
            response=response.text
        )


if __name__ == '__main__':
    main()
