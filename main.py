import pyshorteners
url = "https://stefan-ci.herokuapp.com/articles/Python/comment-raccourcir-un-lien-en-python/"
shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(url))
