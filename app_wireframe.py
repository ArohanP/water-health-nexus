import streamlit as st
import pandas as pd
### Global Variables ------
industry_details={} ## 
### Functions ------
#1) farming
#2) industry_questionaire
#3) water_quality
#4) if_industry_present
#5) industry
def random_pieces_of_codes():
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
    pass

def farming():
    st.write("Please enter the details of farming practises surrounding the region")
    # Add any other content you want for this page
def industry_questionaire():
    st.write('Please answer the following questionaire')
def water_quality():
    st.write(f'The function id of this function is {id(water_quality)}')
    st.write('Please enter the details of the water quality parameters')
    is_dataset = st.radio('Do you have the data documented in an excel or csv format?',['Yes','No'],key='is_dataset present?')
    if is_dataset == 'Yes':
        uploaded_dataset = st.file_uploader('Please upload your dataset here', key='file_uploader')
    else:
        total_datapoints=st.number_input('How many samples have you analysed?',step=1)
        parameters={'Turbidity':0,'Iron':0,'Alkalinity':0,'Chloride':0,'Hardness':0,'pH':0,'Fluoride':0,'Nitrate':0,'Nitrite':0,'Ammonia':0,'Phosphate':0,'Calcium':0,'Magnesium':0}
        parameter_BIS_standards={'Turbidity':1,'Iron':0.3,'Alkalinity':200,'Chloride':250,'Hardness':200,'pH':'To be determined','Fluoride':1,'Nitrate':45,'Nitrite':'To be determined','Ammonia':0.5,'Phosphate':'TO be determined','Calcium':75,'Magnesium':30}
        #st.write('Please list the parameters that you have measured (Select all that apply)')
        options=['Turbidity','Iron','Alkalinity','Chloride','Hardness','pH','Fluoride','Nitrate','Nitrite','Ammonia','Phosphate','Calcium','Magnesium','Conductivity']
        params_measured=[]
        key_counter=0
        def multiselect_fun(key_counter):
            parameters_measured = st.multiselect('Please select the water quality parameters that you have measured (Select all that apply and press enter when you are done selecting)',options,key=str('param_options'+str(key_counter)))
            params_measured.append(parameters_measured)
        multiselect_fun(key_counter)
        params_measured=params_measured[0]
        if st.button('Enter',key=str('button'+str(key_counter))):
            for param in parameters.keys():
                if param in params_measured:
                    parameters[f'{param}']=1
            params_print = ', '.join(i for i in params_measured)
            
            st.write(f'The parameters that have been measured are **{params_print}**')
            
            if 'pH' in params_measured:
                params_measured.remove('pH')
                st.write('**The pH level should be between x1 and x2 levels for a healthy water body.**')
            Acceptable_limits = [parameter_BIS_standards[param] for param in params_measured]
            BIS_data=pd.DataFrame({'Parameters':params_measured,'Acceptable limits':Acceptable_limits})
            BIS_data.index=range(1,len(BIS_data)+1)
            st.table(BIS_data)
            key_counter+=1    
            options=['Enter the data for each parameter manually','For each parameter give the number of data points above the acceptable limit']
            determine_percentage=st.radio('We need to determine the percentage of these parameters that are above the acceptable limit. How do you want to do it?',options,key='determine_percentage')
            if determine_percentage=='Enter the data for each parameter manually':
                param_values={}
                def get_value(param,key_counter):
                    num_input=st.number_input(f'Please enter the value of {param}',key=str(param+'_'+str(key_counter)))
                    return num_input
                count=1
                for param in params_measured:
                    print(count)
                    st.write('**The for loop is starting now**')
                    count+=1
                    param_values[f'{param}']=[]
                    key_counter=0
                    while True:
                        print(key_counter)
                        st.write('**The while loop is starting now**')
                        param_values[f'{param}'].append(get_value(param,key_counter))
                        st.write(f'{id(water_quality)}')
                        st.write('**Entering into the if statement**')
                        if st.button('Add More',key=str('Add more'+param+str(key_counter))):
                            key_counter+=1
                            continue
                        else:break
                print(param_values)
                param_percentage_above_limit={}
                for i in param_values.keys():
                    count=0
                    for j in param_values[param]:
                        if j>parameter_BIS_standards[param]:count+=1
                    param_percentage_above_limit[param]=(count/total_datapoints)*100
                    st.write(f'The percentage of {param} above the acceptable limit is {param_percentage_above_limit[param]}')
                
                    



        # A=set(measured_parameters).intersection(set(parameters.keys()))
        # for param in A:
        #     parameters[f'{param}']=1
        # for param in parameters.keys():
        #     if parameters[f'{param}']==1:
        #         st.write(f'The water qualities that have been measured are {param}')

        # st.write(f'Measured parameters are {A}')
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
     
st.header('Agri-Industry-Water-Health Application')
is_water_testing = st.radio('Is water quality testing done?',('Yes','No'),key="is_water_testing")
if is_water_testing=='Yes':
    water_quality()
    st.write(f'printing when the function exits {id(water_quality)}')
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

