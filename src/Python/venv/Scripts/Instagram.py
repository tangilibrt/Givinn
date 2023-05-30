import json
from datetime import datetime, timedelta
import instaloader
import re
import pickle
import locale
import os
import requests

L = instaloader.Instaloader(dirname_pattern='pfps')
L.load_session_from_file('tangilibrt')


# Load cookies from cookies.json file
with open('cookies.json') as f:
    cookies = json.load(f)

for cookie_data in cookies.values():
    L.context._session.cookies.update(cookie_data)


def get_profile_details(username):
    try:
        # Code that is causing the LoginRequiredException
        profile = instaloader.Profile.from_username(L.context, username)
        download_profile_pic(username)
    except instaloader.exceptions.LoginRequiredException:
        # Handle the error here
        print(f"Login required for profile {username}. Skipping.")
        return None

    profile_details = {
        'username': profile.username,
        'followers': profile.followers,
        'followees': profile.followees,
        'biography': profile.biography,
        'external_url': profile.external_url,
        'is_verified': profile.is_verified,
        'profile_pic_url': profile.profile_pic_url,
        'date_first_post': next(profile.get_posts()).date,
        'likes_first_post': next(profile.get_posts()).likes,
        'comments_first_post': next(profile.get_posts()).comments,
        'is_business_account': profile.is_business_account,

    }
    return profile_details


def download_profile_pic(username):
    dirname = '../../../../public/assets'
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except instaloader.exceptions.LoginRequiredException:
        print(f"Login required for profile {username}. Skipping.")
        return None

    profile_pic_url = profile.profile_pic_url
    try:
        L.download_pic(f"{username}_profile_pic", profile_pic_url, datetime.now())
        print(f"Profile pic downloaded for {username} at the place {username}_profile_pic.jpg")
    except:
        print("Error while downloading profile pic")

        return None

def get_all_posts():

    L.context.login('tangilibrt', 'wolacacasselescouilles94')
    array = []
    for post in L.get_hashtag_posts('jeuconcours'):
        if get_profile_details(post.owner_username) is None:
            continue
        post_info = {
            'caption': post.caption,
            'username': post.owner_username,
            'date': post.date,
            'likes': post.likes,
            'comments': post.comments,
            'profile_details': get_profile_details(post.owner_username),
            'end_date': get_end_date(post.caption),
            'confidence': "",
            'intConfidence': 0,
            'url': f'https://www.instagram.com/p/{post.shortcode}'


        }

        array.append(post_info)
        if len(array) == 5:
            break
    print(array)
    return array


# graph_url = 'https://graph.facebook.com/v16.0/'
# access_token="EAALa1viDUegBAOEofxFFRoHDQgrb5Qy8gFxYT54JckEsPgM97kSH0dqGvST2SAXOZB9jT0Lm3eXAxMMInQkpK79MHnNzxeVJBBZAqn0OWoUcGIxkHgfYTY0tk8bAQ58UZCZCH9NXSYEHQTRse14TgVIyqYkdlRZC5YWGSfNeAfnKdnRtNEe9bGMJWdm9kZBklwTlyByDixGwZDZD"

# ----------------------------------------------------------------------------------------------------------------------#
### DB connection ###
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
### PART 1 : IMPORT THE POSTS ###
# ----------------------------------------------------------------------------------------------------------------------#

# def get_hashtag_id(hashtag = '',instagram_account_id = '',access_token = ''):
#     url = graph_url + 'ig_hashtag_search'
#     params = {
#         'user_id': instagram_account_id,
#         'q': hashtag,
#         'access_token': access_token
#     }
#     response = requests.get(url, params=params)
#     response = response.json()
#     print(response)
#     hashtag_id = response['data'][0]['id']
#
#     return hashtag_id

# def get_recent_media(hashtag_id='',access_token = '',instagram_account_id = '', after = '25'):
#     url = graph_url + hashtag_id + '/recent_media'
#     param = {
#         'access_token': access_token,
#         'user_id': instagram_account_id,
#         'fields': 'caption,like_count,permalink',
#         'after': after,
#         'limit': 2
#     }
#     response = requests.get(url, params=param)
#     response = response.json()
#     print(response)
#     print('----------------------------------------------------------------------------------------------------------------------')
#     data = response['data']
#     paging = response['paging']
#     for i in range(param['limit']):
#         next_url = paging['next']
#         next_response = requests.get(next_url)
#         next_response = next_response.json()
#         data += next_response['data']
#         paging = next_response['paging']
#     print(data)
#
#     print(response)
#
#     return data


# def get_post_info(post_id='CsjLx66KwZo'):
#     #returns a json type dict with the following keys : id, media_type, media_url, permalink
#     # we will use this result to find all the infos on the post and to apply the different functions before adding it to the db
#     url = f'https://graph.facebook.com/{post_id}?fields=id,media_type,media_url,permalink&access_token={access_token}'
#     response = requests.get(url)
#     media_data = response.json()
#
#     print(media_data)

# ----------------------------------------------------------------------------------------------------------------------#
### PART 2 : VERIFICATION ###
# ----------------------------------------------------------------------------------------------------------------------#

test ="Vous n’avez toujours pas une blouse de chez @ma_petite_etincelle et vos espadrilles @escadrilleparis pour commencer la saison ? 😎⁠@ma_petite_etincelle, la marque de création de vêtement, pour femmes, enfants et bébé chic et tendance.@escadrilleparis, la marque d’espadrille mythique et authentique qui vient de sortir sa nouvelle collection d’été. ⁠Les deux marques s'associent pour vous proposer ce concours de rêve !⁠ 🤍⁠⁠Ma petite étincelle & Élise avaient envie de vous faire découvrir leurs univers en vous offrant une belle surprise pour la saison estivale. ⁠⁠À gagner⁠ 🎁 :⁠La blouse de votre choix & une paire d’espadrilles !⁠⁠Pour participer :⁠- Être abonnée à @ma_petite_etincelle et @escadrilleparis⁠- Liker ce post et identifier vos ami(e)s en commentaire ⁠⁠Bonus : doublez vos chances en partageant ce concours en story !⁠⁠Fin du concours, le dimanche 28 mai en fin de journée.⁠⁠Bonne chance & belle journée 🍀*Uniquement en France métropolitaine et Corse"


def get_end_date(caption=''):
    # returns the date of the end of the giveaway under the type datetime
    pattern1 = [
        {
            'regex': r"\b\d{2}\/\d{2}\b ",
            'format': '%d/%m',
            'separator': '/'
        },
        {
            'regex': r"\b\d{2}-\d{2}-\b ",
            'format': '%d-%m',
            'separator': '-'
        },
        {
            'regex': r"\b\d{2}\.\d{2}\b ",
            'format': '%d.%m',
            'separator': '.'
        },
        {
            'regex': r"\b\d{2} \d{2}\b ",
            'format': '%d %m',
            'separator': ' '
        },
        {
            'regex': r'\b(\d{1,2})\s*(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b',
            'format': '%d %B',
            'separator': ' '
        },

        # r"| \b\d{2}-\d{2}-\b ",
        # r"| \b\d{2}\.\d{2}\b ",
        # r"| \b\d{2} \d{2}\b ",
        # r'\b\(d{1,2})\s*(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b',
        ## r"| \b(Lundi | Mardi | Mercredi | Jeudi | Vendredi | Samedi | Dimanche) \d{1,2} (?Janvier | Février | Mars "
        ## r"| Avril | Mai | Juin | Juillet | Août | Septembre | Octobre | Novembre | Décembre)\b ",
        ## r"| \b\d{1,2} (?janv. | févr. | mars | avr. | mai | juin | juil. | août | sept. | oct. | nov. | déc.)\b ",
        ## r"| \b\d{1,2} (?Janv. | Févr. | Mars | Avr. | Mai | Juin | Juil. | Août | Sept. | Oct. | Nov. | Déc.)\b "
    ]

    pattern2 = [
        r"\b\d{2}\/\d{2}\/\d{4}\b ",
        r"\b\d{2}-\d{2}-\d{4}\b ",
        r"\b\d{2}\.\d{2}\.\d{4}\b ",
        r"\b\d{2} \d{2} \d{4}\b ",
        # r"\b(?lundi | mardi | mercredi | jeudi | vendredi | samedi | dimanche) \d{1,2} (?janvier | février | mars | avril "
        # r"| mai | juin | juillet | août | septembre | octobre | novembre | décembre) \d{4}\b ",
        # r"\b(?Lundi | Mardi | Mercredi | Jeudi | Vendredi | Samedi | Dimanche) \d{1,2} (?Janvier | Février | Mars | Avril "
        # r"| Mai | Juin | Juillet | Août | Septembre | Octobre | Novembre | Décembre) \d{4}\b ",
        # r"\b\d{1,2} (?janv. | févr. | mars | avr. | mai | juin | juil. | août | sept. | oct. | nov. | déc.) \d{4}\b ",
        # r"\b\d{1,2} (?Janv. | Févr. | Mars | Avr. | Mai | Juin | Juil. | Août | Sept. | Oct. | Nov. | Déc.) \d{4}\b "
    ]

    pattern3 = [
        r"| \b\d{2}\/\d{2}\/\d{2}\b ",
        r"| \b\d{2}-\d{2}-\d{2}\b ",
        r"| \b\d{2}\.\d{2}\.\d{2}\b ",
        r"| \b\d{2} \d{2} \d{2}\b "
    ]
    date = None
    for pattern in pattern1:
        matches = re.findall(pattern['regex'], caption, re.IGNORECASE)
        for match in matches:
            date_str = pattern['separator'].join(match)
            try:
                date_obj = datetime.strptime(date_str, pattern['format'])
                date_obj = date_obj.replace(year=datetime.now().year)
                date = date_obj
            except ValueError:
                pass
    if date is None:
        date = datetime.now() + timedelta(days=7)
    return date


def check_if_concours(post=''):
    score = 0
    # part 1 : get rid of the words that prove that it's the results of a giveaway
    if 'gagnants sont' in post:
        score -= 1
    if 'gagnant est' in post:
        score -= 1
    if 'gagnante est' in post:
        score -= 1
    if 'gagnantes sont' in post:
        score -= 1
    if 'gagnant(e) est' in post:
        score -= 1
    if 'gagnant(e)s sont' in post:
        score -= 1
    if 'bravo' in post:
        score -= 1
    if 'félicitations' in post:
        score -= 1
    if 'gagné' in post:
        score -= 1

    # Part 2 : identify if there are words that imply that it is actually a giveaway

    if '#jeuconcours' in post:
        score += 3
    else:
        score -= 1
    if '#jeuconcoursinstagram' in post:
        score += 1
    if 'participe' in post:
        score += 1
    if 'Participe' in post:
        score += 1
    if 'liker' in post:
        score += 1
    if 'Liker' in post:
        score += 1
    if 'like' in post:
        score += 1
    if 'Like' in post:
        score += 1
    if 'abonne' in post:
        score += 1
    if 'Abonne' in post:
        score += 1
    if 'suivre' in post:
        score += 1
    if 'Suivre' in post:
        score += 1
    if 'partage' in post:
        score += 1
    if 'Partage' in post:
        score += 1
    if 'commente' in post:
        score += 1
    if 'Commente' in post:
        score += 1
    if 'tag' in post:
        score += 1
    if 'Tag' in post:
        score += 1
    if 'ami' in post:
        score += 1
    if 'Ami' in post:
        score += 1
    if 'tirage au sort' in post:
        score += 1
    if 'Tirage au sort' in post:
        score += 1
    if 'bonne chance' in post:
        score += 1
    if 'Bonne chance' in post:
        score += 1
    if 'mentionne' in post:
        score += 1
    if 'Mentionne' in post:
        score += 1
    print("score : ", score)
    return score


def confidence_score(post):
    score = 0
    p = post['profile_details']
    if p['is_verified']:
        score += 80
    if p['is_business_account']:
        score += 10
    if p['followers'] > 20:
        score += 10
    if p['followers'] > 100:
        score += 15
    if p['followers'] > 1000:
        score += 20
    if p['followers'] > 10000:
        score += 10
    if p['followers'] > 100000:
        score += 10
    if p['date_first_post'] < datetime.now() - timedelta(days=180):
        score += 20
    if p['date_first_post'] < datetime.now() - timedelta(days=365):
        score += 10
    if p['likes_first_post'] > 100:
        score += 10
    if p['comments_first_post'] > 20:
        score += 10
    if score > 100:
        score = 100
    return score


# ----------------------------------------------------------------------------------------------------------------------#
### PART 3 : ADD TO THE DB ###
# ----------------------------------------------------------------------------------------------------------------------#

# def get_followers(username = ''):
#     url = f'https://www.instagram.com/{username}/?__a=1'
#     response = requests.get(url)
#     response = response.json()
#     followers = response['graphql']['user']['edge_followed_by']['count']
#     return followers

def add_to_db(media):
    # media is a json type dict which looks like this :
    #  'caption': 'This is a caption',
    #  'username': 'username',
    #  'likes': 0,
    #  'end_date': '2021-08-12T14:00:00+0000' si la date n'est pas indiquée, on prend la date de publication + 10 jours
    #  'followers': 0,
    #  'confidence': "0%",
    #  'intConfidence': 0
    # }
    score = check_if_concours(media['caption'])
    end_date = media['end_date']
    if not end_date:
        end_date = datetime.strptime(media['end_date'], '%d-%m-%Y') + timedelta(days=7)
        media['end_date'] = end_date.strftime('%d-%m-%Y')
    else:
        media['end_date'] = end_date.strftime('%d-%m-%Y')
    print(confidence_score(media))

    media['intConfidence'] = confidence_score(media)
    media['confidence'] = str(media['intConfidence']) + "%"
    media['date'] = media['date'].strftime('%d-%m-%Y')
    media['profile_details']['date_first_post'] = media['profile_details']['date_first_post'].strftime('%d-%m-%Y')
    post = media['caption']
    check_end_date()
    if score < 2:
        print("not a concours")
        return False
    elif end_date < datetime.now():
        print("concours ended")
        return False
    else:
        with open('db/concours.json', 'r') as file:
            concours = json.load(file)
            if media['caption'] not in concours:
                concours["concours"][f'{media["username"] }'] = media
                with open('db/concours.json', 'w') as NewFile:
                    print(concours)
                    # a = input("press enter to continue") # if i want to control whats written
                    json.dump(concours, NewFile)
                    return True


def check_end_date():
    with open('db/concours.json', 'r') as file:
        data = json.load(file)
        concours = data['concours']
        posts_to_remove = []
        for post_id, post in concours.items():
            end_date = datetime.strptime(post['end_date'], '%d-%m-%Y')
            if end_date < datetime.now():
                posts_to_remove.append(post_id)

        for post_id in posts_to_remove:
            del concours[post_id]

        with open('db/concours.json', 'w') as new_file:
            json.dump(data, new_file)

import os
import json

def check_pictures():
    with open('db/concours.json') as file:
        data = json.load(file)
        for filename in os.listdir():  # Iterate through files in the current folder
            if filename.endswith('.jpg'):
                for post_id, post in data['concours'].items():
                    if filename == f"{post['username']}_profile_pic.jpg":
                        break  # File matches username, move to the next file
                else:
                    file_path = os.path.join(os.getcwd(), filename)
                    os.remove(file_path)
                    print(f"Deleted file: {filename}")



# ig account id :17841404002252884


# hid = get_hashtag_id(hashtag="concours", instagram_account_id="17841404002252884", access_token=access_token)
# print(hid)
# get_recent_media(hashtag_id=hid, access_token=access_token, instagram_account_id="17841404002252884")
# check_if_concours(
#     post="Elle est là, pile pour les beaux jours ☀️! La collection de coussins outdoor #Riviera de @haomy_officiel vient d'arriver dans tous les magasins @fabriquedestyles 🎉 Des dizaines d'options avec des chiliennes, 5 tailles différentes de coussins, 4 coloris à rayures... Bref, de quoi imaginer votre déco de jardin sur-mesure, pour une farniente de qualité tout l'été ! Pour fêter cette collab' vitaminée, nos 2 comptes s'associent pour vous offrir la touche colorée qui manquait à votre déco : 🎁 Une chilienne et 3 coussins @haomy_officiel (80x80, 40x60 et 45x45cm) du coloris Riviera de votre choix (valeur : 180€70) 🎁 1 carte cadeau de 100€ valable dans tous les magasins Fabrique de Styles ou sur l'e-shop www.fabriquedestyles.com Pour participer : 👉 Suivre nos comptes @fabriquedestyles et @haomy_officiel 👉 Likez ce post et commentez en tagguant 2 amis fans de déco 👉 Partagez et/ou enregistrez le post (petite icone en bas à droite du post) si vous voulez nous soutenir 💛 📅 Tirage au sort le 21/04 à 10h 🤞 🚩 Concours réservé aux participants de France Métropolitaine")
# check_if_concours(
#     post="@skills_fr et l’@eabasket49 te donnent l’opportunité d’immortaliser cette saison en remportant le maillot collector de Printemps dédicacé par toute l'équipe ! 🤯😍 Pour tenter de le gagner, c’est simple, tu dois : ❤️ Liker cette publication 🔄 La partager en story 💬 Résumer la saison de l’EAB en 1 mot dans les commentaires 👤Être abonné à @skills_fr et @eabasket49 Si tu es tiré(e) au sort, nous te remettrons le maillot à la mi-temps du match de playoff de l’EAB face à Chalon-Reims le lundi 22 mai prochain, un moment unique ! 🤩 Si tu as déjà rêvé de fouler le parquet de Jean Bouin en tant que grand gagnant et remporter un maillot collector produit entièrement à partir de bouteilles recyclés ♻️, alors participe au concours ! #skills #artisandusport #basket #sport #equipement #match #maillot #france #angers #madeinfrance #ecoresponsable #qualité #EAB #concours #collector #playoff #proB")
print("------------------------------------")
# get_post_info()
# get_followers(username="tangilibrt")
posts = get_all_posts()
for post in posts:
    add_to_db(post)
check_pictures()