import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate

st.set_page_config(page_title="Marketing Content AI")
st.title('Marketing Content AI')
from langchain.chat_models import ChatOpenAI
openai_api_key = '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'

def generate_response(input_text):
  # llm = OpenAI(temperature=0.2, openai_api_key=openai_api_key)
  chat = ChatOpenAI(temperature=0.0, openai_api_key=openai_api_key)
  st.info(chat(input_text).content)


from langchain import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")

with st.form('my_form'):
  # Audience
  # Set the title of the app
  st.title("Audence")

  # Generate a list of age ranges
  page_describtion = st.text_area('Enter FB/Insta page describtion:')
  brand_name = st.text_area('Brand Name:')
  industry = st.text_area('Industry')
  age_ranges = [str(age) + "-" + str(age + 9) for age in range(18, 100, 10)]
  # Dropdown widget for selecting age range
  age_range = st.selectbox("Select Age Range", age_ranges)
  gender = st.selectbox(
    'Select Audience Main Gender',
    ('Male', 'Female', 'Equal','Does not matter'))
  tone = st.selectbox(
    'Select Tone',
    ('informative', 'casual', 'professional', 'imaginative'))
  locations = ['Aremnia','Ukraine','United States', 'UK','Germany']
  # interests = ['Programming','Chockolate','Entertainment', 'Hobbies']
  # b = st.text_input('Movie title', 'Life of Brian')
  selected_location = st.selectbox("Select Users Location", locations)
  hashtags = st.selectbox("Select Users Location", ['Yes','None'])
  post_idea = st.text_area('Enter Initial post content:')
  length = st.text_area('Word count:')
  # length_10 = int(length)-10
  submitted = st.form_submit_button('Submit')

  # template_string = """
  #   Please create content that satisdies this conditions. All  provided informations are for descrbing the target audence. And does not have any connection with generated conten \
     
  
  #   [Age]: {age_range} \
  #   [Gender]: {gender}\
  #   [Page Description]: {page_describtion}:\

  #   [Background Information]:\
  #   {post_idea}\
    
  #   [Tone/Mood]:\
  #   {mood}\

  #   [Length]:
  #   Around 500-600 30-{length} words.

  #   """

  number_of_posts = 5
  social_media_channel = "Facebook"
  business_name = "OkayCode"
  business_value = "Teaeching children programming"
  industry = "Education"
  # page_describtion = ""
  # call_to_action = ""
  # We're reaching out to individuals who share a passion for [interests], aged [age], and living in [city/region/state], [country]. 

  

  template_string = """Generate {number_of_posts} posts for {social_media_channel} that align with our brand's voice and values. {business_name}, specializes in {business_value} within the {industry} section. 

For each post, ensure the following elements are incorporated:

Maintain a friendly tone throughout. Avoid jargon and use approachable language. Emphasize the unique features of [business name].
Aim for approximately [number] words for each post. 
Craft an engaging and creative first sentence to captivate readers and convey the main message effectively. 
Include a clear commercial call to action leading to our website page: [website link].
Integrate [number] targeted hashtags relevant to [social media channel]."""

  # template_string = """Using the provided insights, craft {number_of_posts} Facebook posts that align with our brand's voice and values. Our brand, {brand_name}, is known for {page_description}. We operate in the {industry} industry.

  # Each post should incorporate the following elements:

  # Engaging Introduction: Begin with an attention-grabbing statement that introduces the post's focus.

  # Call-to-Action (CTA): Include a compelling CTA that encourages readers to take a specific action, such as exploring our product line, visiting our website, or making a purchase.

  # Brand Connection: Conclude the post by subtly tying the benefits of the {Product/Service} back to our {brand_name}, reinforcing the value of choosing us. Emphasize how our brand's commitment to {brand_value} enhances the {Product/Service} experience.

  # Tone of Voice: Maintain a {tone} tone throughout the posts. Infuse {tone} to connect with our audience on a personal level. Use {tone} language while highlighting the unique features of the {Product/Service}. Avoid jargon and keep the language approachable.

  # Hashtags: {hashtags}

  # Number of Words: Aim for approximately {length} words for each Facebook post.

  # Initial Post Idea:
  # 1. [Your Initial Post Idea]

  # Feel free to personalize the posts based on the insights while ensuring consistency in messaging and imagery. Let's create posts that resonate with our audience and drive engagement!

  #   """
  

    
  # template_string = """Using the latest Facebook Insights data, craft {number_of_posts} engaging Facebook posts that resonate with our brand's voice and values. As {brand_name}, we are renowned for {page_description}, operating at the forefront of the {industry} industry.

  # Leveraging Facebook Insights, we've discovered the following about our audience:

  # Peak Engagement Times: Our audience is most active between {time_frame} on {days_of_week}, making it ideal to share posts during these periods for maximum visibility.
  # Preferred Content Type: {Content_type} consistently garners the highest engagement. Let's capitalize on this by crafting posts that feature {content_type}, ensuring our audience stays captivated.
  # Top Locations: {Location_insight} Our posts should resonate particularly well with this demographic.


  # Each post should incorporate these key elements:

  # Attention-Grabbing Introduction: Open with a compelling statement that instantly hooks our audience, drawing them into the post.
  # Unique Selling Points Emphasis: Highlight the distinctive selling points that differentiate {brand_name} from competitors. Focus on elements like {unique_selling_points} that resonate with our audience's preferences.
  # Compelling Call-to-Action (CTA): Incorporate an irresistible CTA that guides readers to take a specific action, whether it's exploring our product line, visiting our website, or making a purchase. Customizing the CTA based on our audience's interests can significantly boost engagement.
  # Brand Connection: Conclude the post by subtly connecting the benefits of the {industry} industry to the value {brand_name} provides. This reinforces the audience's choice in opting for us.
  # Tailored Tone of Voice: Infuse the {tone} tone consistently across all posts, creating a personal connection with our audience. While discussing the unique features of the {industry}, maintain an approachable language that avoids jargon and resonates with our audience's preferences.
  # Relevant Hashtags: Incorporate {hashtags} strategically to increase post discoverability and engagement.
  # Word Count Optimization: Aim for approximately {length} words per post to maintain conciseness while conveying the intended message effectively.
  # By integrating these insights, we're poised to create Facebook posts that resonate deeply with our audience and drive meaningful engagement. Let's leverage the power of data to strengthen our brand's online presence and foster connections with our audience."""

  prompt_template = ChatPromptTemplate.from_template(template_string)

  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    customer_messages = prompt_template.format_messages(number_of_posts = number_of_posts, age_range = age_range,gender=gender,page_describtion=page_describtion,post_idea= post_idea,mood = tone,length = length)
    generate_response(customer_messages)
