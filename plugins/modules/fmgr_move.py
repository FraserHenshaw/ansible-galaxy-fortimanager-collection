#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2020-2021 Fortinet, Inc.
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
module: fmgr_move
short_description: Move fortimanager defined Object.
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
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded
options:
    enable_log:
        description: Enable/Disable logging for task
        required: false
        type: bool
        default: false
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
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    move:
        description: the top level parameters set
        type: dict
        required: false
'''

EXAMPLES = '''
- hosts: fortimanager01
  collections:
   - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: Move a firewall vip object
     fmgr_move:
       move:
         selector: 'firewall_vip'
         target: 'ansible-test-vip_first'
         action: 'before'
         self:
           adom: 'root'
           vip: 'ansible-test-vip_second'
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


def main():
    move_metadata = {
        'dnsfilter_domainfilter_entries': {
            'params': [
                'adom',
                'domain-filter',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/dnsfilter/domain-filter/{domain-filter}/entries/{entries}',
                '/pm/config/global/obj/dnsfilter/domain-filter/{domain-filter}/entries/{entries}'
            ]
        },
        'application_list_entries': {
            'params': [
                'adom',
                'list',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}',
                '/pm/config/global/obj/application/list/{list}/entries/{entries}'
            ]
        },
        'vpnsslweb_portal_bookmarkgroup': {
            'params': [
                'adom',
                'portal',
                'bookmark-group'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}',
                '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}'
            ]
        },
        'vpnsslweb_portal_bookmarkgroup_bookmarks': {
            'params': [
                'adom',
                'portal',
                'bookmark-group',
                'bookmarks'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks/{bookmarks}',
                '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}/bookmarks/{bookmarks}'
            ]
        },
        'vpnsslweb_portal_splitdns': {
            'params': [
                'adom',
                'portal',
                'split-dns'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/split-dns/{split-dns}',
                '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/split-dns/{split-dns}'
            ]
        },
        'pkg_firewall_centralsnatmap': {
            'params': [
                'adom',
                'pkg',
                'central-snat-map'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/central-snat-map/{central-snat-map}'
            ]
        },
        'pkg_firewall_dospolicy': {
            'params': [
                'adom',
                'pkg',
                'DoS-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}'
            ]
        },
        'pkg_firewall_dospolicy6': {
            'params': [
                'adom',
                'pkg',
                'DoS-policy6'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy6/{DoS-policy6}'
            ]
        },
        'pkg_firewall_interfacepolicy': {
            'params': [
                'adom',
                'pkg',
                'interface-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}'
            ]
        },
        'pkg_firewall_interfacepolicy6': {
            'params': [
                'adom',
                'pkg',
                'interface-policy6'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy6/{interface-policy6}'
            ]
        },
        'pkg_firewall_localinpolicy': {
            'params': [
                'adom',
                'pkg',
                'local-in-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/local-in-policy/{local-in-policy}'
            ]
        },
        'pkg_firewall_localinpolicy6': {
            'params': [
                'adom',
                'pkg',
                'local-in-policy6'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/local-in-policy6/{local-in-policy6}'
            ]
        },
        'pkg_firewall_multicastpolicy': {
            'params': [
                'adom',
                'pkg',
                'multicast-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/multicast-policy/{multicast-policy}'
            ]
        },
        'pkg_firewall_multicastpolicy6': {
            'params': [
                'adom',
                'pkg',
                'multicast-policy6'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/multicast-policy6/{multicast-policy6}'
            ]
        },
        'pkg_firewall_policy': {
            'params': [
                'adom',
                'pkg',
                'policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy/{policy}'
            ]
        },
        'pkg_firewall_policy46': {
            'params': [
                'adom',
                'pkg',
                'policy46'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy46/{policy46}'
            ]
        },
        'pkg_firewall_policy6': {
            'params': [
                'adom',
                'pkg',
                'policy6'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6/{policy6}'
            ]
        },
        'pkg_firewall_policy64': {
            'params': [
                'adom',
                'pkg',
                'policy64'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy64/{policy64}'
            ]
        },
        'pkg_firewall_proxypolicy': {
            'params': [
                'adom',
                'pkg',
                'proxy-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}'
            ]
        },
        'pkg_firewall_shapingpolicy': {
            'params': [
                'adom',
                'pkg',
                'shaping-policy'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy/{shaping-policy}'
            ]
        },
        'pkg_central_dnat': {
            'params': [
                'adom',
                'pkg',
                'dnat'
            ],
            'urls': [
                '/pm/config/adom/{adom}/pkg/{pkg}/central/dnat/{dnat}'
            ]
        },
        'webfilter_contentheader_entries': {
            'params': [
                'adom',
                'content-header',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/webfilter/content-header/{content-header}/entries/{entries}',
                '/pm/config/global/obj/webfilter/content-header/{content-header}/entries/{entries}'
            ]
        },
        'webfilter_urlfilter_entries': {
            'params': [
                'adom',
                'urlfilter',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}',
                '/pm/config/global/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}'
            ]
        },
        'ips_sensor_entries': {
            'params': [
                'adom',
                'sensor',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}',
                '/pm/config/global/obj/ips/sensor/{sensor}/entries/{entries}'
            ]
        },
        'ips_sensor_filter': {
            'params': [
                'adom',
                'sensor',
                'filter'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/filter/{filter}',
                '/pm/config/global/obj/ips/sensor/{sensor}/filter/{filter}'
            ]
        },
        'spamfilter_bwl_entries': {
            'params': [
                'adom',
                'bwl',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}',
                '/pm/config/global/obj/spamfilter/bwl/{bwl}/entries/{entries}'
            ]
        },
        'spamfilter_bword_entries': {
            'params': [
                'adom',
                'bword',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/spamfilter/bword/{bword}/entries/{entries}',
                '/pm/config/global/obj/spamfilter/bword/{bword}/entries/{entries}'
            ]
        },
        'firewall_carrierendpointbwl_entries': {
            'params': [
                'adom',
                'carrier-endpoint-bwl',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/carrier-endpoint-bwl/{carrier-endpoint-bwl}/entries/{entries}',
                '/pm/config/global/obj/firewall/carrier-endpoint-bwl/{carrier-endpoint-bwl}/entries/{entries}'
            ]
        },
        'firewall_identitybasedroute': {
            'params': [
                'adom',
                'identity-based-route'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/identity-based-route/{identity-based-route}',
                '/pm/config/global/obj/firewall/identity-based-route/{identity-based-route}'
            ]
        },
        'firewall_service_category': {
            'params': [
                'adom',
                'category'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/service/category/{category}',
                '/pm/config/global/obj/firewall/service/category/{category}'
            ]
        },
        'firewall_service_custom': {
            'params': [
                'adom',
                'custom'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/service/custom/{custom}',
                '/pm/config/global/obj/firewall/service/custom/{custom}'
            ]
        },
        'firewall_shapingprofile_shapingentries': {
            'params': [
                'adom',
                'shaping-profile',
                'shaping-entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/shaping-profile/{shaping-profile}/shaping-entries/{shaping-entries}',
                '/pm/config/global/obj/firewall/shaping-profile/{shaping-profile}/shaping-entries/{shaping-entries}'
            ]
        },
        'firewall_vip': {
            'params': [
                'adom',
                'vip'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/firewall/vip/{vip}',
                '/pm/config/global/obj/firewall/vip/{vip}'
            ]
        },
        'system_sdnconnector_externalip': {
            'params': [
                'adom',
                'sdn-connector',
                'external-ip'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/external-ip/{external-ip}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/external-ip/{external-ip}'
            ]
        },
        'system_sdnconnector_nic': {
            'params': [
                'adom',
                'sdn-connector',
                'nic'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/nic/{nic}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/nic/{nic}'
            ]
        },
        'system_sdnconnector_nic_ip': {
            'params': [
                'adom',
                'sdn-connector',
                'nic',
                'ip'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/nic/{nic}/ip/{ip}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/nic/{nic}/ip/{ip}'
            ]
        },
        'system_sdnconnector_routetable': {
            'params': [
                'adom',
                'sdn-connector',
                'route-table'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/route-table/{route-table}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/route-table/{route-table}'
            ]
        },
        'system_sdnconnector_routetable_route': {
            'params': [
                'adom',
                'sdn-connector',
                'route-table',
                'route'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/route-table/{route-table}/route/{route}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/route-table/{route-table}/route/{route}'
            ]
        },
        'system_sdnconnector_route': {
            'params': [
                'adom',
                'sdn-connector',
                'route'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}/route/{route}',
                '/pm/config/global/obj/system/sdn-connector/{sdn-connector}/route/{route}'
            ]
        },
        'wanprof_system_virtualwanlink_members': {
            'params': [
                'adom',
                'wanprof',
                'members'
            ],
            'urls': [
                '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/members/{members}'
            ]
        },
        'wanprof_system_virtualwanlink_service': {
            'params': [
                'adom',
                'wanprof',
                'service'
            ],
            'urls': [
                '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}'
            ]
        },
        'wanprof_system_virtualwanlink_service_sla': {
            'params': [
                'adom',
                'wanprof',
                'service',
                'sla'
            ],
            'urls': [
                '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}/sla/{sla}'
            ]
        },
        'sshfilter_profile_shellcommands': {
            'params': [
                'adom',
                'profile',
                'shell-commands'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/ssh-filter/profile/{profile}/shell-commands/{shell-commands}',
                '/pm/config/global/obj/ssh-filter/profile/{profile}/shell-commands/{shell-commands}'
            ]
        },
        'bonjourprofile_policylist': {
            'params': [
                'adom',
                'bonjour-profile',
                'policy-list'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/wireless-controller/bonjour-profile/{bonjour-profile}/policy-list/{policy-list}',
                '/pm/config/global/obj/wireless-controller/bonjour-profile/{bonjour-profile}/policy-list/{policy-list}'
            ]
        },
        'dlp_filepattern_entries': {
            'params': [
                'adom',
                'filepattern',
                'entries'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}/entries/{entries}',
                '/pm/config/global/obj/dlp/filepattern/{filepattern}/entries/{entries}'
            ]
        },
        'dlp_sensor_filter': {
            'params': [
                'adom',
                'sensor',
                'filter'
            ],
            'urls': [
                '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}/filter/{filter}',
                '/pm/config/global/obj/dlp/sensor/{sensor}/filter/{filter}'
            ]
        }
    }

    module_arg_spec = {
        'enable_log': {
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
        'move': {
            'required': True,
            'type': 'dict',
            'options': {
                'selector': {
                    'required': True,
                    'type': 'str',
                    'choices': [
                        'dnsfilter_domainfilter_entries',
                        'application_list_entries',
                        'vpnsslweb_portal_bookmarkgroup',
                        'vpnsslweb_portal_bookmarkgroup_bookmarks',
                        'vpnsslweb_portal_splitdns',
                        'pkg_firewall_centralsnatmap',
                        'pkg_firewall_dospolicy',
                        'pkg_firewall_dospolicy6',
                        'pkg_firewall_interfacepolicy',
                        'pkg_firewall_interfacepolicy6',
                        'pkg_firewall_localinpolicy',
                        'pkg_firewall_localinpolicy6',
                        'pkg_firewall_multicastpolicy',
                        'pkg_firewall_multicastpolicy6',
                        'pkg_firewall_policy',
                        'pkg_firewall_policy46',
                        'pkg_firewall_policy6',
                        'pkg_firewall_policy64',
                        'pkg_firewall_proxypolicy',
                        'pkg_firewall_shapingpolicy',
                        'pkg_central_dnat',
                        'webfilter_contentheader_entries',
                        'webfilter_urlfilter_entries',
                        'ips_sensor_entries',
                        'ips_sensor_filter',
                        'spamfilter_bwl_entries',
                        'spamfilter_bword_entries',
                        'firewall_carrierendpointbwl_entries',
                        'firewall_identitybasedroute',
                        'firewall_service_category',
                        'firewall_service_custom',
                        'firewall_shapingprofile_shapingentries',
                        'firewall_vip',
                        'system_sdnconnector_externalip',
                        'system_sdnconnector_nic',
                        'system_sdnconnector_nic_ip',
                        'system_sdnconnector_routetable',
                        'system_sdnconnector_routetable_route',
                        'system_sdnconnector_route',
                        'wanprof_system_virtualwanlink_members',
                        'wanprof_system_virtualwanlink_service',
                        'wanprof_system_virtualwanlink_service_sla',
                        'sshfilter_profile_shellcommands',
                        'bonjourprofile_policylist',
                        'dlp_filepattern_entries',
                        'dlp_sensor_filter'
                    ]
                },
                'self': {
                    'required': True,
                    'type': 'dict'
                },
                'target': {
                    'required': True,
                    'type': 'str'
                },
                'action': {
                    'required': True,
                    'type': 'str',
                    'choices': [
                        'after',
                        'before'
                    ]
                }
            }
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(None, None, None, None, module, connection)
        fmgr.process_move(move_metadata)
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
