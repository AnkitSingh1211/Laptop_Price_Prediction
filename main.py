import streamlit as st
import pickle
#import sklearn
#import xgboost
import pandas as pd
import numpy as np


pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')

company=st.selectbox('Company',df['Company'].unique())
types=st.selectbox('Laptop Type',df['TypeName'].unique())

ram=st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])


weight=st.number_input('Laptop Weight')

touchscreen=st.selectbox('Touchscreen',['No','Yes'])


ips=st.selectbox('IPS',['No','Yes'])

screen_size=st.number_input('Screen Size')

Resolution=st.selectbox('Screen Resolution',['960×540',
'1280×720',

	'2048×1080',
	'2560×1440',
	'3840×2160 ',
	'4096×2160 ',
	'5120×2880 ',
	'7680×4320' ])

cpu=st.selectbox('CPU Brand',(df['cpu brand'].unique()))

hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu=st.selectbox('GPU',df['Gpu brand'].unique())



os=st.selectbox('OS',df['OS' ].unique())

if st.button('Predict Price'):
    if touchscreen=='Yes':
        touchscreen=1
    elif touchscreen=='No':
        touchscreen=0
    if ips=='Yes':
        ips=1
    elif ips=='No':
        ips=0
    if screen_size==0.00:
        st.write('Screen Size Should Not be Zero')

    else:
        x=Resolution.split('×')[0]
        y=Resolution.split('×')[1]
        ppi=((((int(x))**2)+((int(y))**2))**0.5)/screen_size
        query=np.array([company,types,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os],dtype='object')
        query=query.reshape(1,12)
        st.title('Price of this Configuration:')
        st.title(int(np.exp(pipe.predict(query)[0])))
