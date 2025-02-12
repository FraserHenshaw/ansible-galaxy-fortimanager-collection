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
module: fmgr_spamfilter_profile
short_description: Configure AntiSpam profiles.
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
    spamfilter_profile:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            comment:
                type: str
                description: 'Comment.'
            external:
                type: str
                description: 'Enable/disable external Email inspection.'
                choices:
                    - 'disable'
                    - 'enable'
            flow-based:
                type: str
                description: 'Enable/disable flow-based spam filtering.'
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: 'Profile name.'
            options:
                description: no description
                type: list
                choices:
                 - bannedword
                 - spamemailbwl
                 - spamfsip
                 - spamfssubmit
                 - spamfschksum
                 - spamfsurl
                 - spamhelodns
                 - spamipbwl
                 - spamraddrdns
                 - spamrbl
                 - spamhdrcheck
                 - spamfsphish
                 - spambwl
            replacemsg-group:
                type: str
                description: 'Replacement message group.'
            spam-bwl-table:
                type: str
                description: 'Anti-spam black/white list table ID.'
            spam-bword-table:
                type: str
                description: 'Anti-spam banned word table ID.'
            spam-bword-threshold:
                type: int
                description: 'Spam banned word threshold.'
            spam-filtering:
                type: str
                description: 'Enable/disable spam filtering.'
                choices:
                    - 'disable'
                    - 'enable'
            spam-iptrust-table:
                type: str
                description: 'Anti-spam IP trust table ID.'
            spam-log:
                type: str
                description: 'Enable/disable spam logging for email filtering.'
                choices:
                    - 'disable'
                    - 'enable'
            spam-log-fortiguard-response:
                type: str
                description: 'Enable/disable logging FortiGuard spam response.'
                choices:
                    - 'disable'
                    - 'enable'
            spam-mheader-table:
                type: str
                description: 'Anti-spam MIME header table ID.'
            spam-rbl-table:
                type: str
                description: 'Anti-spam DNSBL table ID.'

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
    - name: Configure AntiSpam profiles.
      fmgr_spamfilter_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         spamfilter_profile:
            comment: <value of string>
            external: <value in [disable, enable]>
            flow-based: <value in [disable, enable]>
            name: <value of string>
            options:
              - bannedword
              - spamemailbwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamipbwl
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambwl
            replacemsg-group: <value of string>
            spam-bwl-table: <value of string>
            spam-bword-table: <value of string>
            spam-bword-threshold: <value of integer>
            spam-filtering: <value in [disable, enable]>
            spam-iptrust-table: <value of string>
            spam-log: <value in [disable, enable]>
            spam-log-fortiguard-response: <value in [disable, enable]>
            spam-mheader-table: <value of string>
            spam-rbl-table: <value of string>

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
        '/pm/config/adom/{adom}/obj/spamfilter/profile',
        '/pm/config/global/obj/spamfilter/profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/spamfilter/profile/{profile}',
        '/pm/config/global/obj/spamfilter/profile/{profile}'
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
        'spamfilter_profile': {
            'required': False,
            'type': 'dict',
            'options': {
                'comment': {
                    'required': False,
                    'type': 'str'
                },
                'external': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'flow-based': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'options': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'bannedword',
                        'spamemailbwl',
                        'spamfsip',
                        'spamfssubmit',
                        'spamfschksum',
                        'spamfsurl',
                        'spamhelodns',
                        'spamipbwl',
                        'spamraddrdns',
                        'spamrbl',
                        'spamhdrcheck',
                        'spamfsphish',
                        'spambwl'
                    ]
                },
                'replacemsg-group': {
                    'required': False,
                    'type': 'str'
                },
                'spam-bwl-table': {
                    'required': False,
                    'type': 'str'
                },
                'spam-bword-table': {
                    'required': False,
                    'type': 'str'
                },
                'spam-bword-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'spam-filtering': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'spam-iptrust-table': {
                    'required': False,
                    'type': 'str'
                },
                'spam-log': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'spam-log-fortiguard-response': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'spam-mheader-table': {
                    'required': False,
                    'type': 'str'
                },
                'spam-rbl-table': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'spamfilter_profile'),
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
