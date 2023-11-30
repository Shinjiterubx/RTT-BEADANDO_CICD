import math


def bekeres(bejovo_parameter):
    while True:
        try:
            value = float(input(bejovo_parameter))
            if value <= 0:
                raise ValueError("Nem lehet negatív szám.")
            return value
        except ValueError:
            print("Nem megfelelő szám.")


def pitagorasz_tetel(a, b):

    c_negyzet = a ** 2 + b ** 2

    result = math.sqrt(c_negyzet)
    return result


def terulet_szamitas(a, b):

    terulet = 0.5 * a * b
    return terulet


def kerulet_szamitas(a, b, c):

    kerulet = a + b + c
    return kerulet


def main():

    a_oldal = bekeres("Ird be az a oldal hosszat: ")

    b_oldal = bekeres("Ird be a b oldal hosszat: ")

    result = pitagorasz_tetel(a_oldal, b_oldal)

    terulet = terulet_szamitas(a_oldal, b_oldal)

    kerulet = kerulet_szamitas(a_oldal, b_oldal, result)

    print(f"Az oldal hossza:  {result}")
    print(f"Derekszogu háromszog területe:  {terulet}")
    print(f"Derekszogu háromszög területe:  {kerulet}")


if __name__ == "__main__":
    main()