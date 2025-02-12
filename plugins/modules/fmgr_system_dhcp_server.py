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
module: fmgr_system_dhcp_server
short_description: Configure DHCP servers.
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
    system_dhcp_server:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            auto-configuration:
                type: str
                description: 'Enable/disable auto configuration.'
                choices:
                    - 'disable'
                    - 'enable'
            conflicted-ip-timeout:
                type: int
                description: 'Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.'
            ddns-auth:
                type: str
                description: 'DDNS authentication mode.'
                choices:
                    - 'disable'
                    - 'tsig'
            ddns-key:
                type: str
                description: 'DDNS update key (base 64 encoding).'
            ddns-keyname:
                type: str
                description: 'DDNS update key name.'
            ddns-server-ip:
                type: str
                description: 'DDNS server IP.'
            ddns-ttl:
                type: int
                description: 'TTL.'
            ddns-update:
                type: str
                description: 'Enable/disable DDNS update for DHCP.'
                choices:
                    - 'disable'
                    - 'enable'
            ddns-update-override:
                type: str
                description: 'Enable/disable DDNS update override for DHCP.'
                choices:
                    - 'disable'
                    - 'enable'
            ddns-zone:
                type: str
                description: 'Zone of your domain name (ex. DDNS.com).'
            default-gateway:
                type: str
                description: 'Default gateway IP address assigned by the DHCP server.'
            dns-server1:
                type: str
                description: 'DNS server 1.'
            dns-server2:
                type: str
                description: 'DNS server 2.'
            dns-server3:
                type: str
                description: 'DNS server 3.'
            dns-service:
                type: str
                description: 'Options for assigning DNS servers to DHCP clients.'
                choices:
                    - 'default'
                    - 'specify'
                    - 'local'
            domain:
                type: str
                description: 'Domain name suffix for the IP addresses that the DHCP server assigns to clients.'
            exclude-range:
                description: no description
                type: list
                suboptions:
                    end-ip:
                        type: str
                        description: 'End of IP range.'
                    id:
                        type: int
                        description: 'ID.'
                    start-ip:
                        type: str
                        description: 'Start of IP range.'
            filename:
                type: str
                description: 'Name of the boot file on the TFTP server.'
            forticlient-on-net-status:
                type: str
                description: 'Enable/disable FortiClient-On-Net service for this DHCP server.'
                choices:
                    - 'disable'
                    - 'enable'
            id:
                type: int
                description: 'ID.'
            interface:
                type: str
                description: 'DHCP server can assign IP configurations to clients connected to this interface.'
            ip-mode:
                type: str
                description: 'Method used to assign client IP.'
                choices:
                    - 'range'
                    - 'usrgrp'
            ip-range:
                description: no description
                type: list
                suboptions:
                    end-ip:
                        type: str
                        description: 'End of IP range.'
                    id:
                        type: int
                        description: 'ID.'
                    start-ip:
                        type: str
                        description: 'Start of IP range.'
            ipsec-lease-hold:
                type: int
                description: 'DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).'
            lease-time:
                type: int
                description: 'Lease time in seconds, 0 means unlimited.'
            mac-acl-default-action:
                type: str
                description: 'MAC access control default action (allow or block assigning IP settings).'
                choices:
                    - 'assign'
                    - 'block'
            netmask:
                type: str
                description: 'Netmask assigned by the DHCP server.'
            next-server:
                type: str
                description: 'IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.'
            ntp-server1:
                type: str
                description: 'NTP server 1.'
            ntp-server2:
                type: str
                description: 'NTP server 2.'
            ntp-server3:
                type: str
                description: 'NTP server 3.'
            ntp-service:
                type: str
                description: 'Options for assigning Network Time Protocol (NTP) servers to DHCP clients.'
                choices:
                    - 'default'
                    - 'specify'
                    - 'local'
            options:
                description: no description
                type: list
                suboptions:
                    code:
                        type: int
                        description: 'DHCP option code.'
                    id:
                        type: int
                        description: 'ID.'
                    ip:
                        description: no description
                        type: str
                    type:
                        type: str
                        description: 'DHCP option type.'
                        choices:
                            - 'hex'
                            - 'string'
                            - 'ip'
                            - 'fqdn'
                    value:
                        type: str
                        description: 'DHCP option value.'
            reserved-address:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Options for the DHCP server to configure the client with the reserved MAC address.'
                        choices:
                            - 'assign'
                            - 'block'
                            - 'reserved'
                    description:
                        type: str
                        description: 'Description.'
                    id:
                        type: int
                        description: 'ID.'
                    ip:
                        type: str
                        description: 'IP address to be reserved for the MAC address.'
                    mac:
                        type: str
                        description: 'MAC address of the client that will get the reserved IP address.'
            server-type:
                type: str
                description: 'DHCP server can be a normal DHCP server or an IPsec DHCP server.'
                choices:
                    - 'regular'
                    - 'ipsec'
            status:
                type: str
                description: 'Enable/disable this DHCP configuration.'
                choices:
                    - 'disable'
                    - 'enable'
            tftp-server:
                description: no description
                type: str
            timezone:
                type: str
                description: 'Select the time zone to be assigned to DHCP clients.'
                choices:
                    - '00'
                    - '01'
                    - '02'
                    - '03'
                    - '04'
                    - '05'
                    - '06'
                    - '07'
                    - '08'
                    - '09'
                    - '10'
                    - '11'
                    - '12'
                    - '13'
                    - '14'
                    - '15'
                    - '16'
                    - '17'
                    - '18'
                    - '19'
                    - '20'
                    - '21'
                    - '22'
                    - '23'
                    - '24'
                    - '25'
                    - '26'
                    - '27'
                    - '28'
                    - '29'
                    - '30'
                    - '31'
                    - '32'
                    - '33'
                    - '34'
                    - '35'
                    - '36'
                    - '37'
                    - '38'
                    - '39'
                    - '40'
                    - '41'
                    - '42'
                    - '43'
                    - '44'
                    - '45'
                    - '46'
                    - '47'
                    - '48'
                    - '49'
                    - '50'
                    - '51'
                    - '52'
                    - '53'
                    - '54'
                    - '55'
                    - '56'
                    - '57'
                    - '58'
                    - '59'
                    - '60'
                    - '61'
                    - '62'
                    - '63'
                    - '64'
                    - '65'
                    - '66'
                    - '67'
                    - '68'
                    - '69'
                    - '70'
                    - '71'
                    - '72'
                    - '73'
                    - '74'
                    - '75'
                    - '76'
                    - '77'
                    - '78'
                    - '79'
                    - '80'
                    - '81'
                    - '82'
                    - '83'
                    - '84'
                    - '85'
                    - '86'
                    - '87'
            timezone-option:
                type: str
                description: 'Options for the DHCP server to set the clients time zone.'
                choices:
                    - 'disable'
                    - 'default'
                    - 'specify'
            vci-match:
                type: str
                description: 'Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.'
                choices:
                    - 'disable'
                    - 'enable'
            vci-string:
                description: no description
                type: str
            wifi-ac1:
                type: str
                description: 'WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).'
            wifi-ac2:
                type: str
                description: 'WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).'
            wifi-ac3:
                type: str
                description: 'WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).'
            wins-server1:
                type: str
                description: 'WINS server 1.'
            wins-server2:
                type: str
                description: 'WINS server 2.'

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
    - name: Configure DHCP servers.
      fmgr_system_dhcp_server:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         system_dhcp_server:
            auto-configuration: <value in [disable, enable]>
            conflicted-ip-timeout: <value of integer>
            ddns-auth: <value in [disable, tsig]>
            ddns-key: <value of string>
            ddns-keyname: <value of string>
            ddns-server-ip: <value of string>
            ddns-ttl: <value of integer>
            ddns-update: <value in [disable, enable]>
            ddns-update-override: <value in [disable, enable]>
            ddns-zone: <value of string>
            default-gateway: <value of string>
            dns-server1: <value of string>
            dns-server2: <value of string>
            dns-server3: <value of string>
            dns-service: <value in [default, specify, local]>
            domain: <value of string>
            exclude-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            filename: <value of string>
            forticlient-on-net-status: <value in [disable, enable]>
            id: <value of integer>
            interface: <value of string>
            ip-mode: <value in [range, usrgrp]>
            ip-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            ipsec-lease-hold: <value of integer>
            lease-time: <value of integer>
            mac-acl-default-action: <value in [assign, block]>
            netmask: <value of string>
            next-server: <value of string>
            ntp-server1: <value of string>
            ntp-server2: <value of string>
            ntp-server3: <value of string>
            ntp-service: <value in [default, specify, local]>
            options:
              -
                  code: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  type: <value in [hex, string, ip, ...]>
                  value: <value of string>
            reserved-address:
              -
                  action: <value in [assign, block, reserved]>
                  description: <value of string>
                  id: <value of integer>
                  ip: <value of string>
                  mac: <value of string>
            server-type: <value in [regular, ipsec]>
            status: <value in [disable, enable]>
            tftp-server: <value of string>
            timezone: <value in [00, 01, 02, ...]>
            timezone-option: <value in [disable, default, specify]>
            vci-match: <value in [disable, enable]>
            vci-string: <value of string>
            wifi-ac1: <value of string>
            wifi-ac2: <value of string>
            wifi-ac3: <value of string>
            wins-server1: <value of string>
            wins-server2: <value of string>

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
        '/pm/config/adom/{adom}/obj/system/dhcp/server',
        '/pm/config/global/obj/system/dhcp/server'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/dhcp/server/{server}',
        '/pm/config/global/obj/system/dhcp/server/{server}'
    ]

    url_params = ['adom']
    module_primary_key = 'id'
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
        'system_dhcp_server': {
            'required': False,
            'type': 'dict',
            'options': {
                'auto-configuration': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'conflicted-ip-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'ddns-auth': {
                    'required': False,
                    'choices': [
                        'disable',
                        'tsig'
                    ],
                    'type': 'str'
                },
                'ddns-key': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-keyname': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-server-ip': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-ttl': {
                    'required': False,
                    'type': 'int'
                },
                'ddns-update': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ddns-update-override': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ddns-zone': {
                    'required': False,
                    'type': 'str'
                },
                'default-gateway': {
                    'required': False,
                    'type': 'str'
                },
                'dns-server1': {
                    'required': False,
                    'type': 'str'
                },
                'dns-server2': {
                    'required': False,
                    'type': 'str'
                },
                'dns-server3': {
                    'required': False,
                    'type': 'str'
                },
                'dns-service': {
                    'required': False,
                    'choices': [
                        'default',
                        'specify',
                        'local'
                    ],
                    'type': 'str'
                },
                'domain': {
                    'required': False,
                    'type': 'str'
                },
                'exclude-range': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'end-ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'start-ip': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'filename': {
                    'required': False,
                    'type': 'str'
                },
                'forticlient-on-net-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'id': {
                    'required': True,
                    'type': 'int'
                },
                'interface': {
                    'required': False,
                    'type': 'str'
                },
                'ip-mode': {
                    'required': False,
                    'choices': [
                        'range',
                        'usrgrp'
                    ],
                    'type': 'str'
                },
                'ip-range': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'end-ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'start-ip': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'ipsec-lease-hold': {
                    'required': False,
                    'type': 'int'
                },
                'lease-time': {
                    'required': False,
                    'type': 'int'
                },
                'mac-acl-default-action': {
                    'required': False,
                    'choices': [
                        'assign',
                        'block'
                    ],
                    'type': 'str'
                },
                'netmask': {
                    'required': False,
                    'type': 'str'
                },
                'next-server': {
                    'required': False,
                    'type': 'str'
                },
                'ntp-server1': {
                    'required': False,
                    'type': 'str'
                },
                'ntp-server2': {
                    'required': False,
                    'type': 'str'
                },
                'ntp-server3': {
                    'required': False,
                    'type': 'str'
                },
                'ntp-service': {
                    'required': False,
                    'choices': [
                        'default',
                        'specify',
                        'local'
                    ],
                    'type': 'str'
                },
                'options': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'code': {
                            'required': False,
                            'type': 'int'
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'type': {
                            'required': False,
                            'choices': [
                                'hex',
                                'string',
                                'ip',
                                'fqdn'
                            ],
                            'type': 'str'
                        },
                        'value': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'reserved-address': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'assign',
                                'block',
                                'reserved'
                            ],
                            'type': 'str'
                        },
                        'description': {
                            'required': False,
                            'type': 'str'
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'mac': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'server-type': {
                    'required': False,
                    'choices': [
                        'regular',
                        'ipsec'
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
                'tftp-server': {
                    'required': False,
                    'type': 'str'
                },
                'timezone': {
                    'required': False,
                    'choices': [
                        '00',
                        '01',
                        '02',
                        '03',
                        '04',
                        '05',
                        '06',
                        '07',
                        '08',
                        '09',
                        '10',
                        '11',
                        '12',
                        '13',
                        '14',
                        '15',
                        '16',
                        '17',
                        '18',
                        '19',
                        '20',
                        '21',
                        '22',
                        '23',
                        '24',
                        '25',
                        '26',
                        '27',
                        '28',
                        '29',
                        '30',
                        '31',
                        '32',
                        '33',
                        '34',
                        '35',
                        '36',
                        '37',
                        '38',
                        '39',
                        '40',
                        '41',
                        '42',
                        '43',
                        '44',
                        '45',
                        '46',
                        '47',
                        '48',
                        '49',
                        '50',
                        '51',
                        '52',
                        '53',
                        '54',
                        '55',
                        '56',
                        '57',
                        '58',
                        '59',
                        '60',
                        '61',
                        '62',
                        '63',
                        '64',
                        '65',
                        '66',
                        '67',
                        '68',
                        '69',
                        '70',
                        '71',
                        '72',
                        '73',
                        '74',
                        '75',
                        '76',
                        '77',
                        '78',
                        '79',
                        '80',
                        '81',
                        '82',
                        '83',
                        '84',
                        '85',
                        '86',
                        '87'
                    ],
                    'type': 'str'
                },
                'timezone-option': {
                    'required': False,
                    'choices': [
                        'disable',
                        'default',
                        'specify'
                    ],
                    'type': 'str'
                },
                'vci-match': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'vci-string': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-ac1': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-ac2': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-ac3': {
                    'required': False,
                    'type': 'str'
                },
                'wins-server1': {
                    'required': False,
                    'type': 'str'
                },
                'wins-server2': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_dhcp_server'),
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
