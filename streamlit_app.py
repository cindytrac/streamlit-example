import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
from io import StringIO

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Submit", "Upload", "About Project ACORN"])

with tab1:
   header1 = st.header("ERFT Dictionary")
   
   text_input9 = st.text_input(
        "Search for an acronym",
        label_visibility="visible",
        placeholder="e.g. ERFT"
    )

   

   # word1 = st.expander("FLU"):
   #     st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

   st.divider()  # 👈 Draws a horizontal rule

   st.subheader("ERFT - Enterprise Risk and Finance Technology")
   st.write("See ERFT Line of Business and Link for more information.")
   st.divider() 

   st.subheader("ERFT - Enterprise Risk and Finance Technology")

   st.divider()  # 👈 Draws a horizontal rule

   st.subheader("ERFT - Enterprise Risk and Finance Technology")
   
   st.divider() 


   

with tab2:
   header2 = st.header("Submit an Acronym")
   
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
        ("What subteam does this acronym belong to (if applicable)?"),
        label_visibility="visible",
        placeholder="e.g. ERFT (General)"
    )

  
with tab3:
   header3 = st.header("Upload a File to Parse for Acronyms")
   uploaded_files = st.file_uploader("Choose a PDF or TXT file", accept_multiple_files=True)
   for uploaded_file in uploaded_files:
       bytes_data = uploaded_file.read()
       st.write("File Uploaded:", uploaded_file.name)
       # st.write(bytes_data)
       st.subheader("Acronyms Detected")

       st.write("""
            a1 = st.checkbox('FLU')
            a2 = st.checkbox('GBAM')
            a3 = st.checkbox('ORCIT')
            a4 = st.checkbox('SDAR')
            a5 = st.checkbox('SLA')
            a6 = st.checkbox('BofA')
            a7 = st.checkbox('MRA')
       """)
      

   
      

with tab4:
   header4 = st.header("Project ACORN")
 
