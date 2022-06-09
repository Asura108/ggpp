# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:08:50 2022

@author: Deep
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Deep/PythonProjectDeploying/Web_model.sav', 'rb'))

def func(input_D):
   
    new_parameters = np.array(input_D)
    new_parameters = new_parameters.reshape(1,5)
    
    new_prediction = loaded_model.predict(new_parameters)

    if (new_prediction[0]==0):
        return "JUDGING BY YOUR INPUTS I WOULD SAY THAT YOU WONT CLICK ON THE ADVERTISEMENT"
    else:
        return "YOU WILL CLICK ON MY ADVERTISEMENT SIRE!"
    
    
    
    
def main():
    #giving a title 
    st.title("Advertisement prediction of click")
    
    #getting input data from the user using the website
    DTSS = st.text_input("Please enter the Daily Time Spent on Site = ")
    Age = st.text_input("Please enter your age = ")
    AreaInc = st.text_input("Please enter the Area income = ")
    DIU = st.text_input("Please enter your Daily Internet Usage = ")
    Gender = st.text_input("Please state your gender [1 for male and 0 for female] = ")
   
   
    
    #code for prediction
    new_list = [DTSS,Age,AreaInc,DIU,Gender]
    diagnosis = ''
    
    #creating a button 
    if st.button("SHOW ME THE RESULTS!"):
        diagnosis = func(new_list)
        

        
    st.success(diagnosis)
    
    
    
    
    
    
if __name__ == '__main__':
    main()