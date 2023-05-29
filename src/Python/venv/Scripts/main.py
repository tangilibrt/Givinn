import Instagram as IG

def main():
    """
    Main function of the program.
    The program is supposed to scrap all the posts of the "concours" hashtag and after a thorough analysis, it will
    decide if it is worth adding it to the json database, while giving it a score of confidence regarding the
    trustability of the post. It will also check in the said json database if the giveaway is outdated or not and remove
    it if so.
    :return:
    """

    ''' Fist, we will get the 25 latest posts and their respective infos'''

    posts = IG.get_all_posts()
    for post in posts:
        IG.add_to_db(post)

    ''' Once we got the post, we analyse it to get the number of likes, the number of followers of the account, etc...      
        But since we don't have the permission yet, we couldn't find the exact type of the data returned by the API so 
        let's suppose that it is under the form 'media' detailed in the 'add_to_db' function in Instagram.py and that we
        we have actually successfully retrieved the data. We will first attribute a confidence score to the post and
        then add it to the database.
    '''



if __name__ == '__main__':
    main()
