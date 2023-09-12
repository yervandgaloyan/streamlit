import streamlit as st
import openai

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

st.title("Social Media Post Generator")

# Streamlit UI elements for user input
number_of_posts = st.slider("Number of Posts", min_value=1, max_value=10)
social_media_channel = st.selectbox("Social Media Channel", ["Facebook", "Twitter", "Instagram"])
business_name = st.text_input("Business Name")
business_value = st.text_input("Business Value")
industry = st.text_input("Industry")
number = st.slider("Number of Words", min_value=5, max_value=50)
website_link = st.text_input("Website Link")
number_of_hashtags = st.slider("Number of Hashtags", min_value=1, max_value=10)
# hashtags = st.text_area("Enter Relevant Hashtags (comma-separated)")

def generate_post():
    post_parts = []

    if number_of_posts:
        post_parts.append(f"Generate {number_of_posts} posts for {social_media_channel} that align with our brand's voice and values.")
    if business_name:
        post_parts.append(f"{business_name}, specializes in {business_value} within the {industry} section.")
    if number:
        post_parts.append(f"Aim for approximately {number} words for each post.")
    post_parts.append("For each post, ensure the following elements are incorporated:")
    post_parts.append("Maintain a friendly tone throughout. Avoid jargon and use approachable language.")
    post_parts.append("Craft an engaging and creative first sentence to captivate readers and convey the main message effectively. ")
    if business_name:
        post_parts.append(f" Emphasize the unique features of {business_name}")
    if website_link:
        post_parts.append(f"Include a clear commercial call to action leading to our website page: {website_link}.")
    if number_of_hashtags:
        post_parts.append(f"Integrate {number_of_hashtags} targeted hashtags relevant to {social_media_channel}")
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