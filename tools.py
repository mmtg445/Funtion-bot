
import requests
from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime, timedelta
import random
import base64
import string

# --- Text Tools ---
def reverse_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    reversed_text = text[::-1]
    update.message.reply_text(f"🔄 Reversed: {reversed_text}")

def uppercase_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    update.message.reply_text(f"🔤 Uppercase: {text.upper()}")

def lowercase_text(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    update.message.reply_text(f"🔡 Lowercase: {text.lower()}")

def count_words(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    word_count = len(text.split())
    update.message.reply_text(f"📏 Word Count: {word_count}")

def count_characters(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    char_count = len(text)
    update.message.reply_text(f"🔢 Character Count: {char_count}")

def word_synonyms(update: Update, context: CallbackContext) -> None:
    word = ' '.join(context.args)
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()
    if 'title' in data and data['title'] == 'No Definitions Found':
        update.message.reply_text("❌ No synonyms found.")
        return
    synonyms = data[0]['meanings'][0]['synonyms']
    update.message.reply_text(f"🔍 Synonyms for {word}: {', '.join(synonyms)}")

def text_length(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    length = len(text)
    update.message.reply_text(f"📏 Text Length: {length}")

# --- Calculation Tools ---
def add(update: Update, context: CallbackContext) -> None:
    try:
        num1 = float(context.args[0])
        num2 = float(context.args[1])
        result = num1 + num2
        update.message.reply_text(f"➕ Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide two numbers.")

def subtract(update: Update, context: CallbackContext) -> None:
    try:
        num1 = float(context.args[0])
        num2 = float(context.args[1])
        result = num1 - num2
        update.message.reply_text(f"➖ Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide two numbers.")

def multiply(update: Update, context: CallbackContext) -> None:
    try:
        num1 = float(context.args[0])
        num2 = float(context.args[1])
        result = num1 * num2
        update.message.reply_text(f"✖️ Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide two numbers.")

def divide(update: Update, context: CallbackContext) -> None:
    try:
        num1 = float(context.args[0])
        num2 = float(context.args[1])
        if num2 == 0:
            update.message.reply_text("🚫 Cannot divide by zero.")
            return
        result = num1 / num2
        update.message.reply_text(f"➗ Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide two numbers.")

def percentage(update: Update, context: CallbackContext) -> None:
    try:
        num = float(context.args[0])
        percent = float(context.args[1])
        result = (num * percent) / 100
        update.message.reply_text(f"📊 Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide a number and a percentage.")

def square_root(update: Update, context: CallbackContext) -> None:
    try:
        num = float(context.args[0])
        result = num ** 0.5
        update.message.reply_text(f"√ Result: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide a number.")

def factorial(update: Update, context: CallbackContext) -> None:
    try:
        num = int(context.args[0])
        result = 1
        for i in range(1, num + 1):
            result *= i
        update.message.reply_text(f"📈 Factorial of {num}: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide a positive integer.")

def power(update: Update, context: CallbackContext) -> None:
    try:
        base = float(context.args[0])
        exponent = float(context.args[1])
        result = base ** exponent
        update.message.reply_text(f"📈 {base} raised to the power of {exponent} is {result}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide a base and an exponent.")

# --- Date and Time Tools ---
def current_time(update: Update, context: CallbackContext) -> None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f"🕒 Current Time: {now}")

def add_days_to_date(update: Update, context: CallbackContext) -> None:
    try:
        date = datetime.strptime(context.args[0], '%Y-%m-%d')
        days = int(context.args[1])
        new_date = date + timedelta(days=days)
        update.message.reply_text(f"📅 New Date: {new_date.strftime('%Y-%m-%d')}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Provide a date in YYYY-MM-DD format and number of days.")

def days_until_event(update: Update, context: CallbackContext) -> None:
    try:
        event_date = datetime.strptime(context.args[0], '%Y-%m-%d')
        today = datetime.now()
        diff = (event_date - today).days
        update.message.reply_text(f"⏳ Days until event: {diff} days")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Provide a date in YYYY-MM-DD format.")

def get_day_of_week(update: Update, context: CallbackContext) -> None:
    try:
        date = datetime.strptime(context.args[0], '%Y-%m-%d')
        day_of_week = date.strftime('%A')
        update.message.reply_text(f"📅 Day of the Week: {day_of_week}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Provide a date in YYYY-MM-DD format.")

def time_difference(update: Update, context: CallbackContext) -> None:
    try:
        time1 = datetime.strptime(context.args[0], '%H:%M')
        time2 = datetime.strptime(context.args[1], '%H:%M')
        diff = abs((time2 - time1).seconds // 60)
        update.message.reply_text(f"⏰ Time Difference: {diff} minutes")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Provide two times in HH:MM format.")

def current_date(update: Update, context: CallbackContext) -> None:
    now = datetime.now().strftime('%Y-%m-%d')
    update.message.reply_text(f"📅 Current Date: {now}")

# --- Fun Tools ---
def random_joke(update: Update, context: CallbackContext) -> None:
    jokes = [
        "😂 Why don't scientists trust atoms? Because they make up everything!",
        "📚 Why did the math book look sad? Because it had too many problems.",
        "😄 Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    update.message.reply_text(random.choice(jokes))

def random_quote(update: Update, context: CallbackContext) -> None:
    quotes = [
        "🌟 The best way to predict the future is to invent it.",
        "🍀 Life is what happens when you're busy making other plans.",
        "☀️ Keep your face always toward the sunshine—and shadows will fall behind you."
    ]
    update.message.reply_text(random.choice(quotes))

def riddles(update: Update, context: CallbackContext) -> None:
    riddles = [
        {"question": "🤔 What has keys but can't open locks?", "answer": "A piano"},
        {"question": "🗣️ I speak without a mouth and hear without ears. What am I?", "answer": "An echo"}
    ]
    riddle = random.choice(riddles)
    update.message.reply_text(f"🧩 Riddle: {riddle['question']} (Type /answer to get the answer)")

def would_you_rather(update: Update, context: CallbackContext) -> None:
    questions = [
        "🤔 Would you rather have the ability to fly or be invisible?",
        "🦁 Would you rather fight one horse-sized duck or a hundred duck-sized horses?"
    ]
    update.message.reply_text(random.choice(questions))

def fun_fact(update: Update, context: CallbackContext) -> None:
    facts = [
        "🤯 Honey never spoils.",
        "🌍 A day on Venus is longer than a year on Venus."
    ]
    update.message.reply_text(random.choice(facts))

def trivia_quiz(update: Update, context: CallbackContext) -> None:
    questions = [
        {"question": "What is the capital of France?", "options": ["1. Paris", "2. London", "3. Rome", "4. Berlin"], "answer": "1"},
        {"question": "What is the largest planet in our solar system?", "options": ["1. Earth", "2. Jupiter", "3. Mars", "4. Saturn"], "answer": "2"}
    ]
    question = random.choice(questions)
    options = "\n".join(question["options"])
    update.message.reply_text(f"🔍 Quiz: {question['question']}\n{options}\nType /answer <number> to answer.")

# --- Utility Tools ---
def currency_converter(update: Update, context: CallbackContext) -> None:
    # Placeholder for currency conversion functionality
    update.message.reply_text("💱 Currency Converter: (Functionality not implemented yet)")

def news_headlines(update: Update, context: CallbackContext) -> None:
    # Placeholder for news fetching functionality
    update.message.reply_text("📰 Latest News: (Functionality not implemented yet)")

def random_name_generator(update: Update, context: CallbackContext) -> None:
    names = ["Alice", "Bob", "Charlie", "Diana"]
    update.message.reply_text(f"🎉 Random Name: {random.choice(names)}")

def random_color(update: Update, context: CallbackContext) -> None:
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    update.message.reply_text(f"🎨 Random Color: {color}")

def tips(update: Update, context: CallbackContext) -> None:
    tips = [
        "💡 Keep a positive mindset!",
        "📚 Read at least one book a month."
    ]
    update.message.reply_text(f"💬 Tip: {random.choice(tips)}")

def random_password_generator(update: Update, context: CallbackContext) -> None:
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    update.message.reply_text(f"🔑 Random Password: {password}")

# --- Developer Tools ---
def base64_encode(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    encoded_text = base64.b64encode(text.encode()).decode()
    update.message.reply_text(f"🔐 Encoded: {encoded_text}")

def base64_decode(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    try:
        decoded_text = base64.b64decode(text).decode()
        update.message.reply_text(f"🔓 Decoded: {decoded_text}")
    except Exception:
        update.message.reply_text("⚠️ Error in decoding. Please provide valid Base64 text.")

def json_formatter(update: Update, context: CallbackContext) -> None:
    # Placeholder for JSON formatting functionality
    update.message.reply_text("📄 JSON Formatter: (Functionality not implemented yet)")

def regex_tester(update: Update, context: CallbackContext) -> None:
    # Placeholder for regex testing functionality
    update.message.reply_text("🔍 Regex Tester: (Functionality not implemented yet)")

def api_status_checker(update: Update, context: CallbackContext) -> None:
    # Placeholder for API status checking functionality
    update.message.reply_text("🔗 API Status Checker: (Functionality not implemented yet)")

# --- Educational Tools ---
def dictionary_lookup(update: Update, context: CallbackContext) -> None:
    word = ' '.join(context.args)
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()
    if 'title' in data and data['title'] == 'No Definitions Found':
        update.message.reply_text("❌ Word not found.")
        return
    meaning = data[0]['meanings'][0]['definitions'][0]['definition']
    update.message.reply_text(f"📖 {word.capitalize()}: {meaning}")

def math_solver(update: Update, context: CallbackContext) -> None:
    # Placeholder for a simple math solver functionality
    update.message.reply_text("🧮 Math Solver: (Functionality not implemented yet)")

def science_facts(update: Update, context: CallbackContext) -> None:
    facts = [
        "🌌 The Milky Way galaxy is about 100,000 light-years in diameter.",
        "🔬 The human body has about 37.2 trillion cells."
    ]
    update.message.reply_text(random.choice(facts))

def history_facts(update: Update, context: CallbackContext) -> None:
    facts = [
        "🗿 The Great Pyramid of Giza was built around 2580–2560 BC.",
        "📜 The Declaration of Independence was adopted on July 4, 1776."
    ]
    update.message.reply_text(random.choice(facts))

# --- Social Media Tools ---
def instagram_profile_info(update: Update, context: CallbackContext) -> None:
    username = ''.join(context.args)
    response = requests.get(f"https://www.instagram.com/{username}/?__a=1")
    data = response.json()
    if 'graphql' not in data:
        update.message.reply_text("❌ Profile not found.")
        return
    info = data['graphql']['user']
    message = f"📸 Name: {info['full_name']}\n📝 Bio: {info['biography']}\n👥 Followers: {info['edge_followed_by']['count']}"
    update.message.reply_text(message)

def twitter_profile_info(update: Update, context: CallbackContext) -> None:
    username = ''.join(context.args)
    update.message.reply_text(f"🐦 Twitter Profile Info: (Functionality not implemented yet)")

def youtube_channel_info(update: Update, context: CallbackContext) -> None:
    channel_id = ''.join(context.args)
    update.message.reply_text(f"📹 YouTube Channel Info: (Functionality not implemented yet)")

def facebook_profile_info(update: Update, context: CallbackContext) -> None:
    username = ''.join(context.args)
    update.message.reply_text(f"📘 Facebook Profile Info: (Functionality not implemented yet)")

# --- Movie and Anime Tools ---
def get_top_week_movies(update: Update, context: CallbackContext) -> None:
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=YOUR_API_KEY&language=en-US&page=1")
    data = response.json()
    movies = data['results'][:5]  # Get top 5
    message = "🎬 Top Movies This Week:\n"
    for movie in movies:
        message += f"🌟 {movie['title']} (Rating: {movie['vote_average']})\n"
    update.message.reply_text(message)

def get_new_releases(update: Update, context: CallbackContext) -> None:
    response = requests.get("https://api.themoviedb.org/3/movie/latest?api_key=YOUR_API_KEY&language=en-US")
    data = response.json()
    message = f"🎉 New Release: {data['title']} (Rating: {data['vote_average']})"
    update.message.reply_text(message)

def get_upcoming_movies(update: Update, context: CallbackContext) -> None:
    response = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=YOUR_API_KEY&language=en-US&page=1")
    data = response.json()
    movies = data['results'][:5]  # Get upcoming movies
    message = "🔜 Upcoming Movies:\n"
    for movie in movies:
        message += f"🌟 {movie['title']} (Release Date: {movie['release_date']})\n"
    update.message.reply_text(message)

def get_anime_recommendations(update: Update, context: CallbackContext) -> None:
    response = requests.get("https://api.jikan.moe/v3/top/anime/1/upcoming")
    data = response.json()
    animes = data['top'][:5]  # Get top 5 anime
    message = "🍣 Recommended Anime:\n"
    for anime in animes:
        message += f"🌟 {anime['title']} (Score: {anime['score']})\n"
    update.message.reply_text(message)

def get_anime_details(update: Update, context: CallbackContext) -> None:
    anime_id = context.args[0] if context.args else 1  # Default to 1 if no ID provided
    response = requests.get(f"https://api.jikan.moe/v3/anime/{anime_id}")
    data = response.json()
    message = f"📺 {data['title']}\n🔍 Synopsis: {data['synopsis']}\n🌟 Score: {data['score']}\n🗓️ Aired: {data['aired']['string']}"
    update.message.reply_text(message)

# --- Health and Fitness Tools ---
def calorie_tracker(update: Update, context: CallbackContext) -> None:
    # Placeholder for calorie tracker functionality
    update.message.reply_text("🍏 Calorie Tracker: (Functionality not implemented yet)")

def workout_suggestions(update: Update, context: CallbackContext) -> None:
    workouts = [
        "🏋️‍♂️ Push-ups",
        "🧘‍♀️ Yoga",
        "🏃‍♀️ Running"
    ]
    update.message.reply_text(f"💪 Workout Suggestion: {random.choice(workouts)}")

def daily_water_intake(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("💧 Daily Water Intake Reminder: Drink at least 8 glasses of water!")

def bmi_calculator(update: Update, context: CallbackContext) -> None:
    try:
        weight = float(context.args[0])
        height = float(context.args[1]) / 100  # height in meters
        bmi = weight / (height ** 2)
        update.message.reply_text(f"⚖️ Your BMI: {bmi:.2f}")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please provide weight in kg and height in cm.")

# --- Creative Tools ---
def story_generator(update: Update, context: CallbackContext) -> None:
    # Placeholder for story generator functionality
    update.message.reply_text("📖 Story Generator: (Functionality not implemented yet)")

def poem_generator(update: Update, context: CallbackContext) -> None:
    # Placeholder for poem generator functionality
    update.message.reply_text("📝 Poem Generator: (Functionality not implemented yet)")

def character_name_generator(update: Update, context: CallbackContext) -> None:
    names = ["Frodo", "Gandalf", "Aragorn", "Hermione"]
    update.message.reply_text(f"🌟 Character Name: {random.choice(names)}")

def recipe_suggestion(update: Update, context: CallbackContext) -> None:
    recipes = [
        "🍝 Spaghetti Bolognese",
        "🍣 Sushi",
        "🥗 Caesar Salad"
    ]
    update.message.reply_text(f"🍽️ Recipe Suggestion: {random.choice(recipes)}")

# --- Miscellaneous Tools ---
def random_facts(update: Update, context: CallbackContext) -> None:
    facts = [
        "🤯 Honey never spoils.",
        "🌍 A day on Venus is longer than a year on Venus."
    ]
    update.message.reply_text(random.choice(facts))

def horoscope(update: Update, context: CallbackContext) -> None:
    # Placeholder for horoscope functionality
    update.message.reply_text("🔮 Horoscope: (Functionality not implemented yet)")

def personal_diary(update: Update, context: CallbackContext) -> None:
    # Placeholder for personal diary functionality
    update.message.reply_text("📓 Personal Diary: (Functionality not implemented yet)")

# --- Seasonal Tools ---
def holiday_countdown(update: Update, context: CallbackContext) -> None:
    holidays = {
        "New Year": "2024-01-01",
        "Christmas": "2023-12-25"
    }
    now = datetime.now()
    messages = []
    for holiday, date in holidays.items():
        holiday_date = datetime.strptime(date, "%Y-%m-%d")
        days_until = (holiday_date - now).days
        messages.append(f"{holiday}: {days_until} days left!")
    update.message.reply_text("\n".join(messages))

# --- Community Tools ---
def local_events_info(update: Update, context: CallbackContext) -> None:
    # Placeholder for local events functionality
    update.message.reply_text("📍 Local Events: (Functionality not implemented yet)")

def volunteer_opportunities(update: Update, context: CallbackContext) -> None:
    # Placeholder for volunteer opportunities functionality
    update.message.reply_text("🤝 Volunteer Opportunities: (Functionality not implemented yet)")

def community_tips(update: Update, context: CallbackContext) -> None:
    tips = [
        "🌱 Start a community garden!",
        "📚 Organize a book exchange."
    ]
    update.message.reply_text(f"💬 Community Tip: {random.choice(tips)}")
