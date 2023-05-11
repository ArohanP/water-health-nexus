import streamlit as st

st.title('Water Quality App')
def industry_details():

    def handle_inputs(k1,k2):
        ind_name=st.text_input('Please enter the name of the industry',key=k1)
        st.write('First Line executed')
        ind_type = st.text_input('Please enter the type of the industry',key=k2)
        inputs[f'{ind_name}'] = ind_type
        inputs
    st.write('Please enter the details of the industries present in the vicinity of the region')
    inputs={}
    
    
    # Add any other content you want for this page
    
def farming_details():
    st.title("Please enter the details of the industries surrounding the region")
    # Add any other content you want for this page

# Define the pages of the app
pages = {
    "Industry": industry_details,
    "Farming": farming_details
}

# Add a dropdown menu to the sidebar to allow users to switch between pages
page = st.sidebar.selectbox("Select a page", tuple(pages.keys()))

# Call the function corresponding to the selected page
pages[page]()

