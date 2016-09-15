# kindle_anki
Script to export vocab.db and create Anki cards. 

1. Install Leo: http://search.cpan.org/~tlinden/WWW-Dict-Leo-Org/leo
1.1 You might have to install Perl HTML_TableParser

2. Export vocab.db from the kindle

3. Parse database using tables.py script: "python tables.py vocab.db anki.csv"

4. import anki.csv into the desired anki deck
	-set "ignore line where first field matches"
	This allows the db to be updated without worrying about duplicates


