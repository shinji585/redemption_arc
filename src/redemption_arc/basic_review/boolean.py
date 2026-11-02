def main():
    sebastian = "Sebastian"
    samuel = "Samuel"
    SANTIAGO = "SANTIAGO"

    if (
        sebastian.casefold() == samuel.casefold()
        and sebastian.casefold() != SANTIAGO.casefold()
    ):
        print("Sebastian es caga")
    elif (
        samuel.casefold() != sebastian.casefold()
        and SANTIAGO.casefold() != samuel.casefold()
    ):
        print("Samuel es un crack")
    else:
        print("Santiago es caga")


if __name__ == "__main__":
    main()
