import streamlit as st
def farming():
    st.write("Please enter the details of farming practises surrounding the region")
    # Add any other content you want for this page
industry_details={}
def industry_questionaire():
    st.write('Please answer the following questionaire')
def water_quality():
    st.write('Please enter the details of the water quality parameter')
def if_industry_present(ind_num):
    ind_name = st.text_input('Please enter the name of the industry',key='ind_name'+str(ind_num))
    industry_details[f'{ind_name}']={}
    ind_dist=st.number_input('Please enter the distance of this industry from area centre',key='ind_dist'+str(ind_num))
    industry_details[f'{ind_name}']['distance']=ind_dist
    is_ind_type = st.radio('Do you know the type of the industry?',['Yes','No'],key='ind_type'+str(ind_num))
    if is_ind_type=='Yes':
        ind_type = st.text_input('Please enter the type of the industry',key='enter_text'+str(ind_num))
        industry_details[f'{ind_name}']['Type']=ind_type
    else:
        pass
    is_waste_water = st.radio('Is this industry throwing its waste water in the water body surrounding the region',('Yes','No'),key="is_waste_water"+str(ind_num))
    if is_waste_water=='Yes':
        is_waste_water_testing = st.radio('Has the waste been tested?',('Yes','No'),key="is_wste_water_testing"+str(ind_num))
        if is_waste_water_testing=='Yes':
                industry_questionaire()
        else:
            if is_ind_type=='Yes':
                st.write(f'Since the type of the industry is {ind_type}, we can suggest that the water would be high in X which will lead to Y percent increase in disease Z')
            else:
                st.write('For now we cannot give any assessment without the information of either industry type or the composition of waste water.')
    else:
        st.write('In that case, it is highly improbable that this industry is contributing significantly to the water quality in the region')
def industry():
    st.write('Please enter the details of the industries surrounding the region')
    is_industry_present = st.radio('Are there industries present in the vicinity of the region?',['Yes','No'],key="is_industry_present")
    if is_industry_present=='No':
        st.write('Clearly industry is not affecting the water quality in the region, so lets visit the details of the farming practises.')
        farming()
    else:
        ind_num=1
        while True:
            if_industry_present(ind_num)
            if st.button('Add More',key="While_loop"+str(ind_num)):
                ind_num+=1
                continue
            else:
                break
    # else:
    #     ind_num = st.number_input('How many industries are present in the vicinity of the area?',step=1,key="ind_num")
    #     industry_details={}
    #     counter=1
    #     while ind_num:
    #         st.markdown(f"#### Please enter the details of industry {counter}")
    #         ind_name = st.text_input('Please enter the name of the industry',key='ind_name'+str(ind_num))
    #         industry_details[f'{ind_name}']={}
    #         ind_dist=st.number_input('Please enter the distance of this industry from area centre',key='ind_dist'+str(ind_num))
    #         industry_details[f'{ind_name}']['distance']=ind_dist
    #         is_ind_type = st.radio('Do you know the type of the industry?',['Yes','No'],key='ind_type'+str(ind_num))
    #         if is_ind_type=='Yes':
    #             ind_type = st.text_input('Please enter the type of the industry',key='enter_text'+str(ind_num))
    #             industry_details[f'{ind_name}']['Type']=ind_type
    #         else:
    #             pass
    #         is_waste_water = st.radio('Is this industry throwing its waste water in the water body surrounding the region',('Yes','No'),key="is_waste_water"+str(ind_num))
    #         if is_waste_water=='Yes':
    #             is_waste_water_testing = st.radio('Has the waste been tested?',('Yes','No'),key="is_wste_water_testing"+str(ind_num))
    #             if is_waste_water_testing=='Yes':
    #                 industry_questionaire()
    #             else:
    #                 if is_ind_type=='Yes':
    #                     st.write(f'Since the type of the industry is {ind_type}, we can suggest that the water would be high in X which will lead to Y percent increase in disease Z')
    #                 else:
    #                     st.write('For now we cannot give any assessment without the information of either industry type or the composition of waste water.')
    #         else:
    #             st.write('In that case, it is highly improbable that this industry is contributing significantly to the water quality in the region')
    #         ind_num-=1 
    #         counter+=1  
st.header('Agri-Industry-Water-Health Application')
is_water_testing = st.radio('Is water quality testing done?',('Yes','No'),key="is_water_testing")
if is_water_testing=='Yes':
    water_quality()
else:
    pages = {
    "Industry": industry,
    "Farming": farming
    }
    # Add a dropdown menu to the sidebar to allow users to switch between pages
    page = st.sidebar.selectbox("Select a page", tuple(pages.keys()))

    # Call the function corresponding to the selected page
    pages[page]()




# Add any other content you want for this page
    

# Define the pages of the app

