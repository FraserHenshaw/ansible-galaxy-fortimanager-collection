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
module: fmgr_system_replacemsggroup_mm7
short_description: Replacement message table entries.
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
    replacemsg-group:
        description: the parameter (replacemsg-group) in requested url
        type: str
        required: true
    system_replacemsggroup_mm7:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            add-smil:
                type: str
                description: 'add message encapsulation'
                choices:
                    - 'disable'
                    - 'enable'
            addr-type:
                type: str
                description: 'from address type'
                choices:
                    - 'rfc2822-addr'
                    - 'number'
                    - 'short-code'
            allow-content-adaptation:
                type: str
                description: 'allow content adaptations'
                choices:
                    - 'disable'
                    - 'enable'
            charset:
                type: str
                description: 'character encoding used for replacement message'
                choices:
                    - 'us-ascii'
                    - 'utf-8'
            class:
                type: str
                description: 'message class'
                choices:
                    - 'personal'
                    - 'advertisement'
                    - 'informational'
                    - 'auto'
                    - 'not-included'
            format:
                type: str
                description: 'Format flag.'
                choices:
                    - 'none'
                    - 'text'
                    - 'html'
                    - 'wml'
            from:
                type: str
                description: 'from address'
            from-sender:
                type: str
                description: 'notification message sent from recipient'
                choices:
                    - 'disable'
                    - 'enable'
            header:
                type: str
                description: 'Header flag.'
                choices:
                    - 'none'
                    - 'http'
                    - '8bit'
            image:
                type: str
                description: 'Message string.'
            message:
                type: str
                description: 'message text'
            msg-type:
                type: str
                description: 'Message type.'
            priority:
                type: str
                description: 'message priority'
                choices:
                    - 'low'
                    - 'normal'
                    - 'high'
                    - 'not-included'
            rsp-status:
                type: str
                description: 'response status'
                choices:
                    - 'success'
                    - 'partial-success'
                    - 'client-err'
                    - 'oper-restrict'
                    - 'addr-err'
                    - 'addr-not-found'
                    - 'content-refused'
                    - 'msg-id-not-found'
                    - 'link-id-not-found'
                    - 'msg-fmt-corrupt'
                    - 'app-id-not-found'
                    - 'repl-app-id-not-found'
                    - 'srv-err'
                    - 'not-possible'
                    - 'msg-rejected'
                    - 'multiple-addr-not-supp'
                    - 'app-addr-not-supp'
                    - 'gen-service-err'
                    - 'improper-ident'
                    - 'unsupp-ver'
                    - 'unsupp-oper'
                    - 'validation-err'
                    - 'service-err'
                    - 'service-unavail'
                    - 'service-denied'
                    - 'app-denied'
            smil-part:
                type: str
                description: 'message encapsulation text'
            subject:
                type: str
                description: 'subject text string'

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
    - name: Replacement message table entries.
      fmgr_system_replacemsggroup_mm7:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         replacemsg-group: <your own value>
         state: <value in [present, absent]>
         system_replacemsggroup_mm7:
            add-smil: <value in [disable, enable]>
            addr-type: <value in [rfc2822-addr, number, short-code]>
            allow-content-adaptation: <value in [disable, enable]>
            charset: <value in [us-ascii, utf-8]>
            class: <value in [personal, advertisement, informational, ...]>
            format: <value in [none, text, html, ...]>
            from: <value of string>
            from-sender: <value in [disable, enable]>
            header: <value in [none, http, 8bit]>
            image: <value of string>
            message: <value of string>
            msg-type: <value of string>
            priority: <value in [low, normal, high, ...]>
            rsp-status: <value in [success, partial-success, client-err, ...]>
            smil-part: <value of string>
            subject: <value of string>

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
        '/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7',
        '/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm7'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7/{mm7}',
        '/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm7/{mm7}'
    ]

    url_params = ['adom', 'replacemsg-group']
    module_primary_key = 'msg-type'
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
        'replacemsg-group': {
            'required': True,
            'type': 'str'
        },
        'system_replacemsggroup_mm7': {
            'required': False,
            'type': 'dict',
            'options': {
                'add-smil': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'addr-type': {
                    'required': False,
                    'choices': [
                        'rfc2822-addr',
                        'number',
                        'short-code'
                    ],
                    'type': 'str'
                },
                'allow-content-adaptation': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'charset': {
                    'required': False,
                    'choices': [
                        'us-ascii',
                        'utf-8'
                    ],
                    'type': 'str'
                },
                'class': {
                    'required': False,
                    'choices': [
                        'personal',
                        'advertisement',
                        'informational',
                        'auto',
                        'not-included'
                    ],
                    'type': 'str'
                },
                'format': {
                    'required': False,
                    'choices': [
                        'none',
                        'text',
                        'html',
                        'wml'
                    ],
                    'type': 'str'
                },
                'from': {
                    'required': False,
                    'type': 'str'
                },
                'from-sender': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'header': {
                    'required': False,
                    'choices': [
                        'none',
                        'http',
                        '8bit'
                    ],
                    'type': 'str'
                },
                'image': {
                    'required': False,
                    'type': 'str'
                },
                'message': {
                    'required': False,
                    'type': 'str'
                },
                'msg-type': {
                    'required': True,
                    'type': 'str'
                },
                'priority': {
                    'required': False,
                    'choices': [
                        'low',
                        'normal',
                        'high',
                        'not-included'
                    ],
                    'type': 'str'
                },
                'rsp-status': {
                    'required': False,
                    'choices': [
                        'success',
                        'partial-success',
                        'client-err',
                        'oper-restrict',
                        'addr-err',
                        'addr-not-found',
                        'content-refused',
                        'msg-id-not-found',
                        'link-id-not-found',
                        'msg-fmt-corrupt',
                        'app-id-not-found',
                        'repl-app-id-not-found',
                        'srv-err',
                        'not-possible',
                        'msg-rejected',
                        'multiple-addr-not-supp',
                        'app-addr-not-supp',
                        'gen-service-err',
                        'improper-ident',
                        'unsupp-ver',
                        'unsupp-oper',
                        'validation-err',
                        'service-err',
                        'service-unavail',
                        'service-denied',
                        'app-denied'
                    ],
                    'type': 'str'
                },
                'smil-part': {
                    'required': False,
                    'type': 'str'
                },
                'subject': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_replacemsggroup_mm7'),
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
