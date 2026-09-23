# Project 1 - Video Game Backlog Tracker

games = []

print("Welcome to the Video Game Backlog Tracker!")
print("\nMenu")
print("1. Add a game")
print("2. View games")
print("3. Search for a game")
print("4. Mark a game as completed")
print("5. Rate a game")
print("6. Show statistics")
print("7. Quit")

choice = input("Enter your choice: ")
if choice == "1":
  title = input("Enter the game title: ")
  genre = input("Enter the game genre: ")
  status = input("Enter the game status: ")
  
  game = {
    "title": title,
    "genre": genre,
    "status": status
  }
  games.append(game)

  print(title, "was added to your backlog!")
elif choice == "2":
  print("View games selected")
elif choice == "3":
  print("Search for a game selected")
elif choice == "4":
  print("Mark a game as completed selected")
elif choice == "5":
  print("Rate a game selected")
elif choice == "6":
  print("Show statistics selected")
elif choice == "7":
  print("Goodbye!")
else:
  print("Invalid choice")
