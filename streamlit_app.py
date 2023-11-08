import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Submit", "Upload", "About Project ACORN"])

with tab1:
   st.header("ERFT Dictionary")
   
   text_input = st.text_input(
        "Search for an acronym",
        label_visibility="visible",
        placeholder="e.g. ERFT"
    )

with st.expander("FLU") e1:
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

with st.expander("ERFT") e2:
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
   
   

with tab2:
   st.header("Submit an Acronym")
   
   text_input1 = st.text_input(
        "Enter the ACRONYM you would like to add.",
        label_visibility="visible",
        placeholder="e.g. ERFT"
    )

   text_input2 = st.text_input(
        ("What does the acronym stand for?"),
        label_visibility="visible",
        placeholder="e.g. Enterprise Risk and Finance Technology"
    )

   text_input3 = st.text_input(
        ("Describe the acronym and give some content."),
        label_visibility="visible",
        placeholder="e.g. ERFT is a sub line of business within Bank of America. ERFT is responsible for "
    )

   text_input4 = st.text_input(
        ("Describe the acronym and give some content."),
        label_visibility="visible",
        placeholder="e.g. ERFT is a sub line of business within Bank of America. ERFT is responsible for "
    )
 
with tab3:
   st.header("An owl")

with tab4:
   st.header("Project ACORN")
 
