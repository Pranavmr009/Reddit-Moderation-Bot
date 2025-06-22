import os 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
def Moderate_Sub(POST_TITLE, POST_BODY):

        
    response = model.generate_content(f'''
            You are an AI moderator helping manage a Reddit community called r/NEET. 

            In this subreddit, 'NEET' stands for 'Not in Employment, Education, or Training' — referring to people who are unemployed and disconnected from school or work. It is a lifestyle or socio-economic status discussion group, often discussing topics like unemployment, mental health, social isolation, and alternative lifestyles.

            Some users mistakenly confuse r/NEET with the Indian 'NEET' medical entrance exam (National Eligibility cum Entrance Test), and they post questions about test prep, medical admissions, or Indian colleges — these posts are completely off-topic.

            Your job is to decide whether a post is on-topic for r/NEET.

            ---

            Check the following post:

            Title: {POST_TITLE}

            Body: {POST_BODY}

            ---

            Reply with one word only:  
            'yes' → if it belongs in r/NEET (lifestyle)  
            'no' → if it is about the Indian NEET exam or otherwise unrelated
''')
    answer = response.text.strip().lower()
    return answer

# Moderate_Sub("  What games you guys playing?  ", '''Looking to start some new stuff
# ''')

