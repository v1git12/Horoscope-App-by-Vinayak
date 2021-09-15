import random
import streamlit as st
import pandas as pd

from datetime import date

today = date.today()
date = today.strftime("%B %d, %Y")
data = pd.read_csv("data.csv")

st.title("Welcome to Daily Horoscope"
         "  Astrology prediction by Pythonrishi")
sunsign = st.sidebar.selectbox("Select your Zodiac sign",("Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"))

imaget =f"image\\{sunsign}.png"

lucky_number = random.randint(1,100)
colours = ["red","yellow","blue","brown","orange","green","violet","black","carnation pink", "yellow orange", "blue green", "red violet", "red orange",
                            "yellow green", "blue violet", "white", "violet red","apricot", "scarlet", "green yellow","indigo","gray"]
lucky_color = random.choice(colours)

# print(lucky_color)
#convert data frame to list
listofhs = data["SS_horoscope"].values.tolist()
listoflf = data["SS_selection1"].values.tolist()

#randomly select
lovefocus = random.choice(listoflf)
horoscope = random.choice(listofhs)

# print(horoscope)
st.title(f"{sunsign}")
st.header(f"Horoscope for {date} ")

st.subheader(f"{horoscope}")
st.image(imaget)
st.write(f"Your lucky number is {lucky_number}")
st.write(f"Your lucky Color is {lucky_color}")
st.write(f"{lovefocus}")
