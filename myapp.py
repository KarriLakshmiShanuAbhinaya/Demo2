import streamlit as st
st.set_page_config(page_title='Cats')
st.header("types od cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("American Short hair cat")
  st.image("https://www.thesprucepets.com/thmb/17UY4UpiMekV7WpeXDziXsnt7q4=/1646x0/filters:no_upscale():strip_icc()/GettyImages-145577979-d97e955b5d8043fd96747447451f78b7.jpg")
  st.witre("persian cats aare cute")
with col2:
  st.subheader("Birman")
  st.image("https://www.thesprucepets.com/thmb/D5s03LINbIYpZuiG6uvBpKrAKXk=/3500x0/filters:no_upscale():strip_icc()/GettyImages-623368786-f66c97ad6d2d494287b448415f4340a8.jpg")
  st.witre("rainbow rose's are very beutiful")
