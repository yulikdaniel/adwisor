# adwisor

Описание
--------

Наша модель идентифицирует ошибки в
согласовании подлежащего и сказуемого, она работает на основе
токенизатора [spacy](https://spacy.io/).

Использование
-------------

На вход программе подается путь к папке с предложениями. В ней должны 
находиться либо только текстовые файлы либо только Excel таблицы, в которых 
должна быть колонка "Sentence" и, возможно, другие колонки, например, "Filename".
 Вторым аргументом можно уточнить, нужно ли программе выписывать все предложения и помечать, 
 в каких из них есть ошибка (only errors=False), или выписывать только предложения с ошибкой (only errors=True).Предложения можно записать в отдельный Excel файл с помощью команды writeln, 
которой надо передать массив предложений и путь к таблице.
Пример запуска:
```
f = search('directory', False)
writeln(f, "result.xlsx")
```

Установка
---------

Перед использованием программы необходимо установить следующие библиотеки:

- nltk
- pandas
- spacy
- xlswriter

Для этого можно ипользовать такие команды:
```
python3 -m pip install pandas xlsxwriter spacy nltk
python3 -m spacy download en_core_web_trf
```
Так же необходимо запустить такой python скрипт:
```
#!/usr/bin/env python

import nltk
nltk.download("punkt")
```

Важная информация
-----------------

Nет Vойне
