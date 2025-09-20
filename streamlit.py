import streamlit as st
st.title('Website name')
st.subheader('Welcome!')
if st.button('click'):
    st.write('Hello There!')
tab1, tab2 = st.columns(2)

with tab1:
    st.write('This website will guide you')
with st.sidebar:
    st.subheader('What we offer:')
    st.write('Get your work done easily')

    st.write('- We provide only the best services')
    st.write('- We excel and exceed exceptionally')
    st.write('- Subscribe to our program now!')
    st.write('---')
    st.subheader('Contact us now')
    st.write('- Mobile: +92 3242700848')
    st.write('- Email: click2ahmedsalman@gmail.com')
    st.write('- Feel free to contact')
    st.write('---')
