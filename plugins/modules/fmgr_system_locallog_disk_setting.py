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
module: fmgr_system_locallog_disk_setting
short_description: Settings for local disk logging.
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
    system_locallog_disk_setting:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            diskfull:
                type: str
                default: 'overwrite'
                description:
                 - 'Policy to apply when disk is full.'
                 - 'overwrite - Overwrite oldest log when disk is full.'
                 - 'nolog - Stop logging when disk is full.'
                choices:
                    - 'overwrite'
                    - 'nolog'
            log-disk-full-percentage:
                type: int
                default: 80
                description: 'Consider log disk as full at this usage percentage.'
            max-log-file-size:
                type: int
                default: 100
                description: 'Maximum log file size before rolling.'
            roll-day:
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
            roll-schedule:
                type: str
                default: 'none'
                description:
                 - 'Frequency to check log file for rolling.'
                 - 'none - Not scheduled.'
                 - 'daily - Every day.'
                 - 'weekly - Every week.'
                choices:
                    - 'none'
                    - 'daily'
                    - 'weekly'
            roll-time:
                description: no description
                type: str
            server-type:
                type: str
                default: 'FTP'
                description:
                 - 'Server type.'
                 - 'FTP - Upload via FTP.'
                 - 'SFTP - Upload via SFTP.'
                 - 'SCP - Upload via SCP.'
                choices:
                    - 'FTP'
                    - 'SFTP'
                    - 'SCP'
            severity:
                type: str
                default: 'information'
                description:
                 - 'Least severity level to log.'
                 - 'emergency - Emergency level.'
                 - 'alert - Alert level.'
                 - 'critical - Critical level.'
                 - 'error - Error level.'
                 - 'warning - Warning level.'
                 - 'notification - Notification level.'
                 - 'information - Information level.'
                 - 'debug - Debug level.'
                choices:
                    - 'emergency'
                    - 'alert'
                    - 'critical'
                    - 'error'
                    - 'warning'
                    - 'notification'
                    - 'information'
                    - 'debug'
            status:
                type: str
                default: 'enable'
                description:
                 - 'Enable/disable local disk log.'
                 - 'disable - Do not log to local disk.'
                 - 'enable - Log to local disk.'
                choices:
                    - 'disable'
                    - 'enable'
            upload:
                type: str
                default: 'disable'
                description:
                 - 'Upload log file when rolling.'
                 - 'disable - Disable uploading when rolling log file.'
                 - 'enable - Enable uploading when rolling log file.'
                choices:
                    - 'disable'
                    - 'enable'
            upload-delete-files:
                type: str
                default: 'enable'
                description:
                 - 'Delete log files after uploading (default = enable).'
                 - 'disable - Do not delete log files after uploading.'
                 - 'enable - Delete log files after uploading.'
                choices:
                    - 'disable'
                    - 'enable'
            upload-time:
                description: no description
                type: str
            uploaddir:
                type: str
                description: 'Log file upload remote directory.'
            uploadip:
                type: str
                default: '0.0.0.0'
                description: 'IP address of log uploading server.'
            uploadpass:
                description: no description
                type: str
            uploadport:
                type: int
                default: 0
                description: 'Server port (0 = default protocol port).'
            uploadsched:
                type: str
                default: 'disable'
                description:
                 - 'Scheduled upload (disable = upload when rolling).'
                 - 'disable - Upload when rolling.'
                 - 'enable - Scheduled upload.'
                choices:
                    - 'disable'
                    - 'enable'
            uploadtype:
                description: no description
                type: list
                choices:
                 - event
            uploaduser:
                type: str
                description: 'User account in upload server.'
            uploadzip:
                type: str
                default: 'disable'
                description:
                 - 'Compress upload logs.'
                 - 'disable - Upload log files as plain text.'
                 - 'enable - Upload log files compressed.'
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
    - name: Settings for local disk logging.
      fmgr_system_locallog_disk_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_locallog_disk_setting:
            diskfull: <value in [overwrite, nolog]>
            log-disk-full-percentage: <value of integer>
            max-log-file-size: <value of integer>
            roll-day:
              - sunday
              - monday
              - tuesday
              - wednesday
              - thursday
              - friday
              - saturday
            roll-schedule: <value in [none, daily, weekly]>
            roll-time: <value of string>
            server-type: <value in [FTP, SFTP, SCP]>
            severity: <value in [emergency, alert, critical, ...]>
            status: <value in [disable, enable]>
            upload: <value in [disable, enable]>
            upload-delete-files: <value in [disable, enable]>
            upload-time: <value of string>
            uploaddir: <value of string>
            uploadip: <value of string>
            uploadpass: <value of string>
            uploadport: <value of integer>
            uploadsched: <value in [disable, enable]>
            uploadtype:
              - event
            uploaduser: <value of string>
            uploadzip: <value in [disable, enable]>

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
        '/cli/global/system/locallog/disk/setting'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/locallog/disk/setting/{setting}'
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
        'system_locallog_disk_setting': {
            'required': False,
            'type': 'dict',
            'options': {
                'diskfull': {
                    'required': False,
                    'choices': [
                        'overwrite',
                        'nolog'
                    ],
                    'type': 'str'
                },
                'log-disk-full-percentage': {
                    'required': False,
                    'type': 'int'
                },
                'max-log-file-size': {
                    'required': False,
                    'type': 'int'
                },
                'roll-day': {
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
                'roll-schedule': {
                    'required': False,
                    'choices': [
                        'none',
                        'daily',
                        'weekly'
                    ],
                    'type': 'str'
                },
                'roll-time': {
                    'required': False,
                    'type': 'str'
                },
                'server-type': {
                    'required': False,
                    'choices': [
                        'FTP',
                        'SFTP',
                        'SCP'
                    ],
                    'type': 'str'
                },
                'severity': {
                    'required': False,
                    'choices': [
                        'emergency',
                        'alert',
                        'critical',
                        'error',
                        'warning',
                        'notification',
                        'information',
                        'debug'
                    ],
                    'type': 'str'
                },
                'status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'upload': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'upload-delete-files': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'upload-time': {
                    'required': False,
                    'type': 'str'
                },
                'uploaddir': {
                    'required': False,
                    'type': 'str'
                },
                'uploadip': {
                    'required': False,
                    'type': 'str'
                },
                'uploadpass': {
                    'required': False,
                    'type': 'str'
                },
                'uploadport': {
                    'required': False,
                    'type': 'int'
                },
                'uploadsched': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'uploadtype': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'event'
                    ]
                },
                'uploaduser': {
                    'required': False,
                    'type': 'str'
                },
                'uploadzip': {
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
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_locallog_disk_setting'),
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
