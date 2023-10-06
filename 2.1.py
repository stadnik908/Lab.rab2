def is_password_good(password):
    answer = False
    if len(password) > 7 and not password.isupper() and not password.islower() and not password.isdigit():
        for i in password:
            if i.isdigit():
                answer = True
    return answer


pas = input("Введите пароль : ")
print(is_password_good(pas))
