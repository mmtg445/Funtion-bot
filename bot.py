
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from flask import Flask
import tools  # Importing the tools module with our functions

# Flask setup
app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram Bot is running!"

# Telegram bot functions
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Ultimate Tool Bot! Use /help for commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🔄 Reverse Text", callback_data='reverse_text')],
        [InlineKeyboardButton("➕ Add Numbers", callback_data='add')],
        [InlineKeyboardButton("➖ Subtract Numbers", callback_data='subtract')],
        [InlineKeyboardButton("✖️ Multiply Numbers", callback_data='multiply')],
        [InlineKeyboardButton("➗ Divide Numbers", callback_data='divide')],
        [InlineKeyboardButton("√ Square Root", callback_data='square_root')],
        [InlineKeyboardButton("📈 Factorial", callback_data='factorial')],
        [InlineKeyboardButton("🕒 Current Time", callback_data='current_time')],
        [InlineKeyboardButton("📅 Current Date", callback_data='current_date')],
        [InlineKeyboardButton("😂 Random Joke", callback_data='random_joke')],
        [InlineKeyboardButton("🎬 Top Movies", callback_data='top_movies')],
        [InlineKeyboardButton("🎉 New Releases", callback_data='new_releases')],
        [InlineKeyboardButton("🔜 Upcoming Movies", callback_data='upcoming_movies')],
        [InlineKeyboardButton("🍣 Anime Recommendations", callback_data='anime_recommendations')],
        [InlineKeyboardButton("📺 Anime Details", callback_data='get_anime_details')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Available Tools:", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()  # Acknowledge the button press

    # Provide instructions for each command
    if query.data == 'reverse_text':
        query.edit_message_text(text="🔄 Send me the text you want to reverse using /reverse_text <text>")
    elif query.data == 'add':
        query.edit_message_text(text="➕ Send me the numbers you want to add using /add <num1> <num2>")
    elif query.data == 'subtract':
        query.edit_message_text(text="➖ Send me the numbers you want to subtract using /subtract <num1> <num2>")
    elif query.data == 'multiply':
        query.edit_message_text(text="✖️ Send me the numbers you want to multiply using /multiply <num1> <num2>")
    elif query.data == 'divide':
        query.edit_message_text(text="➗ Send me the numbers you want to divide using /divide <num1> <num2>")
    elif query.data == 'square_root':
        query.edit_message_text(text="√ Send me the number you want the square root of using /square_root <num>")
    elif query.data == 'factorial':
        query.edit_message_text(text="📈 Send me the number you want the factorial of using /factorial <num>")
    elif query.data == 'current_time':
        query.edit_message_text(text="🕒 Use /current_time to get the current time.")
    elif query.data == 'current_date':
        query.edit_message_text(text="📅 Use /current_date to get the current date.")
    elif query.data == 'random_joke':
        query.edit_message_text(text="😂 Use /random_joke to get a random joke.")
    elif query.data == 'top_movies':
        query.edit_message_text(text="🎬 Use /top_movies to get the top movies this week.")
    elif query.data == 'new_releases':
        query.edit_message_text(text="🎉 Use /new_releases to get new movie releases.")
    elif query.data == 'upcoming_movies':
        query.edit_message_text(text="🔜 Use /upcoming_movies to get upcoming movies.")
    elif query.data == 'anime_recommendations':
        query.edit_message_text(text="🍣 Use /anime_recommendations to get anime recommendations.")
    elif query.data == 'get_anime_details':
        query.edit_message_text(text="📺 Send me the anime ID you want details about using /get_anime_details <anime_id>.")

def main():
    # Initialize Telegram bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    dispatcher = updater.dispatcher

    # Core commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Tool commands from tools.py
    dispatcher.add_handler(CommandHandler("reverse_text", tools.reverse_text))
    dispatcher.add_handler(CommandHandler("add", tools.add))
    dispatcher.add_handler(CommandHandler("subtract", tools.subtract))
    dispatcher.add_handler(CommandHandler("multiply", tools.multiply))
    dispatcher.add_handler(CommandHandler("divide", tools.divide))
    dispatcher.add_handler(CommandHandler("square_root", tools.square_root))
    dispatcher.add_handler(CommandHandler("factorial", tools.factorial))
    dispatcher.add_handler(CommandHandler("current_time", tools.current_time))
    dispatcher.add_handler(CommandHandler("current_date", tools.current_date))
    dispatcher.add_handler(CommandHandler("random_joke", tools.random_joke))
    dispatcher.add_handler(CommandHandler("top_movies", tools.get_top_week_movies))
    dispatcher.add_handler(CommandHandler("new_releases", tools.get_new_releases))
    dispatcher.add_handler(CommandHandler("upcoming_movies", tools.get_upcoming_movies))
    dispatcher.add_handler(CommandHandler("anime_recommendations", tools.get_anime_recommendations))
    dispatcher.add_handler(CommandHandler("get_anime_details", tools.get_anime_details))

    # Handle button callbacks
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # Start the bot
    updater.start_polling()

    # Run Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()
```
