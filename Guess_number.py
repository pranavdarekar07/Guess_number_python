#Guess the output
import numpy as np
def main():
    score = 10
    match_num = np.random.randint(1,5)
    for i in range(5):
        guess = int(input("Enter the no "))
        if match_num == guess:
            print("You Win")
            break
        else:
            print("try again")
            score -= 2
    print(f"Your score is {score}")    
main()
