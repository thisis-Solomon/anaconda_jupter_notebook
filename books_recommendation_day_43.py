import pandas as pd

data = [
    {
        "title": "The Nightingale",
        "author": "Kristin Hannah",
        "genre": "Historical Fiction",
        "description": "Set in France during World War II, this novel follows the lives of two sisters as they navigate the difficulties of living in a war-torn country."
    },
    {
        "title": "The Hate U Give",
        "author": "Angie Thomas",
        "genre": "Young Adult",
        "description": "This novel follows the story of a 16-year-old girl who witnesses the fatal shooting of her unarmed friend by a police officer."
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Spiritual Fiction",
        "description": "This novel follows the story of a young shepherd on a journey to fulfill his dreams and find his Personal Legend."
    },
    {
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "Crime Fiction",
        "description": "This novel follows the story of a journalist and a hacker who team up to solve a decades-old mystery."
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Literary Fiction",
        "description": "This novel follows the story of two childhood friends in Afghanistan and their journey to redemption."
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Classic",
        "description": "This novel follows the story of a disillusioned teenager as he navigates the challenges of adolescence."
    },
    {
        "title": "The Help",
        "author": "Kathryn Stockett",
        "genre": "Historical Fiction",
        "description": "This novel follows the story of a young white woman and her black maid in 1960s Mississippi as they navigate the complexities of racial tension."
    },
    {
        "title": "The Perks of Being a Wallflower",
        "author": "Stephen Chbosky",
        "genre": "Young Adult",
        "description": "This novel follows the story of a shy teenager who finds acceptance and belonging among a group of outsiders in the 1990s."
    },
    {
        "title": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "genre": "Dystopian",
        "description": "This novel follows the story of a group of women who are forced into reproductive servitude in a totalitarian society."
    },
    {
        "title": "The Power",
        "author": "Naomi Alderman",
        "genre": "Speculative Fiction",
        "description": "This novel follows the story of a group of women who suddenly develop the ability to release electrical jolts from their fingertips, and how this shift in power dynamics changes society."
    }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("Date saved")