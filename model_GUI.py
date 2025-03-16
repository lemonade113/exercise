# -*- coding: utf-8 -*-
import streamlit as st
import time
import pandas as pd
import joblib
from PIL import Image
import pandas as pd
import plotly.express as px
# 设置网页标题，以及使用宽屏模式
st.set_page_config(
    page_title="心脏病预测",
    layout="wide"

)

# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 左边导航栏
sidebar = st.sidebar.radio(
    "导航栏",
    ("首页", "数据挖掘一览", "模型分析", "预测")
)
if sidebar == "数据挖掘一览":
    st.title("数据可视化图")
    # 项目选择框
    project_name = st.selectbox(
        "请选择您要查看的属性",
        ["心脏病和心绞痛类型之间的关系","心脏病与年龄和最大心率的关系",
         '血压-患病关系','年龄-患病情况','运动引起的心绞痛-心率-患病关系']
    )
    
    
    
    if project_name=="心脏病和心绞痛类型之间的关系":
        image = Image.open('D:\\心脏病和心绞痛类型之间的关系.png')
        st.image(image, use_column_width=True)
    if project_name=="心脏病与年龄和最大心率的关系":
        image = Image.open('D:\\心脏病与年龄和最大心率的关系.png')
        st.image(image, use_column_width=True)
    if project_name=="血压-患病关系":
        st.text('target0表示未患病，target1表示患病')
        image = Image.open('D:\\血压-患病关系.png')
        st.image(image, use_column_width=True)
    if project_name=="年龄-患病情况":
        st.text('target0表示未患病，target1表示患病')
        image = Image.open('D:\\年龄-患病情况.png')
        st.image(image, use_column_width=True) 
    if project_name=="运动引起的心绞痛-心率-患病关系":
        st.text('target0表示未患病，target1表示患病')
        image = Image.open('D:\\运动引起的心绞痛-心率-患病关系.png')
        st.image(image, use_column_width=True) 
    
    
elif sidebar == "模型分析":
    st.title("模型分析")
    st.header("模型综合分析")
    st.write("本系统运用SVM分类器，选用900多个数据，经过训练与分析，得到如下结果")
    st.header("模型性能如下：")
    st.write("支持向量机的准确率: 0.83")
    st.write("交叉验证的平均值: 0.78")
    st.write("精准率: 0.79")
    st.write("召回率: 0.89")
    st.write("F1-score综合指标: 0.84")
    
    col1, col2 = st.columns([1, 1.3])
    with col1:
        col1.subheader("混淆矩阵")
        image = Image.open('D:\混淆矩阵.png')
        st.image(image)
    
    with col2:
        col2.subheader("精确率和召回率")
        image = Image.open('D:\精确率和召回率.png')
        st.image(image)
        
elif sidebar == "预测":
    st.title("预测")
    x = st.text_input("请输入胸部疼痛情况（1：典型心绞痛；2：非典型心绞痛；3：没有心绞痛；4：无症状）")
    #induced_angina= st.number_input("请输入运动诱发心绞痛情况（1：yes；0：no）")
    #thal=st.number_input("请输入一种血液疾病情况（3：正常；6：固定缺陷；7：可逆的缺陷）")
    #st.write("0：未患病  1：患病")
   # 点击提交按钮
    if st.button("Submit"):
       # 引入训练好的模型
       model=joblib.load("F:\\桌面\\rf.pkl")
       # 转换成DataFrame格式的数据
       
    
       # 获取预测出来的值
       prediction = model.predict(x)[0]
       
       st.text(f"您的预测患病情况是：{prediction}")
       
else:
    
    image = Image.open('D:\\1.png')
    st.image(image, use_column_width=True)
    st.title("心脏病预测")
    
    
    