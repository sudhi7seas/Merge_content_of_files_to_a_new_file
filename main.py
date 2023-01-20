from pathlib import Path
files_dir = Path('files')

merged = ''

for index, filepath in enumerate (files_dir.iterdir()):
  with open(filepath, 'r') as file:
    #to get the list instead of a single string - use 'readlines()''
    content = file.readlines()

    #Except the header, get the remaining contents of the files - use content[1:]
    new_content = content[1:]

    #in order to have the header only in the 1st file or only once in a merged file
    if index == 0:
      #to convert the list into the string
      content = ''.join(content)
      merged = merged + content + '\n'

    else:
      #to convert the list into the string
      new_content = ''.join(new_content)
      merged = merged + new_content + '\n'

with open('merged.csv', 'w') as file:
  file.write(merged)