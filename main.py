import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
import datetime

import copy


uploaded_files = st.file_uploader(
    "アップロードする順番で世代数が決まります。",
    type="csv",
    accept_multiple_files=True,
)

if st.button('実行', key='execute', help='処理を実行します。'):
    if uploaded_files is not None:
        #*data
        root: str = os.getcwd()
        os.chdir("fastapi")
        shutil.rmtree("data")
        os.makedirs(root + "\\fastapi\\data\\", exist_ok=False)
        #仮
        uploaded_files_1 = copy.deepcopy(uploaded_files)
        for i, file in enumerate(uploaded_files_1):
            df: pd.DataFrame = pd.read_csv(file)
            generation_dir_path: str = root + "\\fastapi\\data\\" + str(i+1)
            os.makedirs(generation_dir_path, exist_ok=False)
            #* 取得
            st.write(os.getcwd())
            os.chdir("data")
            os.chdir(str(i+1))
            for i in range(df.shape[0]):
                data: pd.Series = df.iloc[i]

                plt.figure()
                df.plot()
                img_name: str = str(i+1) + ".svg"
                plt.rcParams["svg.fonttype"] = "none"
                plt.savefig(img_name, format="svg")
                plt.close("all")

                st.write(data)
            os.chdir("../../")
            #* 取得
            st.write(os.getcwd())
        os.chdir("../")
        #* 取得
        st.write(os.getcwd())

        #*archive
        # root: str = os.getcwd()
        time_dir = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        dir_path = root + "\\fastapi\\archive\\" + time_dir
        os.makedirs(dir_path, exist_ok=False)
        #仮
        uploaded_files_2 = copy.deepcopy(uploaded_files)
        for i, file in enumerate(uploaded_files_2):
            df: pd.DataFrame = pd.read_csv(file)
            generation_dir_path: str = dir_path + "\\" + str(i+1)
            os.chdir("fastapi")
            os.makedirs(generation_dir_path, exist_ok=False)
            os.chdir("archive")
            os.chdir(time_dir)
            os.chdir(str(i+1))
            for i in range(df.shape[0]):
                data: pd.Series = df.iloc[i]

                plt.figure()
                df.plot()
                img_name: str = str(i+1) + ".svg"
                plt.rcParams["svg.fonttype"] = "none"
                plt.savefig(img_name, format="svg")
                plt.close('all')

                st.write(data)
            os.chdir("../../../../")
        ##########################################################
        #*data
        root: str = os.getcwd()
        os.chdir("plumber")
        shutil.rmtree("data")
        os.makedirs(root + "\\plumber\\data\\", exist_ok=False)
        #仮
        uploaded_files_3 = copy.deepcopy(uploaded_files)
        for i, file in enumerate(uploaded_files_3):
            df: pd.DataFrame = pd.read_csv(file)
            generation_dir_path: str = root + "\\plumber\\data\\" + str(i+1)
            os.makedirs(generation_dir_path, exist_ok=False)
            #* 取得
            st.write(os.getcwd())
            os.chdir("data")
            os.chdir(str(i+1))
            for i in range(df.shape[0]):
                data: pd.Series = df.iloc[i]

                plt.figure()
                df.plot()
                img_name: str = str(i+1) + ".svg"
                plt.rcParams["svg.fonttype"] = "none"
                plt.savefig(img_name, format="svg")
                plt.close("all")

                st.write(data)
            os.chdir("../../")
            #* 取得
            st.write(os.getcwd())
        os.chdir("../")
        #* 取得
        st.write(os.getcwd())

        #*archive
        # root: str = os.getcwd()
        time_dir = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        dir_path = root + "\\plumber\\archive\\" + time_dir
        os.makedirs(dir_path, exist_ok=False)
        for i, file in enumerate(uploaded_files):
            df: pd.DataFrame = pd.read_csv(file)
            generation_dir_path: str = dir_path + "\\" + str(i+1)
            os.chdir("plumber")
            os.makedirs(generation_dir_path, exist_ok=False)
            os.chdir("archive")
            os.chdir(time_dir)
            os.chdir(str(i+1))
            for i in range(df.shape[0]):
                data: pd.Series = df.iloc[i]

                plt.figure()
                df.plot()
                img_name: str = str(i+1) + ".svg"
                plt.rcParams["svg.fonttype"] = "none"
                plt.savefig(img_name, format="svg")
                plt.close('all')

                st.write(data)
            os.chdir("../../../../")
