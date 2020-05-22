#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_interface_trunk
description:
    - Trunk interface
short_description: Configures A10 interface.trunk
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    oper:
        description:
        - "Field oper"
        required: False
        suboptions:
            icmp6_rate_over_limit_drop:
                description:
                - "Field icmp6_rate_over_limit_drop"
            ipv4_addr_count:
                description:
                - "Field ipv4_addr_count"
            ipv6_link_local_type:
                description:
                - "Field ipv6_link_local_type"
            ipv6_addr_count:
                description:
                - "Field ipv6_addr_count"
            icmp_rate_over_limit_drop:
                description:
                - "Field icmp_rate_over_limit_drop"
            vlan_id:
                description:
                - "Field vlan_id"
            trunk_member:
                description:
                - "Field trunk_member"
            ipv4_address:
                description:
                - "IP address"
            ipv4_list:
                description:
                - "Field ipv4_list"
            Hardware:
                description:
                - "Field Hardware"
            ipv6_list:
                description:
                - "Field ipv6_list"
            ipv4_netmask:
                description:
                - "IP subnet mask"
            ipv6_link_local:
                description:
                - "Field ipv6_link_local"
            ifnum:
                description:
                - "Trunk interface number"
            icmp6_rate_limit_current:
                description:
                - "Field icmp6_rate_limit_current"
            state:
                description:
                - "Field state"
            icmp_rate_limit_current:
                description:
                - "Field icmp_rate_limit_current"
            igmp_query_sent:
                description:
                - "Field igmp_query_sent"
            Address:
                description:
                - "Field Address"
            ipv6_link_local_scope:
                description:
                - "Field ipv6_link_local_scope"
            line_protocol:
                description:
                - "Field line_protocol"
            ipv6_link_local_prefix:
                description:
                - "Field ipv6_link_local_prefix"
    trap_source:
        description:
        - "The trap source"
        required: False
    ip:
        description:
        - "Field ip"
        required: False
        suboptions:
            nat:
                description:
                - "Field nat"
            uuid:
                description:
                - "uuid of the object"
            address_list:
                description:
                - "Field address_list"
            generate_membership_query:
                description:
                - "Enable Membership Query"
            cache_spoofing_port:
                description:
                - "This interface connects to spoofing cache"
            router:
                description:
                - "Field router"
            allow_promiscuous_vip:
                description:
                - "Allow traffic to be associated with promiscuous VIP"
            server:
                description:
                - "Server facing interface for IPv4/v6 traffic"
            max_resp_time:
                description:
                - "Maximum Response Time (Max Response Time (Default is 100))"
            query_interval:
                description:
                - "1 - 255 (Default is 125)"
            helper_address_list:
                description:
                - "Field helper_address_list"
            stateful_firewall:
                description:
                - "Field stateful_firewall"
            client:
                description:
                - "Client facing interface for IPv4/v6 traffic"
            rip:
                description:
                - "Field rip"
            ttl_ignore:
                description:
                - "Ignore TTL decrement for a received packet"
            dhcp:
                description:
                - "Use DHCP to configure IP address"
            ospf:
                description:
                - "Field ospf"
            slb_partition_redirect:
                description:
                - "Redirect SLB traffic across partition"
    ddos:
        description:
        - "Field ddos"
        required: False
        suboptions:
            outside:
                description:
                - "DDoS inside (trusted) or outside (untrusted) interface"
            inside:
                description:
                - "DDoS inside (trusted) or outside (untrusted) interface"
            uuid:
                description:
                - "uuid of the object"
    timer:
        description:
        - "Timer to re-check the threshold under certain conditions (Time in seconds (Default= 10))"
        required: False
    access_list:
        description:
        - "Field access_list"
        required: False
        suboptions:
            acl_name:
                description:
                - "Apply an access list (Named Access List)"
            acl_id:
                description:
                - "ACL id"
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            num_tx_pkts:
                description:
                - "Field num_tx_pkts"
            dropped_dis_tx_pkts:
                description:
                - "Field dropped_dis_tx_pkts"
            num_total_tx_bytes:
                description:
                - "Field num_total_tx_bytes"
            num_multicast_pkts:
                description:
                - "Field num_multicast_pkts"
            num_unicast_pkts:
                description:
                - "Field num_unicast_pkts"
            num_broadcast_tx_pkts:
                description:
                - "Field num_broadcast_tx_pkts"
            num_broadcast_pkts:
                description:
                - "Field num_broadcast_pkts"
            num_multicast_tx_pkts:
                description:
                - "Field num_multicast_tx_pkts"
            ifnum:
                description:
                - "Trunk interface number"
            num_unicast_tx_pkts:
                description:
                - "Field num_unicast_tx_pkts"
            dropped_rx_pkts:
                description:
                - "Field dropped_rx_pkts"
            num_total_bytes:
                description:
                - "Field num_total_bytes"
            num_pkts:
                description:
                - "Field num_pkts"
            dropped_dis_rx_pkts:
                description:
                - "Field dropped_dis_rx_pkts"
            dropped_tx_pkts:
                description:
                - "Field dropped_tx_pkts"
    uuid:
        description:
        - "uuid of the object"
        required: False
    bfd:
        description:
        - "Field bfd"
        required: False
        suboptions:
            interval_cfg:
                description:
                - "Field interval_cfg"
            authentication:
                description:
                - "Field authentication"
            echo:
                description:
                - "Enable BFD Echo"
            uuid:
                description:
                - "uuid of the object"
            demand:
                description:
                - "Demand mode"
    ifnum:
        description:
        - "Trunk interface number"
        required: True
    do_auto_recovery:
        description:
        - "(Only for LACP trunks) Attempt auto-recovery after ports-treshold is triggered"
        required: False
    ipv6:
        description:
        - "Field ipv6"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
            address_list:
                description:
                - "Field address_list"
            router_adver:
                description:
                - "Field router_adver"
            rip:
                description:
                - "Field rip"
            ipv6_enable:
                description:
                - "Enable IPv6 processing"
            stateful_firewall:
                description:
                - "Field stateful_firewall"
            nat:
                description:
                - "Field nat"
            ttl_ignore:
                description:
                - "Ignore TTL decrement for a received packet"
            router:
                description:
                - "Field router"
            access_list_cfg:
                description:
                - "Field access_list_cfg"
            ospf:
                description:
                - "Field ospf"
    map:
        description:
        - "Field map"
        required: False
        suboptions:
            inside:
                description:
                - "Configure MAP inside interface (connected to MAP domains)"
            map_t_inside:
                description:
                - "Configure MAP inside interface (connected to MAP domains)"
            uuid:
                description:
                - "uuid of the object"
            map_t_outside:
                description:
                - "Configure MAP outside interface"
            outside:
                description:
                - "Configure MAP outside interface"
    ports_threshold:
        description:
        - "Threshold for the minimum number of ports that need to be UP for the trunk to remain UP"
        required: False
    nptv6:
        description:
        - "Field nptv6"
        required: False
        suboptions:
            domain_list:
                description:
                - "Field domain_list"
    icmp_rate_limit:
        description:
        - "Field icmp_rate_limit"
        required: False
        suboptions:
            lockup:
                description:
                - "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)"
            lockup_period:
                description:
                - "Lockup period (second)"
            normal:
                description:
                - "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit"
    isis:
        description:
        - "Field isis"
        required: False
        suboptions:
            priority_list:
                description:
                - "Field priority_list"
            padding:
                description:
                - "Add padding to IS-IS hello packets"
            hello_interval_minimal_list:
                description:
                - "Field hello_interval_minimal_list"
            mesh_group:
                description:
                - "Field mesh_group"
            network:
                description:
                - "'broadcast'= Specify IS-IS broadcast multi-access network; 'point-to-point'= Specify IS-IS point-to-point network; "
            authentication:
                description:
                - "Field authentication"
            csnp_interval_list:
                description:
                - "Field csnp_interval_list"
            retransmit_interval:
                description:
                - "Set per-LSP retransmission interval (Interval between retransmissions of the same LSP (seconds))"
            password_list:
                description:
                - "Field password_list"
            bfd_cfg:
                description:
                - "Field bfd_cfg"
            wide_metric_list:
                description:
                - "Field wide_metric_list"
            hello_interval_list:
                description:
                - "Field hello_interval_list"
            circuit_type:
                description:
                - "'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2 adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed; "
            hello_multiplier_list:
                description:
                - "Field hello_multiplier_list"
            metric_list:
                description:
                - "Field metric_list"
            lsp_interval:
                description:
                - "Set LSP transmission interval (LSP transmission interval (milliseconds))"
            uuid:
                description:
                - "uuid of the object"
    name:
        description:
        - "Name for the interface"
        required: False
    icmpv6_rate_limit:
        description:
        - "Field icmpv6_rate_limit"
        required: False
        suboptions:
            lockup_period_v6:
                description:
                - "Lockup period (second)"
            normal_v6:
                description:
                - "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit"
            lockup_v6:
                description:
                - "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)"
    user_tag:
        description:
        - "Customized tag"
        required: False
    mtu:
        description:
        - "Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'num_pkts'= num_pkts; 'num_total_bytes'= num_total_bytes; 'num_unicast_pkts'= num_unicast_pkts; 'num_broadcast_pkts'= num_broadcast_pkts; 'num_multicast_pkts'= num_multicast_pkts; 'num_tx_pkts'= num_tx_pkts; 'num_total_tx_bytes'= num_total_tx_bytes; 'num_unicast_tx_pkts'= num_unicast_tx_pkts; 'num_broadcast_tx_pkts'= num_broadcast_tx_pkts; 'num_multicast_tx_pkts'= num_multicast_tx_pkts; 'dropped_dis_rx_pkts'= dropped_dis_rx_pkts; 'dropped_rx_pkts'= dropped_rx_pkts; 'dropped_dis_tx_pkts'= dropped_dis_tx_pkts; 'dropped_tx_pkts'= dropped_tx_pkts; "
    lw_4o6:
        description:
        - "Field lw_4o6"
        required: False
        suboptions:
            outside:
                description:
                - "Configure LW-4over6 inside interface"
            inside:
                description:
                - "Configure LW-4over6 outside interface"
            uuid:
                description:
                - "uuid of the object"
    action:
        description:
        - "'enable'= Enable; 'disable'= Disable; "
        required: False
    l3_vlan_fwd_disable:
        description:
        - "Disable L3 forwarding between VLANs"
        required: False


'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["access_list","action","bfd","ddos","do_auto_recovery","icmp_rate_limit","icmpv6_rate_limit","ifnum","ip","ipv6","isis","l3_vlan_fwd_disable","lw_4o6","map","mtu","name","nptv6","oper","ports_threshold","sampling_enable","stats","timer","trap_source","user_tag","uuid",]

# our imports go at the top so we fail fast.
try:
    from ansible_collections.a10.acos_axapi.plugins.module_utils import errors as a10_ex
    from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import client_factory, session_factory
    from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        oper=dict(type='dict', icmp6_rate_over_limit_drop=dict(type='int', ), ipv4_addr_count=dict(type='int', ), ipv6_link_local_type=dict(type='str', ), ipv6_addr_count=dict(type='int', ), icmp_rate_over_limit_drop=dict(type='int', ), vlan_id=dict(type='int', ), trunk_member=dict(type='list', members=dict(type='int', )), ipv4_address=dict(type='str', ), ipv4_list=dict(type='list', mask=dict(type='str', ), addr=dict(type='str', )), Hardware=dict(type='str', choices=['TrunkGroup']), ipv6_list=dict(type='list', is_anycast=dict(type='int', ), prefix=dict(type='str', ), addr=dict(type='str', )), ipv4_netmask=dict(type='str', ), ipv6_link_local=dict(type='str', ), ifnum=dict(type='int', required=True, ), icmp6_rate_limit_current=dict(type='int', ), state=dict(type='str', choices=['up', 'disabled', 'down']), icmp_rate_limit_current=dict(type='int', ), igmp_query_sent=dict(type='int', ), Address=dict(type='str', ), ipv6_link_local_scope=dict(type='str', ), line_protocol=dict(type='str', choices=['up', 'down']), ipv6_link_local_prefix=dict(type='str', )),
        trap_source=dict(type='bool', ),
        ip=dict(type='dict', nat=dict(type='dict', inside=dict(type='bool', ), outside=dict(type='bool', )), uuid=dict(type='str', ), address_list=dict(type='list', ipv4_address=dict(type='str', ), ipv4_netmask=dict(type='str', )), generate_membership_query=dict(type='bool', ), cache_spoofing_port=dict(type='bool', ), router=dict(type='dict', isis=dict(type='dict', tag=dict(type='str', ), uuid=dict(type='str', ))), allow_promiscuous_vip=dict(type='bool', ), server=dict(type='bool', ), max_resp_time=dict(type='int', ), query_interval=dict(type='int', ), helper_address_list=dict(type='list', helper_address=dict(type='str', )), stateful_firewall=dict(type='dict', uuid=dict(type='str', ), class_list=dict(type='str', ), inside=dict(type='bool', ), outside=dict(type='bool', ), acl_id=dict(type='int', ), access_list=dict(type='bool', )), client=dict(type='bool', ), rip=dict(type='dict', receive_cfg=dict(type='dict', receive=dict(type='bool', ), version=dict(type='str', choices=['1', '2', '1-2'])), uuid=dict(type='str', ), receive_packet=dict(type='bool', ), split_horizon_cfg=dict(type='dict', state=dict(type='str', choices=['poisoned', 'disable', 'enable'])), authentication=dict(type='dict', key_chain=dict(type='dict', key_chain=dict(type='str', )), mode=dict(type='dict', mode=dict(type='str', choices=['md5', 'text'])), str=dict(type='dict', string=dict(type='str', ))), send_cfg=dict(type='dict', version=dict(type='str', choices=['1', '2', '1-compatible', '1-2']), send=dict(type='bool', )), send_packet=dict(type='bool', )), ttl_ignore=dict(type='bool', ), dhcp=dict(type='bool', ), ospf=dict(type='dict', ospf_ip_list=dict(type='list', dead_interval=dict(type='int', ), authentication_key=dict(type='str', ), uuid=dict(type='str', ), mtu_ignore=dict(type='bool', ), transmit_delay=dict(type='int', ), value=dict(type='str', choices=['message-digest', 'null']), priority=dict(type='int', ), authentication=dict(type='bool', ), cost=dict(type='int', ), database_filter=dict(type='str', choices=['all']), hello_interval=dict(type='int', ), ip_addr=dict(type='str', required=True, ), retransmit_interval=dict(type='int', ), message_digest_cfg=dict(type='list', md5_value=dict(type='str', ), message_digest_key=dict(type='int', ), encrypted=dict(type='str', )), out=dict(type='bool', )), ospf_global=dict(type='dict', cost=dict(type='int', ), dead_interval=dict(type='int', ), authentication_key=dict(type='str', ), network=dict(type='dict', broadcast=dict(type='bool', ), point_to_multipoint=dict(type='bool', ), non_broadcast=dict(type='bool', ), point_to_point=dict(type='bool', ), p2mp_nbma=dict(type='bool', )), mtu_ignore=dict(type='bool', ), transmit_delay=dict(type='int', ), authentication_cfg=dict(type='dict', authentication=dict(type='bool', ), value=dict(type='str', choices=['message-digest', 'null'])), retransmit_interval=dict(type='int', ), bfd_cfg=dict(type='dict', disable=dict(type='bool', ), bfd=dict(type='bool', )), disable=dict(type='str', choices=['all']), hello_interval=dict(type='int', ), database_filter_cfg=dict(type='dict', database_filter=dict(type='str', choices=['all']), out=dict(type='bool', )), priority=dict(type='int', ), mtu=dict(type='int', ), message_digest_cfg=dict(type='list', message_digest_key=dict(type='int', ), md5=dict(type='dict', md5_value=dict(type='str', ), encrypted=dict(type='str', ))), uuid=dict(type='str', ))), slb_partition_redirect=dict(type='bool', )),
        ddos=dict(type='dict', outside=dict(type='bool', ), inside=dict(type='bool', ), uuid=dict(type='str', )),
        timer=dict(type='int', ),
        access_list=dict(type='dict', acl_name=dict(type='str', ), acl_id=dict(type='int', )),
        stats=dict(type='dict', num_tx_pkts=dict(type='str', ), dropped_dis_tx_pkts=dict(type='str', ), num_total_tx_bytes=dict(type='str', ), num_multicast_pkts=dict(type='str', ), num_unicast_pkts=dict(type='str', ), num_broadcast_tx_pkts=dict(type='str', ), num_broadcast_pkts=dict(type='str', ), num_multicast_tx_pkts=dict(type='str', ), ifnum=dict(type='int', required=True, ), num_unicast_tx_pkts=dict(type='str', ), dropped_rx_pkts=dict(type='str', ), num_total_bytes=dict(type='str', ), num_pkts=dict(type='str', ), dropped_dis_rx_pkts=dict(type='str', ), dropped_tx_pkts=dict(type='str', )),
        uuid=dict(type='str', ),
        bfd=dict(type='dict', interval_cfg=dict(type='dict', interval=dict(type='int', ), min_rx=dict(type='int', ), multiplier=dict(type='int', )), authentication=dict(type='dict', encrypted=dict(type='str', ), password=dict(type='str', ), method=dict(type='str', choices=['md5', 'meticulous-md5', 'meticulous-sha1', 'sha1', 'simple']), key_id=dict(type='int', )), echo=dict(type='bool', ), uuid=dict(type='str', ), demand=dict(type='bool', )),
        ifnum=dict(type='int', required=True, ),
        do_auto_recovery=dict(type='bool', ),
        ipv6=dict(type='dict', uuid=dict(type='str', ), address_list=dict(type='list', address_type=dict(type='str', choices=['anycast', 'link-local']), ipv6_addr=dict(type='str', )), router_adver=dict(type='dict', max_interval=dict(type='int', ), default_lifetime=dict(type='int', ), reachable_time=dict(type='int', ), vrid=dict(type='dict', use_floating_ip_default_vrid=dict(type='bool', ), floating_ip_default_vrid=dict(type='str', ), adver_vrid_default=dict(type='bool', ), floating_ip=dict(type='str', ), adver_vrid=dict(type='int', ), use_floating_ip=dict(type='bool', )), other_config_action=dict(type='str', choices=['enable', 'disable']), managed_config_action=dict(type='str', choices=['enable', 'disable']), min_interval=dict(type='int', ), rate_limit=dict(type='int', ), mtu=dict(type='dict', adver_mtu=dict(type='int', ), adver_mtu_disable=dict(type='bool', )), prefix_list=dict(type='list', not_autonomous=dict(type='bool', ), not_on_link=dict(type='bool', ), valid_lifetime=dict(type='int', ), prefix=dict(type='str', ), preferred_lifetime=dict(type='int', )), action=dict(type='str', choices=['enable', 'disable']), retransmit_timer=dict(type='int', ), hop_limit=dict(type='int', )), rip=dict(type='dict', split_horizon_cfg=dict(type='dict', state=dict(type='str', choices=['poisoned', 'disable', 'enable'])), uuid=dict(type='str', )), ipv6_enable=dict(type='bool', ), stateful_firewall=dict(type='dict', uuid=dict(type='str', ), class_list=dict(type='str', ), acl_name=dict(type='str', ), inside=dict(type='bool', ), outside=dict(type='bool', ), access_list=dict(type='bool', )), nat=dict(type='dict', inside=dict(type='bool', ), outside=dict(type='bool', )), ttl_ignore=dict(type='bool', ), router=dict(type='dict', ripng=dict(type='dict', uuid=dict(type='str', ), rip=dict(type='bool', )), ospf=dict(type='dict', area_list=dict(type='list', area_id_addr=dict(type='str', ), tag=dict(type='str', ), instance_id=dict(type='int', ), area_id_num=dict(type='int', )), uuid=dict(type='str', )), isis=dict(type='dict', tag=dict(type='str', ), uuid=dict(type='str', ))), access_list_cfg=dict(type='dict', inbound=dict(type='bool', ), v6_acl_name=dict(type='str', )), ospf=dict(type='dict', uuid=dict(type='str', ), bfd=dict(type='bool', ), cost_cfg=dict(type='list', cost=dict(type='int', ), instance_id=dict(type='int', )), priority_cfg=dict(type='list', priority=dict(type='int', ), instance_id=dict(type='int', )), hello_interval_cfg=dict(type='list', hello_interval=dict(type='int', ), instance_id=dict(type='int', )), mtu_ignore_cfg=dict(type='list', mtu_ignore=dict(type='bool', ), instance_id=dict(type='int', )), retransmit_interval_cfg=dict(type='list', retransmit_interval=dict(type='int', ), instance_id=dict(type='int', )), disable=dict(type='bool', ), transmit_delay_cfg=dict(type='list', transmit_delay=dict(type='int', ), instance_id=dict(type='int', )), neighbor_cfg=dict(type='list', neighbor_priority=dict(type='int', ), neighbor_poll_interval=dict(type='int', ), neig_inst=dict(type='int', ), neighbor=dict(type='str', ), neighbor_cost=dict(type='int', )), network_list=dict(type='list', broadcast_type=dict(type='str', choices=['broadcast', 'non-broadcast', 'point-to-point', 'point-to-multipoint']), p2mp_nbma=dict(type='bool', ), network_instance_id=dict(type='int', )), dead_interval_cfg=dict(type='list', dead_interval=dict(type='int', ), instance_id=dict(type='int', )))),
        map=dict(type='dict', inside=dict(type='bool', ), map_t_inside=dict(type='bool', ), uuid=dict(type='str', ), map_t_outside=dict(type='bool', ), outside=dict(type='bool', )),
        ports_threshold=dict(type='int', ),
        nptv6=dict(type='dict', domain_list=dict(type='list', domain_name=dict(type='str', required=True, ), bind_type=dict(type='str', required=True, choices=['inside', 'outside']), uuid=dict(type='str', ))),
        icmp_rate_limit=dict(type='dict', lockup=dict(type='int', ), lockup_period=dict(type='int', ), normal=dict(type='int', )),
        isis=dict(type='dict', priority_list=dict(type='list', priority=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), padding=dict(type='bool', ), hello_interval_minimal_list=dict(type='list', hello_interval_minimal=dict(type='bool', ), level=dict(type='str', choices=['level-1', 'level-2'])), mesh_group=dict(type='dict', value=dict(type='int', ), blocked=dict(type='bool', )), network=dict(type='str', choices=['broadcast', 'point-to-point']), authentication=dict(type='dict', send_only_list=dict(type='list', send_only=dict(type='bool', ), level=dict(type='str', choices=['level-1', 'level-2'])), mode_list=dict(type='list', mode=dict(type='str', choices=['md5']), level=dict(type='str', choices=['level-1', 'level-2'])), key_chain_list=dict(type='list', key_chain=dict(type='str', ), level=dict(type='str', choices=['level-1', 'level-2']))), csnp_interval_list=dict(type='list', csnp_interval=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), retransmit_interval=dict(type='int', ), password_list=dict(type='list', password=dict(type='str', ), level=dict(type='str', choices=['level-1', 'level-2'])), bfd_cfg=dict(type='dict', disable=dict(type='bool', ), bfd=dict(type='bool', )), wide_metric_list=dict(type='list', wide_metric=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), hello_interval_list=dict(type='list', hello_interval=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), circuit_type=dict(type='str', choices=['level-1', 'level-1-2', 'level-2-only']), hello_multiplier_list=dict(type='list', hello_multiplier=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), metric_list=dict(type='list', metric=dict(type='int', ), level=dict(type='str', choices=['level-1', 'level-2'])), lsp_interval=dict(type='int', ), uuid=dict(type='str', )),
        name=dict(type='str', ),
        icmpv6_rate_limit=dict(type='dict', lockup_period_v6=dict(type='int', ), normal_v6=dict(type='int', ), lockup_v6=dict(type='int', )),
        user_tag=dict(type='str', ),
        mtu=dict(type='int', ),
        sampling_enable=dict(type='list', counters1=dict(type='str', choices=['all', 'num_pkts', 'num_total_bytes', 'num_unicast_pkts', 'num_broadcast_pkts', 'num_multicast_pkts', 'num_tx_pkts', 'num_total_tx_bytes', 'num_unicast_tx_pkts', 'num_broadcast_tx_pkts', 'num_multicast_tx_pkts', 'dropped_dis_rx_pkts', 'dropped_rx_pkts', 'dropped_dis_tx_pkts', 'dropped_tx_pkts'])),
        lw_4o6=dict(type='dict', outside=dict(type='bool', ), inside=dict(type='bool', ), uuid=dict(type='str', )),
        action=dict(type='str', choices=['enable', 'disable']),
        l3_vlan_fwd_disable=dict(type='bool', )
    ))
   

    return rv

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/trunk/{ifnum}"

    f_dict = {}
    f_dict["ifnum"] = module.params["ifnum"]

    return url_base.format(**f_dict)

def oper_url(module):
    """Return the URL for operational data of an existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/oper"

def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"

def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]

def get(module):
    return module.client.get(existing_url(module))

def get_list(module):
    return module.client.get(list_url(module))

def get_oper(module):
    if module.params.get("oper"):
        query_params = {}
        for k,v in module.params["oper"].items():
            query_params[k.replace('_', '-')] = v 
        return module.client.get(oper_url(module),
                                 params=query_params)
    return module.client.get(oper_url(module))

def get_stats(module):
    if module.params.get("stats"):
        query_params = {}
        for k,v in module.params["stats"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(stats_url(module),
                                 params=query_params)
    return module.client.get(stats_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_envelope(title, data):
    return {
        title: data
    }

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/trunk/{ifnum}"

    f_dict = {}
    f_dict["ifnum"] = ""

    return url_base.format(**f_dict)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["trunk"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
               break
            else:
                if existing_config["trunk"][k] != v:
                    if result["changed"] != True:
                        result["changed"] = True
                    existing_config["trunk"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result

def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result, existing_config):
    payload = build_json("trunk", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)

def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol, ansible_username, ansible_password)
    
    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)
    
    if state == 'present':
        result = present(module, result, existing_config)

    elif state == 'absent':
        result = absent(module, result, existing_config)
    
    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
        elif module.params.get("get_type") == "oper":
            result["result"] = get_oper(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
    module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()