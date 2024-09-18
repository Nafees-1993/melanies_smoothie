# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup with straw: Customize your smoothie! :cup with straw:")
st.write(
    """Choose the fruits you want in your custom smoothie!
""")

#import streamlit as st

name_on_order = st.text_input('Name on smoothie:')
st.write('The name of your Smoothie will be :', name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'choose up to five ingredents:'
    ,my_dataframe
    ,max_selections=5
    
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''
    
    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen + ' '
    #st.write(ingredients_string)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
    

    time_to_insert= st.button('Submit Order')

    if time_to_insert:

        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered!,'"" + name_on_order + ""'', icon="✅")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
