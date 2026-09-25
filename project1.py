# Project 1 - Video Game Backlog Tracker

games = []

print("Welcome to the Video Game Backlog Tracker!")
while True:
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
      if len(games) == 0:
        print("No games in your backlog.")
      else:
        for game in games:
          print(game["title"], "-", game["genre"], "-", game["status"])
  elif choice == "3":
    search = input("Enter the game title:")

    found = False

    for game in games:
      if game["title"].lower() == search.lower():
          print("Game found!")
          print("Title:", game["title"])
          print("Genre:", game["genre"])
          print("Status:", game["status"])
          found = True
    if not found:
        print("Game not found.")
  elif choice == "4":
    title = input("Enter the game title: ")

    found = False

    for game in games:
      if game["title"].lower() == title.lower():
          game["status"] = "Completed"
          print(title, "has been marked as completed!")
          found = True
          break

    if not found:
        print("Game not found.")
  elif choice == "5":
    title = input("Enter the game title: ")

    found = False

    for game in games:
      if game["title"].lower() == title.lower():
          rating = input("Rate this game from 1 to 10: ")

          if rating.isdigit() and 1 <= int(rating) <= 10:
              game["rating"] = int(rating)
              print(title, "has been rated", rating, "out of 10!")
          else:
              print("Invalid rating. Enter a number from 1 to 10.")

          found = True
          break

  if not found:
      print("Game not found.")
  elif choice == "6":
    print("Show statistics selected")
  elif choice == "7":
    print("Goodbye!")
    break
    
  else:
    print("Invalid choice")
