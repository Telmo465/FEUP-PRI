import pandas as pd

def get_relavent_q1(final, file_name):

    file = open(file_name, "w")
    
    for i in final.index:
        if "spy" in final['description'][i] or "spies" in final['description'][i]:
            file.writelines(final['movie_title'][i] + '\n')
    
    file.close()


def get_relavent_q2(final, file_name):

    file = open(file_name, "w")
    
    for i in final.index:
        if "Brad Pitt" in final['actors'][i] or "Angelina Jolie" in final['actors'][i]:
            file.writelines(final['movie_title'][i] + '\n')
    
    file.close()


def get_relavent_q3(final, file_name):

    file = open(file_name, "w")
    
    for i in final.index:
        if ("thrilling" in final['reviews'][i].lower() or "exciting" in final['reviews'][i].lower() or "exhilarating" in final['reviews'][i].lower())\
        and final['tomatometer_rating'][i] > 90.0:
            file.writelines(final['movie_title'][i] + '\n')
    
    file.close()
    

def get_relavent_q4(final, file_name):

    file = open(file_name, "w")
    
    for i in final.index:
        if final['available_netflix'][i] and final['tomatometer_rating'][i] == 100.0:
            file.writelines(final['movie_title'][i] + '\n')
    
    file.close()


final = pd.read_csv('final_lol.csv')


get_relavent_q1(final, 'q1/qrels1.txt')
get_relavent_q2(final, 'q2/qrels2.txt')
get_relavent_q3(final, 'q3/qrels3.txt')
get_relavent_q4(final, 'q4/qrels4.txt')









