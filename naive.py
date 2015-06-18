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

class myNaiveBayes:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('bayes.db')
        except NameError, x:
            print "Connection failed!", x
            raise

    def dbQuery(self, table_name, spam_or_ham):
        self.table_name = table_name

        sql = 'CREATE TABLE IF NOT EXISTS ' + self.table_name + \
                ' (word TEXT NOT NULL, \
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
        sql = 'SELECT * FROM '+ self.table_name + \
                ' WHERE word LIKE ' + word + ';'
        print sql


    def __del__(self):
        self.conn.close()



if __name__ == '__main__':
    myBayes = myNaiveBayes()
    myBayes.dbQuery('test', spam_set)
