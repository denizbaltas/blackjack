
import random

class game:
    def __init__(self): 
        cards = self.cards()
        balance = 1000
        while True : 
            if balance == 0 : 
                print("Your Balance Is 0 You Lost \n ")
                break

            bet = int(input(f"You Have {balance} balance\nHow Much Do You Want to Bet : "))
            
            if bet > balance : 
                print(f"Your Max Bet is {balance}")
                continue

            if bet == 0 : 
                print("Bet Must Be More Than 1")
                continue

            userCards = []
            userCards.append(self.hit(cards))
            userCards.append(self.hit(cards))

            print(f"User Hand : {userCards} \nUser Hand Value : {self.cardvalues(userCards)}\n")


            dealerCards = []
            dealerCards.append(self.hit(cards))
            dealerCards.append(self.hit(cards))
            print(f"Dealer Cards : [{dealerCards[0]}, ?] \nDealer Hand Value : {self.dealervalue(dealerCards)}\n")

            while True : 
                if self.cardvalues(userCards) == 21 and self.cardvalues(dealerCards) != 21 : 
                    print("You Won")
                    break
                elif self.cardvalues(userCards) == 21 and self.cardvalues(dealerCards) == 21 :
                    print("Tie")
                    break

                choice = input("Hit or Stand : ")
                choice = choice.lower()
                if choice[0] == "h" : 
                    userCards.append(self.hit(cards))
                    print(f"User Hand : {userCards} \nUser Hand Value : {self.cardvalues(userCards)}\n")

                elif choice[0] == "s": 
                    while self.cardvalues(dealerCards) <= 16 :
                        dealerCards.append(self.hit(cards))
                    
                    print(f"Dealer Cards : {dealerCards}\nDealer Card Value {self.cardvalues(dealerCards)}\n")
                    
                    finalDealerCardValue = self.cardvalues(dealerCards)
                    finalUserCardValue = self.cardvalues(userCards)

                    if finalDealerCardValue > 21: 
                        print("Dealer Busted You Won\n")
                        balance += bet
                    elif finalDealerCardValue < finalUserCardValue : 
                        print("You Won\n") 
                        balance += bet
                    elif finalUserCardValue < finalDealerCardValue : 
                        print("You Lost\n")
                        balance -= bet
                    elif finalDealerCardValue == finalUserCardValue :
                        print("Tie\n")

                    break

                else : 
                    print("Type hit or stand\n")

                if self.cardvalues(userCards) == 21 and self.cardvalues(dealerCards) != 21 : 
                    print("You Won\n")
                    balance += bet
                    break
                elif self.cardvalues(userCards) == 21 and self.cardvalues(dealerCards) == 21 : 
                    print("Tie\n")

                elif self.cardvalues(userCards) > 21  :
                    print("Busted\n")
                    balance -= bet
                    break
            print(f"Your Balance : {balance}\n")

    def hit(self,cards): 
        card = random.choice(cards)
        cards.remove(card)
        return card

    def cardvalues(self,handCards):
        toplam = 0
        for x in handCards : 
            if x == "K" : 
                x = 10
            elif x == "Q" : 
                x = 10 
            elif x == "J" : 
                x = 10
            elif x == "A" : 
                controlCards = handCards
                controlCards.remove("A")

                if 10 >= self.cardvalues(controlCards) : 
                    x = 11
                elif 10 < self.cardvalues(controlCards) :
                    x = 1
                
            
            toplam += x
        return toplam

    def dealervalue(self,handCards): 
        if handCards[0] == "K" : 
            toplam = 10
        elif handCards[0] == "J":
            toplam = 10
        elif handCards[0] == "Q": 
            toplam = 10

        else : 
            toplam = handCards[0]
        
        return toplam


    def cards(self):
        cards = []
        for x in range(24):
            cards.append(1)
            cards.append(2)
            cards.append(3)
            cards.append(4)
            cards.append(5)
            cards.append(6)
            cards.append(7)
            cards.append(8)
            cards.append(9)
            cards.append(10)
            cards.append("Q")
            cards.append("J")
            cards.append("K")
            cards.append("A")
        return cards
game()