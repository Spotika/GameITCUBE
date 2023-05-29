## Запуск игры
<h3>Требования</h3>
Для работы игры требуется установленный интерпретатор python 3.11 и установленная библиотека pygame. <br><br>
Скачать и установить python 3.11 можно с оффициального сайта https://www.python.org

Для установки библиотеки выполните команду `pip install pygame` в консоли

### Запуск через консоль

Для запуска выполните команду из директории проекта `python main.py` тем самым запустив **main.py**


## Описание игры
<h3>Суть</h3>
Игра представляет из себя окно в котором движутся платформы. а так же появляются разные объекты, при падении вниз или потере всего здоровья игра заканчивается.
<h3>Цель</h3>
Собрать как можно больше монет и получить как можно больший уровень, так же попутаться не умереть от враждебных мобов и боссов.
<h3>Управление</h3>
Движение осуществляется на стрелочки, на левую ри правую ходить, вверх прыгать, вниз спрыгивать с платформы. Персонаж имеет три способности, первая способность "сурикен" кидается на букву z по вектору движения персонажа, чем быстрее скорость персонажа тем быстрее он летит и больше его урон. Вторая способность "толчок" применяется на букву x, толкает персонажа по вектору его движения. Третяя способность применяется на c, уменьшает скорость игры и увеличивает количество получаемых монет за раз.
<h3>Механики</h3>
В игре есть несколько статистик персонажа. Первая уровень, чем выше уровень тем выше стальные показатели. Вторая здоровье и мана, их восстановление зависит от интеллекта и силы, они же зависят от уровня. Третие ловкость, зависит от уровня, чем выше ловкость тем выше скорость персонажа и количество прыжков. Прыжок, изначально у персонажа есть два прыжка, с ростом ловкости их количество увеличивается. На платформе с определённым шансом может появиться либо монета либо кабанчик либо ничего. Монету можно собрать, чем больше монет тем выше скорость игры, чем больше монет относительно уровня тем легче уровень получить и наоборот. Кабанчика можно убить с помощью первой способности, когда ты касаешься кабанчика он наносит тебе урон и толкает по вектору своего движения. Боссы, с каждым новым уровнем есть шанс что появится один из двух боссов, первый огненный вызывает метеориты которые при попадании в персонажа наносят ему существенный урон, а при попадании по платформе с некоторым шансом ломают её, второй кислотный выпускает большое количество колб с зельем который при попадании в персонажа наносят ему урон и отнимают уровень.
