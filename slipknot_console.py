import csv
import re

print("This is the Slipknot song console which reads songs from a csv file")

def menu():
    print("[1] Search songs by name")
    print("[2] Search songs by year")
    print("[3] Search songs by producer")
    print("[Q] Press Q to quit")

menu()
option = input("Enter your option: ")

while option.lower() != "q":
    if option == "1":
        song_name = input("Enter song name: ")
        with open('./slipknot_songs.csv' , 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                pattern = re.compile(song_name, re.IGNORECASE)
                found = False
                for row in reader:
                    if re.search(pattern, row[0]):
                        print("Song name: " + row[0] + " | Release year: " + row[1] + " | Producer: " + row[2])
                        found = True
                if not found:
                    print("No matching songs found.")
    
    elif option == "2":
        release_year = input("Enter release year: ")
        with open('./slipknot_songs.csv' , 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                pattern = re.compile(release_year, re.IGNORECASE)
                found = False
                for row in reader:
                    if re.search(pattern, row[1]):
                        print("Song name: " + row[0] + " | Release year: " + row[1] + " | Producer: " + row[2])
                        found = True
                if not found:
                    print("No matching songs found.")


    elif option == "3":
        producer_name = input("Enter producer name: ")
        with open('./slipknot_songs.csv' , 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                pattern = re.compile(producer_name, re.IGNORECASE)
                found = False
                for row in reader:
                    if re.search(pattern, row[2]):
                        print("Song name: " + row[0] + " | Release year: " + row[1] + " | Producer: " + row[2])
                        found = True
                if not found:
                    print("No matching songs found.")

    else:
        print("Invalid option")

    print()
    menu()
    option = input("Enter your option: ")

print("Thanks for using the Slipknot songs console!")