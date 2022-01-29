def get_title(post):
    splitted_post = post.split()
    word = splitted_post[0]
    tittle = []
    i=0
    while word.isupper() or word.isnumeric():
        tittle.append(word)
        i+=1
        word = splitted_post[i]

    #return " ".join(tittle)
    print(" ".join(tittle))
