# example for using the length-type value de&encoding
# and the "length includes tag size" option

from uttlv import TLV

t = TLV()

# types and tags for BLE advertisement data which is LTV
bleadvCconfig = {
    0x01: {TLV.Config.Type: bytes, TLV.Config.Name: "FLAGS"},
    0x02: {TLV.Config.Type: bytes, TLV.Config.Name: "INCOMP_UUIDS16"},
    0x03: {TLV.Config.Type: bytes, TLV.Config.Name: "COMP_UUIDS16"},
    0x04: {TLV.Config.Type: bytes, TLV.Config.Name: "INCOMP_UUIDS32"},
    0x05: {TLV.Config.Type: bytes, TLV.Config.Name: "COMP_UUIDS32"},
    0x06: {TLV.Config.Type: bytes, TLV.Config.Name: "INCOMP_UUIDS128"},
    0x07: {TLV.Config.Type: bytes, TLV.Config.Name: "COMP_UUIDS128"},
    0x08: {TLV.Config.Type: str, TLV.Config.Name: "INCOMP_NAME"},
    0x09: {TLV.Config.Type: str, TLV.Config.Name: "COMP_NAME"},
    0x0A: {TLV.Config.Type: bytes, TLV.Config.Name: "TX_PWR_LVL"},
    0x12: {TLV.Config.Type: bytes, TLV.Config.Name: "SLAVE_ITVL_RANGE"},
    0x14: {TLV.Config.Type: bytes, TLV.Config.Name: "SOL_UUIDS16"},
    0x15: {TLV.Config.Type: bytes, TLV.Config.Name: "SOL_UUIDS128"},
    0x16: {TLV.Config.Type: bytes, TLV.Config.Name: "SVC_DATA_UUID16"},
    0x17: {TLV.Config.Type: bytes, TLV.Config.Name: "PUBLIC_TGT_ADDR"},
    0x18: {TLV.Config.Type: bytes, TLV.Config.Name: "RANDOM_TGT_ADDR"},
    0x19: {TLV.Config.Type: bytes, TLV.Config.Name: "APPEARANCE"},
    0x1A: {TLV.Config.Type: bytes, TLV.Config.Name: "ADV_ITVL"},
    0x20: {TLV.Config.Type: bytes, TLV.Config.Name: "SVC_DATA_UUID32"},
    0x21: {TLV.Config.Type: bytes, TLV.Config.Name: "SVC_DATA_UUID128"},
    0x24: {TLV.Config.Type: str, TLV.Config.Name: "URI"},
    0x29: {TLV.Config.Type: bytes, TLV.Config.Name: "MESH_PROV"},
    0x2A: {TLV.Config.Type: bytes, TLV.Config.Name: "MESH_MESSAGE"},
    0x2B: {TLV.Config.Type: bytes, TLV.Config.Name: "MESH_BEACON"},
    0xFF: {TLV.Config.Type: bytes, TLV.Config.Name: "MFG_DATA"},
}

# a BLE advertisement as reported by iOS
aad = "0201061bff990405118e5785ffff0070fc1801208f562e0eaadb08d33338ef11079ecadc240ee5a9e093f3a3b50100406e0b095275757669203338454600"

t = TLV(len_size=1,ltv=True,lenTV=True)
t.set_local_tag_map(bleadvCconfig)
t.parse_array(bytes(bytearray.fromhex(aad)))

print(f"decoded:\n{t.tree(use_names=True)}")

arr = t.to_byte_array()
print(f"TLV encoded back:\n{arr.hex()}")

t2 = TLV(len_size=1, ltv=True, lenTV=True)

t2.set_local_tag_map(bleadvCconfig)
t2.parse_array(arr)
print(f"parse back:\n{t.tree(use_names=True)}")
print(t2.to_byte_array().hex())

""""
example output (nb there seems to be a chooped-off trailing zero, not sure if that was in the )

decoded:
FLAGS: 06
MFG_DATA: 990405118e5785ffff0070fc1801208f562e0eaadb08d33338ef
COMP_UUIDS128: 9ecadc240ee5a9e093f3a3b50100406e
COMP_NAME: Ruuvi 38EF

TLV encoded back:
0201061bff990405118e5785ffff0070fc1801208f562e0eaadb08d33338ef11079ecadc240ee5a9e093f3a3b50100406e0b0952757576692033384546
parse back:
FLAGS: 06
MFG_DATA: 990405118e5785ffff0070fc1801208f562e0eaadb08d33338ef
COMP_UUIDS128: 9ecadc240ee5a9e093f3a3b50100406e
COMP_NAME: Ruuvi 38EF

0201061bff990405118e5785ffff0070fc1801208f562e0eaadb08d33338ef11079ecadc240ee5a9e093f3a3b50100406e0b0952757576692033384546
"""