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
module: fmgr_firewall_mmsprofile_notification
short_description: Notification configuration.
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
    mms-profile:
        description: the parameter (mms-profile) in requested url
        type: str
        required: true
    firewall_mmsprofile_notification:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            alert-int:
                type: int
                description: 'Alert notification send interval.'
            alert-int-mode:
                type: str
                description: 'Alert notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            alert-src-msisdn:
                type: str
                description: 'Specify from address for alert messages.'
            alert-status:
                type: str
                description: 'Alert notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            bword-int:
                type: int
                description: 'Banned word notification send interval.'
            bword-int-mode:
                type: str
                description: 'Banned word notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            bword-status:
                type: str
                description: 'Banned word notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            carrier-endpoint-bwl-int:
                type: int
                description: 'Carrier end point black/white list notification send interval.'
            carrier-endpoint-bwl-int-mode:
                type: str
                description: 'Carrier end point black/white list notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            carrier-endpoint-bwl-status:
                type: str
                description: 'Carrier end point black/white list notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            days-allowed:
                description: no description
                type: list
                choices:
                 - sunday
                 - monday
                 - tuesday
                 - wednesday
                 - thursday
                 - friday
                 - saturday
            detect-server:
                type: str
                description: 'Enable/disable automatic server address determination.'
                choices:
                    - 'disable'
                    - 'enable'
            dupe-int:
                type: int
                description: 'Duplicate notification send interval.'
            dupe-int-mode:
                type: str
                description: 'Duplicate notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            dupe-status:
                type: str
                description: 'Duplicate notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            file-block-int:
                type: int
                description: 'File block notification send interval.'
            file-block-int-mode:
                type: str
                description: 'File block notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            file-block-status:
                type: str
                description: 'File block notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            flood-int:
                type: int
                description: 'Flood notification send interval.'
            flood-int-mode:
                type: str
                description: 'Flood notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            flood-status:
                type: str
                description: 'Flood notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            from-in-header:
                type: str
                description: 'Enable/disable insertion of from address in HTTP header.'
                choices:
                    - 'disable'
                    - 'enable'
            mms-checksum-int:
                type: int
                description: 'MMS checksum notification send interval.'
            mms-checksum-int-mode:
                type: str
                description: 'MMS checksum notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            mms-checksum-status:
                type: str
                description: 'MMS checksum notification status.'
                choices:
                    - 'disable'
                    - 'enable'
            mmsc-hostname:
                type: str
                description: 'Host name or IP address of the MMSC.'
            mmsc-password:
                description: no description
                type: str
            mmsc-port:
                type: int
                description: 'Port used on the MMSC for sending MMS messages (1 - 65535).'
            mmsc-url:
                type: str
                description: 'URL used on the MMSC for sending MMS messages.'
            mmsc-username:
                type: str
                description: 'User name required for authentication with the MMSC.'
            msg-protocol:
                type: str
                description: 'Protocol to use for sending notification messages.'
                choices:
                    - 'mm1'
                    - 'mm3'
                    - 'mm4'
                    - 'mm7'
            msg-type:
                type: str
                description: 'MM7 message type.'
                choices:
                    - 'submit-req'
                    - 'deliver-req'
            protocol:
                type: str
                description: 'Protocol.'
            rate-limit:
                type: int
                description: 'Rate limit for sending notification messages (0 - 250).'
            tod-window-duration:
                type: str
                description: 'Time of day window duration.'
            tod-window-end:
                type: str
                description: 'Obsolete.'
            tod-window-start:
                type: str
                description: 'Time of day window start.'
            user-domain:
                type: str
                description: 'Domain name to which the user addresses belong.'
            vas-id:
                type: str
                description: 'VAS identifier.'
            vasp-id:
                type: str
                description: 'VASP identifier.'
            virus-int:
                type: int
                description: 'Virus notification send interval.'
            virus-int-mode:
                type: str
                description: 'Virus notification interval mode.'
                choices:
                    - 'hours'
                    - 'minutes'
            virus-status:
                type: str
                description: 'Virus notification status.'
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
    - name: Notification configuration.
      fmgr_firewall_mmsprofile_notification:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         mms-profile: <your own value>
         firewall_mmsprofile_notification:
            alert-int: <value of integer>
            alert-int-mode: <value in [hours, minutes]>
            alert-src-msisdn: <value of string>
            alert-status: <value in [disable, enable]>
            bword-int: <value of integer>
            bword-int-mode: <value in [hours, minutes]>
            bword-status: <value in [disable, enable]>
            carrier-endpoint-bwl-int: <value of integer>
            carrier-endpoint-bwl-int-mode: <value in [hours, minutes]>
            carrier-endpoint-bwl-status: <value in [disable, enable]>
            days-allowed:
              - sunday
              - monday
              - tuesday
              - wednesday
              - thursday
              - friday
              - saturday
            detect-server: <value in [disable, enable]>
            dupe-int: <value of integer>
            dupe-int-mode: <value in [hours, minutes]>
            dupe-status: <value in [disable, enable]>
            file-block-int: <value of integer>
            file-block-int-mode: <value in [hours, minutes]>
            file-block-status: <value in [disable, enable]>
            flood-int: <value of integer>
            flood-int-mode: <value in [hours, minutes]>
            flood-status: <value in [disable, enable]>
            from-in-header: <value in [disable, enable]>
            mms-checksum-int: <value of integer>
            mms-checksum-int-mode: <value in [hours, minutes]>
            mms-checksum-status: <value in [disable, enable]>
            mmsc-hostname: <value of string>
            mmsc-password: <value of string>
            mmsc-port: <value of integer>
            mmsc-url: <value of string>
            mmsc-username: <value of string>
            msg-protocol: <value in [mm1, mm3, mm4, ...]>
            msg-type: <value in [submit-req, deliver-req]>
            protocol: <value of string>
            rate-limit: <value of integer>
            tod-window-duration: <value of string>
            tod-window-end: <value of string>
            tod-window-start: <value of string>
            user-domain: <value of string>
            vas-id: <value of string>
            vasp-id: <value of string>
            virus-int: <value of integer>
            virus-int-mode: <value in [hours, minutes]>
            virus-status: <value in [disable, enable]>

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
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification/{notification}',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification/{notification}'
    ]

    url_params = ['adom', 'mms-profile']
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
        'mms-profile': {
            'required': True,
            'type': 'str'
        },
        'firewall_mmsprofile_notification': {
            'required': False,
            'type': 'dict',
            'options': {
                'alert-int': {
                    'required': False,
                    'type': 'int'
                },
                'alert-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'alert-src-msisdn': {
                    'required': False,
                    'type': 'str'
                },
                'alert-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'bword-int': {
                    'required': False,
                    'type': 'int'
                },
                'bword-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'bword-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'carrier-endpoint-bwl-int': {
                    'required': False,
                    'type': 'int'
                },
                'carrier-endpoint-bwl-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'carrier-endpoint-bwl-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'days-allowed': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'sunday',
                        'monday',
                        'tuesday',
                        'wednesday',
                        'thursday',
                        'friday',
                        'saturday'
                    ]
                },
                'detect-server': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'dupe-int': {
                    'required': False,
                    'type': 'int'
                },
                'dupe-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'dupe-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'file-block-int': {
                    'required': False,
                    'type': 'int'
                },
                'file-block-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'file-block-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'flood-int': {
                    'required': False,
                    'type': 'int'
                },
                'flood-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'flood-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'from-in-header': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mms-checksum-int': {
                    'required': False,
                    'type': 'int'
                },
                'mms-checksum-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'mms-checksum-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mmsc-hostname': {
                    'required': False,
                    'type': 'str'
                },
                'mmsc-password': {
                    'required': False,
                    'type': 'str'
                },
                'mmsc-port': {
                    'required': False,
                    'type': 'int'
                },
                'mmsc-url': {
                    'required': False,
                    'type': 'str'
                },
                'mmsc-username': {
                    'required': False,
                    'type': 'str'
                },
                'msg-protocol': {
                    'required': False,
                    'choices': [
                        'mm1',
                        'mm3',
                        'mm4',
                        'mm7'
                    ],
                    'type': 'str'
                },
                'msg-type': {
                    'required': False,
                    'choices': [
                        'submit-req',
                        'deliver-req'
                    ],
                    'type': 'str'
                },
                'protocol': {
                    'required': False,
                    'type': 'str'
                },
                'rate-limit': {
                    'required': False,
                    'type': 'int'
                },
                'tod-window-duration': {
                    'required': False,
                    'type': 'str'
                },
                'tod-window-end': {
                    'required': False,
                    'type': 'str'
                },
                'tod-window-start': {
                    'required': False,
                    'type': 'str'
                },
                'user-domain': {
                    'required': False,
                    'type': 'str'
                },
                'vas-id': {
                    'required': False,
                    'type': 'str'
                },
                'vasp-id': {
                    'required': False,
                    'type': 'str'
                },
                'virus-int': {
                    'required': False,
                    'type': 'int'
                },
                'virus-int-mode': {
                    'required': False,
                    'choices': [
                        'hours',
                        'minutes'
                    ],
                    'type': 'str'
                },
                'virus-status': {
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
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_mmsprofile_notification'),
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
