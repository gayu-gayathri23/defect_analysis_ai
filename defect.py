import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from PIL import Image

st.set_page_config('DEFECT AI',page_icon='🤖',layout='wide')

st.title('AI POWERED DEFECT ANALYZR 🤖🧠🇦🇮👾')
st.header(":red[Prototype of automated structural defect analyzer using AI]🎯")
st.subheader(f":blue[AI powered structural defect analysis using Streamlit that allows users to upload the image of any structural defects and to get suggestions and recommendations for repair and rebuilt]🚀")


with st.expander('➤About the app:'):
    st.markdown(f'''This app helps to detect the defects like cracks, misalligments etc and provider 
                - **Defect Detection**
                -**Recommendation**
                -**Suggestions for improvement**''')
    
import os
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
    
input_image = st.file_uploader('Upload your file here ➤',type=['jpg','jpeg','png'])

img=''

if input_image:
    img = Image.open(input_image).convert('RGB')
    st.image(img, caption='Uploaded Sucessfully ✅')
    
prompt = f'''You are an quality enginner and civil engineer. You need to Analyze the input 
image and provide necessary details for the below given questions 
in bullet points (max 3 points for each questions)

1.Identify the type of structural defect in the given image like cracks,bends,misalligements etc
2.Identify the color of the defect in the given image
3.Provide suggestions for repairing the defect in the given image
4.Indentify the possible causes of the defect in the given image
5.Provide recommendations for preventing such defects in the future
6.Provide a severity level for the defect in the given image (low, medium, high)
7.Identify any potential safety hazards associated with the defect in the given image
8.Provide any additional observations or insights about the defect in the given image
9.Provide a summary of the analysis in one or two sentences
10.Provide a list of similar defects that have been observed in the past and their outcomes'''

model=genai.GenerativeModel('gemini-2.5-flash-lite')

def geneate_result(prompt,img):
    result=model.generate_content(f'''Using the given{prompt}
                                    and given image {img}
                                    analyze the image and give the 
                                    results as per the given prompt''')
    return result.text

submit=st.button('Analyze the Image 🎯')

if submit:
    with st.spinner('Results Loading....🧑🏽‍💻'):
        response=geneate_result(prompt,img)
        
        st.markdown('## :green[Results]')
        st.write(response)