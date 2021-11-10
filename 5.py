# count the no of vowels in a string 

# def countVowels(string, vowels):
# 	result = [i for i in string if i in vowels]
# 	print(len(result))
	
	

# string = input()
# vowels = "AaEeIiOoUu"
# countVowels(string, vowels)
# ............................................ 
def countVowels(string):
	result = [i for i in string if i in ['a','e','i','o','u','A','E','I','O','U']]
	print(len(result))
string=input()
countVowels(string)
