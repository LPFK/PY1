# verbs are functions, nouns are variables, adjectives are data types, adverbs are arguments,
# prepositions are operators, conjunctions are control structures, interjections are comments

#Functions in python are defined using the def keyword. 
#Variables are defined using the = operator.
#Data types are defined using the type() function.
#Arguments are defined using the () operator.
#Operators are defined using the + - * / operator.
#Control structures are defined using the if, elif, else keywords.

# methods exist for str such as .lower() or .upper() to convert a string to lowercase or uppercase respectively.

# conditionals are > >= <= < == != >= <=


nom = input("Who are you ?").capitalize() # create a variable named 'nom' and assign it the value of the user's input
print(f"Hello, how are you {nom} ?") # print the gathered value of the variable 'nom', here we use an f-string
#print('Hello, how are you', nom, '?') # print the gathered value of the variable 'nom', here we use a string

salutation = "Hiiii" # create a variable named 'salutation' and assign it the value of "Hiiii" this variable is a str data type (string) 
print(salutation + ", how are you " + nom + " ?") # print the gathered value of the variable 'nom', here we use a string
