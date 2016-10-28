#!/usr/bin/python
import sys, sqlite3, subprocess, shlex,time, magic

reload(sys)
sys.setdefaultencoding('utf-8') # helps with odd formatting

if len(sys.argv) != 3:
  print "expected database or csv file name"
  sys.exit()
file = sys.argv[1]

conn = sqlite3.connect(file)
c = conn.cursor()

word_count = 0
rows = c.execute('SELECT * FROM `LOOKUPS`')

books = [tup[0] for tup in rows.fetchall()]
name_list = []

for book in books:
	print(book)
	name = book.split(":",1)[0] #name in database has funky letters after
	if name not in name_list:
		name_list.append(name)

i = 0
for name in name_list:
	print(str(i) + " " + name)
	i = i + 1

desired_book = input('Enter the book number: ')

print(name_list[desired_book])

rows = c.execute('SELECT * FROM `LOOKUPS`') #fetch data again...

for row in rows:
	row_book_name = row[0].split(":",1)[0] 
	if row_book_name == name_list[desired_book]:
		#print(row_book_name)
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
