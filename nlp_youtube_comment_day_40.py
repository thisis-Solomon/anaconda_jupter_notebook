import pandas as pd
import numpy as np

toxi_comments = [
    "You're so dumb","This is trash", "Worst video ever", "Stop making content",
    "You sound horrible", "Clickbait title", "Can't believe people like this", 
    "Waste of time", "cringe content", "You're such a loser", "You're so bad",
]

supportive_comments = [
    "This helped me a lot", "You're amazing!", "Best tutorial I've seen",
    "Thanks for the content", "Keep up the great work", "So clear and helpful",
    "Awesome explanation", "I learned a lot", "Thanks for sharing", "You're a genius",
    "You're so talented", "Legend!"
]

data = []

for i in range(50):
    data.append({
        "comment": np.random.choice(toxi_comments), "label": "toxic"
    })
    data.append({
        "comment": np.random.choice(supportive_comments), "label": "supportive"
    })
    
df = pd.DataFrame(data)
df.to_csv("youtube_comments.csv", index=False)  
print("Data saved in file")
