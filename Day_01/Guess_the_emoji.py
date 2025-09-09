# Emoji Guessing Game 🎮
import random

emojis = ['😀', '🐶', '🍕', '🚗', '🏀', '🎲', '🌟', '🎵', '🍎', '🐱']
emoji_names = {
	'😀': 'smile',
	'🐶': 'dog',
	'🍕': 'pizza',
	'🚗': 'car',
	'🏀': 'basketball',
	'🎲': 'dice',
	'🌟': 'star',
	'🎵': 'music',
	'🍎': 'apple',
	'🐱': 'cat'
}

print("Welcome to the Emoji Guessing Game! 🎮")
print("Guess the name of the emoji. Type 'exit' to quit.")
score = 0
rounds = 5

for i in range(rounds):
	emoji = random.choice(emojis)
	print(f"Round {i+1}/{rounds}")
	print(f"Emoji: {emoji}")
	guess = input("Your guess: ").strip().lower()
	if guess == 'exit':
		print("Game exited early. 👋")
		break
	if guess == emoji_names[emoji]:
		print("Correct! 🎉")
		score += 1
	else:
		print(f"Wrong! 😢 The answer was '{emoji_names[emoji]}'.")
	print()

if score == rounds:
	print(f"Amazing! You got all {rounds} right! 🏆")
elif score >= 3:
	print(f"Great job! You scored {score}/{rounds}! 👍")
else:
	print(f"You scored {score}/{rounds}. Better luck next time! 💪")
