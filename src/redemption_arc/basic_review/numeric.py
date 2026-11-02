import math


def main():
    def integer_value(number: int, exponent: int):
        return int(math.pow(number, exponent))

    def decimal_value(number: float, exponent: float):
        return math.pow(number, exponent)

    def complex_value(number: int, exponent: int):
        return complex(math.pow(number, exponent))

    retult_integer = integer_value(number=2, exponent=2)
    result_decimal = decimal_value(number=2, exponent=2)
    result_complex = complex_value(number=2, exponent=2)

    print(f"Result for Integer Value: {retult_integer}")
    print(f"Result for Decimal Value: {result_decimal}")
    print(f"Result for Complex Value: {result_complex}")


if __name__ == "__main__":
    main()
