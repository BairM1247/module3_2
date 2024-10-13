def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" not in recipient or "@" not in sender) or \
       (not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"))) or \
       (not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет!", "vasyok1337@gmail.com")
send_email("Привет!", "urban.fan@mail.ru", "urban.info@gmail.com")
send_email("Привет!", "urban.student@mail.ru", 'urban.teacher@mail.uk')  # Невозможно отправить письмо
send_email("Привет!", "university.help@gmail.com", "university.help@gmail.com")