social_media_posts=[

    [1,"classi",1000,7500,"akshay"],
    [2,"oldmoney",500,13000,"aksheyy"],
    [3,"vintage",3000,17000,"aksheyyuhh"],
    [4,"italy",13000,62000,"akshayreels"],

]
print(social_media_posts[1][1])
print(social_media_posts[1][-1])

all_captions=[ lst[1] for lst in social_media_posts]
print(all_captions)
all_fb_likes=[lst[2] for lst in social_media_posts]
print(all_fb_likes)
all_insta_like=[lst[3] for lst in social_media_posts]
print(all_insta_like)
all_names=[lst[4] for lst in social_media_posts]
print(all_names)


insta_most_view=[lst[4] for lst in social_media_posts if lst[3]>50000]
print(insta_most_view)

max_view_insta=max([lst[-2] for lst in social_media_posts])
max_view_insta=[lst[-1] for lst in social_media_posts if lst[-2]==max_view_insta]
print(max_view_insta)

food_log=[
    
    [1, "adithya", "dosa", "meals", "chapthy", 1800],
    [2,"shreya", "idly", "biriyani", "chapthy", 2100], 
    [3, "amritha", "appam", "meals", "puttu", 1700],
    [4, "dijo", "protien shake", "mandhi", "salad", 1900]

]

most_oderded_dish=[lst[1] for lst in food_log]