import streamlit as st
st.set_page_config(page_title='Cats')
st.header("types od cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("American Short hair cat")
  st.image("https://www.thesprucepets.com/thmb/17UY4UpiMekV7WpeXDziXsnt7q4=/1646x0/filters:no_upscale():strip_icc()/GettyImages-145577979-d97e955b5d8043fd96747447451f78b7.jpg",width=200)
  st.write("American Short hair cats are cute")
with col2:
  st.subheader("Birman")
  st.image("https://www.thesprucepets.com/thmb/D5s03LINbIYpZuiG6uvBpKrAKXk=/3500x0/filters:no_upscale():strip_icc()/GettyImages-623368786-f66c97ad6d2d494287b448415f4340a8.jpg",width=200)
  st.write("Birman are very beutiful")
col3,col4=st.columns(2)
with col3:
  st.subheader("Burmesecat")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp3h22InvhCrmGBT4jVXM3f-5kJoCHZl2mDucWsUD9Z6lIJa7V",width=200)
  st.write("Burmese cats are cute")
with col4:
  st.subheader("Tom and jerry")
  st.image("https://www.icegif.com/wp-content/uploads/tom-and-jerry-icegif-11.gif",width=200)
  st.write("Tom and Jerry are best friends")
