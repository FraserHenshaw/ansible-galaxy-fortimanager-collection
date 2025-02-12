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
module: fmgr_voip_profile_sip
short_description: SIP.
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
    profile:
        description: the parameter (profile) in requested url
        type: str
        required: true
    voip_profile_sip:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            ack-rate:
                type: int
                description: 'ACK request rate limit (per second, per policy).'
            block-ack:
                type: str
                description: 'Enable/disable block ACK requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-bye:
                type: str
                description: 'Enable/disable block BYE requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-cancel:
                type: str
                description: 'Enable/disable block CANCEL requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-geo-red-options:
                type: str
                description: 'Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.'
                choices:
                    - 'disable'
                    - 'enable'
            block-info:
                type: str
                description: 'Enable/disable block INFO requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-invite:
                type: str
                description: 'Enable/disable block INVITE requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-long-lines:
                type: str
                description: 'Enable/disable block requests with headers exceeding max-line-length.'
                choices:
                    - 'disable'
                    - 'enable'
            block-message:
                type: str
                description: 'Enable/disable block MESSAGE requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-notify:
                type: str
                description: 'Enable/disable block NOTIFY requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-options:
                type: str
                description: 'Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.'
                choices:
                    - 'disable'
                    - 'enable'
            block-prack:
                type: str
                description: 'Enable/disable block prack requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-publish:
                type: str
                description: 'Enable/disable block PUBLISH requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-refer:
                type: str
                description: 'Enable/disable block REFER requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-register:
                type: str
                description: 'Enable/disable block REGISTER requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-subscribe:
                type: str
                description: 'Enable/disable block SUBSCRIBE requests.'
                choices:
                    - 'disable'
                    - 'enable'
            block-unknown:
                type: str
                description: 'Block unrecognized SIP requests (enabled by default).'
                choices:
                    - 'disable'
                    - 'enable'
            block-update:
                type: str
                description: 'Enable/disable block UPDATE requests.'
                choices:
                    - 'disable'
                    - 'enable'
            bye-rate:
                type: int
                description: 'BYE request rate limit (per second, per policy).'
            call-keepalive:
                type: int
                description: 'Continue tracking calls with no RTP for this many minutes.'
            cancel-rate:
                type: int
                description: 'CANCEL request rate limit (per second, per policy).'
            contact-fixup:
                type: str
                description: 'Fixup contact anyway even if contacts IP:port doesnt match sessions IP:port.'
                choices:
                    - 'disable'
                    - 'enable'
            hnt-restrict-source-ip:
                type: str
                description: 'Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.'
                choices:
                    - 'disable'
                    - 'enable'
            hosted-nat-traversal:
                type: str
                description: 'Hosted NAT Traversal (HNT).'
                choices:
                    - 'disable'
                    - 'enable'
            info-rate:
                type: int
                description: 'INFO request rate limit (per second, per policy).'
            invite-rate:
                type: int
                description: 'INVITE request rate limit (per second, per policy).'
            ips-rtp:
                type: str
                description: 'Enable/disable allow IPS on RTP.'
                choices:
                    - 'disable'
                    - 'enable'
            log-call-summary:
                type: str
                description: 'Enable/disable logging of SIP call summary.'
                choices:
                    - 'disable'
                    - 'enable'
            log-violations:
                type: str
                description: 'Enable/disable logging of SIP violations.'
                choices:
                    - 'disable'
                    - 'enable'
            malformed-header-allow:
                type: str
                description: 'Action for malformed Allow header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-call-id:
                type: str
                description: 'Action for malformed Call-ID header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-contact:
                type: str
                description: 'Action for malformed Contact header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-content-length:
                type: str
                description: 'Action for malformed Content-Length header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-content-type:
                type: str
                description: 'Action for malformed Content-Type header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-cseq:
                type: str
                description: 'Action for malformed CSeq header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-expires:
                type: str
                description: 'Action for malformed Expires header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-from:
                type: str
                description: 'Action for malformed From header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-max-forwards:
                type: str
                description: 'Action for malformed Max-Forwards header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-p-asserted-identity:
                type: str
                description: 'Action for malformed P-Asserted-Identity header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-rack:
                type: str
                description: 'Action for malformed RAck header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-record-route:
                type: str
                description: 'Action for malformed Record-Route header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-route:
                type: str
                description: 'Action for malformed Route header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-rseq:
                type: str
                description: 'Action for malformed RSeq header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-a:
                type: str
                description: 'Action for malformed SDP a line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-b:
                type: str
                description: 'Action for malformed SDP b line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-c:
                type: str
                description: 'Action for malformed SDP c line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-i:
                type: str
                description: 'Action for malformed SDP i line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-k:
                type: str
                description: 'Action for malformed SDP k line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-m:
                type: str
                description: 'Action for malformed SDP m line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-o:
                type: str
                description: 'Action for malformed SDP o line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-r:
                type: str
                description: 'Action for malformed SDP r line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-s:
                type: str
                description: 'Action for malformed SDP s line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-t:
                type: str
                description: 'Action for malformed SDP t line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-v:
                type: str
                description: 'Action for malformed SDP v line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-sdp-z:
                type: str
                description: 'Action for malformed SDP z line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-to:
                type: str
                description: 'Action for malformed To header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-header-via:
                type: str
                description: 'Action for malformed VIA header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            malformed-request-line:
                type: str
                description: 'Action for malformed request line.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            max-body-length:
                type: int
                description: 'Maximum SIP message body length (0 meaning no limit).'
            max-dialogs:
                type: int
                description: 'Maximum number of concurrent calls/dialogs (per policy).'
            max-idle-dialogs:
                type: int
                description: 'Maximum number established but idle dialogs to retain (per policy).'
            max-line-length:
                type: int
                description: 'Maximum SIP header line length (78-4096).'
            message-rate:
                type: int
                description: 'MESSAGE request rate limit (per second, per policy).'
            nat-trace:
                type: str
                description: 'Enable/disable preservation of original IP in SDP i line.'
                choices:
                    - 'disable'
                    - 'enable'
            no-sdp-fixup:
                type: str
                description: 'Enable/disable no SDP fix-up.'
                choices:
                    - 'disable'
                    - 'enable'
            notify-rate:
                type: int
                description: 'NOTIFY request rate limit (per second, per policy).'
            open-contact-pinhole:
                type: str
                description: 'Enable/disable open pinhole for non-REGISTER Contact port.'
                choices:
                    - 'disable'
                    - 'enable'
            open-record-route-pinhole:
                type: str
                description: 'Enable/disable open pinhole for Record-Route port.'
                choices:
                    - 'disable'
                    - 'enable'
            open-register-pinhole:
                type: str
                description: 'Enable/disable open pinhole for REGISTER Contact port.'
                choices:
                    - 'disable'
                    - 'enable'
            open-via-pinhole:
                type: str
                description: 'Enable/disable open pinhole for Via port.'
                choices:
                    - 'disable'
                    - 'enable'
            options-rate:
                type: int
                description: 'OPTIONS request rate limit (per second, per policy).'
            prack-rate:
                type: int
                description: 'PRACK request rate limit (per second, per policy).'
            preserve-override:
                type: str
                description: 'Override i line to preserve original IPS (default: append).'
                choices:
                    - 'disable'
                    - 'enable'
            provisional-invite-expiry-time:
                type: int
                description: 'Expiry time for provisional INVITE (10 - 3600 sec).'
            publish-rate:
                type: int
                description: 'PUBLISH request rate limit (per second, per policy).'
            refer-rate:
                type: int
                description: 'REFER request rate limit (per second, per policy).'
            register-contact-trace:
                type: str
                description: 'Enable/disable trace original IP/port within the contact header of REGISTER requests.'
                choices:
                    - 'disable'
                    - 'enable'
            register-rate:
                type: int
                description: 'REGISTER request rate limit (per second, per policy).'
            rfc2543-branch:
                type: str
                description: 'Enable/disable support via branch compliant with RFC 2543.'
                choices:
                    - 'disable'
                    - 'enable'
            rtp:
                type: str
                description: 'Enable/disable create pinholes for RTP traffic to traverse firewall.'
                choices:
                    - 'disable'
                    - 'enable'
            ssl-algorithm:
                type: str
                description: 'Relative strength of encryption algorithms accepted in negotiation.'
                choices:
                    - 'high'
                    - 'medium'
                    - 'low'
            ssl-auth-client:
                type: str
                description: 'Require a client certificate and authenticate it with the peer/peergrp.'
            ssl-auth-server:
                type: str
                description: 'Authenticate the servers certificate with the peer/peergrp.'
            ssl-client-certificate:
                type: str
                description: 'Name of Certificate to offer to server if requested.'
            ssl-client-renegotiation:
                type: str
                description: 'Allow/block client renegotiation by server.'
                choices:
                    - 'allow'
                    - 'deny'
                    - 'secure'
            ssl-max-version:
                type: str
                description: 'Highest SSL/TLS version to negotiate.'
                choices:
                    - 'ssl-3.0'
                    - 'tls-1.0'
                    - 'tls-1.1'
                    - 'tls-1.2'
            ssl-min-version:
                type: str
                description: 'Lowest SSL/TLS version to negotiate.'
                choices:
                    - 'ssl-3.0'
                    - 'tls-1.0'
                    - 'tls-1.1'
                    - 'tls-1.2'
            ssl-mode:
                type: str
                description: 'SSL/TLS mode for encryption & decryption of traffic.'
                choices:
                    - 'off'
                    - 'full'
            ssl-pfs:
                type: str
                description: 'SSL Perfect Forward Secrecy.'
                choices:
                    - 'require'
                    - 'deny'
                    - 'allow'
            ssl-send-empty-frags:
                type: str
                description: 'Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).'
                choices:
                    - 'disable'
                    - 'enable'
            ssl-server-certificate:
                type: str
                description: 'Name of Certificate return to the client in every SSL connection.'
            status:
                type: str
                description: 'Enable/disable SIP.'
                choices:
                    - 'disable'
                    - 'enable'
            strict-register:
                type: str
                description: 'Enable/disable only allow the registrar to connect.'
                choices:
                    - 'disable'
                    - 'enable'
            subscribe-rate:
                type: int
                description: 'SUBSCRIBE request rate limit (per second, per policy).'
            unknown-header:
                type: str
                description: 'Action for unknown SIP header.'
                choices:
                    - 'pass'
                    - 'discard'
                    - 'respond'
            update-rate:
                type: int
                description: 'UPDATE request rate limit (per second, per policy).'

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
    - name: SIP.
      fmgr_voip_profile_sip:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         profile: <your own value>
         voip_profile_sip:
            ack-rate: <value of integer>
            block-ack: <value in [disable, enable]>
            block-bye: <value in [disable, enable]>
            block-cancel: <value in [disable, enable]>
            block-geo-red-options: <value in [disable, enable]>
            block-info: <value in [disable, enable]>
            block-invite: <value in [disable, enable]>
            block-long-lines: <value in [disable, enable]>
            block-message: <value in [disable, enable]>
            block-notify: <value in [disable, enable]>
            block-options: <value in [disable, enable]>
            block-prack: <value in [disable, enable]>
            block-publish: <value in [disable, enable]>
            block-refer: <value in [disable, enable]>
            block-register: <value in [disable, enable]>
            block-subscribe: <value in [disable, enable]>
            block-unknown: <value in [disable, enable]>
            block-update: <value in [disable, enable]>
            bye-rate: <value of integer>
            call-keepalive: <value of integer>
            cancel-rate: <value of integer>
            contact-fixup: <value in [disable, enable]>
            hnt-restrict-source-ip: <value in [disable, enable]>
            hosted-nat-traversal: <value in [disable, enable]>
            info-rate: <value of integer>
            invite-rate: <value of integer>
            ips-rtp: <value in [disable, enable]>
            log-call-summary: <value in [disable, enable]>
            log-violations: <value in [disable, enable]>
            malformed-header-allow: <value in [pass, discard, respond]>
            malformed-header-call-id: <value in [pass, discard, respond]>
            malformed-header-contact: <value in [pass, discard, respond]>
            malformed-header-content-length: <value in [pass, discard, respond]>
            malformed-header-content-type: <value in [pass, discard, respond]>
            malformed-header-cseq: <value in [pass, discard, respond]>
            malformed-header-expires: <value in [pass, discard, respond]>
            malformed-header-from: <value in [pass, discard, respond]>
            malformed-header-max-forwards: <value in [pass, discard, respond]>
            malformed-header-p-asserted-identity: <value in [pass, discard, respond]>
            malformed-header-rack: <value in [pass, discard, respond]>
            malformed-header-record-route: <value in [pass, discard, respond]>
            malformed-header-route: <value in [pass, discard, respond]>
            malformed-header-rseq: <value in [pass, discard, respond]>
            malformed-header-sdp-a: <value in [pass, discard, respond]>
            malformed-header-sdp-b: <value in [pass, discard, respond]>
            malformed-header-sdp-c: <value in [pass, discard, respond]>
            malformed-header-sdp-i: <value in [pass, discard, respond]>
            malformed-header-sdp-k: <value in [pass, discard, respond]>
            malformed-header-sdp-m: <value in [pass, discard, respond]>
            malformed-header-sdp-o: <value in [pass, discard, respond]>
            malformed-header-sdp-r: <value in [pass, discard, respond]>
            malformed-header-sdp-s: <value in [pass, discard, respond]>
            malformed-header-sdp-t: <value in [pass, discard, respond]>
            malformed-header-sdp-v: <value in [pass, discard, respond]>
            malformed-header-sdp-z: <value in [pass, discard, respond]>
            malformed-header-to: <value in [pass, discard, respond]>
            malformed-header-via: <value in [pass, discard, respond]>
            malformed-request-line: <value in [pass, discard, respond]>
            max-body-length: <value of integer>
            max-dialogs: <value of integer>
            max-idle-dialogs: <value of integer>
            max-line-length: <value of integer>
            message-rate: <value of integer>
            nat-trace: <value in [disable, enable]>
            no-sdp-fixup: <value in [disable, enable]>
            notify-rate: <value of integer>
            open-contact-pinhole: <value in [disable, enable]>
            open-record-route-pinhole: <value in [disable, enable]>
            open-register-pinhole: <value in [disable, enable]>
            open-via-pinhole: <value in [disable, enable]>
            options-rate: <value of integer>
            prack-rate: <value of integer>
            preserve-override: <value in [disable, enable]>
            provisional-invite-expiry-time: <value of integer>
            publish-rate: <value of integer>
            refer-rate: <value of integer>
            register-contact-trace: <value in [disable, enable]>
            register-rate: <value of integer>
            rfc2543-branch: <value in [disable, enable]>
            rtp: <value in [disable, enable]>
            ssl-algorithm: <value in [high, medium, low]>
            ssl-auth-client: <value of string>
            ssl-auth-server: <value of string>
            ssl-client-certificate: <value of string>
            ssl-client-renegotiation: <value in [allow, deny, secure]>
            ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-mode: <value in [off, full]>
            ssl-pfs: <value in [require, deny, allow]>
            ssl-send-empty-frags: <value in [disable, enable]>
            ssl-server-certificate: <value of string>
            status: <value in [disable, enable]>
            strict-register: <value in [disable, enable]>
            subscribe-rate: <value of integer>
            unknown-header: <value in [pass, discard, respond]>
            update-rate: <value of integer>

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
        '/pm/config/adom/{adom}/obj/voip/profile/{profile}/sip',
        '/pm/config/global/obj/voip/profile/{profile}/sip'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/voip/profile/{profile}/sip/{sip}',
        '/pm/config/global/obj/voip/profile/{profile}/sip/{sip}'
    ]

    url_params = ['adom', 'profile']
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
        'profile': {
            'required': True,
            'type': 'str'
        },
        'voip_profile_sip': {
            'required': False,
            'type': 'dict',
            'options': {
                'ack-rate': {
                    'required': False,
                    'type': 'int'
                },
                'block-ack': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-bye': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-cancel': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-geo-red-options': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-info': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-invite': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-long-lines': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-message': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-notify': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-options': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-prack': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-publish': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-refer': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-register': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-subscribe': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-unknown': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'block-update': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'bye-rate': {
                    'required': False,
                    'type': 'int'
                },
                'call-keepalive': {
                    'required': False,
                    'type': 'int'
                },
                'cancel-rate': {
                    'required': False,
                    'type': 'int'
                },
                'contact-fixup': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'hnt-restrict-source-ip': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'hosted-nat-traversal': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'info-rate': {
                    'required': False,
                    'type': 'int'
                },
                'invite-rate': {
                    'required': False,
                    'type': 'int'
                },
                'ips-rtp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'log-call-summary': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'log-violations': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'malformed-header-allow': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-call-id': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-contact': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-content-length': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-content-type': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-cseq': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-expires': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-from': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-max-forwards': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-p-asserted-identity': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-rack': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-record-route': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-route': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-rseq': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-a': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-b': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-c': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-i': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-k': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-m': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-o': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-r': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-s': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-t': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-v': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-sdp-z': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-to': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-header-via': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'malformed-request-line': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'max-body-length': {
                    'required': False,
                    'type': 'int'
                },
                'max-dialogs': {
                    'required': False,
                    'type': 'int'
                },
                'max-idle-dialogs': {
                    'required': False,
                    'type': 'int'
                },
                'max-line-length': {
                    'required': False,
                    'type': 'int'
                },
                'message-rate': {
                    'required': False,
                    'type': 'int'
                },
                'nat-trace': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'no-sdp-fixup': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'notify-rate': {
                    'required': False,
                    'type': 'int'
                },
                'open-contact-pinhole': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'open-record-route-pinhole': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'open-register-pinhole': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'open-via-pinhole': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'options-rate': {
                    'required': False,
                    'type': 'int'
                },
                'prack-rate': {
                    'required': False,
                    'type': 'int'
                },
                'preserve-override': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'provisional-invite-expiry-time': {
                    'required': False,
                    'type': 'int'
                },
                'publish-rate': {
                    'required': False,
                    'type': 'int'
                },
                'refer-rate': {
                    'required': False,
                    'type': 'int'
                },
                'register-contact-trace': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'register-rate': {
                    'required': False,
                    'type': 'int'
                },
                'rfc2543-branch': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'rtp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ssl-algorithm': {
                    'required': False,
                    'choices': [
                        'high',
                        'medium',
                        'low'
                    ],
                    'type': 'str'
                },
                'ssl-auth-client': {
                    'required': False,
                    'type': 'str'
                },
                'ssl-auth-server': {
                    'required': False,
                    'type': 'str'
                },
                'ssl-client-certificate': {
                    'required': False,
                    'type': 'str'
                },
                'ssl-client-renegotiation': {
                    'required': False,
                    'choices': [
                        'allow',
                        'deny',
                        'secure'
                    ],
                    'type': 'str'
                },
                'ssl-max-version': {
                    'required': False,
                    'choices': [
                        'ssl-3.0',
                        'tls-1.0',
                        'tls-1.1',
                        'tls-1.2'
                    ],
                    'type': 'str'
                },
                'ssl-min-version': {
                    'required': False,
                    'choices': [
                        'ssl-3.0',
                        'tls-1.0',
                        'tls-1.1',
                        'tls-1.2'
                    ],
                    'type': 'str'
                },
                'ssl-mode': {
                    'required': False,
                    'choices': [
                        'off',
                        'full'
                    ],
                    'type': 'str'
                },
                'ssl-pfs': {
                    'required': False,
                    'choices': [
                        'require',
                        'deny',
                        'allow'
                    ],
                    'type': 'str'
                },
                'ssl-send-empty-frags': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ssl-server-certificate': {
                    'required': False,
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
                'strict-register': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'subscribe-rate': {
                    'required': False,
                    'type': 'int'
                },
                'unknown-header': {
                    'required': False,
                    'choices': [
                        'pass',
                        'discard',
                        'respond'
                    ],
                    'type': 'str'
                },
                'update-rate': {
                    'required': False,
                    'type': 'int'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'voip_profile_sip'),
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
