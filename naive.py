#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1) NAUKA

# 1.1) Otwórz pliki do nauki

# 1.2) Pobierz wszystkie słowa z train_spam_and_ham
#      Osobna baza słów dla train_spam i train_ham
#      Zlicz wystąpienia tych słów
#      Zlicz pliki (200) i na tej podstawie wylicz szanse
#      http://www.statsoft.pl/textbook/stathome_stat.html?http%3A%2F%2Fwww.statsoft.pl%2Ftextbook%2Fstnaiveb.html


# 2) Jedziemy z koksem

# 2.1) Otwórz plik z katalogu test

# 2.2) Pobierz wszystkie słowa z pliku
#      Może się mylę ale prawdopodobieństwo a priori = 1,
#      bo na wstępie nie możemy sklasyfikować danych

# 2.3) Oblicz prawdopodobieństwo a posteriori dla danego pliku
#      tzn. jeśli a posteriori słów częściej występujących w train_spam
#      jest większe sklasyfikuj jako spam
import os
import sqlite3

ham_set ='/home/krzysztof/codes/py/skull/train_spam_and_ham/train_ham/'
spam_set = '/home/krzysztof/codes/py/skull/train_spam_and_ham/train_spam/'
test_set = '/home/krzysztof/codes/py/skull/test/'

class myNaiveBayes:
    
    # Konstruktor klasy
    def __init__(self):
        try:
            self.conn = sqlite3.connect('bayes.db')
        except NameError, x:
            print "Connection failed!", x
            raise
    
    # Tworzymy baze
    # Parametry: (nazwa naszej bazy, lokalizacja plików do nauki)
    def dbQuery(self, table_name, spam_or_ham):
        self.table_name = table_name

        sql = 'CREATE TABLE IF NOT EXISTS ' + self.table_name + \
                ' (Id INTEGER PRIMARY KEY, word TEXT NOT NULL, \
                count INT NOT NULL);'
        self.conn.execute(sql)
        self.conn.commit()
        self.getData(spam_or_ham)

    def getData(self, train_set):
        for filename in os.listdir(train_set):
            self.getWords(train_set, filename)

    def getWords(self, path,  filename):
        with open(path + filename, 'rb') as f:
            for line in f:
                for word in line.split():
                    pass
                    #print word
                    self.addToTable(word, self.table_name)

    def addToTable(self, word, table_name):
        self.conn.execute("SELECT count(*) FROM ? WHERE word = ?", (self.table_name, word,))
        data = self.conn.fetchone()[0]
        if data==0:
            print('There is no component named %s'%word)
            self.conn.execute('INSERT INTO '+ self.table_name + " ( VALUES (Id,'"+ word +"', 1);")
        else:
            print('Component %s found in %s row(s)'%(word, data))
            self.conn.execute('SELECT count FROM ' + self.table_name + ' WHERE word = '+ word +';')
            data = self.conn.fetchone()[0]
            self.conn.execute('INSERT INTO '+ self.table_name + "(count) ( VALUES (?)",(data + 1)
            
    def teachMe(self, path):
        for filename in os.listdir(path):
            with open(path + filename, 'rb') as f:
                for line in f:
                    for word in line.split():
                        pass
                        #print word
        
    def checkChance(self, word):
        
        
    # Dekonstruktor klasy
    def __del__(self):
        self.conn.close()


def main():
    myBayes = myNaiveBayes()
    myBayes.dbQuery('spam', spam_set)
    myBayes.dbQuery('ham', ham_set)
    


if __name__ == '__main__':
    main()

    
            #sql = 'SELECT word FROM '+ self.table_name + \
        #        ' WHERE word LIKE ' + word + ';'
        
        
        #sql = 'INSERT INTO '+ self.table_name + " VALUES ('"+ word +"', 1);"
        
        # CREATE TABLE users('pk' INTEGER PRIMARY KEY, 'name' VARCHAR(100) UNIQUE, 'count' INTEGER) << name bdzie unikatowe


        # This will update 2 of the columns. When ID=1 exists, the NAME will be unaffected. 
        # When ID=1 does not exist, the name will be default (NULL).
        # INSERT OR REPLACE INTO Employee (id, role, name) 
        #VALUES (  1, 
        #    'code monkey',
        #    (SELECT name FROM Employee WHERE id = 1)
        #  );

        """
        sql = 'SELECT EXISTS(SELECT * FROM '+ self.table_name +' WHERE word LIKE '+ word +');'
        self.conn.execute(sql)
        if self.conn.fetchone():
            print 'Już jest ', word
        else:
            print 'nie ma'
        """
        #if self.conn.execute(sql) == True:
        #    print "exist"
        """
        try:
            with self.conn:
                self.conn.execute('''INSERT INTO '''+ self.table_name +''' VALUES(?,?)''', (word, 1))
        except sqlite3.IntegrityError:
            print('Record ' + word+ ' already exists')

        """
        # lid = cur.lastrowid
        # print "The last Id of the inserted row is %d" % lid
        
        
        #sql = 'SELECT * FROM '+ self.table_name +';'
        #self.conn.execute(sql)
        #self.conn.commit()
        #s = self.conn.fetchone()
        #print word
