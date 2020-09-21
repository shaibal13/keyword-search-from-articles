def string_matching (articles, keywordForSearch):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result=[]
    for article in articles:
        no_punct = " "
        for char in article:
            if char not in punctuations:          
               no_punct = no_punct + char
        res = no_punct.split()                   
        singleArticle=[]
        for resupdate in res:                      
            singleArticle.append(resupdate.lower())
        if(keywordForSearch in singleArticle):
            result.append(article)
           
    
    return result                         



articles=[]
articles_count=int(input ('How many articles you want to input?: '))
print('Enter articles: ')
for i in range(articles_count):
  article = input().lower()
  articles.append(article)
print('Enter Keyword For searching articles which contains this Keyword: ')
keyword = input().lower()
result = string_matching(articles,keyword)      
for resultPrint in result:             
    print(resultPrint)
    print("\n")


