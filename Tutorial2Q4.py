'''
Created on 1 Oct 2017
4. You see the code “string[::-1]” in some python code on the internet. You might guess that is 
has something to do with slicing a string (slicing is taking a subsection or substring e.g. print 
"0123456789"[2:5] will print 234). It is difficult to Google “python string[::-1]” for example, 
as Google largely ignores punctuation symbols such as “:” and “]” (see 
http://www.techradar.com/news/internet/web/101-google-tips-tricks-and-hacks-462143). 
What experiments can you devise to understand “string[::-1]”? When you write your own 
programs you should test them, and this exercise is about developing a set of test/questions 
to make sure you understand what “string[::-1]” does. 
@author: campbell
'''

TestString = "0123456789"

print(TestString[::-1])
print(TestString[-1:3:-1])
print(TestString[0:9:-1])
print(TestString[::-1])
print(TestString[::-1])
