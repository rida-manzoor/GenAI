import Langchain02 as lch
import streamlit as st

st.title("Pets Name Generator")

options = ("Dog", "Cat", "Bird", "Fish")

# Create the selectbox in the sidebar
animal_type = st.sidebar.selectbox("What is your pet?", options)

if animal_type == "Cat":
    pet_color = st.sidebar.text_area(label = "What color is your cat?",
                                     max_chars=15)
    
if animal_type == "Dog":
    pet_color = st.sidebar.text_area(label = "What color is your dog?",
                                     max_chars=15)
    

if animal_type == "Cow":
    pet_color = st.sidebar.text_area(label = "What color is your cow?",
                                     max_chars=15)
    

if pet_color:
    response = lch.generate_pet_name(animal_type,pet_color)
    st.text(response)