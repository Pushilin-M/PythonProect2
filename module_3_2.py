
def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    while recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
        break
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    while sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        break
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')



send_email('Проверка работы кода', 'vasyok1337@gmail.com')
send_email('Проверка работы кода', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Проверка работы кода', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Проверка работы кода', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
