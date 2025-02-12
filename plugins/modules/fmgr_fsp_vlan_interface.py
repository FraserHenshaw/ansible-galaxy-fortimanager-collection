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
module: fmgr_fsp_vlan_interface
short_description: no description
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
    vlan:
        description: the parameter (vlan) in requested url
        type: str
        required: true
    fsp_vlan_interface:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            ac-name:
                type: str
                description: no description
            aggregate:
                type: str
                description: no description
            algorithm:
                type: str
                description: no description
                choices:
                    - 'L2'
                    - 'L3'
                    - 'L4'
            alias:
                type: str
                description: no description
            allowaccess:
                description: no description
                type: list
                choices:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - auto-ipsec
                 - radius-acct
                 - probe-response
                 - capwap
                 - dnp
                 - ftm
            ap-discover:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            arpforward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            atm-protocol:
                type: str
                description: no description
                choices:
                    - 'none'
                    - 'ipoa'
            auth-type:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - 'pap'
                    - 'chap'
                    - 'mschapv1'
                    - 'mschapv2'
            auto-auth-extension-device:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            bfd:
                type: str
                description: no description
                choices:
                    - 'global'
                    - 'enable'
                    - 'disable'
            bfd-desired-min-tx:
                type: int
                description: no description
            bfd-detect-mult:
                type: int
                description: no description
            bfd-required-min-rx:
                type: int
                description: no description
            broadcast-forticlient-discovery:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            broadcast-forward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            captive-portal:
                type: int
                description: no description
            cli-conn-status:
                type: int
                description: no description
            color:
                type: int
                description: no description
            ddns:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ddns-auth:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'tsig'
            ddns-domain:
                type: str
                description: no description
            ddns-key:
                type: str
                description: no description
            ddns-keyname:
                type: str
                description: no description
            ddns-password:
                description: no description
                type: str
            ddns-server:
                type: str
                description: no description
                choices:
                    - 'dhs.org'
                    - 'dyndns.org'
                    - 'dyns.net'
                    - 'tzo.com'
                    - 'ods.org'
                    - 'vavic.com'
                    - 'now.net.cn'
                    - 'dipdns.net'
                    - 'easydns.com'
                    - 'genericDDNS'
            ddns-server-ip:
                type: str
                description: no description
            ddns-sn:
                type: str
                description: no description
            ddns-ttl:
                type: int
                description: no description
            ddns-username:
                type: str
                description: no description
            ddns-zone:
                type: str
                description: no description
            dedicated-to:
                type: str
                description: no description
                choices:
                    - 'none'
                    - 'management'
            defaultgw:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            description:
                type: str
                description: no description
            detected-peer-mtu:
                type: int
                description: no description
            detectprotocol:
                description: no description
                type: list
                choices:
                 - ping
                 - tcp-echo
                 - udp-echo
            detectserver:
                type: str
                description: no description
            device-access-list:
                type: str
                description: no description
            device-identification:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            device-identification-active-scan:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            device-netscan:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            device-user-identification:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            devindex:
                type: int
                description: no description
            dhcp-client-identifier:
                type: str
                description: no description
            dhcp-relay-agent-option:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-ip:
                description: no description
                type: str
            dhcp-relay-service:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-type:
                type: str
                description: no description
                choices:
                    - 'regular'
                    - 'ipsec'
            dhcp-renew-time:
                type: int
                description: no description
            disc-retry-timeout:
                type: int
                description: no description
            disconnect-threshold:
                type: int
                description: no description
            distance:
                type: int
                description: no description
            dns-query:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'recursive'
                    - 'non-recursive'
            dns-server-override:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            drop-fragment:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            drop-overlapped-fragment:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            egress-cos:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'cos0'
                    - 'cos1'
                    - 'cos2'
                    - 'cos3'
                    - 'cos4'
                    - 'cos5'
                    - 'cos6'
                    - 'cos7'
            egress-shaping-profile:
                type: str
                description: no description
            endpoint-compliance:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            estimated-downstream-bandwidth:
                type: int
                description: no description
            estimated-upstream-bandwidth:
                type: int
                description: no description
            explicit-ftp-proxy:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            explicit-web-proxy:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            external:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fail-action-on-extender:
                type: str
                description: no description
                choices:
                    - 'soft-restart'
                    - 'hard-restart'
                    - 'reboot'
            fail-alert-interfaces:
                type: str
                description: no description
            fail-alert-method:
                type: str
                description: no description
                choices:
                    - 'link-failed-signal'
                    - 'link-down'
            fail-detect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fail-detect-option:
                description: no description
                type: list
                choices:
                 - detectserver
                 - link-down
            fdp:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fortiheartbeat:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fortilink:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fortilink-backup-link:
                type: int
                description: no description
            fortilink-split-interface:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fortilink-stacking:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            forward-domain:
                type: int
                description: no description
            forward-error-correction:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
                    - 'rs-fec'
                    - 'base-r-fec'
            fp-anomaly:
                description: no description
                type: list
                choices:
                 - drop_tcp_fin_noack
                 - pass_winnuke
                 - pass_tcpland
                 - pass_udpland
                 - pass_icmpland
                 - pass_ipland
                 - pass_iprr
                 - pass_ipssrr
                 - pass_iplsrr
                 - pass_ipstream
                 - pass_ipsecurity
                 - pass_iptimestamp
                 - pass_ipunknown_option
                 - pass_ipunknown_prot
                 - pass_icmp_frag
                 - pass_tcp_no_flag
                 - pass_tcp_fin_noack
                 - drop_winnuke
                 - drop_tcpland
                 - drop_udpland
                 - drop_icmpland
                 - drop_ipland
                 - drop_iprr
                 - drop_ipssrr
                 - drop_iplsrr
                 - drop_ipstream
                 - drop_ipsecurity
                 - drop_iptimestamp
                 - drop_ipunknown_option
                 - drop_ipunknown_prot
                 - drop_icmp_frag
                 - drop_tcp_no_flag
            fp-disable:
                description: no description
                type: list
                choices:
                 - all
                 - ipsec
                 - none
            gateway-address:
                type: str
                description: no description
            gi-gk:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            gwaddr:
                type: str
                description: no description
            gwdetect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ha-priority:
                type: int
                description: no description
            icmp-accept-redirect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            icmp-redirect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            icmp-send-redirect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ident-accept:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            idle-timeout:
                type: int
                description: no description
            if-mdix:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - 'normal'
                    - 'crossover'
            if-media:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - 'copper'
                    - 'fiber'
            in-force-vlan-cos:
                type: int
                description: no description
            inbandwidth:
                type: int
                description: no description
            ingress-cos:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'cos0'
                    - 'cos1'
                    - 'cos2'
                    - 'cos3'
                    - 'cos4'
                    - 'cos5'
                    - 'cos6'
                    - 'cos7'
            ingress-spillover-threshold:
                type: int
                description: no description
            internal:
                type: int
                description: no description
            ip:
                type: str
                description: no description
            ipmac:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ips-sniffer-mode:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ipunnumbered:
                type: str
                description: no description
            ipv6:
                description: no description
                type: dict
                required: false
                suboptions:
                    autoconf:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-client-options:
                        description: no description
                        type: list
                        choices:
                         - rapid
                         - iapd
                         - iana
                         - dns
                         - dnsname
                    dhcp6-information-request:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-delegation:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-hint:
                        type: str
                        description: no description
                    dhcp6-prefix-hint-plt:
                        type: int
                        description: no description
                    dhcp6-prefix-hint-vlt:
                        type: int
                        description: no description
                    dhcp6-relay-ip:
                        type: str
                        description: no description
                    dhcp6-relay-service:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-relay-type:
                        type: str
                        description: no description
                        choices:
                            - 'regular'
                    ip6-address:
                        type: str
                        description: no description
                    ip6-allowaccess:
                        description: no description
                        type: list
                        choices:
                         - https
                         - ping
                         - ssh
                         - snmp
                         - http
                         - telnet
                         - fgfm
                         - capwap
                    ip6-default-life:
                        type: int
                        description: no description
                    ip6-dns-server-override:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-hop-limit:
                        type: int
                        description: no description
                    ip6-link-mtu:
                        type: int
                        description: no description
                    ip6-manage-flag:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-max-interval:
                        type: int
                        description: no description
                    ip6-min-interval:
                        type: int
                        description: no description
                    ip6-mode:
                        type: str
                        description: no description
                        choices:
                            - 'static'
                            - 'dhcp'
                            - 'pppoe'
                            - 'delegated'
                    ip6-other-flag:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-reachable-time:
                        type: int
                        description: no description
                    ip6-retrans-time:
                        type: int
                        description: no description
                    ip6-send-adv:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-subnet:
                        type: str
                        description: no description
                    ip6-upstream-interface:
                        type: str
                        description: no description
                    nd-cert:
                        type: str
                        description: no description
                    nd-cga-modifier:
                        type: str
                        description: no description
                    nd-mode:
                        type: str
                        description: no description
                        choices:
                            - 'basic'
                            - 'SEND-compatible'
                    nd-security-level:
                        type: int
                        description: no description
                    nd-timestamp-delta:
                        type: int
                        description: no description
                    nd-timestamp-fuzz:
                        type: int
                        description: no description
                    vrip6_link_local:
                        type: str
                        description: no description
                    vrrp-virtual-mac6:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
            l2forward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            l2tp-client:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            lacp-ha-slave:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            lacp-mode:
                type: str
                description: no description
                choices:
                    - 'static'
                    - 'passive'
                    - 'active'
            lacp-speed:
                type: str
                description: no description
                choices:
                    - 'slow'
                    - 'fast'
            lcp-echo-interval:
                type: int
                description: no description
            lcp-max-echo-fails:
                type: int
                description: no description
            link-up-delay:
                type: int
                description: no description
            listen-forticlient-connection:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            lldp-network-policy:
                type: str
                description: no description
            lldp-reception:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
                    - 'vdom'
            lldp-transmission:
                type: str
                description: no description
                choices:
                    - 'enable'
                    - 'disable'
                    - 'vdom'
            log:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            macaddr:
                type: str
                description: no description
            management-ip:
                type: str
                description: no description
            max-egress-burst-rate:
                type: int
                description: no description
            max-egress-rate:
                type: int
                description: no description
            mediatype:
                type: str
                description: no description
                choices:
                    - 'serdes-sfp'
                    - 'sgmii-sfp'
                    - 'cfp2-sr10'
                    - 'cfp2-lr4'
                    - 'serdes-copper-sfp'
                    - 'sr'
                    - 'cr'
                    - 'lr'
                    - 'qsfp28-sr4'
                    - 'qsfp28-lr4'
                    - 'qsfp28-cr4'
            member:
                type: str
                description: no description
            min-links:
                type: int
                description: no description
            min-links-down:
                type: str
                description: no description
                choices:
                    - 'operational'
                    - 'administrative'
            mode:
                type: str
                description: no description
                choices:
                    - 'static'
                    - 'dhcp'
                    - 'pppoe'
                    - 'pppoa'
                    - 'ipoa'
                    - 'eoa'
            mtu:
                type: int
                description: no description
            mtu-override:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mux-type:
                type: str
                description: no description
                choices:
                    - 'llc-encaps'
                    - 'vc-encaps'
            name:
                type: str
                description: no description
            ndiscforward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            netbios-forward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            netflow-sampler:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'tx'
                    - 'rx'
                    - 'both'
            npu-fastpath:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            nst:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            out-force-vlan-cos:
                type: int
                description: no description
            outbandwidth:
                type: int
                description: no description
            padt-retry-timeout:
                type: int
                description: no description
            password:
                description: no description
                type: str
            peer-interface:
                type: str
                description: no description
            phy-mode:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - 'adsl'
                    - 'vdsl'
            ping-serv-status:
                type: int
                description: no description
            poe:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            polling-interval:
                type: int
                description: no description
            pppoe-unnumbered-negotiate:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            pptp-auth-type:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - 'pap'
                    - 'chap'
                    - 'mschapv1'
                    - 'mschapv2'
            pptp-client:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            pptp-password:
                description: no description
                type: str
            pptp-server-ip:
                type: str
                description: no description
            pptp-timeout:
                type: int
                description: no description
            pptp-user:
                type: str
                description: no description
            preserve-session-route:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            priority:
                type: int
                description: no description
            priority-override:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            proxy-captive-portal:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            redundant-interface:
                type: str
                description: no description
            remote-ip:
                type: str
                description: no description
            replacemsg-override-group:
                type: str
                description: no description
            retransmission:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            role:
                type: str
                description: no description
                choices:
                    - 'lan'
                    - 'wan'
                    - 'dmz'
                    - 'undefined'
            sample-direction:
                type: str
                description: no description
                choices:
                    - 'rx'
                    - 'tx'
                    - 'both'
            sample-rate:
                type: int
                description: no description
            scan-botnet-connections:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'block'
                    - 'monitor'
            secondary-IP:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            secondaryip:
                description: no description
                type: list
                suboptions:
                    allowaccess:
                        description: no description
                        type: list
                        choices:
                         - https
                         - ping
                         - ssh
                         - snmp
                         - http
                         - telnet
                         - fgfm
                         - auto-ipsec
                         - radius-acct
                         - probe-response
                         - capwap
                         - dnp
                         - ftm
                    detectprotocol:
                        description: no description
                        type: list
                        choices:
                         - ping
                         - tcp-echo
                         - udp-echo
                    detectserver:
                        type: str
                        description: no description
                    gwdetect:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    ha-priority:
                        type: int
                        description: no description
                    id:
                        type: int
                        description: no description
                    ip:
                        type: str
                        description: no description
                    ping-serv-status:
                        type: int
                        description: no description
                    seq:
                        type: int
                        description: no description
            security-8021x-dynamic-vlan-id:
                type: int
                description: no description
            security-8021x-master:
                type: str
                description: no description
            security-8021x-mode:
                type: str
                description: no description
                choices:
                    - 'default'
                    - 'dynamic-vlan'
                    - 'fallback'
                    - 'slave'
            security-exempt-list:
                type: str
                description: no description
            security-external-logout:
                type: str
                description: no description
            security-external-web:
                type: str
                description: no description
            security-groups:
                type: str
                description: no description
            security-mac-auth-bypass:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
                    - 'mac-auth-only'
            security-mode:
                type: str
                description: no description
                choices:
                    - 'none'
                    - 'captive-portal'
                    - '802.1X'
            security-redirect-url:
                type: str
                description: no description
            service-name:
                type: str
                description: no description
            sflow-sampler:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            speed:
                type: str
                description: no description
                choices:
                    - 'auto'
                    - '10full'
                    - '10half'
                    - '100full'
                    - '100half'
                    - '1000full'
                    - '1000half'
                    - '10000full'
                    - '1000auto'
                    - '10000auto'
                    - '40000full'
                    - '100Gfull'
                    - '25000full'
                    - '40000auto'
                    - '25000auto'
                    - '100Gauto'
            spillover-threshold:
                type: int
                description: no description
            src-check:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            status:
                type: str
                description: no description
                choices:
                    - 'down'
                    - 'up'
            stp:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            stp-ha-slave:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
                    - 'priority-adjust'
            stpforward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            stpforward-mode:
                type: str
                description: no description
                choices:
                    - 'rpl-all-ext-id'
                    - 'rpl-bridge-ext-id'
                    - 'rpl-nothing'
            strip-priority-vlan-tag:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            subst:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            substitute-dst-mac:
                type: str
                description: no description
            switch:
                type: str
                description: no description
            switch-controller-access-vlan:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-arp-inspection:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-auth:
                type: str
                description: no description
                choices:
                    - 'radius'
                    - 'usergroup'
            switch-controller-dhcp-snooping:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-dhcp-snooping-option82:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-dhcp-snooping-verify-mac:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-igmp-snooping:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-learning-limit:
                type: int
                description: no description
            switch-controller-radius-server:
                type: str
                description: no description
            switch-controller-traffic-policy:
                type: str
                description: no description
            tc-mode:
                type: str
                description: no description
                choices:
                    - 'ptm'
                    - 'atm'
            tcp-mss:
                type: int
                description: no description
            trunk:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            trust-ip-1:
                type: str
                description: no description
            trust-ip-2:
                type: str
                description: no description
            trust-ip-3:
                type: str
                description: no description
            trust-ip6-1:
                type: str
                description: no description
            trust-ip6-2:
                type: str
                description: no description
            trust-ip6-3:
                type: str
                description: no description
            type:
                type: str
                description: no description
                choices:
                    - 'physical'
                    - 'vlan'
                    - 'aggregate'
                    - 'redundant'
                    - 'tunnel'
                    - 'wireless'
                    - 'vdom-link'
                    - 'loopback'
                    - 'switch'
                    - 'hard-switch'
                    - 'hdlc'
                    - 'vap-switch'
                    - 'wl-mesh'
                    - 'fortilink'
                    - 'switch-vlan'
                    - 'fctrl-trunk'
                    - 'tdm'
                    - 'fext-wan'
                    - 'vxlan'
                    - 'emac-vlan'
            username:
                type: str
                description: no description
            vci:
                type: int
                description: no description
            vectoring:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            vindex:
                type: int
                description: no description
            vlanforward:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            vlanid:
                type: int
                description: no description
            vpi:
                type: int
                description: no description
            vrf:
                type: int
                description: no description
            vrrp:
                description: no description
                type: list
                suboptions:
                    accept-mode:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    adv-interval:
                        type: int
                        description: no description
                    ignore-default-route:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    preempt:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    priority:
                        type: int
                        description: no description
                    start-time:
                        type: int
                        description: no description
                    status:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
                    version:
                        type: str
                        description: no description
                        choices:
                            - '2'
                            - '3'
                    vrdst:
                        description: no description
                        type: str
                    vrdst-priority:
                        type: int
                        description: no description
                    vrgrp:
                        type: int
                        description: no description
                    vrid:
                        type: int
                        description: no description
                    vrip:
                        type: str
                        description: no description
            vrrp-virtual-mac:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            wccp:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            weight:
                type: int
                description: no description
            wifi-5g-threshold:
                type: str
                description: no description
            wifi-acl:
                type: str
                description: no description
                choices:
                    - 'deny'
                    - 'allow'
            wifi-ap-band:
                type: str
                description: no description
                choices:
                    - 'any'
                    - '5g-preferred'
                    - '5g-only'
            wifi-auth:
                type: str
                description: no description
                choices:
                    - 'PSK'
                    - 'RADIUS'
                    - 'radius'
                    - 'usergroup'
            wifi-auto-connect:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            wifi-auto-save:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            wifi-broadcast-ssid:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            wifi-encrypt:
                type: str
                description: no description
                choices:
                    - 'TKIP'
                    - 'AES'
            wifi-fragment-threshold:
                type: int
                description: no description
            wifi-key:
                description: no description
                type: str
            wifi-keyindex:
                type: int
                description: no description
            wifi-mac-filter:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            wifi-passphrase:
                description: no description
                type: str
            wifi-radius-server:
                type: str
                description: no description
            wifi-rts-threshold:
                type: int
                description: no description
            wifi-security:
                type: str
                description: no description
                choices:
                    - 'None'
                    - 'WEP64'
                    - 'wep64'
                    - 'WEP128'
                    - 'wep128'
                    - 'WPA_PSK'
                    - 'WPA_RADIUS'
                    - 'WPA'
                    - 'WPA2'
                    - 'WPA2_AUTO'
                    - 'open'
                    - 'wpa-personal'
                    - 'wpa-enterprise'
                    - 'wpa-only-personal'
                    - 'wpa-only-enterprise'
                    - 'wpa2-only-personal'
                    - 'wpa2-only-enterprise'
            wifi-ssid:
                type: str
                description: no description
            wifi-usergroup:
                type: str
                description: no description
            wins-ip:
                type: str
                description: no description

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
    - name: no description
      fmgr_fsp_vlan_interface:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         fsp_vlan_interface:
            ac-name: <value of string>
            aggregate: <value of string>
            algorithm: <value in [L2, L3, L4]>
            alias: <value of string>
            allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
            ap-discover: <value in [disable, enable]>
            arpforward: <value in [disable, enable]>
            atm-protocol: <value in [none, ipoa]>
            auth-type: <value in [auto, pap, chap, ...]>
            auto-auth-extension-device: <value in [disable, enable]>
            bfd: <value in [global, enable, disable]>
            bfd-desired-min-tx: <value of integer>
            bfd-detect-mult: <value of integer>
            bfd-required-min-rx: <value of integer>
            broadcast-forticlient-discovery: <value in [disable, enable]>
            broadcast-forward: <value in [disable, enable]>
            captive-portal: <value of integer>
            cli-conn-status: <value of integer>
            color: <value of integer>
            ddns: <value in [disable, enable]>
            ddns-auth: <value in [disable, tsig]>
            ddns-domain: <value of string>
            ddns-key: <value of string>
            ddns-keyname: <value of string>
            ddns-password: <value of string>
            ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
            ddns-server-ip: <value of string>
            ddns-sn: <value of string>
            ddns-ttl: <value of integer>
            ddns-username: <value of string>
            ddns-zone: <value of string>
            dedicated-to: <value in [none, management]>
            defaultgw: <value in [disable, enable]>
            description: <value of string>
            detected-peer-mtu: <value of integer>
            detectprotocol:
              - ping
              - tcp-echo
              - udp-echo
            detectserver: <value of string>
            device-access-list: <value of string>
            device-identification: <value in [disable, enable]>
            device-identification-active-scan: <value in [disable, enable]>
            device-netscan: <value in [disable, enable]>
            device-user-identification: <value in [disable, enable]>
            devindex: <value of integer>
            dhcp-client-identifier: <value of string>
            dhcp-relay-agent-option: <value in [disable, enable]>
            dhcp-relay-ip: <value of string>
            dhcp-relay-service: <value in [disable, enable]>
            dhcp-relay-type: <value in [regular, ipsec]>
            dhcp-renew-time: <value of integer>
            disc-retry-timeout: <value of integer>
            disconnect-threshold: <value of integer>
            distance: <value of integer>
            dns-query: <value in [disable, recursive, non-recursive]>
            dns-server-override: <value in [disable, enable]>
            drop-fragment: <value in [disable, enable]>
            drop-overlapped-fragment: <value in [disable, enable]>
            egress-cos: <value in [disable, cos0, cos1, ...]>
            egress-shaping-profile: <value of string>
            endpoint-compliance: <value in [disable, enable]>
            estimated-downstream-bandwidth: <value of integer>
            estimated-upstream-bandwidth: <value of integer>
            explicit-ftp-proxy: <value in [disable, enable]>
            explicit-web-proxy: <value in [disable, enable]>
            external: <value in [disable, enable]>
            fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
            fail-alert-interfaces: <value of string>
            fail-alert-method: <value in [link-failed-signal, link-down]>
            fail-detect: <value in [disable, enable]>
            fail-detect-option:
              - detectserver
              - link-down
            fdp: <value in [disable, enable]>
            fortiheartbeat: <value in [disable, enable]>
            fortilink: <value in [disable, enable]>
            fortilink-backup-link: <value of integer>
            fortilink-split-interface: <value in [disable, enable]>
            fortilink-stacking: <value in [disable, enable]>
            forward-domain: <value of integer>
            forward-error-correction: <value in [disable, enable, rs-fec, ...]>
            fp-anomaly:
              - drop_tcp_fin_noack
              - pass_winnuke
              - pass_tcpland
              - pass_udpland
              - pass_icmpland
              - pass_ipland
              - pass_iprr
              - pass_ipssrr
              - pass_iplsrr
              - pass_ipstream
              - pass_ipsecurity
              - pass_iptimestamp
              - pass_ipunknown_option
              - pass_ipunknown_prot
              - pass_icmp_frag
              - pass_tcp_no_flag
              - pass_tcp_fin_noack
              - drop_winnuke
              - drop_tcpland
              - drop_udpland
              - drop_icmpland
              - drop_ipland
              - drop_iprr
              - drop_ipssrr
              - drop_iplsrr
              - drop_ipstream
              - drop_ipsecurity
              - drop_iptimestamp
              - drop_ipunknown_option
              - drop_ipunknown_prot
              - drop_icmp_frag
              - drop_tcp_no_flag
            fp-disable:
              - all
              - ipsec
              - none
            gateway-address: <value of string>
            gi-gk: <value in [disable, enable]>
            gwaddr: <value of string>
            gwdetect: <value in [disable, enable]>
            ha-priority: <value of integer>
            icmp-accept-redirect: <value in [disable, enable]>
            icmp-redirect: <value in [disable, enable]>
            icmp-send-redirect: <value in [disable, enable]>
            ident-accept: <value in [disable, enable]>
            idle-timeout: <value of integer>
            if-mdix: <value in [auto, normal, crossover]>
            if-media: <value in [auto, copper, fiber]>
            in-force-vlan-cos: <value of integer>
            inbandwidth: <value of integer>
            ingress-cos: <value in [disable, cos0, cos1, ...]>
            ingress-spillover-threshold: <value of integer>
            internal: <value of integer>
            ip: <value of string>
            ipmac: <value in [disable, enable]>
            ips-sniffer-mode: <value in [disable, enable]>
            ipunnumbered: <value of string>
            ipv6:
               autoconf: <value in [disable, enable]>
               dhcp6-client-options:
                 - rapid
                 - iapd
                 - iana
                 - dns
                 - dnsname
               dhcp6-information-request: <value in [disable, enable]>
               dhcp6-prefix-delegation: <value in [disable, enable]>
               dhcp6-prefix-hint: <value of string>
               dhcp6-prefix-hint-plt: <value of integer>
               dhcp6-prefix-hint-vlt: <value of integer>
               dhcp6-relay-ip: <value of string>
               dhcp6-relay-service: <value in [disable, enable]>
               dhcp6-relay-type: <value in [regular]>
               ip6-address: <value of string>
               ip6-allowaccess:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
               ip6-default-life: <value of integer>
               ip6-dns-server-override: <value in [disable, enable]>
               ip6-hop-limit: <value of integer>
               ip6-link-mtu: <value of integer>
               ip6-manage-flag: <value in [disable, enable]>
               ip6-max-interval: <value of integer>
               ip6-min-interval: <value of integer>
               ip6-mode: <value in [static, dhcp, pppoe, ...]>
               ip6-other-flag: <value in [disable, enable]>
               ip6-reachable-time: <value of integer>
               ip6-retrans-time: <value of integer>
               ip6-send-adv: <value in [disable, enable]>
               ip6-subnet: <value of string>
               ip6-upstream-interface: <value of string>
               nd-cert: <value of string>
               nd-cga-modifier: <value of string>
               nd-mode: <value in [basic, SEND-compatible]>
               nd-security-level: <value of integer>
               nd-timestamp-delta: <value of integer>
               nd-timestamp-fuzz: <value of integer>
               vrip6_link_local: <value of string>
               vrrp-virtual-mac6: <value in [disable, enable]>
            l2forward: <value in [disable, enable]>
            l2tp-client: <value in [disable, enable]>
            lacp-ha-slave: <value in [disable, enable]>
            lacp-mode: <value in [static, passive, active]>
            lacp-speed: <value in [slow, fast]>
            lcp-echo-interval: <value of integer>
            lcp-max-echo-fails: <value of integer>
            link-up-delay: <value of integer>
            listen-forticlient-connection: <value in [disable, enable]>
            lldp-network-policy: <value of string>
            lldp-reception: <value in [disable, enable, vdom]>
            lldp-transmission: <value in [enable, disable, vdom]>
            log: <value in [disable, enable]>
            macaddr: <value of string>
            management-ip: <value of string>
            max-egress-burst-rate: <value of integer>
            max-egress-rate: <value of integer>
            mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
            member: <value of string>
            min-links: <value of integer>
            min-links-down: <value in [operational, administrative]>
            mode: <value in [static, dhcp, pppoe, ...]>
            mtu: <value of integer>
            mtu-override: <value in [disable, enable]>
            mux-type: <value in [llc-encaps, vc-encaps]>
            name: <value of string>
            ndiscforward: <value in [disable, enable]>
            netbios-forward: <value in [disable, enable]>
            netflow-sampler: <value in [disable, tx, rx, ...]>
            npu-fastpath: <value in [disable, enable]>
            nst: <value in [disable, enable]>
            out-force-vlan-cos: <value of integer>
            outbandwidth: <value of integer>
            padt-retry-timeout: <value of integer>
            password: <value of string>
            peer-interface: <value of string>
            phy-mode: <value in [auto, adsl, vdsl]>
            ping-serv-status: <value of integer>
            poe: <value in [disable, enable]>
            polling-interval: <value of integer>
            pppoe-unnumbered-negotiate: <value in [disable, enable]>
            pptp-auth-type: <value in [auto, pap, chap, ...]>
            pptp-client: <value in [disable, enable]>
            pptp-password: <value of string>
            pptp-server-ip: <value of string>
            pptp-timeout: <value of integer>
            pptp-user: <value of string>
            preserve-session-route: <value in [disable, enable]>
            priority: <value of integer>
            priority-override: <value in [disable, enable]>
            proxy-captive-portal: <value in [disable, enable]>
            redundant-interface: <value of string>
            remote-ip: <value of string>
            replacemsg-override-group: <value of string>
            retransmission: <value in [disable, enable]>
            role: <value in [lan, wan, dmz, ...]>
            sample-direction: <value in [rx, tx, both]>
            sample-rate: <value of integer>
            scan-botnet-connections: <value in [disable, block, monitor]>
            secondary-IP: <value in [disable, enable]>
            secondaryip:
              -
                  allowaccess:
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                  detectprotocol:
                    - ping
                    - tcp-echo
                    - udp-echo
                  detectserver: <value of string>
                  gwdetect: <value in [disable, enable]>
                  ha-priority: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  ping-serv-status: <value of integer>
                  seq: <value of integer>
            security-8021x-dynamic-vlan-id: <value of integer>
            security-8021x-master: <value of string>
            security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
            security-exempt-list: <value of string>
            security-external-logout: <value of string>
            security-external-web: <value of string>
            security-groups: <value of string>
            security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
            security-mode: <value in [none, captive-portal, 802.1X]>
            security-redirect-url: <value of string>
            service-name: <value of string>
            sflow-sampler: <value in [disable, enable]>
            speed: <value in [auto, 10full, 10half, ...]>
            spillover-threshold: <value of integer>
            src-check: <value in [disable, enable]>
            status: <value in [down, up]>
            stp: <value in [disable, enable]>
            stp-ha-slave: <value in [disable, enable, priority-adjust]>
            stpforward: <value in [disable, enable]>
            stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
            strip-priority-vlan-tag: <value in [disable, enable]>
            subst: <value in [disable, enable]>
            substitute-dst-mac: <value of string>
            switch: <value of string>
            switch-controller-access-vlan: <value in [disable, enable]>
            switch-controller-arp-inspection: <value in [disable, enable]>
            switch-controller-auth: <value in [radius, usergroup]>
            switch-controller-dhcp-snooping: <value in [disable, enable]>
            switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
            switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
            switch-controller-igmp-snooping: <value in [disable, enable]>
            switch-controller-learning-limit: <value of integer>
            switch-controller-radius-server: <value of string>
            switch-controller-traffic-policy: <value of string>
            tc-mode: <value in [ptm, atm]>
            tcp-mss: <value of integer>
            trunk: <value in [disable, enable]>
            trust-ip-1: <value of string>
            trust-ip-2: <value of string>
            trust-ip-3: <value of string>
            trust-ip6-1: <value of string>
            trust-ip6-2: <value of string>
            trust-ip6-3: <value of string>
            type: <value in [physical, vlan, aggregate, ...]>
            username: <value of string>
            vci: <value of integer>
            vectoring: <value in [disable, enable]>
            vindex: <value of integer>
            vlanforward: <value in [disable, enable]>
            vlanid: <value of integer>
            vpi: <value of integer>
            vrf: <value of integer>
            vrrp:
              -
                  accept-mode: <value in [disable, enable]>
                  adv-interval: <value of integer>
                  ignore-default-route: <value in [disable, enable]>
                  preempt: <value in [disable, enable]>
                  priority: <value of integer>
                  start-time: <value of integer>
                  status: <value in [disable, enable]>
                  version: <value in [2, 3]>
                  vrdst: <value of string>
                  vrdst-priority: <value of integer>
                  vrgrp: <value of integer>
                  vrid: <value of integer>
                  vrip: <value of string>
            vrrp-virtual-mac: <value in [disable, enable]>
            wccp: <value in [disable, enable]>
            weight: <value of integer>
            wifi-5g-threshold: <value of string>
            wifi-acl: <value in [deny, allow]>
            wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
            wifi-auth: <value in [PSK, RADIUS, radius, ...]>
            wifi-auto-connect: <value in [disable, enable]>
            wifi-auto-save: <value in [disable, enable]>
            wifi-broadcast-ssid: <value in [disable, enable]>
            wifi-encrypt: <value in [TKIP, AES]>
            wifi-fragment-threshold: <value of integer>
            wifi-key: <value of string>
            wifi-keyindex: <value of integer>
            wifi-mac-filter: <value in [disable, enable]>
            wifi-passphrase: <value of string>
            wifi-radius-server: <value of string>
            wifi-rts-threshold: <value of integer>
            wifi-security: <value in [None, WEP64, wep64, ...]>
            wifi-ssid: <value of string>
            wifi-usergroup: <value of string>
            wins-ip: <value of string>

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
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/{interface}',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface/{interface}'
    ]

    url_params = ['adom', 'vlan']
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
        'vlan': {
            'required': True,
            'type': 'str'
        },
        'fsp_vlan_interface': {
            'required': False,
            'type': 'dict',
            'options': {
                'ac-name': {
                    'required': False,
                    'type': 'str'
                },
                'aggregate': {
                    'required': False,
                    'type': 'str'
                },
                'algorithm': {
                    'required': False,
                    'choices': [
                        'L2',
                        'L3',
                        'L4'
                    ],
                    'type': 'str'
                },
                'alias': {
                    'required': False,
                    'type': 'str'
                },
                'allowaccess': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'https',
                        'ping',
                        'ssh',
                        'snmp',
                        'http',
                        'telnet',
                        'fgfm',
                        'auto-ipsec',
                        'radius-acct',
                        'probe-response',
                        'capwap',
                        'dnp',
                        'ftm'
                    ]
                },
                'ap-discover': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'arpforward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'atm-protocol': {
                    'required': False,
                    'choices': [
                        'none',
                        'ipoa'
                    ],
                    'type': 'str'
                },
                'auth-type': {
                    'required': False,
                    'choices': [
                        'auto',
                        'pap',
                        'chap',
                        'mschapv1',
                        'mschapv2'
                    ],
                    'type': 'str'
                },
                'auto-auth-extension-device': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'bfd': {
                    'required': False,
                    'choices': [
                        'global',
                        'enable',
                        'disable'
                    ],
                    'type': 'str'
                },
                'bfd-desired-min-tx': {
                    'required': False,
                    'type': 'int'
                },
                'bfd-detect-mult': {
                    'required': False,
                    'type': 'int'
                },
                'bfd-required-min-rx': {
                    'required': False,
                    'type': 'int'
                },
                'broadcast-forticlient-discovery': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'broadcast-forward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'captive-portal': {
                    'required': False,
                    'type': 'int'
                },
                'cli-conn-status': {
                    'required': False,
                    'type': 'int'
                },
                'color': {
                    'required': False,
                    'type': 'int'
                },
                'ddns': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ddns-auth': {
                    'required': False,
                    'choices': [
                        'disable',
                        'tsig'
                    ],
                    'type': 'str'
                },
                'ddns-domain': {
                    'required': False,
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
                'ddns-password': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-server': {
                    'required': False,
                    'choices': [
                        'dhs.org',
                        'dyndns.org',
                        'dyns.net',
                        'tzo.com',
                        'ods.org',
                        'vavic.com',
                        'now.net.cn',
                        'dipdns.net',
                        'easydns.com',
                        'genericDDNS'
                    ],
                    'type': 'str'
                },
                'ddns-server-ip': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-sn': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-ttl': {
                    'required': False,
                    'type': 'int'
                },
                'ddns-username': {
                    'required': False,
                    'type': 'str'
                },
                'ddns-zone': {
                    'required': False,
                    'type': 'str'
                },
                'dedicated-to': {
                    'required': False,
                    'choices': [
                        'none',
                        'management'
                    ],
                    'type': 'str'
                },
                'defaultgw': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'description': {
                    'required': False,
                    'type': 'str'
                },
                'detected-peer-mtu': {
                    'required': False,
                    'type': 'int'
                },
                'detectprotocol': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'ping',
                        'tcp-echo',
                        'udp-echo'
                    ]
                },
                'detectserver': {
                    'required': False,
                    'type': 'str'
                },
                'device-access-list': {
                    'required': False,
                    'type': 'str'
                },
                'device-identification': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'device-identification-active-scan': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'device-netscan': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'device-user-identification': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'devindex': {
                    'required': False,
                    'type': 'int'
                },
                'dhcp-client-identifier': {
                    'required': False,
                    'type': 'str'
                },
                'dhcp-relay-agent-option': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'dhcp-relay-ip': {
                    'required': False,
                    'type': 'str'
                },
                'dhcp-relay-service': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'dhcp-relay-type': {
                    'required': False,
                    'choices': [
                        'regular',
                        'ipsec'
                    ],
                    'type': 'str'
                },
                'dhcp-renew-time': {
                    'required': False,
                    'type': 'int'
                },
                'disc-retry-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'disconnect-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'distance': {
                    'required': False,
                    'type': 'int'
                },
                'dns-query': {
                    'required': False,
                    'choices': [
                        'disable',
                        'recursive',
                        'non-recursive'
                    ],
                    'type': 'str'
                },
                'dns-server-override': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'drop-fragment': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'drop-overlapped-fragment': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'egress-cos': {
                    'required': False,
                    'choices': [
                        'disable',
                        'cos0',
                        'cos1',
                        'cos2',
                        'cos3',
                        'cos4',
                        'cos5',
                        'cos6',
                        'cos7'
                    ],
                    'type': 'str'
                },
                'egress-shaping-profile': {
                    'required': False,
                    'type': 'str'
                },
                'endpoint-compliance': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'estimated-downstream-bandwidth': {
                    'required': False,
                    'type': 'int'
                },
                'estimated-upstream-bandwidth': {
                    'required': False,
                    'type': 'int'
                },
                'explicit-ftp-proxy': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'explicit-web-proxy': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
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
                'fail-action-on-extender': {
                    'required': False,
                    'choices': [
                        'soft-restart',
                        'hard-restart',
                        'reboot'
                    ],
                    'type': 'str'
                },
                'fail-alert-interfaces': {
                    'required': False,
                    'type': 'str'
                },
                'fail-alert-method': {
                    'required': False,
                    'choices': [
                        'link-failed-signal',
                        'link-down'
                    ],
                    'type': 'str'
                },
                'fail-detect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fail-detect-option': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'detectserver',
                        'link-down'
                    ]
                },
                'fdp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fortiheartbeat': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fortilink': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fortilink-backup-link': {
                    'required': False,
                    'type': 'int'
                },
                'fortilink-split-interface': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fortilink-stacking': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'forward-domain': {
                    'required': False,
                    'type': 'int'
                },
                'forward-error-correction': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable',
                        'rs-fec',
                        'base-r-fec'
                    ],
                    'type': 'str'
                },
                'fp-anomaly': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'drop_tcp_fin_noack',
                        'pass_winnuke',
                        'pass_tcpland',
                        'pass_udpland',
                        'pass_icmpland',
                        'pass_ipland',
                        'pass_iprr',
                        'pass_ipssrr',
                        'pass_iplsrr',
                        'pass_ipstream',
                        'pass_ipsecurity',
                        'pass_iptimestamp',
                        'pass_ipunknown_option',
                        'pass_ipunknown_prot',
                        'pass_icmp_frag',
                        'pass_tcp_no_flag',
                        'pass_tcp_fin_noack',
                        'drop_winnuke',
                        'drop_tcpland',
                        'drop_udpland',
                        'drop_icmpland',
                        'drop_ipland',
                        'drop_iprr',
                        'drop_ipssrr',
                        'drop_iplsrr',
                        'drop_ipstream',
                        'drop_ipsecurity',
                        'drop_iptimestamp',
                        'drop_ipunknown_option',
                        'drop_ipunknown_prot',
                        'drop_icmp_frag',
                        'drop_tcp_no_flag'
                    ]
                },
                'fp-disable': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'all',
                        'ipsec',
                        'none'
                    ]
                },
                'gateway-address': {
                    'required': False,
                    'type': 'str'
                },
                'gi-gk': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'gwaddr': {
                    'required': False,
                    'type': 'str'
                },
                'gwdetect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ha-priority': {
                    'required': False,
                    'type': 'int'
                },
                'icmp-accept-redirect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'icmp-redirect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'icmp-send-redirect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ident-accept': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'idle-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'if-mdix': {
                    'required': False,
                    'choices': [
                        'auto',
                        'normal',
                        'crossover'
                    ],
                    'type': 'str'
                },
                'if-media': {
                    'required': False,
                    'choices': [
                        'auto',
                        'copper',
                        'fiber'
                    ],
                    'type': 'str'
                },
                'in-force-vlan-cos': {
                    'required': False,
                    'type': 'int'
                },
                'inbandwidth': {
                    'required': False,
                    'type': 'int'
                },
                'ingress-cos': {
                    'required': False,
                    'choices': [
                        'disable',
                        'cos0',
                        'cos1',
                        'cos2',
                        'cos3',
                        'cos4',
                        'cos5',
                        'cos6',
                        'cos7'
                    ],
                    'type': 'str'
                },
                'ingress-spillover-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'internal': {
                    'required': False,
                    'type': 'int'
                },
                'ip': {
                    'required': False,
                    'type': 'str'
                },
                'ipmac': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ips-sniffer-mode': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ipunnumbered': {
                    'required': False,
                    'type': 'str'
                },
                'ipv6': {
                    'required': False,
                    'type': 'dict',
                    'options': {
                        'autoconf': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'dhcp6-client-options': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'rapid',
                                'iapd',
                                'iana',
                                'dns',
                                'dnsname'
                            ]
                        },
                        'dhcp6-information-request': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'dhcp6-prefix-delegation': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'dhcp6-prefix-hint': {
                            'required': False,
                            'type': 'str'
                        },
                        'dhcp6-prefix-hint-plt': {
                            'required': False,
                            'type': 'int'
                        },
                        'dhcp6-prefix-hint-vlt': {
                            'required': False,
                            'type': 'int'
                        },
                        'dhcp6-relay-ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'dhcp6-relay-service': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'dhcp6-relay-type': {
                            'required': False,
                            'choices': [
                                'regular'
                            ],
                            'type': 'str'
                        },
                        'ip6-address': {
                            'required': False,
                            'type': 'str'
                        },
                        'ip6-allowaccess': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'https',
                                'ping',
                                'ssh',
                                'snmp',
                                'http',
                                'telnet',
                                'fgfm',
                                'capwap'
                            ]
                        },
                        'ip6-default-life': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-dns-server-override': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'ip6-hop-limit': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-link-mtu': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-manage-flag': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'ip6-max-interval': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-min-interval': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-mode': {
                            'required': False,
                            'choices': [
                                'static',
                                'dhcp',
                                'pppoe',
                                'delegated'
                            ],
                            'type': 'str'
                        },
                        'ip6-other-flag': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'ip6-reachable-time': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-retrans-time': {
                            'required': False,
                            'type': 'int'
                        },
                        'ip6-send-adv': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'ip6-subnet': {
                            'required': False,
                            'type': 'str'
                        },
                        'ip6-upstream-interface': {
                            'required': False,
                            'type': 'str'
                        },
                        'nd-cert': {
                            'required': False,
                            'type': 'str'
                        },
                        'nd-cga-modifier': {
                            'required': False,
                            'type': 'str'
                        },
                        'nd-mode': {
                            'required': False,
                            'choices': [
                                'basic',
                                'SEND-compatible'
                            ],
                            'type': 'str'
                        },
                        'nd-security-level': {
                            'required': False,
                            'type': 'int'
                        },
                        'nd-timestamp-delta': {
                            'required': False,
                            'type': 'int'
                        },
                        'nd-timestamp-fuzz': {
                            'required': False,
                            'type': 'int'
                        },
                        'vrip6_link_local': {
                            'required': False,
                            'type': 'str'
                        },
                        'vrrp-virtual-mac6': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'l2forward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'l2tp-client': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'lacp-ha-slave': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'lacp-mode': {
                    'required': False,
                    'choices': [
                        'static',
                        'passive',
                        'active'
                    ],
                    'type': 'str'
                },
                'lacp-speed': {
                    'required': False,
                    'choices': [
                        'slow',
                        'fast'
                    ],
                    'type': 'str'
                },
                'lcp-echo-interval': {
                    'required': False,
                    'type': 'int'
                },
                'lcp-max-echo-fails': {
                    'required': False,
                    'type': 'int'
                },
                'link-up-delay': {
                    'required': False,
                    'type': 'int'
                },
                'listen-forticlient-connection': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'lldp-network-policy': {
                    'required': False,
                    'type': 'str'
                },
                'lldp-reception': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable',
                        'vdom'
                    ],
                    'type': 'str'
                },
                'lldp-transmission': {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable',
                        'vdom'
                    ],
                    'type': 'str'
                },
                'log': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'macaddr': {
                    'required': False,
                    'type': 'str'
                },
                'management-ip': {
                    'required': False,
                    'type': 'str'
                },
                'max-egress-burst-rate': {
                    'required': False,
                    'type': 'int'
                },
                'max-egress-rate': {
                    'required': False,
                    'type': 'int'
                },
                'mediatype': {
                    'required': False,
                    'choices': [
                        'serdes-sfp',
                        'sgmii-sfp',
                        'cfp2-sr10',
                        'cfp2-lr4',
                        'serdes-copper-sfp',
                        'sr',
                        'cr',
                        'lr',
                        'qsfp28-sr4',
                        'qsfp28-lr4',
                        'qsfp28-cr4'
                    ],
                    'type': 'str'
                },
                'member': {
                    'required': False,
                    'type': 'str'
                },
                'min-links': {
                    'required': False,
                    'type': 'int'
                },
                'min-links-down': {
                    'required': False,
                    'choices': [
                        'operational',
                        'administrative'
                    ],
                    'type': 'str'
                },
                'mode': {
                    'required': False,
                    'choices': [
                        'static',
                        'dhcp',
                        'pppoe',
                        'pppoa',
                        'ipoa',
                        'eoa'
                    ],
                    'type': 'str'
                },
                'mtu': {
                    'required': False,
                    'type': 'int'
                },
                'mtu-override': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mux-type': {
                    'required': False,
                    'choices': [
                        'llc-encaps',
                        'vc-encaps'
                    ],
                    'type': 'str'
                },
                'name': {
                    'required': False,
                    'type': 'str'
                },
                'ndiscforward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'netbios-forward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'netflow-sampler': {
                    'required': False,
                    'choices': [
                        'disable',
                        'tx',
                        'rx',
                        'both'
                    ],
                    'type': 'str'
                },
                'npu-fastpath': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'nst': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'out-force-vlan-cos': {
                    'required': False,
                    'type': 'int'
                },
                'outbandwidth': {
                    'required': False,
                    'type': 'int'
                },
                'padt-retry-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'password': {
                    'required': False,
                    'type': 'str'
                },
                'peer-interface': {
                    'required': False,
                    'type': 'str'
                },
                'phy-mode': {
                    'required': False,
                    'choices': [
                        'auto',
                        'adsl',
                        'vdsl'
                    ],
                    'type': 'str'
                },
                'ping-serv-status': {
                    'required': False,
                    'type': 'int'
                },
                'poe': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'polling-interval': {
                    'required': False,
                    'type': 'int'
                },
                'pppoe-unnumbered-negotiate': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'pptp-auth-type': {
                    'required': False,
                    'choices': [
                        'auto',
                        'pap',
                        'chap',
                        'mschapv1',
                        'mschapv2'
                    ],
                    'type': 'str'
                },
                'pptp-client': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'pptp-password': {
                    'required': False,
                    'type': 'str'
                },
                'pptp-server-ip': {
                    'required': False,
                    'type': 'str'
                },
                'pptp-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'pptp-user': {
                    'required': False,
                    'type': 'str'
                },
                'preserve-session-route': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'priority': {
                    'required': False,
                    'type': 'int'
                },
                'priority-override': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'proxy-captive-portal': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'redundant-interface': {
                    'required': False,
                    'type': 'str'
                },
                'remote-ip': {
                    'required': False,
                    'type': 'str'
                },
                'replacemsg-override-group': {
                    'required': False,
                    'type': 'str'
                },
                'retransmission': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'role': {
                    'required': False,
                    'choices': [
                        'lan',
                        'wan',
                        'dmz',
                        'undefined'
                    ],
                    'type': 'str'
                },
                'sample-direction': {
                    'required': False,
                    'choices': [
                        'rx',
                        'tx',
                        'both'
                    ],
                    'type': 'str'
                },
                'sample-rate': {
                    'required': False,
                    'type': 'int'
                },
                'scan-botnet-connections': {
                    'required': False,
                    'choices': [
                        'disable',
                        'block',
                        'monitor'
                    ],
                    'type': 'str'
                },
                'secondary-IP': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'secondaryip': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'allowaccess': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'https',
                                'ping',
                                'ssh',
                                'snmp',
                                'http',
                                'telnet',
                                'fgfm',
                                'auto-ipsec',
                                'radius-acct',
                                'probe-response',
                                'capwap',
                                'dnp',
                                'ftm'
                            ]
                        },
                        'detectprotocol': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'ping',
                                'tcp-echo',
                                'udp-echo'
                            ]
                        },
                        'detectserver': {
                            'required': False,
                            'type': 'str'
                        },
                        'gwdetect': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'ha-priority': {
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
                        'ping-serv-status': {
                            'required': False,
                            'type': 'int'
                        },
                        'seq': {
                            'required': False,
                            'type': 'int'
                        }
                    }
                },
                'security-8021x-dynamic-vlan-id': {
                    'required': False,
                    'type': 'int'
                },
                'security-8021x-master': {
                    'required': False,
                    'type': 'str'
                },
                'security-8021x-mode': {
                    'required': False,
                    'choices': [
                        'default',
                        'dynamic-vlan',
                        'fallback',
                        'slave'
                    ],
                    'type': 'str'
                },
                'security-exempt-list': {
                    'required': False,
                    'type': 'str'
                },
                'security-external-logout': {
                    'required': False,
                    'type': 'str'
                },
                'security-external-web': {
                    'required': False,
                    'type': 'str'
                },
                'security-groups': {
                    'required': False,
                    'type': 'str'
                },
                'security-mac-auth-bypass': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable',
                        'mac-auth-only'
                    ],
                    'type': 'str'
                },
                'security-mode': {
                    'required': False,
                    'choices': [
                        'none',
                        'captive-portal',
                        '802.1X'
                    ],
                    'type': 'str'
                },
                'security-redirect-url': {
                    'required': False,
                    'type': 'str'
                },
                'service-name': {
                    'required': False,
                    'type': 'str'
                },
                'sflow-sampler': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'speed': {
                    'required': False,
                    'choices': [
                        'auto',
                        '10full',
                        '10half',
                        '100full',
                        '100half',
                        '1000full',
                        '1000half',
                        '10000full',
                        '1000auto',
                        '10000auto',
                        '40000full',
                        '100Gfull',
                        '25000full',
                        '40000auto',
                        '25000auto',
                        '100Gauto'
                    ],
                    'type': 'str'
                },
                'spillover-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'src-check': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'status': {
                    'required': False,
                    'choices': [
                        'down',
                        'up'
                    ],
                    'type': 'str'
                },
                'stp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'stp-ha-slave': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable',
                        'priority-adjust'
                    ],
                    'type': 'str'
                },
                'stpforward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'stpforward-mode': {
                    'required': False,
                    'choices': [
                        'rpl-all-ext-id',
                        'rpl-bridge-ext-id',
                        'rpl-nothing'
                    ],
                    'type': 'str'
                },
                'strip-priority-vlan-tag': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'subst': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'substitute-dst-mac': {
                    'required': False,
                    'type': 'str'
                },
                'switch': {
                    'required': False,
                    'type': 'str'
                },
                'switch-controller-access-vlan': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-arp-inspection': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-auth': {
                    'required': False,
                    'choices': [
                        'radius',
                        'usergroup'
                    ],
                    'type': 'str'
                },
                'switch-controller-dhcp-snooping': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-dhcp-snooping-option82': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-dhcp-snooping-verify-mac': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-igmp-snooping': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'switch-controller-learning-limit': {
                    'required': False,
                    'type': 'int'
                },
                'switch-controller-radius-server': {
                    'required': False,
                    'type': 'str'
                },
                'switch-controller-traffic-policy': {
                    'required': False,
                    'type': 'str'
                },
                'tc-mode': {
                    'required': False,
                    'choices': [
                        'ptm',
                        'atm'
                    ],
                    'type': 'str'
                },
                'tcp-mss': {
                    'required': False,
                    'type': 'int'
                },
                'trunk': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'trust-ip-1': {
                    'required': False,
                    'type': 'str'
                },
                'trust-ip-2': {
                    'required': False,
                    'type': 'str'
                },
                'trust-ip-3': {
                    'required': False,
                    'type': 'str'
                },
                'trust-ip6-1': {
                    'required': False,
                    'type': 'str'
                },
                'trust-ip6-2': {
                    'required': False,
                    'type': 'str'
                },
                'trust-ip6-3': {
                    'required': False,
                    'type': 'str'
                },
                'type': {
                    'required': False,
                    'choices': [
                        'physical',
                        'vlan',
                        'aggregate',
                        'redundant',
                        'tunnel',
                        'wireless',
                        'vdom-link',
                        'loopback',
                        'switch',
                        'hard-switch',
                        'hdlc',
                        'vap-switch',
                        'wl-mesh',
                        'fortilink',
                        'switch-vlan',
                        'fctrl-trunk',
                        'tdm',
                        'fext-wan',
                        'vxlan',
                        'emac-vlan'
                    ],
                    'type': 'str'
                },
                'username': {
                    'required': False,
                    'type': 'str'
                },
                'vci': {
                    'required': False,
                    'type': 'int'
                },
                'vectoring': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'vindex': {
                    'required': False,
                    'type': 'int'
                },
                'vlanforward': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'vlanid': {
                    'required': False,
                    'type': 'int'
                },
                'vpi': {
                    'required': False,
                    'type': 'int'
                },
                'vrf': {
                    'required': False,
                    'type': 'int'
                },
                'vrrp': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'accept-mode': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'adv-interval': {
                            'required': False,
                            'type': 'int'
                        },
                        'ignore-default-route': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'preempt': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'priority': {
                            'required': False,
                            'type': 'int'
                        },
                        'start-time': {
                            'required': False,
                            'type': 'int'
                        },
                        'status': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'version': {
                            'required': False,
                            'choices': [
                                '2',
                                '3'
                            ],
                            'type': 'str'
                        },
                        'vrdst': {
                            'required': False,
                            'type': 'str'
                        },
                        'vrdst-priority': {
                            'required': False,
                            'type': 'int'
                        },
                        'vrgrp': {
                            'required': False,
                            'type': 'int'
                        },
                        'vrid': {
                            'required': False,
                            'type': 'int'
                        },
                        'vrip': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'vrrp-virtual-mac': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'wccp': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'weight': {
                    'required': False,
                    'type': 'int'
                },
                'wifi-5g-threshold': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-acl': {
                    'required': False,
                    'choices': [
                        'deny',
                        'allow'
                    ],
                    'type': 'str'
                },
                'wifi-ap-band': {
                    'required': False,
                    'choices': [
                        'any',
                        '5g-preferred',
                        '5g-only'
                    ],
                    'type': 'str'
                },
                'wifi-auth': {
                    'required': False,
                    'choices': [
                        'PSK',
                        'RADIUS',
                        'radius',
                        'usergroup'
                    ],
                    'type': 'str'
                },
                'wifi-auto-connect': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'wifi-auto-save': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'wifi-broadcast-ssid': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'wifi-encrypt': {
                    'required': False,
                    'choices': [
                        'TKIP',
                        'AES'
                    ],
                    'type': 'str'
                },
                'wifi-fragment-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'wifi-key': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-keyindex': {
                    'required': False,
                    'type': 'int'
                },
                'wifi-mac-filter': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'wifi-passphrase': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-radius-server': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-rts-threshold': {
                    'required': False,
                    'type': 'int'
                },
                'wifi-security': {
                    'required': False,
                    'choices': [
                        'None',
                        'WEP64',
                        'wep64',
                        'WEP128',
                        'wep128',
                        'WPA_PSK',
                        'WPA_RADIUS',
                        'WPA',
                        'WPA2',
                        'WPA2_AUTO',
                        'open',
                        'wpa-personal',
                        'wpa-enterprise',
                        'wpa-only-personal',
                        'wpa-only-enterprise',
                        'wpa2-only-personal',
                        'wpa2-only-enterprise'
                    ],
                    'type': 'str'
                },
                'wifi-ssid': {
                    'required': False,
                    'type': 'str'
                },
                'wifi-usergroup': {
                    'required': False,
                    'type': 'str'
                },
                'wins-ip': {
                    'required': False,
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'fsp_vlan_interface'),
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
