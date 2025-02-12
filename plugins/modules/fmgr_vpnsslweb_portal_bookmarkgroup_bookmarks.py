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
module: fmgr_vpnsslweb_portal_bookmarkgroup_bookmarks
short_description: Bookmark table.
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
    portal:
        description: the parameter (portal) in requested url
        type: str
        required: true
    bookmark-group:
        description: the parameter (bookmark-group) in requested url
        type: str
        required: true
    vpnsslweb_portal_bookmarkgroup_bookmarks:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            additional-params:
                type: str
                description: 'Additional parameters.'
            apptype:
                type: str
                description: 'Application type.'
                choices:
                    - 'web'
                    - 'telnet'
                    - 'ssh'
                    - 'ftp'
                    - 'smb'
                    - 'vnc'
                    - 'rdp'
                    - 'citrix'
                    - 'rdpnative'
                    - 'portforward'
                    - 'sftp'
            description:
                type: str
                description: 'Description.'
            folder:
                type: str
                description: 'Network shared file folder parameter.'
            form-data:
                description: no description
                type: list
                suboptions:
                    name:
                        type: str
                        description: 'Name.'
                    value:
                        type: str
                        description: 'Value.'
            host:
                type: str
                description: 'Host name/IP parameter.'
            listening-port:
                type: int
                description: 'Listening port (0 - 65535).'
            load-balancing-info:
                type: str
                description: 'The load balancing information or cookie which should be provided to the connection broker.'
            logon-password:
                description: no description
                type: str
            logon-user:
                type: str
                description: 'Logon user.'
            name:
                type: str
                description: 'Bookmark name.'
            port:
                type: int
                description: 'Remote port.'
            preconnection-blob:
                type: str
                description: 'An arbitrary string which identifies the RDP source.'
            preconnection-id:
                type: int
                description: 'The numeric ID of the RDP source (0-2147483648).'
            remote-port:
                type: int
                description: 'Remote port (0 - 65535).'
            security:
                type: str
                description: 'Security mode for RDP connection.'
                choices:
                    - 'rdp'
                    - 'nla'
                    - 'tls'
                    - 'any'
            server-layout:
                type: str
                description: 'Server side keyboard layout.'
                choices:
                    - 'en-us-qwerty'
                    - 'de-de-qwertz'
                    - 'fr-fr-azerty'
                    - 'it-it-qwerty'
                    - 'sv-se-qwerty'
                    - 'failsafe'
                    - 'en-gb-qwerty'
                    - 'es-es-qwerty'
                    - 'fr-ch-qwertz'
                    - 'ja-jp-qwerty'
                    - 'pt-br-qwerty'
                    - 'tr-tr-qwerty'
            show-status-window:
                type: str
                description: 'Enable/disable showing of status window.'
                choices:
                    - 'disable'
                    - 'enable'
            sso:
                type: str
                description: 'Single Sign-On.'
                choices:
                    - 'disable'
                    - 'static'
                    - 'auto'
            sso-credential:
                type: str
                description: 'Single sign-on credentials.'
                choices:
                    - 'sslvpn-login'
                    - 'alternative'
            sso-credential-sent-once:
                type: str
                description: 'Single sign-on credentials are only sent once to remote server.'
                choices:
                    - 'disable'
                    - 'enable'
            sso-password:
                description: no description
                type: str
            sso-username:
                type: str
                description: 'SSO user name.'
            url:
                type: str
                description: 'URL parameter.'

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
    - name: Bookmark table.
      fmgr_vpnsslweb_portal_bookmarkgroup_bookmarks:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         portal: <your own value>
         bookmark-group: <your own value>
         state: <value in [present, absent]>
         vpnsslweb_portal_bookmarkgroup_bookmarks:
            additional-params: <value of string>
            apptype: <value in [web, telnet, ssh, ...]>
            description: <value of string>
            folder: <value of string>
            form-data:
              -
                  name: <value of string>
                  value: <value of string>
            host: <value of string>
            listening-port: <value of integer>
            load-balancing-info: <value of string>
            logon-password: <value of string>
            logon-user: <value of string>
            name: <value of string>
            port: <value of integer>
            preconnection-blob: <value of string>
            preconnection-id: <value of integer>
            remote-port: <value of integer>
            security: <value in [rdp, nla, tls, ...]>
            server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
            show-status-window: <value in [disable, enable]>
            sso: <value in [disable, static, auto]>
            sso-credential: <value in [sslvpn-login, alternative]>
            sso-credential-sent-once: <value in [disable, enable]>
            sso-password: <value of string>
            sso-username: <value of string>
            url: <value of string>

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
        '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks',
        '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks/{bookmarks}',
        '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks/{bookmarks}'
    ]

    url_params = ['adom', 'portal', 'bookmark-group']
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
        'portal': {
            'required': True,
            'type': 'str'
        },
        'bookmark-group': {
            'required': True,
            'type': 'str'
        },
        'vpnsslweb_portal_bookmarkgroup_bookmarks': {
            'required': False,
            'type': 'dict',
            'options': {
                'additional-params': {
                    'required': False,
                    'type': 'str'
                },
                'apptype': {
                    'required': False,
                    'choices': [
                        'web',
                        'telnet',
                        'ssh',
                        'ftp',
                        'smb',
                        'vnc',
                        'rdp',
                        'citrix',
                        'rdpnative',
                        'portforward',
                        'sftp'
                    ],
                    'type': 'str'
                },
                'description': {
                    'required': False,
                    'type': 'str'
                },
                'folder': {
                    'required': False,
                    'type': 'str'
                },
                'form-data': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'name': {
                            'required': False,
                            'type': 'str'
                        },
                        'value': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'host': {
                    'required': False,
                    'type': 'str'
                },
                'listening-port': {
                    'required': False,
                    'type': 'int'
                },
                'load-balancing-info': {
                    'required': False,
                    'type': 'str'
                },
                'logon-password': {
                    'required': False,
                    'type': 'str'
                },
                'logon-user': {
                    'required': False,
                    'type': 'str'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'port': {
                    'required': False,
                    'type': 'int'
                },
                'preconnection-blob': {
                    'required': False,
                    'type': 'str'
                },
                'preconnection-id': {
                    'required': False,
                    'type': 'int'
                },
                'remote-port': {
                    'required': False,
                    'type': 'int'
                },
                'security': {
                    'required': False,
                    'choices': [
                        'rdp',
                        'nla',
                        'tls',
                        'any'
                    ],
                    'type': 'str'
                },
                'server-layout': {
                    'required': False,
                    'choices': [
                        'en-us-qwerty',
                        'de-de-qwertz',
                        'fr-fr-azerty',
                        'it-it-qwerty',
                        'sv-se-qwerty',
                        'failsafe',
                        'en-gb-qwerty',
                        'es-es-qwerty',
                        'fr-ch-qwertz',
                        'ja-jp-qwerty',
                        'pt-br-qwerty',
                        'tr-tr-qwerty'
                    ],
                    'type': 'str'
                },
                'show-status-window': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'sso': {
                    'required': False,
                    'choices': [
                        'disable',
                        'static',
                        'auto'
                    ],
                    'type': 'str'
                },
                'sso-credential': {
                    'required': False,
                    'choices': [
                        'sslvpn-login',
                        'alternative'
                    ],
                    'type': 'str'
                },
                'sso-credential-sent-once': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'sso-password': {
                    'required': False,
                    'type': 'str'
                },
                'sso-username': {
                    'required': False,
                    'type': 'str'
                },
                'url': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'vpnsslweb_portal_bookmarkgroup_bookmarks'),
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
