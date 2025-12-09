# def WordCount():

#     phrase = input().strip()
#     total_words = phrase.count(' ')+1
#     print(total_words)

# WordCount()

# def ConeVolume():

#     PI = 3.141592653589793
#     radius = int(input())
#     height = int(input())
#     volume = (PI*(height**2)*radius)/3
#     print(volume)

# ConeVolume()

# def WhoWon():
#     appleScoreThree = int(input())
#     appleScoreTwo = int(input())
#     appleScoreOne = int(input())
    
#     bananaScoreThree = int(input())
#     bananaScoreTwo = int(input())
#     bananaScoreOne = int(input())

#     TotalAppleScore = appleScoreOne + appleScoreTwo*2 + appleScoreThree*3
#     TotalBananaScore = bananaScoreOne + bananaScoreTwo*2 + bananaScoreThree*3

#     if TotalAppleScore > TotalBananaScore:
#         print("Apple Won!")
#     elif TotalBananaScore > TotalAppleScore:
#         print("Banana Won!")
#     else:
#         print("It's a tie!")

# WhoWon()


# def TelemarketerNumber():

#     firstDigit = int(input())
#     secondDigit = int(input())
#     thirdDigit = int(input())
#     fourthDigit = int(input())

#     phoneNumber = list([firstDigit,secondDigit,thirdDigit,fourthDigit])

#     if phoneNumber[0] == 8 or 9 and phoneNumber[1] == phoneNumber[2]:
#         print("This is a Telemarketer!")
#     else:
#         print("This is not a telemarketer")

# TelemarketerNumber()

# def ThreeCups():

#     swaps = input()
#     ball_location = 1

#     for swap_type in swaps:
#         print(ball_location)
#         if swap_type == 'A' and ball_location == 1:
#             ball_location = 2
#             print(ball_location)
#         elif swap_type == 'A' and ball_location == 2:
#             ball_location = 1
            
#         elif swap_type == 'B' and ball_location == 2:
#             ball_location = 3
            
#         elif swap_type == 'B' and ball_location == 3:
#             ball_location = 2
            
#         elif swap_type == 'C' and ball_location == 1:
#             ball_location = 3
            
#         elif swap_type == 'C' and ball_location == 3:
#             ball_location = 1
            
#     print(ball_location)

# ThreeCups()

# def OccupiedSpaces():

#     # n = int(input())
#     yesterday = input()
#     today = input()

#     occupied = 0

#     for position in range(len(yesterday)):
#         if yesterday[position] == 'C' and today[position] == 'C':
#             occupied = occupied + 1
#     print(occupied)

# OccupiedSpaces()

# def DataPlan():

#     monthly_mb = int(input())
#     n = int(input())
#     total_mb = monthly_mb * (n + 1)
#     for i in range(n):
#         used = int(input())
#         total_mb = total_mb - used
#     print(total_mb)

# DataPlan()

# def SlotMachines():

#     quarters = int(input())        # tracks the number of quarters that Martha has.
#     first = int(input())           # tracks the number of plays since the last payment.
#     second = int(input())          # tracks the number of plays since the last payment.
#     third = int(input())           # tracks the number of plays since the last payment.
#     plays = 0                      # tracks the number of slot machines that Martha has played.
#     machine = 0                    # tracks the slot machine that Martha will play next.

#     while quarters >= 1:

#         quarters = quarters -1

#         if machine == 0:                                            # Check which machine we're on
#             first = first + 1                                       # Increase the number of plays for this particular machine
#             if first == 35                                          # Check if it is time to payout
#                 first = 0                                           # If the payout was made then start the count of number of plays all over again
#                 quarters = quarters +30                             # If number of plays for this machine has reached 35 then add 30 quarters for Martha out of the remaining quarters she already has 
        
#         elif machine == 1:
#             second = second +1
#             if second = 100:
#                 second = 0
#                 quarters = quarters + 60
        
#         elif machine == 2:
#             third = third + 1
#             if third == 10:
#                 third = 0
#                 quarters = quarters + 9
        
#         plays = plays + 1
#         machine = machine + 1
#         if machine == 3:
#             machine = 0
        
#     plays = plays + 1
#     machine = machine + 1
#     if machine == 3:
#         machine = 0

#     print("Martha's plays", plays, "times befote going broke.")

# SlotMachines()


# def SlotMachinesCount():

#     quarters = int(input())
#     first = int(input())
#     second = int(input())
#     third = int(input())

#     plays = 0

#     while quarters >=1:
#         machine = plays % 3
#         quarters = quarters -1
        
#         if machine == 0:
#             first = first +1
#             if first % 35 == 0:
#                 quarters = quarters + 30
        
#         elif machine == 1:
#             second = second + 1
#             if second % 100 == 0:
#                 quarters = quarters + 60
        
#         elif machine == 2:
#             third = third + 1
#             if third % 10 == 0:
#                 quarters = quarters + 9

#         plays = plays + 1

#     print(f"Martha plays, {plays} times before going broke.")

# SlotMachinesCount()


# def SongPlaylist():

#     songs = 'ABCDE'
#     button = 0

#     while button !=4:
#         button = int(input())
#         presses = int(input())

#         for i in range(presses):
#             if button == 1:
#                 songs = song[1:] + songs[0]

#             elif button == 2:
#                 songs = songs[-1] + songs[:-1]
            
#             elif button == 3:
#                 songs = songs[1] + songs[0] + songs[2:]

#     output = ""

#     for song in songs:
#         output = output + song + " "
    
#     print(output[:-1])

# SongPlaylist()


# def SecretSentence():

#     sentence = input()

#     result = ""
#     i = 0

#     while i < len(sentence):
#         result = result + sentence[i]
#         if sentence[i] in "aeiou":
#             i = i + 3
#         else:
#             i = i + 1
#     print(result)


# SecretSentence()


def Playlist()

    songs = 'ABDE'

    While True:
        button = int(input())

        if button == 4:
            break
        presses = int(input())
        for i in range(presses):
            if button == 1:
                songs = songs[1:] + songs[0]
            elif button == 2:
                songs = songs[-1] + songs[:-1]
            elif button == 3:
                songs = songs[1] + songs[0] + songs[2:]

    output = ''
    for song in songs:
        output = output + song + ' '
    print(output[:-1])

Playlist()