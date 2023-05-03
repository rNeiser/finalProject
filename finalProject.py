import streamlit as st
import pydeck as pdk
import pandas as pd
import random as rd
pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.width', None, 'max_colwidth', None)

"""
Name:       Ryan Neiser
CS230:      Section 5
Data:       RollerCoasters Geo
URL:        Link to your web application on Streamlit Cloud (if posted) 

Description:    

This program ... (List all the features you included)
"""
def readDataList():
    r_file = open("RollerCoasters-Geo.csv", "r")
    line_list = r_file.readlines()
    r_file.close()
    return line_list

def readDataPandas():
    df_all_data = pd.read_csv("RollerCoasters-Geo.csv")
    return df_all_data

def main():
    dataList = readDataList()
    ogDF = readDataPandas()
    print(ogDF)

main()