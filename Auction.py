from replit import clear # this module work only in replit 'replit.com'
import art # The art file is also in PythonBeginner with the name of art.py ,it is just a logo if you want to use it do copy it

#HINT: You can call clear() to clear the output in the consol
print(art.logo)
bids={}
bidding_end =False

def highest_bid(bid_data):
  high=0
  winner=''
  for bid in bid_data:
    bidamount=bid_data[bid]
    if bidamount> high:
      high=bidamount
      winner=bid
  print(f"The winner is {winner} with the bid of {high} ")    




while not bidding_end:
  Name=input("Enter your name ?\n")
  price=int(input('Enter bid amount: RS'))
  bids[Name]=price
  more=input("Any one else want to bid ?Type 'yes or no.").lower()
  if more =='no':
    bidding_end =True
    highest_bid(bids)
  elif more=='yes':
    clear()  
