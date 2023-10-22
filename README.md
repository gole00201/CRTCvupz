## АРМ для воздухозаборников серии ВУПЗ
Вводные: Электронная управляющая аппаратура имеет выводы RS-485 протокола, и зашитый асинхронный формат общения с пользователем (Запрос - ответ). Запрос должен быть отправлен в виде строки, ответ соответственно тоже - строка. 

Задача: Была поставлена задача разработать программный продукт для десктопа электромехаников ШЧ-6 четвертой сортировочной горки. Чтобы была возможность оперативно по 485 стандарту получать информацию о тормозных позициях и иметь возможность подстраивать параметры не выходя из за рабочего места. 

Выбранный стек: pyserial + dearpygui + python3.10
## Пример взаимодествия с ВУПз-15Э

```
– bmk:XXX:getCount – запрос счетчиков срабатывания катушек и ступеней торможения
– bmk:XXX:getDelta − запрос коэффициентов, для расчета скорости нарастания и спада
давления
– bmk:XXX:getStatus − запрос общих параметров системы
– bmk:XXX:gPr − запрос давления

Запрос: bmk:009:getStatus
Ответ : bmk=009 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 
P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 
timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 
cs=114
```


## Карта проекта

- Написать парсер принимаемых строк ✔

- Описать протокол общения с ВУПз-15Э ✔

- Описать GUI в сотрудничестве с сотрудниками ШЧ-6 ✔

- Подготовить все аппаратные средства 

- Ввод программы в эксплуатацию 

- Написание текстовой части диплома


## Документация

[Документация к ВУПз-15Э](
https://drive.google.com/drive/folders/14EMP5XCe8nRsD5xzLtuE5_0WZRoL-A8t)

[Документация к dearpygui](
https://dearpygui.readthedocs.io)

[Документация к pyserial](
https://pythonhosted.org/pyserial/index.html)

## Настройка и запуск
- Установить необходимые зависимости **python3.11** -m pip install -r requriments.txt
- Для конфигурации тормозной позиции необходимо ввести корректные адреса в файл /cfg/stp_3.json
- python 3.11 ./main.py 


## Автор

- [@gole00201 - Волков Егор](https://github.com/gole00201)


![Logo](https://school292.spb.ru/wp-content/uploads/2021/04/%D0%BF%D0%B3%D1%83%D0%BF%D1%81.png)
![ЦКЖТ](https://nilksa.ru/wp-content/uploads/2017/05/ckzt_logo.gif)
