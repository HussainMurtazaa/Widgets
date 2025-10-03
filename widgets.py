import streamlit as st
import pandas as pd
import re
import plotly.express as px  # <-- add this

st.set_page_config(page_title="Widgets", page_icon="⚙️")

countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile",
    "China", "Colombia", "Comoros", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark",
    "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Eswatini",
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
    "Greenland", "Grenada", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan",
    "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
    "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
    "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Lucia",
    "Samoa", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Somalia", "South Africa", "South Korea", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"
]

if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    st.title("Page 1")

    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")

    if name:
        st.write(f"Hello, {name}. How are you?")
        if email:
            if re.match(r'^[a-zA-Z0-9.+-]+@gmail\.com$', email):
                st.success(f"Your email {email} is verified")
            else:
                st.error("Invalid email (only @gmail.com allowed)")
    else:
        st.warning("Please enter your name")

    if st.button("Next"):
        if name and email:
            st.session_state["name"] = name
            st.session_state["email"] = email
            st.session_state.page = 2
            st.rerun()
        else:
            st.error("Error")

elif st.session_state.page == 2:
    st.title("Page 2")

    age = st.slider("Select your age:", min_value=0, max_value=120, step=1)
    country = st.selectbox("Select your country:", countries)

    col1, col2 = st.columns([7.5, 1])
    with col1:
        if st.button("Back"):
            st.session_state.page = 1
            st.rerun()
    with col2:
        if st.button("Submit"):
            if age and country:
                st.session_state["age"] = age
                st.session_state["country"] = country
                st.session_state.page = 3
                st.rerun()
            else:
                st.error("Error.")

elif st.session_state.page == 3:
    st.title("Page 3")

    option = ["Python", "Java", "C++"]
    choice = st.selectbox("Choose your favorite language:", option)

    lang_data = {
        "Language": ["Python", "Java", "C++"],
        "Users": [8500000, 7500000, 4000000]  
    }
    df_lang = pd.DataFrame(lang_data)

    total_users = df_lang["Users"].sum()
    selected_users = df_lang[df_lang["Language"] == choice]["Users"].iloc[0]
    percentage = (selected_users / total_users) * 100

    st.info(f"🌍 About **{percentage:.1f}%** of developers worldwide use **{choice}**.")

    fig = px.pie(df_lang, values="Users", names="Language",
                 title="Worldwide Popularity of Programming Languages")
    st.plotly_chart(fig)

    data = {
        "Name": ["Mustafa", "Noman", "Ayesha", "Hania"],
        "Age": [19, 19, 20, 20],
        "City": ["Karachi", "London", "Newyork", "Germany"]
    }
    df = pd.DataFrame(data)
    df.to_csv("sample.csv")

    st.write(df)

    uploaded_file = st.file_uploader("Choose a Csv File", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)