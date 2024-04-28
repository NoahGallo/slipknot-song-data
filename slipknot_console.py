import csv
import re

def menu():
    print("[1] Search songs by name")
    print("[2] Search songs by year")
    print("[3] Search songs by producer")
    print("[Q] Press Q to quit")

def search_songs(criteria, search_term):
    with open('./slipknot_songs.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)  # Skip header
        found = False
        for row in reader:
            if re.search(search_term, row[criteria], re.IGNORECASE):
                print("Song name: " + row[0] + " | Release year: " + row[1] + " | Producer: " + row[2])
                found = True
        if not found:
            print("No matching songs found.")

print("This is the Slipknot song console which reads songs from a csv file")

while True:
    menu()
    option = input("Enter your option: ").lower()

    if option == "q":
        break

    if option == "1":
        song_name = input("Enter song name: ")
        search_songs(0, song_name)

    elif option == "2":
        release_year = input("Enter release year: ")
        search_songs(1, release_year)

    elif option == "3":
        producer_name = input("Enter producer name: ")
        search_songs(2, producer_name)

    else:
        print("Invalid option")

print("Thanks for using the Slipknot songs console!")
