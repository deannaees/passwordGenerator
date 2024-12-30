import random 
import string 


#random selection 
def random_password(letter_limit): 
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '123456789'
    character = '@!$#'
    random_letters = " "
    random_nums = " "
    password = " "
    if letter_limit % 2 == 0:
    # even numb so half the random letters and nums evenly
        for i in range(letter_limit/2):
            random_letter = random.choice(letters)
            random_letters += random_letter
        for i in range((letter_limit/2)-1):
            random_num = random.choice(digits)
            random_nums += random_num
        password = random_letters + random.choice(character) + random_nums
    else: #odd length password
        midpoint = letter_limit//2
        for i in range(midpoint):
            random_letter = random.choice(letters)
            random_letters += random_letter
        for i in range(midpoint, letter_limit-1):
            random_num = random.choice(digits)
            random_nums += random_num
        password = random_letters + random.choice(character) + random_nums


    

     

    # delete white space
    complete_password = password.replace(" ","")
 

  



    print(complete_password, "length: ", len(complete_password))
        
   
      
  
   # random_number = random.randrange(1,10)
if __name__ == "__main__":
    length_password = input("enter length requirement: ") 
    random_password(length_password)
    