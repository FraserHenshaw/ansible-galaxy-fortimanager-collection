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
module: fmgr_devprof_system_global
short_description: Configure global attributes.
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
    devprof:
        description: the parameter (devprof) in requested url
        type: str
        required: true
    devprof_system_global:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            admin-https-redirect:
                type: str
                description: 'Enable/disable redirection of HTTP administration access to HTTPS.'
                choices:
                    - 'disable'
                    - 'enable'
            admin-port:
                type: int
                description: 'Administrative access port for HTTP. (1 - 65535, default = 80).'
            admin-scp:
                type: str
                description: 'Enable/disable using SCP to download the system configuration. You can use SCP as an alternative method for backing up the con...'
                choices:
                    - 'disable'
                    - 'enable'
            admin-sport:
                type: int
                description: 'Administrative access port for HTTPS. (1 - 65535, default = 443).'
            admin-ssh-port:
                type: int
                description: 'Administrative access port for SSH. (1 - 65535, default = 22).'
            admin-ssh-v1:
                type: str
                description: 'Enable/disable SSH v1 compatibility.'
                choices:
                    - 'disable'
                    - 'enable'
            admin-telnet-port:
                type: int
                description: 'Administrative access port for TELNET. (1 - 65535, default = 23).'
            admintimeout:
                type: int
                description: 'Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). A shorter idle time...'
            gui-ipv6:
                type: str
                description: 'Enable/disable IPv6 settings on the GUI.'
                choices:
                    - 'disable'
                    - 'enable'
            gui-lines-per-page:
                type: int
                description: 'Number of lines to display per page for web administration.'
            gui-theme:
                type: str
                description: 'Color scheme for the administration GUI.'
                choices:
                    - 'blue'
                    - 'green'
                    - 'melongene'
                    - 'red'
                    - 'mariner'
            language:
                type: str
                description: 'GUI display language.'
                choices:
                    - 'english'
                    - 'simch'
                    - 'japanese'
                    - 'korean'
                    - 'spanish'
                    - 'trach'
                    - 'french'
                    - 'portuguese'
            switch-controller:
                type: str
                description: 'Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.'
                choices:
                    - 'disable'
                    - 'enable'

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
    - name: Configure global attributes.
      fmgr_devprof_system_global:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_system_global:
            admin-https-redirect: <value in [disable, enable]>
            admin-port: <value of integer>
            admin-scp: <value in [disable, enable]>
            admin-sport: <value of integer>
            admin-ssh-port: <value of integer>
            admin-ssh-v1: <value in [disable, enable]>
            admin-telnet-port: <value of integer>
            admintimeout: <value of integer>
            gui-ipv6: <value in [disable, enable]>
            gui-lines-per-page: <value of integer>
            gui-theme: <value in [blue, green, melongene, ...]>
            language: <value in [english, simch, japanese, ...]>
            switch-controller: <value in [disable, enable]>

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
        '/pm/config/adom/{adom}/devprof/{devprof}/system/global'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/system/global/{global}'
    ]

    url_params = ['adom', 'devprof']
    module_primary_key = None
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
        'adom': {
            'required': True,
            'type': 'str'
        },
        'devprof': {
            'required': True,
            'type': 'str'
        },
        'devprof_system_global': {
            'required': False,
            'type': 'dict',
            'options': {
                'admin-https-redirect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'admin-port': {
                    'required': False,
                    'type': 'int'
                },
                'admin-scp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'admin-sport': {
                    'required': False,
                    'type': 'int'
                },
                'admin-ssh-port': {
                    'required': False,
                    'type': 'int'
                },
                'admin-ssh-v1': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'admin-telnet-port': {
                    'required': False,
                    'type': 'int'
                },
                'admintimeout': {
                    'required': False,
                    'type': 'int'
                },
                'gui-ipv6': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'gui-lines-per-page': {
                    'required': False,
                    'type': 'int'
                },
                'gui-theme': {
                    'required': False,
                    'choices': [
                        'blue',
                        'green',
                        'melongene',
                        'red',
                        'mariner'
                    ],
                    'type': 'str'
                },
                'language': {
                    'required': False,
                    'choices': [
                        'english',
                        'simch',
                        'japanese',
                        'korean',
                        'spanish',
                        'trach',
                        'french',
                        'portuguese'
                    ],
                    'type': 'str'
                },
                'switch-controller': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'devprof_system_global'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_partial_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
