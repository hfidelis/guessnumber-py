from random import randint

symbols = "!@#$%¨&*()_-=+§ª\º/°;:|><.,}{[]"
computerNumber = randint(0, 10)
timesPlayed = 0
won = False

while not won:
    userNumber = (input("\n\033[1:32:40m>> I'm thinking about a number between 0 and 10!\033[m"
                        "\n         \033[1:32:40m>> Try to guess which one!\033[m\n"))
    timesPlayed += 1
    if userNumber.isalpha() is False and userNumber not in symbols:
        userNumber = int(userNumber)
        if -1 < userNumber < 11:
            if userNumber == computerNumber:
                print(f"\n\033[1:33:40m>> Congratulations! You won!\033[m\n\033[1:33:40m>> Your number: {userNumber}"
                      f"\033[m\n\033[1:33:40m>> Computer number: {computerNumber}\033[m"
                      f"\n\033[1:32:40m>> Your tries: {timesPlayed}\033[m")
                won = True
            else:
                if userNumber < computerNumber:
                    print("\n\033[1:35:40m>> A little more... Try again!\033[m")
                    won = False
                elif userNumber > computerNumber:
                    print("\n\033[1:35:40m>> A little less... Try again!\033[m")
                    won = False
        elif userNumber > 10 or userNumber < 0:
            print("\n\033[1:31:40m>> You need to insert a number between (0) and (10)!... <<\033[m")
            won = False
    elif userNumber.isalpha() is True or userNumber.isalnum() is True or userNumber in symbols:
        print("\n\033[1:31:40m>> That's not a number! <<\033[m\n     \033[1:31:40m>> Try again! <<\033[m")
        won = False
