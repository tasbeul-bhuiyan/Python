f=open('hello.txt','r')
print(f.readline(),end="")
print(f.readline(),end="noob")
print(f.readline())
f1=open('hell.txt','w')
print(f1.write("hello world\n"))
print(f1.write("welcome to python"))
for data in f :
    f1.write(data)
g=open('pic.png','rb')
g1=open('mupic.png','wb')
xfile = open('mbox.txt')
count=0
for cheese in xfile:
    count += 1
    print(cheese)
print(count)
a=xfile.read()
print(len(a))
print(a[:20])
for line in xfile:
    if line.startswith('as'):
        print(line)
for line in xfile:
    if line.startswith('uj'):
        continue
    print(line)
fhand=input("Enter file name: ")
fhand=open(fhand)
count=0
print(fhand)

sentence="hELLo wORLd"  
sentence=sentence.lower()
sentence=sentence.split()
a=0
while a<len(sentence):
    sentence[a]=sentence[a].capitalize()
    a=a+1
sentence=" ".join(sentence)
sentence=sentence.strip()
print(sentence)
a="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
a=a.split("@")[1]
print(a)
a=a.split()
print(a)
print(a[0])
domain={'hi':5,'hello':10}
print(domain['hi'])
print(len('''From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Date: Sat, 5 Jan 2008 09:12:18 -0500
To: source@collab.sakaiproject.org
From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39772 - content/branches/

From: louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
Subject: Re: Meeting update!
Hi team,
The meeting is at 3pm.

From: zqian@umich.edu Fri Jan  4 16:05:12 2008
Subject: Quiz-3 marks (updated).
Please check the spreadsheet.

From: rjlowe@iupui.edu Fri Jan  4 07:02:32 2008
Subject: Lunch?
Are we free at 1:00pm?

This line has trailing spaces.        

From: david.horwitz@uct.ac.za Thu Jan  3 11:22:33 2008
Subject: Re: Lunch?
Sure—let's go.

Random notes:
- Python, files, and errors.
- Email: test.user@Example.COM

Subject: This is a subject without a From line
'''.split()))
a=50/1
print(a)
def calculate_sum(a, b):
    print(a + b)

print(calculate_sum(3, 1)) # 4
def hi():
    a=1
    def hello():
        print(a)
    hello()
hi()
a=1
def outer_func():
    msg = 'Hello there!'
    res=''

    def inner_func():
        global res
        res = 'How are you?'
        print(msg)

    inner_func()
    print(res)
    print(a)

outer_func()
def greet():
    pass
    
print(greet())
