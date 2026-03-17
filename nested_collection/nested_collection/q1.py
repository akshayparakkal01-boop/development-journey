movies = [
    [1, "K.G.F: Chapter 1", "Yash", "kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]

# display all movie title

all_movie_title=[lst[1] for lst in movies]
print(all_movie_title)

# movie with top rating

max_raiting=max([lst[4] for lst in movies])

top_movies=[lst[1] for lst in movies if lst[-2]==max_raiting]
print(top_movies)


# display kannada movies
kannada_movies=[lst[1] for lst in movies if lst[3]=="kannada"]
print("kannada movies",kannada_movies)
# display movies whre actor is yash
yash_movies=[lst[1] for lst in movies if lst[2]=="Yash"]
print(yash_movies)
# which language most number of movies
language_list=[lst[3] for lst in movies]
print(language_list)
language_count={lst[3]:language_list.count(lst[3]) for lst in movies}
print(language_count)
language_count_list=[[v,k] for k,v in language_count.items()]
print(sorted(language_count_list,reverse=True))

# movie with max budget

# languages





