#!/usr/bin/python
import sys, sqlite3, subprocess, shlex,time, magic

reload(sys)
sys.setdefaultencoding('utf-8') # helps with odd formatting

if len(sys.argv) != 3:
  print "expected database file name"
  sys.exit()
file = sys.argv[1]

conn = sqlite3.connect(file)
c = conn.cursor()

word_count = 0
rows = c.execute('SELECT * FROM `LOOKUPS`')

for row in rows:
	word = row[1][3:] # cut leading "de:"
	command_line = "leo " + word
	print(word)
	args = shlex.split(command_line)
	proc = subprocess.Popen(args,stdout=subprocess.PIPE)
	def_word = proc.stdout.read()
	new = def_word.replace('\n', '<br />')
	context = row[5]
	time.sleep(3) # http 250 error on leo without break

	f = open(sys.argv[2],'a')
	f.write(word + '<br>' + context + ';' + new.decode('iso-8859-1') + '\n')
	
	print(word_count)
	word_count = word_count+ 1
	
conn.close()
