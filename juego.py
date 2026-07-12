print(r'''
           .,,,,,,,,,,.
         ,;;;;;;;;;;;;;;,
       ,;;;;;;;;;;;)));;(((,,;;;,,_
      ,;;;;;;;;;;'      |)))))))))))\\
      ;;;;;;/ )''    - /,)))((((((((((\
      ;;;;' \        ~|\  ))))))))))))))
      /     /         |   ((((((((((((((
    /'      \      _/~'    ')|()))))))))
  /'         `\   />     o_/)))((((((((
 /          /' `~~(____ /  ()))))))))))
|     ---,   \        \     ((((((((((
          `\   \~-_____|      ))))))))
            `\  |      |_.---.  \      
''')
print("Welcome to The Perfect Date.")
print("Your mission is to have a good impression and get a kiss at the end!")
decision_1 = input("You enter in the restaurant and you see your date is already waiting for you.\n There is table in the middle. You go Left or Right?")
if decision_1 == "Right" or decision_1 == "right" or decision_1 == "RIGHT":
    print("You slipped on a banana peel and now you are dead, you clumsy.")
if decision_1 == "Left" or decision_1 == "left" or decision_1 == "LEFT":
    decision_2 = input("You are heading to your table but all of a sudden a dog enters the room.\n He keeps barking at you and seems angry. Do you Move or Wait for the dog to be calmed?")
    if decision_2 == "Move" or decision_2 == "move" or decision_2 == "MOVE":
        print("You were bitten by the dog. Since you are hypochondriac you ran to the hospital.\n You got killed by a car on your way.")
    if decision_2 == "Wait" or decision_2 == "wait" or decision_2 == "WAIT":
        decision_3 = input("The pet parent took the dog. You finally get to have your lunch.\n When you are done your date asks you which would be the perfect place for a second date. \nCoffeehouse/Mall Center/Disco")
        if decision_3 == "Mall Center" or decision_3 == "mall center" or decision_3 == "MALL CENTER":
            print("At the end, both of you lost interest, second date never happened. Game over, or not?")
        elif decision_3 == "Disco" or decision_3 == "disco" or decision_3 == "DISCO":
            print("Your date is not a disco person, you ended up being friends, nice!" )
        elif decision_3 == "Coffeehouse" or decision_3 == "coffeehouse" or decision_3 == "COFFEEHOUSE":
            print("You went to that second date and enjoyed the Saturday afternoon talking about interests, life, books and passions. \n You both thought the second date was a perfect date. There will not be third date because this game only has part 1.")
else:
    print("Choose!")



