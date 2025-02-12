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
module: fmgr_devprof_log_fortianalyzer_setting
short_description: Global FortiAnalyzer settings.
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
    devprof_log_fortianalyzer_setting:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            certificate:
                type: str
                description: 'Certificate used to communicate with FortiAnalyzer.'
            conn-timeout:
                type: int
                description: 'FortiAnalyzer connection time-out in seconds (for status and log buffer).'
            enc-algorithm:
                type: str
                description: 'Enable/disable sending FortiAnalyzer log data with SSL encryption.'
                choices:
                    - 'default'
                    - 'high'
                    - 'low'
                    - 'disable'
                    - 'high-medium'
                    - 'low-medium'
            hmac-algorithm:
                type: str
                description: 'FortiAnalyzer IPsec tunnel HMAC algorithm.'
                choices:
                    - 'sha256'
                    - 'sha1'
            ips-archive:
                type: str
                description: 'Enable/disable IPS packet archive logging.'
                choices:
                    - 'disable'
                    - 'enable'
            monitor-failure-retry-period:
                type: int
                description: 'Time between FortiAnalyzer connection retries in seconds (for status and log buffer).'
            monitor-keepalive-period:
                type: int
                description: 'Time between OFTP keepalives in seconds (for status and log buffer).'
            reliable:
                type: str
                description: 'Enable/disable reliable logging to FortiAnalyzer.'
                choices:
                    - 'disable'
                    - 'enable'
            ssl-min-proto-version:
                type: str
                description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
                choices:
                    - 'default'
                    - 'TLSv1'
                    - 'TLSv1-1'
                    - 'TLSv1-2'
                    - 'SSLv3'
            upload-day:
                type: str
                description: 'Day of week (month) to upload logs.'
            upload-interval:
                type: str
                description: 'Frequency to upload log files to FortiAnalyzer.'
                choices:
                    - 'daily'
                    - 'weekly'
                    - 'monthly'
            upload-option:
                type: str
                description: 'Enable/disable logging to hard disk and then uploading to FortiAnalyzer.'
                choices:
                    - 'store-and-upload'
                    - 'realtime'
                    - '1-minute'
                    - '5-minute'
            upload-time:
                type: str
                description: 'Time to upload logs (hh:mm).'

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
    - name: Global FortiAnalyzer settings.
      fmgr_devprof_log_fortianalyzer_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_log_fortianalyzer_setting:
            certificate: <value of string>
            conn-timeout: <value of integer>
            enc-algorithm: <value in [default, high, low, ...]>
            hmac-algorithm: <value in [sha256, sha1]>
            ips-archive: <value in [disable, enable]>
            monitor-failure-retry-period: <value of integer>
            monitor-keepalive-period: <value of integer>
            reliable: <value in [disable, enable]>
            ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
            upload-day: <value of string>
            upload-interval: <value in [daily, weekly, monthly]>
            upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
            upload-time: <value of string>

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
        '/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting/{setting}'
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
        'devprof_log_fortianalyzer_setting': {
            'required': False,
            'type': 'dict',
            'options': {
                'certificate': {
                    'required': False,
                    'type': 'str'
                },
                'conn-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'enc-algorithm': {
                    'required': False,
                    'choices': [
                        'default',
                        'high',
                        'low',
                        'disable',
                        'high-medium',
                        'low-medium'
                    ],
                    'type': 'str'
                },
                'hmac-algorithm': {
                    'required': False,
                    'choices': [
                        'sha256',
                        'sha1'
                    ],
                    'type': 'str'
                },
                'ips-archive': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'monitor-failure-retry-period': {
                    'required': False,
                    'type': 'int'
                },
                'monitor-keepalive-period': {
                    'required': False,
                    'type': 'int'
                },
                'reliable': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ssl-min-proto-version': {
                    'required': False,
                    'choices': [
                        'default',
                        'TLSv1',
                        'TLSv1-1',
                        'TLSv1-2',
                        'SSLv3'
                    ],
                    'type': 'str'
                },
                'upload-day': {
                    'required': False,
                    'type': 'str'
                },
                'upload-interval': {
                    'required': False,
                    'choices': [
                        'daily',
                        'weekly',
                        'monthly'
                    ],
                    'type': 'str'
                },
                'upload-option': {
                    'required': False,
                    'choices': [
                        'store-and-upload',
                        'realtime',
                        '1-minute',
                        '5-minute'
                    ],
                    'type': 'str'
                },
                'upload-time': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'devprof_log_fortianalyzer_setting'),
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
