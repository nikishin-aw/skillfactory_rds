import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
print(os.listdir("input"))

data = pd.read_csv('input/imbd-sf/data.csv')
print(data.head(5))

print(len(data))

answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете
data['profit'] = data['revenue'] - data['budget']

# Делаем списки во множественных колонках
def to_list(no_list):
    if '|' in no_list:
        return no_list.split('|')
    else:
        return [no_list]

data['cast_list_col'] = data.cast.apply(to_list)
data['director_list_col'] = data.director.apply(to_list)
data['genres_list_col'] = data.genres.apply(to_list)
data['production_companies_list_col'] = data.production_companies.apply(to_list)
data['release_date_list_col'] = data.release_date.apply(lambda x: x.split('/'))


data_profit_plus = data[data.profit > 0].reset_index(drop=True) # Прибыльные фильмы

question = 1 # Номер текущего вопроса

# 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)
print('Вопрос {}'.format(question))
question += 1

print(data[data.budget == data.budget.max()][['original_title', 'imdb_id']])
answer_ls.append(4)

print()

# 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)
print('Вопрос {}'.format(question))
question += 1

print(data[data.runtime == data.runtime.max()][['original_title', 'imdb_id']])
answer_ls.append(2)

print()

# 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536
print('Вопрос {}'.format(question))
question += 1

print(data[data.runtime == data.runtime.min()][['original_title', 'imdb_id']])
answer_ls.append(3)

print()

# 4. Средняя длительность фильма?
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
print('Вопрос {}'.format(question))
question += 1

print(data.runtime.mean())
answer_ls.append(2)

print()

# 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
print('Вопрос {}'.format(question))
question += 1

print(data.runtime.median())
answer_ls.append(1)

print()

# 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549
print('Вопрос {}'.format(question))
question += 1

print(data[data.profit == data.profit.max()][['original_title', 'imdb_id']])
answer_ls.append(5)

print()

# 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819
print('Вопрос {}'.format(question))
question += 1

print(data[data.profit == data.profit.min()][['original_title', 'imdb_id']])
answer_ls.append(2)

print()

# 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
print('Вопрос {}'.format(question))
question += 1

print(len(data_profit_plus))
answer_ls.append(1)

print()

# 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421
print('Вопрос {}'.format(question))
question += 1

df_temp = data[data.release_year == 2008].reset_index(drop=True)
print(df_temp[df_temp.profit == df_temp.profit.max()][['original_title', 'imdb_id']])
answer_ls.append(4)

print()


# 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
print('Вопрос {}'.format(question))
question += 1

df_temp = data[(data.release_year >= 2012) & (data.release_year <= 2014)].reset_index(drop=True)
print(df_temp[df_temp.profit == df_temp.profit.min()][['original_title', 'imdb_id']])
answer_ls.append(5)

print()

# 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller
print('Вопрос {}'.format(question))
question += 1

genres_list = []
for genres_lst in data['genres_list_col']:
    for gener_one in genres_lst:
        genres_list.append(gener_one)

print(Counter(genres_list).most_common()[0][0])
answer_ls.append(3)

print()

# 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure
print('Вопрос {}'.format(question))
question += 1

genres_list = []
for genres_lst in data_profit_plus['genres_list_col']:
    for gener_one in genres_lst:
        genres_list.append(gener_one)

print(Counter(genres_list).most_common()[0][0])
answer_ls.append(1)

print()

# 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood
print('Вопрос {}'.format(question))
question += 1

director_list = []
for director_lst in data['director_list_col']:
    for director_one in director_lst:
        director_list.append(director_one)

print(Counter(director_list).most_common()[0][0])
answer_ls.append(3)

print()


# 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan
print('Вопрос {}'.format(question))
question += 1

director_list = []
for director_lst in data_profit_plus['director_list_col']:
    for director_one in director_lst:
        director_list.append(director_one)

print(Counter(director_list).most_common()[0][0])
answer_ls.append(4)

print()


# 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Director', 'Profit'])
for i in range(0, len(data)):
    col_one_list = data.loc[i]['director_list_col']
    col_two_list = data.loc[i]['profit']
    df_new_frame = pd.DataFrame({'Director':col_one_list, 'Profit':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Director'])['Profit'].sum().idxmax())
answer_ls.append(5)

print()

# 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Cast', 'Profit'])
for i in range(0, len(data)):
    col_one_list = data.loc[i]['cast_list_col']
    col_two_list = data.loc[i]['profit']
    df_new_frame = pd.DataFrame({'Cast':col_one_list, 'Profit':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Cast'])['Profit'].sum().idxmax())
answer_ls.append(1)

print()

# 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Cast', 'Profit'])
df_temp = data[data.release_year == 2012].reset_index(drop=True)
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['cast_list_col']
    col_two_list = df_temp.loc[i]['profit']
    df_new_frame = pd.DataFrame({'Cast':col_one_list, 'Profit':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Cast'])['Profit'].sum().idxmin())
answer_ls.append(3)

print()


# 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler
print('Вопрос {}'.format(question))
question += 1

cast_list = []
for cast_lst in data[data.budget > data.budget.mean()].reset_index(drop=True)['cast_list_col']:
    for cast_one in cast_lst:
        cast_list.append(cast_one)
print(Counter(cast_list).most_common()[0][0])
answer_ls.append(3)

print()


# 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime
print('Вопрос {}'.format(question))
question += 1

genre_list = []
for gener_lst in data[data.cast.str.contains('Nicolas Cage')].reset_index(drop=True)['genres_list_col']:
    for gener_one in gener_lst:
        genre_list.append(gener_one)
print(Counter(genre_list).most_common()[0][0])
answer_ls.append(2)

print()


# 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation
print('Вопрос {}'.format(question))
question += 1

company_list = []
for company_lst in data['production_companies_list_col']:
    for company_one in company_lst:
        company_list.append(company_one)
print(Counter(company_list).most_common()[0][0])
answer_ls.append(1)

print()


# 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation
print('Вопрос {}'.format(question))
question += 1

company_list = []
for company_lst in data[data.release_year == 2015].reset_index(drop=True)['production_companies_list_col']:
    for company_one in company_lst:
        company_list.append(company_one)
print(Counter(company_list).most_common()[0][0])
answer_ls.append(4)

print()


# 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Company', 'Profit'])
df_temp = data[data.genres.str.contains('Comedy')].reset_index(drop=True)
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['production_companies_list_col']
    col_two_list = df_temp.loc[i]['profit']
    df_new_frame = pd.DataFrame({'Company':col_one_list, 'Profit':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Company'])['Profit'].sum().idxmax())
answer_ls.append(2)

print()


# 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Company', 'Profit'])
df_temp = data[data.release_year == 2012].reset_index(drop=True)
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['production_companies_list_col']
    col_two_list = df_temp.loc[i]['profit']
    df_new_frame = pd.DataFrame({'Company':col_one_list, 'Profit':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Company'])['Profit'].sum().idxmax())
answer_ls.append(3)

print()


# 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517
print('Вопрос {}'.format(question))
question += 1

df_temp = data[data.production_companies.str.contains('Paramount Pictures')].reset_index(drop=True)
print(df_temp[df_temp.profit == df_temp.profit.min()][['original_title', 'imdb_id']].iloc[0])
answer_ls.append(1)

print()


# 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015
print('Вопрос {}'.format(question))
question += 1

print(data.groupby(['release_year'])['profit'].sum().idxmax())
answer_ls.append(5)

print()


# 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015
print('Вопрос {}'.format(question))
question += 1

print(data[data.production_companies.str.contains('Warner Bros')].groupby(['release_year'])['profit'].sum().idxmax())
answer_ls.append(1)

print()


# 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май
print('Вопрос {}'.format(question))
question += 1

mounth_list =[]
for mounth_lst in data['release_date_list_col']:
    mounth_list.append(mounth_lst[0])
print(Counter(mounth_list).most_common()[0][0])
answer_ls.append(4)

print()


# 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381
print('Вопрос {}'.format(question))
question += 1

count_mounth = 0
for mounth_lst in data['release_date_list_col']:
    if mounth_lst[0] in ['6', '7', '8']:
        count_mounth += 1

print(count_mounth)
answer_ls.append(2)

print()


# 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson
print('Вопрос {}'.format(question))
question += 1

df_new = pd.DataFrame(columns=['Director', 'Year', 'Counter'])
df_temp = data[(data.release_date.str.match('12'))|(data.release_date.str.match('1/'))|(data.release_date.str.match('2'))].reset_index(drop=True)
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['director_list_col']
    col_two_list = df_temp.loc[i]['release_year']
    df_new_frame = pd.DataFrame({'Director':col_one_list, 'Year':col_two_list, 'Counter':1})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(by=['Director', 'Year']).sum().reset_index().groupby(['Director'])['Counter'].sum().sort_values(ascending=False).idxmax())
answer_ls.append(5)

print()


# 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май
print('Вопрос {}'.format(question))
question += 1

df_temp = data[['release_date_list_col', 'release_year', 'profit']]
df_temp['mounth'] = df_temp.release_date_list_col.apply(lambda x: x[0])
print(df_temp.groupby(by=['mounth', 'release_year']).sum().reset_index().groupby(['mounth'])['profit'].sum().sort_values(ascending=False).idxmax())
answer_ls.append(2)

print()


# 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions
print('Вопрос 31')

df_new = pd.DataFrame(columns=['Company', 'Counter'], dtype=float)
df_temp = data[['production_companies_list_col', 'original_title']]
df_temp['Counter'] = df_temp.original_title.apply(lambda x: len(x))
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['production_companies_list_col']
    col_two_list = df_temp.loc[i]['Counter']
    df_new_frame = pd.DataFrame({'Company':col_one_list, 'Counter':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Company']).mean().sort_values(['Counter'], ascending=False).reset_index().loc[0][0])
answer_ls.append(5)

print()


# 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions
print('Вопрос 32')

df_new = pd.DataFrame(columns=['Company', 'Counter'], dtype=float)
df_temp = data[['production_companies_list_col', 'original_title']]
df_temp['Counter'] = df_temp.original_title.apply(lambda x: len(x.split(' ')))
for i in range(0, len(df_temp)):
    col_one_list = df_temp.loc[i]['production_companies_list_col']
    col_two_list = df_temp.loc[i]['Counter']
    df_new_frame = pd.DataFrame({'Company':col_one_list, 'Counter':col_two_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

print(df_new.groupby(['Company']).mean().sort_values(['Counter'], ascending=False).reset_index().loc[0][0])
answer_ls.append(5)

print()


# 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432
print('Вопрос 33')

word_list = []
for title in data['original_title']:
    for word in title.lower().split(' '):
        word_list.append(word)
print(len(set(word_list)))
answer_ls.append(3)

print()

# 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin
print('Вопрос 34')

count_one_percent = int(round(len(data)/100, 0))
print(data[['original_title', 'vote_average']].sort_values(['vote_average'], ascending=False).head(count_one_percent))
answer_ls.append(1)

print()


# 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint
print('Вопрос 35')

cast_list = []
for cast_lst in data['cast_list_col']:
    for cast_one in cast_lst:
        cast_list.append(cast_one)
cast_list = set(cast_list)

par_list = []
for cast_one in cast_list:
    df_temp = data[data.cast.str.contains(cast_one)]
    for cast_two_lst in df_temp['cast_list_col']:
        for cast_two in cast_two_lst:
            if cast_one != cast_two:
                par_list.append(cast_one + ' & ' + cast_two)

print(Counter(par_list).most_common(6))
answer_ls.append(5)

print()

# 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood
print('Вопрос 36')

df_new = pd.DataFrame(columns=['Director', 'Plus', 'Minus'])
for i in range(0, len(data)):
    col_one_list = data.loc[i]['director_list_col']
    if data.loc[i]['profit'] > 0:
        col_two_list = 1
        col_three_list = 0
    else:
        col_two_list = 0
        col_three_list = 1
    df_new_frame = pd.DataFrame({'Director':col_one_list, 'Plus':col_two_list, 'Minus':col_three_list})
    df_new = pd.concat([df_new, df_new_frame], ignore_index=True)

df_new = df_new.groupby(['Director']).sum()
df_new['Percent'] = df_new.Plus/(df_new.Plus + df_new.Minus)
df_new = df_new[df_new.Percent == 1].reset_index()
print(df_new.query('Director in ["Quentin Tarantino", "Steven Soderbergh", "Robert Rodriguez", "Christopher Nolan", "Clint Eastwood"]'))
answer_ls.append(4)

print()

# Submission
len(answer_ls)
pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])
