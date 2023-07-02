secret_word = "Love"
guess = " "
guess_count = 0
guess_limit = 3
out_of_time = False

while guess != secret_word and not(out_of_time) :
    if guess_count < guess_limit :
         guess = input("Enter Your Guess Word :")
         guess_count += 1
    else :
         out_of_time = True
     
if out_of_time :
    print ("😞😞, You Lose")
else : 
    print ("🎉🎉🎉, You Win")