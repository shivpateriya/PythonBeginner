#python 
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
choice=input("you're at a crossroad,where do you  want to go?  type 'left' or 'Right'.\n ").lower()
if choice=='left':
  cross=input("Well!!\ Now we have to cross the river to get to the TREASURE island\n DO you want to 'wait' for boat or You want to 'Swim.'  ").lower()   
  if cross=='wait':
    print('''


               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~

    ''')
    door=input("Great you have crossed river\n Here is three gate choice one to get your Treasure'RED','BLUE','YELLOW'").lower()
    if door=='yellow':
      print('''


      {} {}
                          !  !  ! II II !  !  !
                       !  I__I__I_II II_I__I__I  !
                       I_/|__|__|_|| ||_|__|__|\_I
                    ! /|_/|  |  | || || |  |  |\_|\ !
        .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
       /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \
       \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
        }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
       {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
 _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
 _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
 -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
  |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
  |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
  |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
  |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  |
 _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
 -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
 ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~


      ''')
      print('YOU got the treasure')
    else:
      print('ooops!!you got robbered,GAME OVER')    
  else:
    print('you have been swollen by sharks!!')
    print('Oooops !! you fell into hole !!\n GAME OVER....')
else:
 print('YOU ARE FELL INTO HOLE!!GAME OVER')
