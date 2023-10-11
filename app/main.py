import streamlit as st
import openai
import os 
# Set your OpenAI API key here
api_key =  os.environ["OPENAI_API_KEY"]


# Initialize the OpenAI API client
openai.api_key = api_key

st.title("Social Media Post Generator")

post_types = [
    "Simple post",
    "Video post",
    "Event post",
    "Articles post",
    "Polls post",
    "Carousel post",
    "Celebrate an occasion post"
]



channel = st.multiselect(
    'Select Social Media Channel',
    ["Facebook", "Twitter", "Instagram","Linkedin"])



if 'Linkedin' in channel: # If user selects Email  do 
    post_types = st.selectbox("Post Type", post_types)
    
    if "Polls post" in post_types:
        poll_topic = st.text_input("Poll Topic")
        number_of_options = st.slider("Number of Options", min_value=2, max_value=4)
        business_name = st.text_input("Business Name")
        business_describtion = st.text_input("Business Description")
        website_link = st.text_input("Website Link")
        number_of_posts = st.slider("Number of Posts", min_value=1, max_value=10)
        call_to_action = st.selectbox("Call to Action", ["commercial", "informational"])
    
    elif "Simple post" in post_types:
        content_topic = st.text_input("Content Topic")
        post_topic = st.text_input("Post Topic")
        number_of_words = st.slider("Number of Words", min_value=15, max_value=100)
        business_name = st.text_input("Business Name")
        business_describtion = st.text_input("Business Description")
        website_link = st.text_input("Website Link")
        
        # number_of_posts = st.slider("Number of Posts", min_value=1, max_value=10)
        call_to_action = st.selectbox("Call to Action", ["commercial", "informational"])
        notes = st.text_input("Notes (any notes that could be useful)")


# Poll Topic - employee onboarding and offboarding Question 
# character limit - max 140 
# Options - 4 Options 
# character limit - max 30
# Business Name: Raiser 
# Business Description: HR software that automates HR processes Website
# URL - raiser.global
# Number of polls - 3 
# Call to action - informational

# Poll Topic - [poll topic]
# Question character limit - max 140-for mher
# Options - [number]
# Options character limit - max 30-for mher
# Business Name: [business name]
# Business Description: [what does your business do?] - doesn’t make that sense in this case
# Website URL - [URL]
# Number of polls - [number]
# Call to action - [commercial, informational] 



def generate_post():

    post_parts = []
    if "Polls post" in post_types:
        post_parts.append(f"Generate poll based on this criteria")
        post_parts.append(f"Poll Topic - {poll_topic} \n")
        post_parts.append("Question character limit - max 140\n")
        post_parts.append(f"Options - {number_of_options}\n")
        post_parts.append(f"Options character limit - max 30\n")
        post_parts.append(f"Business Name - {business_name}\n")
        post_parts.append(f"Business Description - {business_describtion}\n")
        post_parts.append(f"Website URL  - {website_link}\n")
        post_parts.append(f"Number of posts -  {number_of_posts}\n")
        post_parts.append(f"Call to action - {call_to_action}\n")
        post_parts.append("The structore of generted text something like this ")
        post_parts.append("Poll topic 1")
        post_parts.append("Question 1")
        post_parts.append("Options:")
        post_parts.append("Poll topic 2")
        post_parts.append("Question 2")
        post_parts.append("Options:")
        post_parts.append("and so on")
    elif "Simple post" in post_types:
        post_parts.append(f"Generate post based on this criteria")
        post_parts.append(f"Post Topic - {post_topic} \n")
        post_parts.append(f"Content Topic - {content_topic}\n")
        post_parts.append(f"Business Name - {business_name}\n")
        post_parts.append(f"Business Description - {business_describtion}\n")
        post_parts.append(f"Website URL  - {website_link}\n")
        post_parts.append(f"Word Count   - {number_of_words}\n")
        post_parts.append(f"Call to action - {call_to_action}\n")
        post_parts.append(f"Notes - {notes}\n")

    if post_parts:
        generated_text = "\n\n".join(post_parts)
        st.subheader("Generated Post:")
        st.write(generated_text)

        # Use ChatGPT to suggest improvements or continue the text
        conversation = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": generated_text}]
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=500  # Adjust max_tokens as needed
            )
        assistant_reply = response['choices'][0]['message']['content']
        st.text_area("Assistant:", assistant_reply,  height=400)
    else:
        st.warning("Please fill in at least one of the input fields to generate a post.")



if st.button("Generate Post"):
    generate_post()