﻿##Эмулятор CHIP8

##Автор - Плаксин Иван (plaksin-ivan2@mail.ru)

##Описание: Приложение является эмулятором CHIP8(языка программирования).

##Требования: Python версии 3.4 и выше

##Состав:
* chip8.py - графический запускатор
* cchip8.py - консольный запускатор
* virtual_chip8.py - модуль, реализующий все команды и поведение машины

##Примеры запуска:
* Для запуска игры нужно указать ее название первым аргументом
* py chip8.py MAZE(из консоли)

##Ключики:
* r - registers - вывод в консоли состояния регистров
* m - memory - вывод в консоли состояние памяти
* d - debug - вывод в консоли исполняемых команд и состояния счетчиков
* wd - without delay - запуск без режима задержки(моментальная отрисовка, но неиграбельно)

##Управление:
В зависимости от запущенной игры:
1, 2, 3, 4, q, w, e, r, a, s, d, f, z, x, c, v.

##Состав игр и описание:
1) "15PUZZLE"
Представляет собой набор одинаковых квадратных костяшек с нанесёнными числами, заключённых в квадратную коробку. Длина стороны коробки в четыре раза больше длины стороны костяшек для набора из 15 элементов, соответственно в коробке остаётся незаполненным одно квадратное поле. Цель игры — перемещая костяшки по коробке, добиться упорядочивания их по номерам, желательно сделав как можно меньше перемещений.

2) "Blinky"
Упрощенная версия Pacman, где главный герой должен "съесть" все шарики на поле избегая двух роботов 
3) "BLITZ"
Игрок управляет высадкой пассажиров и требуется высадить их таким образом, чтобы они успешно дошли до нижней границы(по пути их могут сбить проезжающие мимо объекты)
4) "BRIX"
Простейший арканоид - игрок контролирует небольшую платформу-ракетку, которую можно передвигать горизонтально от одной стенки до другой, подставляя её под шарик, предотвращая его падение вниз. Удар шарика по кирпичу приводит к разрушению кирпича. После того как все кирпичи на данном уровне уничтожены, происходит переход на следующий уровень, с новым набором кирпичей.
5) "CONNECT4"
Игра для двоих, в которой игроки сначала выбирают цвет фишек, а затем ходят по очереди, роняя фишки в ячейки вертикальной доски. Цель игры — расположить раньше противника подряд по горизонтали, вертикали или диагонали четыре фишки своего цвета. Существуют варианты игры с полем разного размера, с фишками в форме дисков или шариков.
6) "GUESS"
На экран подаются цифры, заданные определенным правилом. Игроку нужно угадать следующую цифру.
7) "HIDDEN"
Игра состоит из карточек с узорами, некоторые из которых совпадают. Все карточки перевернуты лицевой стороной от игрока(так, чтобы изначально узор не был виден). Игроку предстоит найти все одинаковые карточки так, чтобы они были выбраны последовательно, иначе совершается ошибка(количество возможных попыток ограничено).
8) "INVADERS"
Игрок управляет лазерной пушкой, передвигая её горизонтально, в нижней части экрана, а также отстреливая инопланетян, надвигающихся сверху экрана. Целью игры является уничтожение пяти рядов по одиннадцать инопланетян, которые двигаются горизонтально, а также вертикально, по направлению к низу экрана. Игрок имеет бесконечное количество патронов. Попадая в инопланетянина, игрок уничтожает его, за что получает очки. При уничтожении инопланетян, увеличивается скорость движения оставшихся, а также ускоряется темп звуковых эффектов.
9) "KALEID"
Рисует калейдоскоп на экране.
10) "MAZE"
Рисует картинку на экране.
11) "MERLIN"
На экране появляется четыре квадратика и воспроизводится анимация(мигание) определенных квадратиков в определенной последовательности. Игроку нужно запомнить и воспроизвести это еще раз, нажимая на соответствующие клавиши.
12) "MISSILE"
Игрок управляет выстрелом пушки, перемещающейся в нижней части экрана горизонтально независимо от игрока. Нужно в определенный момент совершить выстрел так, чтобы сбить объект, находящийся в верхней части экрана.
13) "PONG"
Является простейшим симулятором настольного тенниса. Небольшой квадратик, заменяющий пинг-понговый мячик, двигается по экрану по линейной траектории. Если он ударяется о периметр игрового поля или об одну из нарисованных ракеток, то его траектория изменяется в соответствии с углом столкновения.
Геймплей состоит в том, что игроки передвигают свои ракетки вертикально, чтобы защищать свои ворота. Игрок получает одно очко, если ему удаётся отправить мячик за ракетку оппонента.
Здесь соперником выступает машина.
14) "PONG2"
Немного другой PONG.
15) "PUZZLE"
То же, что и 15PUZZLE
16) "SYZYGY"
Аналогично змейке игроку требуется "съедать" появляющиеся на экране предметы, таким образом удлиняя змейку. Змейка не может проходиьт сквозь некоторые объекты и себя.
17) "TANK"
Простейшая реализация танчиков, где игрок, управляя танком, должен сбивать движущийся объект.
18) "TETRIS"
Тетрис - игрок должен подводить падающие объекты таким образом, чтобы они заполнили всю линию, тогда она исчезает. Игра ведется до тех пор, пока эти объекты не упрутся в потолок.
19) "TICTAC"
Крестики-нолики, игрок, выбрав определенный элемент, должен расположить их на поле 3х3 так, чтобы подобные элементы заполнили линию. За один ход можно поставить один элемент. Противник - машина.
20) "UFO"
Похоже на BLITZ, только пассажир должен попасть на транспорт.
21) "VBRIX"
То же что и BRIX, только с вертикальной ориентацией
22) "VERS"
Два игрока управляют линиями, если одна из них пересечет другую - проигрывает вторая.
23) "WIPEOFF"
Похоже на BRIX, только стены стоят на близком расстоянии подобно сетке