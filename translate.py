
import requests, json, sys
reload(sys)  
sys.setdefaultencoding('utf8')

#init default values
frm = 'en'
to = 'ka'
word = ''
file = ''
#put your yandex.translate token
api = ''

def print_help():
  print '\tbefore use script, please, backup your message_[lang].json file!'
  print '\tExample usage on windows cmd.exe:'
  print '\tC:\Users\user\Desktop>python translate.py -from en -to ru -word Deposits'
  print '\tC:\Users\windows-user\Desktop>python translate.py -from en -to ru -file C:\message_ru.json'
  print '\tafter running this^ command, the file message_ru.json will be overwritten'
  print '\n\tExample usage on linux terminal:'
  print '\tlinux-user@linux-host:~$ python ./translate.py -from en -to ru -word Deposits'
  print '\tlinux-user@linux-host:~$ python ./translate.py -from en -to ru -file message_ru.json'
  print '\tafter running this^ command, the file message_ru.json will be overwritten'
  
def translate_word ( language_from , language_to, word ):
  if word != '' and len(word)>0:
    r = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate?lang="
      +language_from+"-"+language_to+"&key="+api, data={'text': word})
    if r.json()['code'] != 200:
    	print r.json()['code']
    	raise Exception('Error: bad response')

    result = r.json()[ 'text' ][0].encode('utf8')
    print result
    return result

  else:
    print '\n\tError: parameter word is empty!\n'
    print_help()
    raise Exception('Error: parameter word is empty')

def translate_file(file):

  with open(file, 'r') as fileObject :
    filedata = fileObject.read()
    jsonFile = json.loads( filedata )
    for i in jsonFile:
		try:
			print jsonFile[i] + ' > '

			jsonFile[i] = translate_word (frm , to, jsonFile[i] )

			content = json.dumps(jsonFile, indent=2, ensure_ascii=False)


			with open(file, 'w')  as fileWrite:
				fileWrite.write(content.decode('utf8'))
		except:
			print 'something wrong'
      

#check&parsing command line args
if len(sys.argv) == 2:
  word = sys.argv[1]
else:
  i = 1
  while i < len(sys.argv):
    if sys.argv[i] == '-from':
      frm = sys.argv[i+1]
    if sys.argv[i] == '-to':
      to = sys.argv[i+1]
    if sys.argv[i] == '-word':
      word = sys.argv[i+1]
    if sys.argv[i] == '-file':
      file = sys.argv[i+1]
    i += 1



#if file != '' and len(file)>0:
translate_file(file)
#else: 
# print translate_word ( frm, to, word )


