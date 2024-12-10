
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load model and data
df = pd.read_csv("body_data.csv")
model = DecisionTreeClassifier().fit(
    df[["Waist", "Hips", "Shoulders"]], df["BodyType"]
)

recommendations = {
    "Hourglass": ["Fitted tops", "A-line skirts", "High-waisted pants"],
    "Pear": ["Wide-leg trousers", "Peplum tops", "A-line dresses"],
    "Rectangle": ["Ruffled tops", "Layered outfits", "Belts to define waist"],
    "Apple": ["Empire-waist dresses", "V-neck tops", "Flared pants"]
}

def recommend_clothing(body_type):
    return recommendations.get(body_type, ["No suggestions available"])

# Streamlit app
st.title("Body Type and Clothing Recommendation")

waist = st.number_input("Enter your waist size (inches):", min_value=20, max_value=50, step=1)
hips = st.number_input("Enter your hip size (inches):", min_value=20, max_value=60, step=1)
shoulders = st.number_input("Enter your shoulder size (inches):", min_value=20, max_value=60, step=1)

if st.button("Get Recommendation"):
    body_type = model.predict([[waist, hips, shoulders]])[0]
    outfits = recommend_clothing(body_type)
    st.write(f"Predicted Body Type: {body_type}")
    st.write("Recommended Clothing:")
    for outfit in outfits:
        st.write(f"- {outfit}")
