# Задача "Рассылка писем":
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# 1. Проверка на корректность e-mail отправителя и получателя.
# 2. Проверка на отправку самому себе.
# 3. Проверка на отправителя по умолчанию.
#
# Пункты задачи:
# 1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# 2. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# 3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# 4. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# 5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# 6. Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# 7. За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
#
def send_email(message, recipient, sender = "university.help@gmail.com"): # Создайте функцию send_email
    # ------------------------------------ Пункт задачи № 2 ----------------------------------
    if "@" in recipient and (".com" in recipient or ".ru" in recipient or ".net" in recipient):
        if "@" in sender and (".com" in sender or ".ru" in sender or ".net" in sender):
            if sender == recipient:  # ------------------------------- Пункт задачи № 3 ----------------------------------
                print("Нельзя отправить письмо самому себе!")
            else:
                if sender == "university.help@gmail.com":  # --------------Пункт задачи № 4 -----------------------------
                    print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
                else:  # -------------------------------------------------Пункт задачи № 5 -----------------------------
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
# Проверяем варианты отправки почты
send_email("Приветствую тебя, о повелитель", "1234567p@mail.ru")
print()
send_email("Приветствую тебя, о повелитель", "1234567p@mail.du")
print()
send_email("Приветствую тебя, о повелитель", "1234567pmail.ru")
print()
send_email("Приветствую тебя, о повелитель", "university.help@gmail.com")
print()
send_email("Приветствую тебя, о повелитель", "1234567@gmail.com", sender = "university.help@gmail.ru" )