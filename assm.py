import os
import glob

print('Create disk image')
towerDiskPath = os.path.join('bin', 'color-tower.dsk')
if not os.path.exists('bin'):
  os.makedirs('bin')
if os.path.exists(towerDiskPath):
  os.remove(towerDiskPath)
os.system(f'xdm99.py -X sssd {towerDiskPath}')

# TODO: Create a method that allows us to pass a path containing source files
print('Copy FORTH code to DIS/VAR 80 files')
for sourceFile in glob.glob(os.path.join('src', '*.fth')):
  print(sourceFile)
  disvarFile = sourceFile.replace(os.path.join('src', ''), '').replace('.fth', '').upper()
  os.system(f'xdm99.py {towerDiskPath} -a {sourceFile} -n {disvarFile} -f DIS/VAR80')