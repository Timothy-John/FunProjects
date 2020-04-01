import re

passage=open('BibleBooksQuestion.txt','r')
passage=passage.read()
passage=passage.lower()
passage=re.sub('[0-9]','',passage)
passage=re.sub('[.,()]','',passage)
passage=re.sub(' ','',passage)

books=open('books.txt','r')
books=books.read()
books=books.lower()
books=re.sub('[0-9]','',books)    # can use \d instead of 0-9
books=re.sub(' ','',books)
books=re.sub('\n',"|",books)      # | means OR

print(passage)
r=re.compile(books)
print("\n",books)
print("\n",r.findall(passage),"\n")