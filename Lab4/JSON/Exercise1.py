import json
input = open("C:\PP2\Lab4\JSON\sample.json", "r").read()
imdata = (json.loads(input))['imdata']
print("Interface Status")
print("=" * 87)
print("DN",' '*47,"Description",' '*8,"Speed",'  ',"MTU")
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)
for i in imdata:
    Phys = i['l1PhysIf']
    attributes = Phys['attributes']
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<61}".format(dn),descr,' '*8,speed,'  ',mtu)