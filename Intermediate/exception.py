# tuna = int(input("What's your fave number?\n"))
# print(tuna)

while True:
    try:
        number = int(input('What\'s you favourite number?\n'))
        print(18/number)
        break
    except ValueError:
        print('Make sure and enter a number\n')
    except ZeroDivisionError:
        print('Don\'t pick zero.')
    except:
        break
    finally: 
        print('Loop completed.')