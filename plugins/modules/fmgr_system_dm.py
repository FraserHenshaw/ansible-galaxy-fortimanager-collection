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
module: fmgr_system_dm
short_description: Configure dm.
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
    system_dm:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            concurrent-install-image-limit:
                type: int
                default: 500
                description: 'Maximum number of concurrent install image (1 - 1000).'
            concurrent-install-limit:
                type: int
                default: 480
                description: 'Maximum number of concurrent installs (5 - 2000).'
            concurrent-install-script-limit:
                type: int
                default: 480
                description: 'Maximum number of concurrent install scripts (5 - 2000).'
            discover-timeout:
                type: int
                default: 6
                description: 'Check connection timeout when discover device (3 - 15).'
            dpm-logsize:
                type: int
                default: 10000
                description: 'Maximum dpm log size per device (1 - 10000K).'
            fgfm-sock-timeout:
                type: int
                default: 360
                description: 'Maximum FGFM socket idle time (90 - 1800 sec).'
            fgfm_keepalive_itvl:
                type: int
                default: 120
                description: 'FGFM protocol keep alive interval (30 - 600 sec).'
            force-remote-diff:
                type: str
                default: 'disable'
                description:
                 - 'Always use remote diff when installing.'
                 - 'disable - Disable.'
                 - 'enable - Enable.'
                choices:
                    - 'disable'
                    - 'enable'
            fortiap-refresh-cnt:
                type: int
                default: 500
                description: 'Max auto refresh FortiAP number each time (1 - 10000).'
            fortiap-refresh-itvl:
                type: int
                default: 10
                description: 'Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh.'
            fortiext-refresh-cnt:
                type: int
                default: 50
                description: 'Max device number for FortiExtender auto refresh (1 - 10000).'
            install-image-timeout:
                type: int
                default: 3600
                description: 'Maximum waiting time for image transfer and device upgrade (600 - 7200 sec).'
            install-tunnel-retry-itvl:
                type: int
                default: 60
                description: 'Time to re-establish tunnel during install (10 - 60 sec).'
            max-revs:
                type: int
                default: 100
                description: 'Maximum number of revisions saved (1 - 250).'
            nr-retry:
                type: int
                default: 1
                description: 'Number of retries.'
            retry:
                type: str
                default: 'enable'
                description:
                 - 'Enable/disable configuration install retry.'
                 - 'disable - Disable.'
                 - 'enable - Enable.'
                choices:
                    - 'disable'
                    - 'enable'
            retry-intvl:
                type: int
                default: 15
                description: 'Retry interval.'
            rollback-allow-reboot:
                type: str
                default: 'disable'
                description:
                 - 'Enable/disable FortiGate reboot to rollback when installing script/config.'
                 - 'disable - Disable.'
                 - 'enable - Enable.'
                choices:
                    - 'disable'
                    - 'enable'
            script-logsize:
                type: int
                default: 100
                description: 'Maximum script log size per device (1 - 10000K).'
            skip-scep-check:
                type: str
                default: 'disable'
                description:
                 - 'Enable/disable installing scep related objects even if scep url is configured.'
                 - 'disable - Disable.'
                 - 'enable - Enable.'
                choices:
                    - 'disable'
                    - 'enable'
            skip-tunnel-fcp-req:
                type: str
                default: 'enable'
                description:
                 - 'Enable/disable skip the fcp request sent from fgfm tunnel'
                 - 'disable - Disable.'
                 - 'enable - Enable.'
                choices:
                    - 'disable'
                    - 'enable'
            verify-install:
                type: str
                default: 'enable'
                description:
                 - 'Verify install against remote configuration.'
                 - 'disable - Disable.'
                 - 'optimal - Verify installation for command errors.'
                 - 'enable - Always verify installation.'
                choices:
                    - 'disable'
                    - 'optimal'
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
    - name: Configure dm.
      fmgr_system_dm:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_dm:
            concurrent-install-image-limit: <value of integer>
            concurrent-install-limit: <value of integer>
            concurrent-install-script-limit: <value of integer>
            discover-timeout: <value of integer>
            dpm-logsize: <value of integer>
            fgfm-sock-timeout: <value of integer>
            fgfm_keepalive_itvl: <value of integer>
            force-remote-diff: <value in [disable, enable]>
            fortiap-refresh-cnt: <value of integer>
            fortiap-refresh-itvl: <value of integer>
            fortiext-refresh-cnt: <value of integer>
            install-image-timeout: <value of integer>
            install-tunnel-retry-itvl: <value of integer>
            max-revs: <value of integer>
            nr-retry: <value of integer>
            retry: <value in [disable, enable]>
            retry-intvl: <value of integer>
            rollback-allow-reboot: <value in [disable, enable]>
            script-logsize: <value of integer>
            skip-scep-check: <value in [disable, enable]>
            skip-tunnel-fcp-req: <value in [disable, enable]>
            verify-install: <value in [disable, optimal, enable]>

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
        '/cli/global/system/dm'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/dm/{dm}'
    ]

    url_params = []
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
        'system_dm': {
            'required': False,
            'type': 'dict',
            'options': {
                'concurrent-install-image-limit': {
                    'required': False,
                    'type': 'int'
                },
                'concurrent-install-limit': {
                    'required': False,
                    'type': 'int'
                },
                'concurrent-install-script-limit': {
                    'required': False,
                    'type': 'int'
                },
                'discover-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'dpm-logsize': {
                    'required': False,
                    'type': 'int'
                },
                'fgfm-sock-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'fgfm_keepalive_itvl': {
                    'required': False,
                    'type': 'int'
                },
                'force-remote-diff': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fortiap-refresh-cnt': {
                    'required': False,
                    'type': 'int'
                },
                'fortiap-refresh-itvl': {
                    'required': False,
                    'type': 'int'
                },
                'fortiext-refresh-cnt': {
                    'required': False,
                    'type': 'int'
                },
                'install-image-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'install-tunnel-retry-itvl': {
                    'required': False,
                    'type': 'int'
                },
                'max-revs': {
                    'required': False,
                    'type': 'int'
                },
                'nr-retry': {
                    'required': False,
                    'type': 'int'
                },
                'retry': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'retry-intvl': {
                    'required': False,
                    'type': 'int'
                },
                'rollback-allow-reboot': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'script-logsize': {
                    'required': False,
                    'type': 'int'
                },
                'skip-scep-check': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'skip-tunnel-fcp-req': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'verify-install': {
                    'required': False,
                    'choices': [
                        'disable',
                        'optimal',
                        'enable'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_dm'),
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
