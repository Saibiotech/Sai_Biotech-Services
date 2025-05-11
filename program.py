print("bikash kumar pal")
import streamlit as st

st.set_page_config(page_title="Sai Biotech Services", layout="wide")

# Header
st.title("Sai Biotech Services")
st.subheader("Empowering Horticulture & Agriculture with Modern Equipment")

# About Section
st.markdown("## About Us")
st.write("""
Sai Biotech Services is dedicated to providing high-quality horticulture and agriculture tools and machinery. 
We aim to support farmers and agribusinesses with reliable and innovative solutions to improve productivity and efficiency.
""")

# Services Section
st.markdown("## Our Products & Services")
st.write("- Horticulture Equipment")
st.write("- Agriculture Tools & Machinery")
st.write("- Greenhouse Supplies")
st.write("- Irrigation Systems")
st.write("- Consultancy & Support")

# Gallery or Product Display (optional: add images if available)
st.markdown("## Product Gallery")
st.info("Image previews coming soon. Contact us for full catalog.")

# Contact Section
st.markdown("## Contact Us")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you! We'll contact you soon.")

# Footer
st.markdown("---")
st.caption("© 2025 Sai Biotech Services |")