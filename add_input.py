username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
temp_created_date = input('Введите дату день-месяц-год, начала работы цифрами через тире: ')
temp_issue_date = input('Введите дату день-месяц-год, конец работы цифрами через тире: ')
print(f'Имя пользователя: {username}','\n' f'Заголовок заметки: {title}','\n' f'Описание заметки: {content}','\n' f'Статус заметки: {status}','\n', f'Дата в начале: {temp_created_date}','\n', f'Дата сдачи: {temp_issue_date}')