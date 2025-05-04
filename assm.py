import os
import glob

def copySource(path):
  for sourceFile in glob.glob(os.path.join(path, '*.fth')):
    print(sourceFile)
    disvarFile = sourceFile.replace(os.path.join(path, ''), '').replace('.fth', '').upper()
    os.system(f'xdm99.py {towerDiskPath} -a {sourceFile} -n {disvarFile} -f DIS/VAR80')

print('Create disk image')
towerDiskPath = os.path.join('bin', 'color-tower.dsk')
if not os.path.exists('bin'):
  os.makedirs('bin')
if os.path.exists(towerDiskPath):
  os.remove(towerDiskPath)
os.system(f'xdm99.py -X sssd {towerDiskPath}')

print('Copy FORTH code to DIS/VAR 80 files')
copySource('src')
copySource('camel99libs')

camel99Path = os.path.join('camel99libs', 'camel99.ti.program')
os.system(f'xdm99.py {towerDiskPath} -a {camel99Path} -n CAMEL99 -f PROGRAM')