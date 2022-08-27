# -*- coding: utf-8 -*-
"""
Code x August
"""
#Request user's input
def main():
    tweet = input('Enter a tweet: ')
    def words_list():                 #define a function to split the sentence
        words = tweet.split()         #separates the words at each space
        return words

    words = words_list()
#print(words) 

#count the words on the tweet                                   
    count = 0   
    for word in words:
        count = count +1
    print(f"Number of words: {count}")
    #len(words)
    #define average function
    def avg_char(): #compute the average number if characters in tweet words
        average = len(tweet)/len(words) #Divide number of letters by number... 
        return average                  #of words by the number of words
    average = avg_char() #Call the function

    print(f"average number of characters: {(average):.2f}")
    count_upper = 0 #count uppercase letters, start at 0 
    for letter in tweet: #use for loop to check through tweet
        if letter.isupper() : 
            count_upper = count_upper + 1 
    print(f"Number of upper case letters: {count_upper}",)
    count_lower = 0 #count lower case letters
    for letter in tweet:
        if letter.islower() :
            count_lower = count_lower + 1
    print(f"Number of lower case letters: {count_lower}",)
    count_all = len(tweet) #reverse the tweet
    rev = ""
    while count_all >=0 : 
            count_all = count_all - 1
            rev = rev + tweet[count_all]
    print(rev) #the tweet is print backwards
    alphabets = 0               #Cont alphabets, digits, and special characters, 
    digits = 0                  #ombined to simplify special character counting
    special = 0 
    for i in range(len(tweet)): 
        if((tweet[i] >= 'a' and tweet[i] <= 'z') or (tweet[i] >= 'A' and tweet[i] <= 'Z')): 
            alphabets = alphabets + 1 
        elif(tweet[i] >= '0' and tweet[i] <= '9'):
            digits = digits + 1
        elif(tweet[i] == ' '):       
            pass
        else:
            special = special + 1
    #print the counts
    print(f"Number of alphabets (a to z and A to Z): {alphabets}",)
    print(f"Number of digits: {digits}",)
    print(f"Number of special characters: {special}",)
    
    
main()