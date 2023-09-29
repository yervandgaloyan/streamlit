import streamlit as st
import openai
import os 
# Set your OpenAI API key here
api_key =  os.environ["OPENAI_API_KEY"]


# Initialize the OpenAI API client
openai.api_key = api_key

st.title("Social Media Post Generator")


post_types = [
    "Product Posts",
    "Engagement Posts",
    "News / Trending Posts",
    "Promotion of Blog Posts",
    "Competitions",
    "Stock Photograph Posts",
    "Screenshot Posts",
    "Infographics",
    "Personal Photograph Posts",
    "Workplace Behind-the-Scenes Posts",
    "Videos",
    "Multimedia / Interactive Content",
    "Polls",
    "Questions",
    "Quotes / Memes",
    "User-Generated Content",
    "Stories",
    "Livestreams"
]

# Streamlit UI elements for user input
number_of_posts = st.slider("Number of Posts", min_value=1, max_value=10)
social_media_channel = st.selectbox("Social Media Channel", ["Facebook", "Twitter", "Instagram","Linkedin"])
# social_media_channel = st.selectbox("Social Media Channel", ["Facebook", "Twitter", "Instagram","Linkedin"])
post_type = st.selectbox("Post Type", post_types)
business_name = st.text_input("Business Name")
# business_value = st.text_input("Business Value")
business_describtion = st.text_input("Business Description")
post_idea = st.text_input("Post Idea")
call_to_action = st.selectbox("Call to Action", ["commercial", "informational"])
# industry = st.text_input("Industry")
tone_of_voice = st.selectbox("Tone of Voice", ["friendly", "academic", "aggressive","humorous"])
number = st.slider("Number of Words", min_value=5, max_value=50)
website_link = st.text_input("Website Link")
number_of_hashtags = st.slider("Number of Hashtags", min_value=0, max_value=10)
# hashtags = st.text_area("Enter Relevant Hashtags (comma-separated)")

# Generate [number] posts for [social media channel].

# Business Name:
# [business name]

# Business Description: 
# [what does your business do?]

# For each post, ensure the following elements are incorporated:

# The social media content topic is about [content topic name]
# The post is about [short description]. 
# Use [keywords, key phrases] .
# Don’t use [keywords, key phrases] words. 
# Craft an engaging and creative first sentence to captivate readers.
# Maintain a [friendly, academic,aggressive, humorous] tone. 
# Aim for approximately [number] words for each post. 
# Include a [commercial, informational]  call to action or text leading to the following URL [URL].
# Remove hashtags from the text






def generate_post():
    post_parts = []

    # if number_of_posts:
    #     post_parts.append(f"Generate {number_of_posts} posts for {social_media_channel}")
    # if business_name:
    #     post_parts.append(f"{business_name}, specializes in {business_value} within the {industry} section.")
    # if number_of_posts:
    #     post_parts.append(f"The type of post is {post_type}")
    # post_parts.append("For each post, ensure the following elements are incorporated:")
    # if number:


    # post_parts.append("Maintain a friendly tone throughout. Avoid jargon and use approachable language.")
    # post_parts.append("Craft an engaging and creative first sentence to captivate readers and convey the main message effectively. ")
    # if business_name:
    #     post_parts.append(f" Emphasize the unique features of {business_name}")
    # if website_link:
    #     post_parts.append(f"Include a clear commercial call to action leading to our website page: {website_link}.")
    # if number_of_hashtags:
    #     post_parts.append(f"Integrate {number_of_hashtags} targeted hashtags relevant to {social_media_channel}")
    # else:
    #     post_parts.append("Remove Hashtags")


    if number_of_posts:
        post_parts.append(f"Generate {number_of_posts} posts for {social_media_channel}")
    if business_name:
        post_parts.append(f"Business Name:{business_name}")
    if business_describtion:
        post_parts.append(f"Business Description: {business_describtion}")
    # if number_of_posts:
    #     post_parts.append(f"The type of post is {post_type}")
    post_parts.append("For each post, ensure the following elements are incorporated:")
    if post_type:
        post_parts.append(f"The social media content topic is about {post_type}")
    if post_idea:
        post_parts.append(f"The post is about {post_idea}.")

    post_parts.append("Craft an engaging and creative first sentence to captivate readers and convey the main message effectively. ")
    post_parts.append(f"Maintain a {tone_of_voice} tone.")
    post_parts.append(f"Aim for approximately {number} words for each post.")
    if business_name:
        post_parts.append(f" Emphasize the unique features of {business_name}")
    if website_link:
        post_parts.append(f"Include a {call_to_action} call to action or text leading to the following URL {website_link}.")
    if number_of_hashtags:
        post_parts.append(f"Integrate {number_of_hashtags} targeted hashtags relevant to {social_media_channel}")
    else:
        post_parts.append("Remove hashtags from the text")
    if post_parts:
        generated_text = "\n\n".join(post_parts)
        st.subheader("Generated Post:")
        st.write(generated_text)

        # Use ChatGPT to suggest improvements or continue the text
        conversation = [{"role": "system", "content": "User"}, {"role": "user", "content": generated_text}]
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=500  # Adjust max_tokens as needed
            )
        assistant_reply = response['choices'][0]['message']['content']
        st.text_area("Assistant:", assistant_reply)
    else:
        st.warning("Please fill in at least one of the input fields to generate a post.")






if st.button("Generate Post"):
    generate_post()