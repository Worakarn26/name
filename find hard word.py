import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an AI finding word that are not often founded in daily life. You will receive a 
            passage and you should give the answer.
            list answer in a JSON array, one answer per line.
            Each answer should have 3 fields:
            - "Word" - the word that is not often found in daily life.
            - "Context" - the sentence that the word is founded.
            - "Definition" - definition of that word.
            Don't say anything at first. Wait for the user to say something.
        """    
st.title('Concluding passages')
st.markdown('Input the passage that you want to find hard word. \n\
            The AI will give you list of word that are not often founded in daily life.')

user_input = st.text_area("Enter some text to correct:", "Your text here")


# submit button after text input
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    answer_dictionary = response.choices[0].message.content

    sd = json.loads(answer_dictionary)

    print (sd)
    answer_df = pd.DataFrame.from_dict(sd)
    print(answer_df)
    st.table(answer_df)