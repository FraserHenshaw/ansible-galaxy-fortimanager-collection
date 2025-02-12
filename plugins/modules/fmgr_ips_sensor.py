#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2021 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_ips_sensor
short_description: Configure IPS sensor.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    enable_log:
        description: Enable/Disable logging for task
        required: false
        type: bool
        default: false
    proposed_method:
        description: The overridden method for the underlying Json RPC request
        required: false
        type: str
        choices:
          - update
          - set
          - add
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    ips_sensor:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            block-malicious-url:
                type: str
                description: 'Enable/disable malicious URL blocking.'
                choices:
                    - 'disable'
                    - 'enable'
            comment:
                type: str
                description: 'Comment.'
            entries:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Action taken with traffic in which signatures are detected.'
                        choices:
                            - 'pass'
                            - 'block'
                            - 'reset'
                            - 'default'
                    application:
                        description: no description
                        type: str
                    exempt-ip:
                        description: no description
                        type: list
                        suboptions:
                            dst-ip:
                                type: str
                                description: 'Destination IP address and netmask.'
                            id:
                                type: int
                                description: 'Exempt IP ID.'
                            src-ip:
                                type: str
                                description: 'Source IP address and netmask.'
                    id:
                        type: int
                        description: 'Rule ID in IPS database (0 - 4294967295).'
                    location:
                        description: no description
                        type: str
                    log:
                        type: str
                        description: 'Enable/disable logging of signatures included in filter.'
                        choices:
                            - 'disable'
                            - 'enable'
                    log-attack-context:
                        type: str
                        description: 'Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer.'
                        choices:
                            - 'disable'
                            - 'enable'
                    log-packet:
                        type: str
                        description: 'Enable/disable packet logging. Enable to save the packet that triggers the filter. You can download the packets in pca...'
                        choices:
                            - 'disable'
                            - 'enable'
                    os:
                        description: no description
                        type: str
                    protocol:
                        description: no description
                        type: str
                    quarantine:
                        type: str
                        description: 'Quarantine method.'
                        choices:
                            - 'none'
                            - 'attacker'
                            - 'both'
                            - 'interface'
                    quarantine-expiry:
                        type: str
                        description: 'Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to ...'
                    quarantine-log:
                        type: str
                        description: 'Enable/disable quarantine logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    rate-count:
                        type: int
                        description: 'Count of the rate.'
                    rate-duration:
                        type: int
                        description: 'Duration (sec) of the rate.'
                    rate-mode:
                        type: str
                        description: 'Rate limit mode.'
                        choices:
                            - 'periodical'
                            - 'continuous'
                    rate-track:
                        type: str
                        description: 'Track the packet protocol field.'
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                            - 'dhcp-client-mac'
                            - 'dns-domain'
                    rule:
                        type: str
                        description: 'Identifies the predefined or custom IPS signatures to add to the sensor.'
                    severity:
                        description: no description
                        type: str
                    status:
                        type: str
                        description: 'Status of the signatures included in filter. default enables the filter and only use filters with default status of en...'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'default'
            extended-log:
                type: str
                description: 'Enable/disable extended logging.'
                choices:
                    - 'disable'
                    - 'enable'
            filter:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Action of selected rules.'
                        choices:
                            - 'pass'
                            - 'block'
                            - 'default'
                            - 'reset'
                    application:
                        description: no description
                        type: str
                    location:
                        description: no description
                        type: str
                    log:
                        type: str
                        description: 'Enable/disable logging of selected rules.'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'default'
                    log-packet:
                        type: str
                        description: 'Enable/disable packet logging of selected rules.'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'default'
                    name:
                        type: str
                        description: 'Filter name.'
                    os:
                        description: no description
                        type: str
                    protocol:
                        description: no description
                        type: str
                    quarantine:
                        type: str
                        description: 'Quarantine IP or interface.'
                        choices:
                            - 'none'
                            - 'attacker'
                            - 'both'
                            - 'interface'
                    quarantine-expiry:
                        type: int
                        description: 'Duration of quarantine in minute.'
                    quarantine-log:
                        type: str
                        description: 'Enable/disable logging of selected quarantine.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        description: no description
                        type: str
                    status:
                        type: str
                        description: 'Selected rules status.'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'default'
            name:
                type: str
                description: 'Sensor name.'
            override:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Action of override rule.'
                        choices:
                            - 'pass'
                            - 'block'
                            - 'reset'
                    exempt-ip:
                        description: no description
                        type: list
                        suboptions:
                            dst-ip:
                                type: str
                                description: 'Destination IP address and netmask.'
                            id:
                                type: int
                                description: 'Exempt IP ID.'
                            src-ip:
                                type: str
                                description: 'Source IP address and netmask.'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    log-packet:
                        type: str
                        description: 'Enable/disable packet logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    quarantine:
                        type: str
                        description: 'Quarantine IP or interface.'
                        choices:
                            - 'none'
                            - 'attacker'
                            - 'both'
                            - 'interface'
                    quarantine-expiry:
                        type: int
                        description: 'Duration of quarantine in minute.'
                    quarantine-log:
                        type: str
                        description: 'Enable/disable logging of selected quarantine.'
                        choices:
                            - 'disable'
                            - 'enable'
                    rule-id:
                        type: int
                        description: 'Override rule ID.'
                    status:
                        type: str
                        description: 'Enable/disable status of override rule.'
                        choices:
                            - 'disable'
                            - 'enable'
            replacemsg-group:
                type: str
                description: 'Replacement message group.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure IPS sensor.
      fmgr_ips_sensor:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         ips_sensor:
            block-malicious-url: <value in [disable, enable]>
            comment: <value of string>
            entries:
              -
                  action: <value in [pass, block, reset, ...]>
                  application: <value of string>
                  exempt-ip:
                    -
                        dst-ip: <value of string>
                        id: <value of integer>
                        src-ip: <value of string>
                  id: <value of integer>
                  location: <value of string>
                  log: <value in [disable, enable]>
                  log-attack-context: <value in [disable, enable]>
                  log-packet: <value in [disable, enable]>
                  os: <value of string>
                  protocol: <value of string>
                  quarantine: <value in [none, attacker, both, ...]>
                  quarantine-expiry: <value of string>
                  quarantine-log: <value in [disable, enable]>
                  rate-count: <value of integer>
                  rate-duration: <value of integer>
                  rate-mode: <value in [periodical, continuous]>
                  rate-track: <value in [none, src-ip, dest-ip, ...]>
                  rule: <value of string>
                  severity: <value of string>
                  status: <value in [disable, enable, default]>
            extended-log: <value in [disable, enable]>
            filter:
              -
                  action: <value in [pass, block, default, ...]>
                  application: <value of string>
                  location: <value of string>
                  log: <value in [disable, enable, default]>
                  log-packet: <value in [disable, enable, default]>
                  name: <value of string>
                  os: <value of string>
                  protocol: <value of string>
                  quarantine: <value in [none, attacker, both, ...]>
                  quarantine-expiry: <value of integer>
                  quarantine-log: <value in [disable, enable]>
                  severity: <value of string>
                  status: <value in [disable, enable, default]>
            name: <value of string>
            override:
              -
                  action: <value in [pass, block, reset]>
                  exempt-ip:
                    -
                        dst-ip: <value of string>
                        id: <value of integer>
                        src-ip: <value of string>
                  log: <value in [disable, enable]>
                  log-packet: <value in [disable, enable]>
                  quarantine: <value in [none, attacker, both, ...]>
                  quarantine-expiry: <value of integer>
                  quarantine-log: <value in [disable, enable]>
                  rule-id: <value of integer>
                  status: <value in [disable, enable]>
            replacemsg-group: <value of string>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/ips/sensor',
        '/pm/config/global/obj/ips/sensor'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}',
        '/pm/config/global/obj/ips/sensor/{sensor}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'enable_log': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'proposed_method': {
            'type': 'str',
            'required': False,
            'choices': [
                'set',
                'update',
                'add'
            ]
        },
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'ips_sensor': {
            'required': False,
            'type': 'dict',
            'options': {
                'block-malicious-url': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'comment': {
                    'required': False,
                    'type': 'str'
                },
                'entries': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'pass',
                                'block',
                                'reset',
                                'default'
                            ],
                            'type': 'str'
                        },
                        'application': {
                            'required': False,
                            'type': 'str'
                        },
                        'exempt-ip': {
                            'required': False,
                            'type': 'list',
                            'options': {
                                'dst-ip': {
                                    'required': False,
                                    'type': 'str'
                                },
                                'id': {
                                    'required': False,
                                    'type': 'int'
                                },
                                'src-ip': {
                                    'required': False,
                                    'type': 'str'
                                }
                            }
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'location': {
                            'required': False,
                            'type': 'str'
                        },
                        'log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'log-attack-context': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'log-packet': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'os': {
                            'required': False,
                            'type': 'str'
                        },
                        'protocol': {
                            'required': False,
                            'type': 'str'
                        },
                        'quarantine': {
                            'required': False,
                            'choices': [
                                'none',
                                'attacker',
                                'both',
                                'interface'
                            ],
                            'type': 'str'
                        },
                        'quarantine-expiry': {
                            'required': False,
                            'type': 'str'
                        },
                        'quarantine-log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'rate-count': {
                            'required': False,
                            'type': 'int'
                        },
                        'rate-duration': {
                            'required': False,
                            'type': 'int'
                        },
                        'rate-mode': {
                            'required': False,
                            'choices': [
                                'periodical',
                                'continuous'
                            ],
                            'type': 'str'
                        },
                        'rate-track': {
                            'required': False,
                            'choices': [
                                'none',
                                'src-ip',
                                'dest-ip',
                                'dhcp-client-mac',
                                'dns-domain'
                            ],
                            'type': 'str'
                        },
                        'rule': {
                            'required': False,
                            'type': 'str'
                        },
                        'severity': {
                            'required': False,
                            'type': 'str'
                        },
                        'status': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable',
                                'default'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'extended-log': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'filter': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'pass',
                                'block',
                                'default',
                                'reset'
                            ],
                            'type': 'str'
                        },
                        'application': {
                            'required': False,
                            'type': 'str'
                        },
                        'location': {
                            'required': False,
                            'type': 'str'
                        },
                        'log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable',
                                'default'
                            ],
                            'type': 'str'
                        },
                        'log-packet': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable',
                                'default'
                            ],
                            'type': 'str'
                        },
                        'name': {
                            'required': False,
                            'type': 'str'
                        },
                        'os': {
                            'required': False,
                            'type': 'str'
                        },
                        'protocol': {
                            'required': False,
                            'type': 'str'
                        },
                        'quarantine': {
                            'required': False,
                            'choices': [
                                'none',
                                'attacker',
                                'both',
                                'interface'
                            ],
                            'type': 'str'
                        },
                        'quarantine-expiry': {
                            'required': False,
                            'type': 'int'
                        },
                        'quarantine-log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'severity': {
                            'required': False,
                            'type': 'str'
                        },
                        'status': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable',
                                'default'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'override': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'pass',
                                'block',
                                'reset'
                            ],
                            'type': 'str'
                        },
                        'exempt-ip': {
                            'required': False,
                            'type': 'list',
                            'options': {
                                'dst-ip': {
                                    'required': False,
                                    'type': 'str'
                                },
                                'id': {
                                    'required': False,
                                    'type': 'int'
                                },
                                'src-ip': {
                                    'required': False,
                                    'type': 'str'
                                }
                            }
                        },
                        'log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'log-packet': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'quarantine': {
                            'required': False,
                            'choices': [
                                'none',
                                'attacker',
                                'both',
                                'interface'
                            ],
                            'type': 'str'
                        },
                        'quarantine-expiry': {
                            'required': False,
                            'type': 'int'
                        },
                        'quarantine-log': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'rule-id': {
                            'required': False,
                            'type': 'int'
                        },
                        'status': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'replacemsg-group': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'ips_sensor'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
