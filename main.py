from art import logo, vs
from data import data
import random



# Function to format account data for display
def format_account_data(account):
    """
    Format the account data to display the name, description, and country.
    """
    account_name = account["name"]
    account_description = account['description']
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# Function to check if the user's guess is correct based on the follower count
def check_answer(user_guess, account_a_followers, account_b_followers):
    """
    Check if the user's guess is correct based on the follower count comparison.
    """
    if account_a_followers > account_b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

score = 0
print(logo)

game_active = True
account_b = random.choice(data)

while game_active:
    account_a = account_b
    account_b = random.choice(data)

    # Ensure the two accounts are different
    if account_a == account_b:
        account_b = random.choice(data)

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    # Display followers' count and account information clearly
    print(f"Followers of A: {followers_a} vs Followers of B: {followers_b}")
    print(f"Compare A: {format_account_data(account_a)}\n")
    print(vs)
    print(f"Against B: {format_account_data(account_b)}\n")

    # Improve user experience by prompting clearly for input
    user_choice = input(">> Who has more followers? Type A or B: ").strip().lower()

    # Check if the user's guess is correct
    is_correct = check_answer(user_choice, followers_a, followers_b)

    # Provide feedback to the user based on their guess
    if is_correct:
        clear()
        score += 1
        print(f"🎉 Correct! Your current score is {score}.\n")
    else:
        print(f"😢 Incorrect! You lose! Your final score is {score}.")
        game_active = False
