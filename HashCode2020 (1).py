# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:11:48 2020

@author: Gowrienanthan
"""

with open('b_read_on.txt','r') as f:
    temp1=f.read() 



inp=temp1.strip().split('\n')

b,l,d=map(int,inp[0].split()) ##line 1

s=list(map(int,inp[1].split())) ##individual book score

n=[]    ##no of books in each library
t=[]    ##no of days for signup
m=[]     ##no of book per day
l=[]    ## library book list
lbs=[]  ##library book score
temp=inp[2:]


for i in range(0,len(temp),2):
  tn,tt,tm=map(int,temp[i].split())   ##for list n,t,m of library i
  n.append(tn)
  t.append(tt)
  m.append(tm) 
  ll=list(map(int,temp[i+1].split()))  ##ids of book in libray i
  l.append(ll)

  score=[s[k] for k in ll]
  totscore=sum(score)

  weight=(tn**2/tm)/tt
  lbs.append(weight)

from operator import itemgetter
libin,sortedlbs =map(list, zip(*sorted(enumerate(lbs), key=itemgetter(1), reverse=True)))


print(libin)

print(sortedlbs)




scanned_books = set()
books_to_scan = []

f2=open('submission.txt','w+')

total_signup_time = 0
number_of_libraries = 0

for lib_id in libin:
    
    if t[lib_id] > d:
        break
    
    total_signup_time += t[lib_id]
    if total_signup_time > d:
        break
    #set of books in the library
    N_lib = set(l[lib_id])
    
    n_books = 0
    books_to_scan.clear()
    for book in l[lib_id]:
        if book in N_lib-scanned_books:
            books_to_scan.append(book)
            n_books += 1
    
    if len(books_to_scan)==0:
        continue
    
    number_of_libraries += 1 
    
    
    

    
    
    
    
    #add library id to line and add no.of books in library to line
    line1 = str(lib_id) + ' ' + str(n_books)
    f2.write(line1)
    
    #next line, add book ids in sorted order 
    bl=list(map(str,books_to_scan))
    f2.write('\n')
    print(' '.join(bl))
    f2.write(' '.join(bl))
    f2.write("\n")
    
    #add books to set of scanned books
    scanned_books.update(l[lib_id])

f2.close()
first_line = str(number_of_libraries)+'\n'
f2=open('submission.txt','r')
con=f2.readlines()
f2.close
con.insert(0,first_line)
con="".join(con)
f2=open('submission.txt','w')
f2.write(con)


f2.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    