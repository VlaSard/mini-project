# Преобразование текста в псевдографику

```
▄▀▄ ▄▀▀ ▄▀ ▀ ▀    █▀▄ ▀▄░▄▀
█▀█ ░▀▄ █░ █ █    █░█ ░░█░░
▀░▀ ▀▀░ ░▀ ▀ ▀ ▀░ █▀░ ░░▀░░
```

Небольшой консольный проект, для преобразования введенного слова в символы псевдографики.

Вводится должно только одно слова, которое может содержать только буквы английского языка и цифры.

Результат работы конвертера записывается в файл **ascii.txt** и выводится в консоль.

Вывод конвертера может использоваться в файлах конфигурации для визуального оформления

Ниже приводится пример вывода в консоль:

```
▄▀▄ ▄▀▀ ▄▀ ▀ ▀
█▀█ ░▀▄ █░ █ █
▀░▀ ▀▀░ ░▀ ▀ ▀
```

## Состав проекта:

```
abc_ascii
├── ascii.json
├── ascii.py
├── AUTHORS
├── CHANGELOG.md
├── README.md
└── src
    ├── abc
    ├── abc_ascii
    ├── ascii
    ├── number
    ├── number_ascii
    └── punctuation
```

 - ascii.json - кодировка символов в псевдографике, включает цифры и символы английского алфавита.
 - ascii.py - конвертер текста
 - AUTHORS - автора проекта
 - CHANGELOG.md - изменения в проекте
 - src - директория с файлами символов
   - src/abs - содержит английский алфавит в одну строку
   - src/ascii - набор символов псевдографики
   - src/abc_ascii - тоже, только в колонку
   - src/number - цифры, в одну строку
   - src/number_ascii - тоже, в колонку
   - src/punctuation - некоторые символы пунктуации

