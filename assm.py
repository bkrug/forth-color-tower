import os
import glob
import xml.etree.ElementTree as ET
from zipfile import ZipFile

print('Create disk image')
towerDiskPath = os.path.join('bin', 'color-tower.dsk')
if not os.path.exists('bin'):
  os.makedirs('bin')
if os.path.exists(towerDiskPath):
  os.remove(towerDiskPath)
os.system(f'xdm99.py -X sssd {towerDiskPath}')

print('Copy FORTH code to DIS/VAR 80 files')
for sourceFile in glob.glob('*.forth'):
  disvarFile = sourceFile.replace('.forth', '').upper()
  os.system(f'xdm99.py {towerDiskPath} -a {sourceFile} -n {disvarFile} -f DIS/VAR80')