import sys
import markdown

arg = sys.argv

def createInputContent(inputfile):
  inputFile = arg[2]
  inputContent = ''
  with open(inputFile) as f:
    inputContent = f.read()
  return inputContent
  
def toHTML(inputfile,outputfile):
  html = markdown.markdown(createInputContent(inputfile), extensions=['sane_lists','tables'])
  with open(outputfile, 'w') as f:
    f.write(html)
  return outputfile

def fileConverter(command):
  if len(command) != 4: raise ValueError('コマンドが正しくありません')
  elif command[1] != 'markdown': raise ValueError('command not found')
  else: return toHTML(command[2],command[3])
  
fileConverter(arg)