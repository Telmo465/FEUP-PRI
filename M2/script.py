import pandas


final = pandas.read_csv('final.csv')
dic = {}


for i in final.index:
    print(i)
    if final['original_title'][i] not in dic.keys():
        dic[final['original_title'][i]] = final['review_content'][i]
    else:
        dic[final['original_title'][i]] += " " + final['review_content'][i]    
    

final = final.sort_values(by=["original_title", 'review_content'])
final = final.drop_duplicates(subset="original_title", inplace=False, keep="last")
final['reviews'] = ''


for i in final.index:
    print(i)
    if final['original_title'][i] in dic.keys():
        final['reviews'][i] = dic[final['original_title'][i]]
        del dic[final['original_title'][i]]
        

final.pop('review_content')
final.to_csv("final_lol.csv")