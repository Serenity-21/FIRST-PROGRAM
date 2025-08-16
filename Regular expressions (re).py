import re
text="Vijay's phone number is 866788-9431 and Vijay got another number"
pattern='Vijay' in text
print(pattern)


re.search('Vijay',text) #give out whether there is a match and index of the match

match=re.search('Vijay',text)

match.span() #span of the word eg: Vijay got 5 letters so the span is 0 to 5

re.findall('Vijay',text)

len(re.findall('Vijay',text)) #to find the length of the match "you can assign this to any word eg; matches=re.findall('Vijay',text)

text="Vijay's phone number is 866788-9431 and Vijay got another number"
for match in re.finditer('Vijay',text):
    print(match)
    text="Vijay's phone number is 866788-9431 and Vijay got another number"
for match in re.finditer('Vijay',text):  #re.finditer combines findall and .search
    print(match)

# \d is for digits
# \w is for alphanumerics(Ab-2b \w\w-\w\w)
# \s is for white space
# \D is for a non digit(ABC)
# \W is for non alphanumerics(symbols like @#!^&**)
# \S is for non whitespace(HIHI)
# + is for occurs one or more times
# {3} occurs exactly 3 times
# {2,4} occurs 2 to 4 times
# {3,} occurs 3 or more times
# * is for occurs 0 or more times
# ? is for occurs once or none


import re
number= 'Vijay use a phone number 866-788-9431'
re.search(r'\d{3}-\d{3}-\d{4}',number)
numbersearch= re.compile(r'(\d{3})-(\d{3})-(\d{4})')  #Complile is used to group the patterns we created as one use them as a word instead of typing everytime
result=re.search(numbersearch,number)
result.group(2) # this is used to call out the result associated with the pattern in 2nd group
print(result)
#%%
#| is used as or command.
re.findall(r'the|at','Vijay sat at the table which was at the hall which had a hat')
#%%
# placing . before the pattern acts like a blank filling the missing one even if not mentioned. the number of dots given reflect the number of blanks before the pattern
re.findall(r'.at','Vijay sat at the table which was at the hall which had a hat')
#%%
#[^] is used to exclude any given pattern
exclude= r'[^at]'
re.findall(exclude,'Vijay sat at the table which was at the hall which had a hat')
#%%
# ^ before any pattern means starts with so it brings by which the statement start if it presents in the pattern
re.findall(r'^\d','21 of the August is my birthday')

#%%
# $ is used for ends with
re.findall(r'\w$','Vijay')
#%%


import re
mail= 'vijay21@gmail.com'
mailpattern= r'[\w]+[\w]+@gmail.com'
re.findall(mailpattern,mail)