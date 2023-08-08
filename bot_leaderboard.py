from sched import scheduler
import time
import lichess.api
import urllib.request
import orjson
import sys

def display_user_rating(username, type):
    user = lichess.api.user(username)
    return "@" + username + ": " + str(user.get('perfs', {}).get(type, {}).get('rating'))

def get_team(team, type):
    team_users = lichess.api.users_by_team(team)
    ratings = []
    for u in team_users:
        ratings.append([u['username'], u['perfs'][type]['rating'], u['perfs'][type]['prog'], u['perfs'][type]['games']])
    print(ratings)

def get_user_rating(username, type):
    user = lichess.api.user(username)
    return [username, user.get('perfs', {}).get(type, {}).get('rating')]

def get_user_rating_from_dict(username, dict, type):
    return [username, dict[type]]

def get_file_name(type):
    return os.path.join(dir, f"{type}.txt")

def get_bot_ratings_online(type, all_bots=False):
    banned_bots = [
        'caissa-ai',
        'ProteusSF',
        'ProteusSF-lite',
        'ProteusSF-Open',
        'ProteusSF-Turbo',
        'QalatBotEngine',
        'Vaxim2000',
        'MedipolUniversity',
        'MustafaYilmazBot',
        'Viet-AI',
        'RexherBot',
        'SamuraiX_v1',
        'YellowFlash_v2',
        'NikitosikVariantsbot',
        'CodingAdventureBot',
        'Nikitosikbot',
        'Anand_Bot',
        'GHDES',
        'caissa-test', 
        'Codingadventurebot',
        'RandomEngine-AI',
        'RandomEngine',
        'OkayWhyYouReadinThis',
        'HappyFarmer3000',
        'HappyFarmerChallenge',
    ]
    online_bots = urllib.request.urlopen('https://lichess.org/api/bot/online')
    user_arr = []
    num_prov = 0
    num_est = 0
    count = 0
    banned = 0
    count2 = 1
    
    for i in online_bots:
        d = orjson.loads(i)
        try:
            result = [d['username'], d['perfs'][type]['rating'], d['perfs'][type]['prog'], d['perfs'][type]['games']]
            print(count, result)
            if all_bots:
                user_arr.append(result)
            else:
                try:
                    if d['perfs'][type]['prov'] == True:
                        print('Provisional rating')
                    num_prov += 1
                except:
                    num_est += 1
                    if result[0] in banned_bots:
                        banned += 1
                    else:
                        user_arr.append(result)
        except:
            print("No " + type + " rating available")
        count += 1
    resulting_arr = sorted(user_arr, key=lambda x: x[1], reverse=True)
    if all_bots:
        dir = './all_bot_leaderboard/'
    else:
        dir = './bot_leaderboard/'
    with open(get_file_name(type, dir), 'w') as f:
                print("{0:<10} {1:<25} {2:<10} {3:<10} {4:<10}".format("Rank", "Bot", "Rating", "Prog", "Games"), file=f)
                for j in resulting_arr:
                    print("{0:<10} {1:<25} {2:<10} {3:<10} {4:<10}".format(str(count2), j[0], str(j[1]), str(j[2]), str(j[3])), file=f)
                    count2 += 1
    return "\n" + "Banned bots: " + str(banned)

while True:
    get_bot_ratings_online('bullet', all_bots=True)
    get_bot_ratings_online('bullet')
    get_bot_ratings_online('rapid', all_bots=True)
    get_bot_ratings_online('rapid')
    get_bot_ratings_online('correspondence', all_bots=True)
    get_bot_ratings_online('correspondence')
    get_bot_ratings_online('atomic', all_bots=True)
    get_bot_ratings_online('atomic')
    get_bot_ratings_online('crazyhouse', all_bots=True)
    get_bot_ratings_online('crazyhouse')
    get_bot_ratings_online('kingOfTheHill', all_bots=True)
    get_bot_ratings_online('kingOfTheHill')
    get_bot_ratings_online('threeCheck', all_bots=True)
    get_bot_ratings_online('threeCheck')
    get_bot_ratings_online('blitz', all_bots=True)
    get_bot_ratings_online('blitz')
    get_bot_ratings_online('classical', all_bots=True)
    get_bot_ratings_online('classical')
    get_bot_ratings_online('antichess', all_bots=True)
    get_bot_ratings_online('antichess')
    get_bot_ratings_online('chess960', all_bots=True)
    get_bot_ratings_online('chess960')
    get_bot_ratings_online('horde', all_bots=True)
    get_bot_ratings_online('horde')
    get_bot_ratings_online('racingKings', all_bots=True)
    get_bot_ratings_online('racingKings')
    time.sleep(300)
    time.sleep(300)

#print(get_team('leaderboard-of-bots', 'bullet'))
