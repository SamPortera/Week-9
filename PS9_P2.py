def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0  # Avoid division by zero
    return hits / at_bats

player_count = 0

print("Enter player details :")

while True:
    try:
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))

        batting_avg = compute_batting_average(hits, at_bats)
        player_count += 1

        print(f"\nPlayer: {last_name}")
        print(f"Batting Average: {batting_avg:.3f}\n")
    except EOFError:
        break  # Stop loop when Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) is pressed
    except ValueError:
        print("Invalid input. Please enter valid numbers for hits and at-bats.")

print(f"\nTotal number of players entered: {player_count}")
