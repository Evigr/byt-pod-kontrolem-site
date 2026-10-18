"""Place the CC0 Kenney car on an original road mesh, keeping embedded assets."""
from pathlib import Path
import json
import struct

folder = Path(__file__).parent / 'docs/assets/models'
data = (folder / 'car.glb').read_bytes()
length = struct.unpack_from('<I', data, 12)[0]
gltf = json.loads(data[20:20+length])
offset = 20 + length
binary_length = struct.unpack_from('<I', data, offset)[0]
binary = bytearray(data[offset+8:offset+8+binary_length])

def surface(name, x0, x1, z0, z1, y, color):
    vertices = [(x0,y,z0),(x0,y,z1),(x1,y,z1),(x0,y,z0),(x1,y,z1),(x1,y,z0)]
    values = b''.join(struct.pack('<3f', *v) for v in vertices)
    view = len(gltf['bufferViews'])
    gltf['bufferViews'].append({'buffer':0,'byteOffset':len(binary),'byteLength':len(values),'target':34962})
    binary.extend(values)
    accessor = len(gltf['accessors'])
    gltf['accessors'].append({'bufferView':view,'componentType':5126,'count':6,'type':'VEC3','min':[x0,y,z0],'max':[x1,y,z1]})
    material = len(gltf['materials'])
    gltf['materials'].append({'name':name,'doubleSided':True,'pbrMetallicRoughness':{'baseColorFactor':color+[1],'metallicFactor':0,'roughnessFactor':1}})
    mesh = len(gltf['meshes'])
    gltf['meshes'].append({'name':name,'primitives':[{'attributes':{'POSITION':accessor},'material':material}]})
    node = len(gltf['nodes'])
    gltf['nodes'].append({'mesh':mesh,'name':name})
    gltf['scenes'][gltf.get('scene',0)]['nodes'].append(node)

surface('Road shoulder',-1.8,1.8,-3,3,-.055,[.11,.20,.30])
surface('Asphalt',-1.65,1.65,-3,3,-.04,[.035,.075,.12])
for x in [-1.46,1.44]: surface('Road edge',x,x+.025,-3,3,-.03,[.37,.67,.85])
for z in [-2.8,-1.8,-.8,.2,1.2,2.2]: surface('Lane marking',.83,.88,z,z+.44,-.025,[.72,.82,.88])
gltf['buffers'][0]['byteLength'] = len(binary)
encoded = json.dumps(gltf,separators=(',',':')).encode()
encoded += b' ' * (-len(encoded)%4)
binary += b'\0' * (-len(binary)%4)
result = struct.pack('<III',0x46546c67,2,12+8+len(encoded)+8+len(binary))
result += struct.pack('<II',len(encoded),0x4e4f534a)+encoded
result += struct.pack('<II',len(binary),0x004e4942)+binary
(folder/'car-road.glb').write_bytes(result)
print('Built car-road.glb:',len(result),'bytes')
