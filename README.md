# kindle_anki
Script to export vocab.db and create Anki cards. 

1. Install Leo: http://search.cpan.org/~tlinden/WWW-Dict-Leo-Org/leo
1.1 You might have to install Perl HTML_TableParser

If might have the package available in your repository. 

Install: sudo apt-get install libwww-dict-leo-org-perl

2. Export vocab.db from the kindle. This file is found in system/vocabulary

3. Parse database using parse_book.py script: "python tables.py vocab.db anki.csv". This script, unlike simple table.py, parses the database for all the books and allows you to select which book you would like to export. 

4. import anki.csv into the desired anki deck
	-set "ignore line where first field matches"
	This allows the db to be updated without worrying about duplicates


