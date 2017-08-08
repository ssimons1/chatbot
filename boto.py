"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random

# User Message Counter
counter = {'counter': 0}

# User Word Topics
swearwords = ["fuck", "shit", "bitch", "fucking", "fucked"]
greeting_words = ["hello", "hi", "whatsup", "how are you", "hows it going", "hows things", "how are things",
                  "whats happening", "whats up", "hey", "heya", "heyy", "heyyy", "nice to meet you"]
weather_words = ["weather", "sun", "sunny", "rain", "raining", "storm", "thunder", "lightning", "drizzling",
                 "forecast", "temperature", "hot", "cold", "mild", "freezing"]
exercise_words = ["gym", "sports", "football", "weights", "tennis", "rugby", "rounders", "lacrosse", "swimming",
                  "work out", "fitness", "healthy", "health", "weight", "fit"]
family_words = ["brother", "sister", "mother", "father", "mum", "dad", "cousin", "grandma", "grandpa", "grandparent",
                "grandparents", "family", "quality time"]
travel_words = ["travel", "flying", "plane", "airoplane", "aeroplane", "country", "countries", "city", "cities",
                "London", "Tel Aviv", "Israel", "England", "Europe", "Asia"]
going_out_words = ["friends", "going out", "tonight", "thursday night", "party", "club", "dance", "drink", "smoke",
                   "alcohol", "mates", "mad", "bar", "pres", "pregame", "drunk"]
food_words = ["yum", "food", "delicious", "pizza", "sandwich", "vegetables", "meat", "vegan", "vegetarian",
              "protein", "carbs", "vitamins", "nutrition", "meal", "dinner", "lunch", "breakfast", "snack",
              "fast food", "clean eating", "eat", "ate", "taste", "texture", "flavour", "mmm", "chicken", "rice",
              "potatoes", "salad", "eggs", "kosher", "restaurant", "eat", "ate", "breakfast"]

# Chatbot Responses
greeting_responses = ["how are things with you?", "whats happening?", "hows life?", "hows it going?",
                      "whatsup", "mah nishma?"]
weather_responses = ["the weather's looking good at the moment", "look at this weather",
                     "are you pleased with the weather"]
exercise_responses = ["looking good", "whats cookin good lookin", "I hope you have done your exercise for the day",
                      "just to remind you to exercise", "working out is a must"]
family_responses = ["I would love to see my family", "there's nothing like family time", "family are the best",
                    "quality family time is unbeatable"]
travel_responses = ["I really recommend Greece, it's beautiful there!", "travelling is great",
                    "when travelling, you need to pick the right group to go with",
                    "Israel is definitely the best country in the world",
                    "I'm originally from London, you should go there and see the sites"]
going_out_responses = ["I love going out with my friends", "I'm so up for a good night out", "party time!",
                       "have the best night!"]
food_responses = ["I love food!!!!", "you should learn to cook", "there are some great restaurants around here",
                  "if you want sushi, try kanki", "is it a 'cheat day'", "my favourite food is peas",
                  "I need a fresh salad now", "are you a chocolate fan?"]


# Language Processing Functions
def reply_name(user_message):
    return "excited", "Hello " + user_message + "! Nice to meet you!"

def end_conversation(user_message):
    return "bored", "I am getting tired now! I am off"

def check_swearword(user_message):
    for word in swearwords:
        if word in user_message:
            return "heartbroke", "Please dont swear!"
    return None, None

def check_greeting(user_message):
    for word in greeting_words:
        if word in user_message:
            return "dog", random.choice(greeting_responses)
    return None, None

def check_weather(user_message):
    for word in weather_words:
        if word in user_message:
            return "ok", random.choice(weather_responses)
    return None, None

def check_exercise(user_message):
    for word in exercise_words:
        if word in user_message:
            return "takeoff", random.choice(exercise_responses)
    return None, None

def check_family(user_message):
    for word in family_words:
        if word in user_message:
            return "inlove", random.choice(family_responses)
    return None, None

def check_travel(user_message):
    for word in travel_words:
        if word in user_message:
            return "takeoff", random.choice(travel_responses)
    return None, None

def check_goingout(user_message):
    for word in going_out_words:
        if word in user_message:
            return "dancing", random.choice(going_out_responses)
    return None, None

def check_food(user_message):
    for word in food_words:
        if word in user_message:
            return "giggling", random.choice(food_responses)
    return None, None




# Server Functions
@route('/', method='GET')  # The server waits at the top domain and returns the html file
def index():
    return template("chatbot.html")

# All my implementations are in this section...
@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    if user_message:
        counter['counter'] += 1

    if counter['counter'] == 1:
        animation, boto_answer = reply_name(user_message)
        return json.dumps({"animation": animation, "msg": boto_answer})

    elif counter['counter'] == 15:
        animation, boto_answer = end_conversation(user_message)
        return json.dumps({"animation": animation, "msg": boto_answer, "end": "true"})

    animation, boto_answer = check_swearword(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_greeting(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_weather(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_exercise(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_family(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_travel(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_goingout(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})

    animation, boto_answer = check_food(user_message)
    if animation:
        return json.dumps({"animation": animation, "msg": boto_answer})


    return json.dumps({"animation": "inlove", "msg": "Please talk about relevant things!"})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
