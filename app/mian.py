import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate

st.set_page_config(page_title="Marketing Content AI")
st.title('Marketing Content AI')
from langchain.chat_models import ChatOpenAI
openai_api_key = ''

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
  age_ranges = [str(age) + "-" + str(age + 9) for age in range(18, 100, 10)]
  # Dropdown widget for selecting age range
  age_range = st.selectbox("Select Age Range", age_ranges)
  gender = st.selectbox(
    'Select Audience Main Gender',
    ('Male', 'Female', 'Equal','Does not matter'))
  tome = st.selectbox(
    'Select Tone',
    ('informative', 'casual', 'professional', 'imaginative'))
  locations = ['Aremnia','Ukraine','United States', 'UK','Germany']
  # interests = ['Programming','Chockolate','Entertainment', 'Hobbies']
  # b = st.text_input('Movie title', 'Life of Brian')
  selected_location = st.selectbox("Select Users Location", locations)
  hashtags = st.selectbox("Select Users Location", ['Yes','No'])
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
  # brand_name = "OkayCode"
  # page_describtion = ""
  # call_to_action = ""
  template_string = """"Using the provided insights, craft {number_of_posts} Facebook posts that align with our brand's voice and values. Our brand, {brand_name}, is known for {page_description}. We operate in the {industry} industry.

  Each post should incorporate the following elements:

  Engaging Introduction: Begin with an attention-grabbing statement that introduces the post's focus.

  Highlight Unique Selling Points: Mention the {number} key unique selling points of the {Product/Service} that set it apart from the competition.

  Call-to-Action (CTA): Include a compelling CTA that encourages readers to take a specific action, such as exploring our product line, visiting our website, or making a purchase.

  Brand Connection: Conclude the post by subtly tying the benefits of the {Product/Service} back to our {brand_name}, reinforcing the value of choosing us. Emphasize how our brand's commitment to {brand_value} enhances the {Product/Service} experience.

  Tone of Voice: Maintain a {tone} tone throughout the posts. Infuse {tone} to connect with our audience on a personal level. Use {tone} language while highlighting the unique features of the {Product/Service}. Avoid jargon and keep the language approachable.

  Hashtags: {hashtags}

  Number of Words: Aim for approximately {length} words for each Facebook post.

  Initial Post Idea:
  1. [Your Initial Post Idea]

  Feel free to personalize the posts based on the insights while ensuring consistency in messaging and imagery. Let's create posts that resonate with our audience and drive engagement!"

    """
  prompt_template = ChatPromptTemplate.from_template(template_string)

  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    customer_messages = prompt_template.format_messages(age_range = age_range,gender=gender,page_describtion=page_describtion,post_idea= post_idea,mood = mood,length = length)
    generate_response(customer_messages)
