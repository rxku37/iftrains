print("1.IT - 18lat, 30.20zł")
print("2.Bat-Man - 16lat, 25.60zł")
print("3.Iron-Man - 16lat, 18.90zł")
print("Podaj kolejność filmu, który Cię interesuje: ")
choose_film = int(input(" "))

option_1 = 1
option_2 = 2
option_3 = 3

check_wiek = int(input("Ile masz lat? "))
check_kasa = int(input("Ile masz pieniędzy? "))

required_wiek = 0
required_kasa = 0

if choose_film == option_1:
    required_wiek = 18
    required_kasa = 30.20
    if check_wiek >= required_wiek and check_kasa >= required_kasa:
        print("Udało ci się kupić bilet na ten film!")
    elif check_wiek >= required_wiek and check_kasa < required_kasa:
        print("Brakuje Ci pieniędzy aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa >= required_kasa:
        print("Masz za mało lat aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa < required_kasa:
        print("Masz za mało lat i pieniędzy aby kupić bilet na ten film...")

if choose_film == option_2:
    required_wiek = 16
    required_kasa = 25.60
    if check_wiek >= required_wiek and check_kasa >= required_kasa:
        print("Udało ci się kupić bilet na ten film!")
    elif check_wiek >= required_wiek and check_kasa < required_kasa:
        print("Brakuje Ci pieniędzy aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa >= required_kasa:
        print("Masz za mało lat aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa < required_kasa:
        print("Masz za mało lat i pieniędzy aby kupić bilet na ten film...")

if choose_film == option_3:
    required_wiek = 16
    required_kasa = 18.90
    if check_wiek >= required_wiek and check_kasa >= required_kasa:
        print("Udało ci się kupić bilet na ten film!")
    elif check_wiek >= required_wiek and check_kasa < required_kasa:
        print("Brakuje Ci pieniędzy aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa >= required_kasa:
        print("Masz za mało lat aby kupić bilet na ten film...")
    elif check_wiek < required_wiek and check_kasa < required_kasa:
        print("Masz za mało lat i pieniędzy aby kupić bilet na ten film...")
