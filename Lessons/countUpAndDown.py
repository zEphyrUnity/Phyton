print("Едем на лифте...")


def countUpAndDown(number, flour):
    print(f"этаж номер: {number}")

    if number >= flour:
        print("Достижение базового случая, верхотура:)")
        return

    countUpAndDown(number + 1, flour)
    print(f"этаж номер: {number}")
    return


countUpAndDown(0, 4)
print("Опять на первом. Ураа")
