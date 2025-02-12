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
module: fmgr_system_interface
short_description: Interface configuration.
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
    system_interface:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            alias:
                type: str
                description: 'Alias.'
            allowaccess:
                description: no description
                type: list
                choices:
                 - ping
                 - https
                 - ssh
                 - snmp
                 - http
                 - webservice
                 - https-logging
            description:
                type: str
                description: 'Description.'
            ip:
                type: str
                default: '0.0.0.0 0.0.0.0'
                description: 'IP address of interface.'
            ipv6:
                description: no description
                type: dict
                required: false
                suboptions:
                    ip6-address:
                        type: str
                        default: '::/0'
                        description: 'IPv6 address/prefix of interface.'
                    ip6-allowaccess:
                        description: no description
                        type: list
                        choices:
                         - ping
                         - https
                         - ssh
                         - snmp
                         - http
                         - webservice
                         - https-logging
                    ip6-autoconf:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable address auto config (SLAAC).'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
            mtu:
                type: int
                default: 1500
                description: 'Maximum transportation unit(68 - 9000).'
            name:
                type: str
                description: 'Interface name.'
            serviceaccess:
                description: no description
                type: list
                choices:
                 - fgtupdates
                 - fclupdates
                 - webfilter-antispam
            speed:
                type: str
                default: 'auto'
                description:
                 - 'Speed.'
                 - 'auto - Auto adjust speed.'
                 - '10full - 10M full-duplex.'
                 - '10half - 10M half-duplex.'
                 - '100full - 100M full-duplex.'
                 - '100half - 100M half-duplex.'
                 - '1000full - 1000M full-duplex.'
                 - '10000full - 10000M full-duplex.'
                choices:
                    - 'auto'
                    - '10full'
                    - '10half'
                    - '100full'
                    - '100half'
                    - '1000full'
                    - '10000full'
            status:
                type: str
                default: 'up'
                description:
                 - 'Interface status.'
                 - 'down - Interface down.'
                 - 'up - Interface up.'
                choices:
                    - 'down'
                    - 'up'

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
    - name: Interface configuration.
      fmgr_system_interface:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_interface:
            alias: <value of string>
            allowaccess:
              - ping
              - https
              - ssh
              - snmp
              - http
              - webservice
              - https-logging
            description: <value of string>
            ip: <value of string>
            ipv6:
               ip6-address: <value of string>
               ip6-allowaccess:
                 - ping
                 - https
                 - ssh
                 - snmp
                 - http
                 - webservice
                 - https-logging
               ip6-autoconf: <value in [disable, enable]>
            mtu: <value of integer>
            name: <value of string>
            serviceaccess:
              - fgtupdates
              - fclupdates
              - webfilter-antispam
            speed: <value in [auto, 10full, 10half, ...]>
            status: <value in [down, up]>

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
        '/cli/global/system/interface'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/interface/{interface}'
    ]

    url_params = []
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
        'system_interface': {
            'required': False,
            'type': 'dict',
            'options': {
                'alias': {
                    'required': False,
                    'type': 'str'
                },
                'allowaccess': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'ping',
                        'https',
                        'ssh',
                        'snmp',
                        'http',
                        'webservice',
                        'https-logging'
                    ]
                },
                'description': {
                    'required': False,
                    'type': 'str'
                },
                'ip': {
                    'required': False,
                    'type': 'str'
                },
                'ipv6': {
                    'required': False,
                    'type': 'dict',
                    'options': {
                        'ip6-address': {
                            'required': False,
                            'type': 'str'
                        },
                        'ip6-allowaccess': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'ping',
                                'https',
                                'ssh',
                                'snmp',
                                'http',
                                'webservice',
                                'https-logging'
                            ]
                        },
                        'ip6-autoconf': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'mtu': {
                    'required': False,
                    'type': 'int'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'serviceaccess': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'fgtupdates',
                        'fclupdates',
                        'webfilter-antispam'
                    ]
                },
                'speed': {
                    'required': False,
                    'choices': [
                        'auto',
                        '10full',
                        '10half',
                        '100full',
                        '100half',
                        '1000full',
                        '10000full'
                    ],
                    'type': 'str'
                },
                'status': {
                    'required': False,
                    'choices': [
                        'down',
                        'up'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_interface'),
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
