#step 1
from pathlib import Path

#step 1
files_dir = Path('files')


#step 2
merged = ''

#step 1
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()

  #step 2
  merged = merged + content + '\n' + '\n'

#step 3
with open('merged.csv', 'w') as file:
  file.write(merged)
  
