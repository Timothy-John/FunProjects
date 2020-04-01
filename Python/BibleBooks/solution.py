import re


def solution(question):
    if question==1:
        passage=open('BibleBooksQuestion1.txt','r')
    elif question==2:
        passage=open('BibleBooksQuestion2.txt','r')
    else:
        print("Enter 1 or 2 ONLY.....")
        repeat()

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

def repeat():
    c=int(input("Question 1 or Question 2 :  "))
    solution(c)    

c=int(input("Question 1 or Question 2 :  "))
solution(c)