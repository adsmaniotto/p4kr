import requests, bs4
import datetime

# Navigate to Pitchfork and pull the URLs for today's featured reviews
prefix = "http://www.pitchfork.com"
res = requests.get(prefix)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

# Pull the div in the HTML code that contains all the album review info
album_details = soup.select('.album-details')

# Step through each of the featured reviews, extract info, and print to console

print("Pitchfork Reviews for " + str(datetime.date.today()))
print("I read Pitchfork reviews every morning so you don't have to.")
print('\n')

for element in album_details[0:5]:

    # Artist and Album Title
    print(element.a.get_text(" - "))
    
    # Genre (prints Other is there isn't one listed)
    if element.find("a", class_='genre-list__link') is None:
        print('Other')
    else:
        print(element.find("a", class_='genre-list__link').string)
    
    # navigates to the review page to pull score box data
    rvw = requests.get(prefix + element.a.get("href"))
    rvw.raise_for_status()
    review = bs4.BeautifulSoup(rvw.text, "lxml")
    
    # score / BNM indicator"
    score_box = review.find("div", class_='score-box')
    print("Score: " + score_box.get_text(" | "))
    bnm = bool(len(score_box.get_text(" ").split(" ")) > 1)
    
    # abstract summary
    print(element.p.get_text())
    
    # link to review
    print(prefix + element.a.get("href"))
    print('\n')


# Ideas for future code that I will write locally so I'm not sharing my Gmail password on GitHub :)
# Email the daily summary to yourself
# Automate the process to run at 6 AM every morning
# On weekends, just pull the first featured review (since they publish less content on weekends)
# BONUS: When an album gets Best New Music, sent an SMS

