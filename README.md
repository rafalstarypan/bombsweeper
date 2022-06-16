# Bombsweeper

## 1. Wstęp

Projekt zaliczeniowy `Bombsweeper` to implementacja gry "Saper" w języku Python.

## 2. Planowane narzędzia do wykorzystania

Narzędzia planowane do wykorzystania w projekcie to język `Python 3` w wersji `3.8.3` oraz
biblioteka `pygame` umożliwiająca budowę prostego GUI.

## 3. Działanie programu

Przed rozpoczęciem gry na ekranie startowym gracz musi wpisać swój nick oraz wybrać jeden
z trzech poziomów trudności: EASY, MEDIUM, HARD.

W trakcie gry tak jak przy grze w klasycznego Sapera celem gracza jest "rozminowanie" całej
planszy. Po kliknięciu w bombę gracz przegrywa (przy okazji ma możliwość zobaczenia lokalizacji wszystkich bomb), z kolei kliknięcie w puste pole powoduje
odsłonięcie sąsiadujących pustych pól wraz z informacją, z iloma bombami sąsiadują (w tym po
przekątnej). Gracz może oznaczać "podejrzane" pola chorągiewkami, których liczba jest
ograniczona oraz widzi aktualny czas gry.

Po zakończeniu rozgrywki graczowi pokazany jest widok podsumowujący, na którym może wybrać
powtórzenie gry lub powrót do początkowego menu.

## 4. Planowana implementacja

Planowane jest zastosowanie wzorca MVC. Za warstwę widoku będą odpowiadały klasy
`WelcomeView`, `MainView`, `SummaryView`, `ViewManager`.

Klasa `MainView`, która jest odpowiedzialna za właściwą część gry będzie miała dostęp
do kontrolera `GameController`. Kontroler ma dostęp do klas `BombFieldGrid`, `FlagManager`,
`TimeManager`, `GameRules` oraz pozostałych klas odpowiedzialnych za warstwę logiczną.

## 5. Instalacja.

Aby zainstalować projekt należy wejść w terminalu do katalogu `bombsweeper\`, aktywować odpowiednią wersję Pythona (od 3.8.3 do 3.8.13) i użyć następujących komend:

`python setup.py build`
`sudo python setup.py install`

Aby uruchomić zainstalowany program należy użyć komendy:
`python src/main.py`

## 6. Dokumentacja.

Dokumentacja została wygenerowana za pomocą biblioteki pydoctor przy użyciu komendy:

`pydoctor --project-name=Bombsweeper --project-version=1.0.0 --make-html --html-output=docs src`

