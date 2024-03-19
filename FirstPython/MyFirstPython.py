name = input("Enter your name: " )

print(f'Hello, {name}!')

def square():
    wysokosc = input("Podaj wysokość trójkąta: ")
    podstawa = input("Podaj długość podstawy trójkąta: ")
       
    wysokosc = int(wysokosc)
    podstawa = int(podstawa)

    pole = 0.5 * wysokosc * podstawa

    return pole

print("Pole trójkąta wynosi:", square())
