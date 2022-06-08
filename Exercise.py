# Exercise 2: Write a program to count vowels and consonants in a string.



def conso_vowels(word):
    vowel=0
    const=0
    list=['a','e','i','o','u']
    for i in word:

       if i in list:
          vowel+=1   
          print(f"The number of vowels is {vowel}")
       else:
         const+=1
         print(f"The number of consonants is {const}")
conso_vowels("virginia")                

        
   
    
 

    
