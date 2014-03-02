from pattern.web    import Twitter
from pattern.en     import tag
from pattern.vector import KNN, count

twitter, knn = Twitter(), KNN()

for i in range(1, 20):
    print "trainning #GOOD tags"
    for tweet in twitter.search('#good', start=i, count=100, cached=False):
        s = tweet.text.lower()
        p = '#good' in s and 'GOOD' # if true convert to WIN
        v = tag(s)
        v = [word for word, pos in v if pos=='JJ'] # JJ = adjective
        v = count(v)
        if v:
            knn.train(v, type=p)

    print "trainning #BAD tags"
    for tweet in twitter.search('#bad', start=i, count=100, cached=False):
        s = tweet.text.lower()
        p = '#bad' in s and 'BAD'
        v = tag(s)
        v = [word for word, pos in v if pos=='JJ'] # JJ = adjective
        v = count(v) 
        if v:
            knn.train(v, type=p)

tweet = "I had a delicious dinner"
print "tweet: \"%s\", predicted hash tag: #%s"%(tweet, knn.classify(tweet))
tweet = "I had a awful dinner"
print "tweet: \"%s\", predicted hash tag: #%s"%(tweet, knn.classify(tweet))