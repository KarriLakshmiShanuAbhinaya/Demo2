import streamlit as st
st.set_page_config(page_title='Cats')
st.markdown("<h1 style='color:#2D9596;'>Types of Cats</h1>", unsafe_allow_html=True)
#st.header("types od cats")
col1,col2,col3=st.columns(3)
with col1:
  st.markdown("<h3 style='color:#FF9800;'>American Cat</h3>", unsafe_allow_html=True)
  st.image("https://www.thesprucepets.com/thmb/17UY4UpiMekV7WpeXDziXsnt7q4=/1646x0/filters:no_upscale():strip_icc()/GettyImages-145577979-d97e955b5d8043fd96747447451f78b7.jpg",width=230)
  st.write("American Short hair cats are cute")
with col2:
  st.markdown("<h3 style='color:#FF9800;'>Birman</h3>", unsafe_allow_html=True)
  st.image("https://www.thesprucepets.com/thmb/D5s03LINbIYpZuiG6uvBpKrAKXk=/3500x0/filters:no_upscale():strip_icc()/GettyImages-623368786-f66c97ad6d2d494287b448415f4340a8.jpg",width=230)
  st.write("Birman are very beutiful")
with col3:
  st.markdown("<h3 style='color:#FF9800;'>Burmes Cat</h3>", unsafe_allow_html=True)
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp3h22InvhCrmGBT4jVXM3f-5kJoCHZl2mDucWsUD9Z6lIJa7V",width=230)
  st.write("Burmese cats are cute")
with col1:
  st.markdown("<h3 style='color:#FF9800;'>Tom and Jerry</h3>", unsafe_allow_html=True)
  st.image("https://www.gifcen.com/wp-content/uploads/2021/09/tom-and-jerry-gif.gif")
  st.write("Tom and Jerry are best friends")
with col2:
  st.markdown("<h3 style='color:#FF9800;'>Tom and Jerry</h3>", unsafe_allow_html=True)
  st.video("https://www.youtube.com/watch?v=8WfMUqd4qH8&pp=ygUUdG9tIGFuZCBqZXJyeSB0ZWx1Z3U%3D")
  st.write("Tom and Jerry are best friends")
with col3:
  st.markdown("<h3 style='color:#FF9800;'>Tom and Jerry</h3>", unsafe_allow_html=True)
  st.video("https://www.youtube.com/watch?v=t0Q2otsqC4I&t=5s&pp=ygUUdG9tIGFuZCBqZXJyeSB0ZWx1Z3U%3D")
  st.write("Tom and Jerry are best friends")
