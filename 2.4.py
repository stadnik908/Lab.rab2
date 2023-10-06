try:
    chislo = int(input("Ваше целое число: "))
except ValueError:
    print("Ваш ввод неверный!")
finally:
    print("Программа завершила свою работу")