# Juego adivinar el Nro
import random
Attemptsmade = 0

print('¡Hi! ¿what is your name?')
myName = input()

number = random.randint(1, 20)
print('Good, ' + myName + ', I am thinking one number between 1 and 20.')

while  Attemptsmade < 6:
    print('Try guess.') # Hay cuatro espacios delante de print.
    estimate = input()
    estimate = int(estimate)

    Attemptsmade = Attemptsmade + 1

    if estimate < number:
        print('Your estimate is very slowly.') # there are 8 spaces before 

        if estimate > number:
            print('You estimate is very tall.')

            if estimate == number:
                break

    if estimate == number:
        Attemptsmade = str(Attemptsmade)
        print('¡God job, ' + myName + '! ¡You guessed my number  in ' + Attemptsmade + ' Attempts!')
        if estimate != number:
            number = str(number)
            print('Well no. The number i was trying was ' + number)


