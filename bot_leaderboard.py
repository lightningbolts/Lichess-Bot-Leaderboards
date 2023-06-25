import lichess.api
import urllib.request
import orjson
import sys

def display_user_rating(username, type):
    user = lichess.api.user(username)
    return "@" + username + ": " + str(user.get('perfs', {}).get(type, {}).get('rating'))

def get_user_rating(username, type):
    user = lichess.api.user(username)
    return [username, user.get('perfs', {}).get(type, {}).get('rating')]

def get_bot_ratings_online(type):
    banned_bots = [
        'caissa-ai',
        'GHDES',
        'ProteusSF',
        'ProteusSF-lite',
        'ProteusSF-Open',
        'ProteusSF-Turbo',
        'QalatBotEngine',
        'SumuraiX_v1',
        'Vaxim2000',
        'MedipolUniversity',
        'MustafaYilmazBot'
    ]
    online_bots = urllib.request.urlopen('https://lichess.org/api/bot/online')
    user_arr = []
    count = 0
    banned = 0
    count2 = 1
    
    for i in online_bots:
        d = orjson.loads(i)
        result = get_user_rating(d['username'], type)
        print(count)
        if result[0] in banned_bots:
            banned += 1
        else:
            user_arr.append(result)
        count += 1
    resulting_arr = sorted(user_arr, key=lambda x: x[1], reverse=True)
    match type:
        case 'bullet':
            with open('bot_leaderboard_bullet.txt', 'w') as f:
                for j in resulting_arr:
                    print(str(count2) + ". " + "@" + j[0] + ": " + str(j[1]), file=f)
                    count2 += 1
        case 'blitz':
            with open('bot_leaderboard_blitz.txt', 'w') as f:
                for j in resulting_arr:
                    print(str(count2) + ". " + "@" + j[0] + ": " + str(j[1]), file=f)
                    count2 += 1
        case 'rapid':
            with open('bot_leaderboard_rapid.txt', 'w') as f:
                for j in resulting_arr:
                    print(str(count2) + ". " + "@" + j[0] + ": " + str(j[1]), file=f)
                    count2 += 1
        case 'classical':
            with open('bot_leaderboard_classical.txt', 'w') as f:
                for j in resulting_arr:
                    print(str(count2) + ". " + "@" + j[0] + ": " + str(j[1]), file=f)
                    count2 += 1

    return "\n" + "Banned bots: " + str(banned)

display_user_rating('TheMatrix2029', 'bullet')
#get_bot_ratings_online('bullet')
get_bot_ratings_online('blitz')
get_bot_ratings_online('rapid')
get_bot_ratings_online('classical')
# with open('bot_leaderboard_bullet.txt', 'w') as f:
#     print(get_bot_ratings_online('bullet'), file=f)
# with open('bot_leaderboard_blitz.txt', 'w') as f:
#     print(get_bot_ratings_online('blitz'), file=f)
# with open('bot_leaderboard_rapid.txt', 'w') as f:
#     print(get_bot_ratings_online('rapid'), file=f)
# with open('bot_leaderboard_classical.txt', 'w') as f:
#     print(get_bot_ratings_online('classical'), file=f)