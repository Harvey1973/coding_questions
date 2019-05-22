import random

def monte_carlo():
    # initial status
    player1 = 2 
    player2 = 2
    count = 0
    denum = 0
    epochs = 1000000

    for i in range (epochs):
        # one epoch :
        p1_1 = random.randint(1,6)
        p1_2 = random.randint(1,6)
        #sum1 = p1_1 + p1_2
        sum1 = p1_1
        p2_1 = random.randint(1,6)
        p2_2 = random.randint(1,6)
        #sum2 = p2_1 + p2_2
        sum2= p2_1
        # comparison 
        # player 1 wins 
        if sum1 > sum2 :
            player1 += 1
            player2 -= 1
        elif sum1 < sum2 :
            player1 -= 1
            player2 += 1
        
        if player1 == 0 or player2 == 0:
            #denum = i - denum
            count = count + 1
            #reset 
            player1 = 2
            player2 = 2
        
    print(count/epochs)
    print(epochs/count)

monte_carlo()



