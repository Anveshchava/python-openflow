"""Defines actions that may be associated with flows packets."""

# System imports
import enum

# Third-party imports

# Local source tree imports
from ..foundation import base
from ..foundation import basic_types

# Enums


class ActionType(enum.Enum):
    """Actions associated with flows and packets.

    Enums:
        OFPAT_OUTPUT            # Output to switch port.
        OFPAT_SET_VLAN_VID      # Set the 802.1q VLAN id.
        OFPAT_SET_VLAN_PCP      # Set the 802.1q priority.
        OFPAT_STRIP_VLAN        # Strip the 802.1q header.
        OFPAT_SET_DL_SRC        # Ethernet source address.
        OFPAT_SET_DL_DST        # Ethernet destination address.
        OFPAT_SET_NW_SRC        # IP source address.
        OFPAT_SET_NW_DST        # IP destination address.
        OFPAT_SET_NW_TOS        # IP ToS (DSCP field, 6 bits).
        OFPAT_SET_TP_SRC        # TCP/UDP source port.
        OFPAT_SET_TP_DST        # TCP/UDP destination port.
        OFPAT_ENQUEUE           # Output to queue.
    """

    OFPAT_OUTPUT = 0
    OFPAT_SET_VLAN_VID = 1
    OFPAT_SET_VLAN_PCP = 2
    OFPAT_STRIP_VLAN = 3
    OFPAT_SET_DL_SRC = 4
    OFPAT_SET_DL_DST = 5
    OFPAT_SET_NW_SRC = 6
    OFPAT_SET_NW_DST = 7
    OFPAT_SET_NW_TOS = 8
    OFPAT_SET_TP_SRC = 9
    OFPAT_SET_TP_DST = 10
    OFPAT_ENQUEUE = 11
    OFPAT_VENDOR = 0xffff


# Classes


class ActionHeader(base.GenericStruct):
    """
    Defines the Header that is common to all actions.

        :param ofpat_type -- One of OFPAT_.
        :param length -- Length of action, including this header.
        :param pad -- Pad for 64-bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    pad = basic_types.UBInt8Array(length=4)

    def __init__(self, ofpat_type=None, length=None, pad=None):
        self.ofpat_type = ofpat_type
        self.length = length
        self.pad = pad


class ActionOutput(base.GenericStruct):
    """Defines the actions output.

        :param ofpat_type -- OFPAT_OUTPUT.
        :param length -- Length is 8.
        :param port -- Output port.
        :param max_length -- Max length to send to controller.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    port = basic_types.UBInt16()
    max_length = basic_types.UBInt16()

    def __init__(self, ofpat_type=None, length=None, port=None,
                 max_length=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.port = port
        self.max_length = max_length


class ActionEnqueue(base.GenericStruct):
    """
    A switch may support only queues that are tied to specific PCP/TOS bits.
    In that case, we cannot map an arbitrary flow to a specific queue,
    therefore the action ENQUEUE is not supported. The user can still use
    these queues and map flows to them by setting the relevant fields
    (TOS, VLAN PCP).

        :param ofpat_type -- OFPAT_ENQUEUE.
        :param length -- Len is 16
        :param port -- Port that queue belongs. Should refer to a valid
                       physical port.
                       (i.e. < OFPP_MAX) or OFPP_IN_PORT
        :param pad -- Pad for 64-bit alignment.
        :param queue_id -- Where to enqueue the packets.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    port = basic_types.UBInt16()
    pad = basic_types.UBInt8Array(length=6)
    queue_id = basic_types.UBInt32()

    def __init__(self, ofpat_type=None, length=None, port=None, pad=None,
                 queue_id=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.port = port
        self.pad = pad
        self.queue_id = queue_id


class ActionVlanVid(base.GenericStruct):
    """Action structure for OFPAT_SET_VLAN_VID

        :param ofpat_type --  OFPAT_SET_VLAN_PCP.
        :param length --   Length is 8.
        :param vlan_id --   VLAN priority.
        :param pad2 -- Pad for bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    vlan_id = basic_types.UBInt16()
    pad2 = basic_types.UBInt8Array(length=2)

    def __init__(self, ofpat_type=None, length=None, vlan_id=None, pad2=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.vlan_id = vlan_id
        self.pad2 = pad2


class ActionVlanPCP(base.GenericStruct):
    """Action structure for OFPAT_SET_VLAN_PCP.

        :param ofpat_type -- OFPAT_SET_VLAN_PCP.
        :param length -- Length is 8.
        :param vlan_pcp -- VLAN Priority.
        :param pad -- Pad for bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    vlan_pcp = basic_types.UBInt8()
    pad = basic_types.UBInt8Array(length=3)

    def __init__(self, ofpat_type=None, length=None, vlan_pcp=None, pad=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.vlan_pcp = vlan_pcp
        self.pad = pad


class ActionDLAddr(base.GenericStruct):
    """Action structure for OFPAT_SET_DL_SRC/DST.

        :param ofpat_type -- OFPAT_SET_DL_SRC/DST.
        :param length -- Length is 16.
        :param dl_addr -- Ethernet address.
        :param pad -- Pad for bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    dl_addr = basic_types.UBInt8Array(length=base.OFP_ETH_ALEN)
    pad = basic_types.UBInt8Array(length=6)

    def __init__(self, ofpat_type=None, length=None, dl_addr=None, pad=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.dl_addr = dl_addr
        self.pad = pad


class ActionNWAddr(base.GenericStruct):
    """Action structure for OFPAT_SET_NW_SRC/DST.

        :param ofpat_type -- OFPAT_SET_TW_SRC/DST.
        :param length -- Length is 8.
        :param nw_addr -- IP Address
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    nw_addr = basic_types.UBInt32()

    def __init__(self, ofpat_type=None, length=None, nw_addr=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.nw_addr = nw_addr


class ActionNWTos(base.GenericStruct):
    """Action structure for OFPAT_SET_NW_TOS.

        :param ofpat_type -- OFPAT_SET_TW_SRC/DST.
        :param length -- Length is 8.
        :param nw_tos -- IP ToS (DSCP field, 6 bits).
        :param pad -- Pad for bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    nw_tos = basic_types.UBInt8()
    pad = basic_types.UBInt8Array(length=3)

    def __init__(self, ofpat_type=None, length=None, nw_tos=None, pad=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.nw_tos = nw_tos
        self.pad = pad


class ActionTPPort(base.GenericStruct):
    """Action structure for OFPAT_SET_TP_SRC/DST.

        :param ofpat_type -- OFPAT_SET_TP_SRC/DST.
        :param length -- Length is 8.
        :param tp_port -- TCP/UDP port.
        :param pad -- Pad for bit alignment.
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    tp_port = basic_types.UBInt16()
    pad = basic_types.UBInt8Array(length=2)

    def __init__(self, ofpat_type=None, length=None, tp_port=None, pad=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.tp_port = tp_port
        self.pad = pad


class ActionVendorHeader(base.GenericStruct):
    """Action header for OFPAT_VENDOR.
    The rest of the body is vendor-defined.

        :param ofpat_type -- OFPAT_VENDOR.
        :param length -- Length is a multiple of 8.
        :param vendor -- Vendor ID, which takes the same form as in "struct
                         ofp_vendor_header".
    """
    ofpat_type = basic_types.UBInt16()
    length = basic_types.UBInt16()
    vendor = basic_types.UBInt32()

    def __init__(self, ofpat_type=None, length=None, vendor=None):

        self.ofpat_type = ofpat_type
        self.length = length
        self.vendor = vendor
