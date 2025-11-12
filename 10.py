import re
from collections import Counter
posts=["loving the new feature of this computer! #productlaunch #Ai",
       "days 2 of #productlaunch -great talks on #Ai and #Security.",
       "bug fix Shpped #changelog #Ai"]

hashtags=[]
for post in posts:
    hashtags += re.findall(r"#\w+", post)
    print(Counter(hashtags).most_common())