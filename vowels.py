s=raw_input("enter the string")
w=""
for i in s:
 if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
   continue
 else:
  w=w+i
print "after removing vowels",w
k=s.upper()
print "after converting to uppercase char",k
f=raw_input("enter the word to search")
p=s.find(f)
if(p==-1):
 print "the word is not there"
else:
 print "the index value of given word is",p
t=raw_input("enter the substring")
q=s.count(t)
print "no: of occurences",q
