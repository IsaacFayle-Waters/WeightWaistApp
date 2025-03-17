import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

#Import data and convert datetime
df = pd.read_csv('weight_loss_waist_size.csv')
df_weights_only = pd.read_csv('weight_loss_only.csv')
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y',errors='coerce')
df_weights_only['date'] = pd.to_datetime(df_weights_only['date'], format='%d/%m/%y',errors='coerce')

#Title
st.title("Zak's Waist and Weight Tracker")

#Weight calcs
height_m = 1.8034
start_kg = 107.4
current_kg = df_weights_only['weight_kg'].iloc[-1]
st_mod = 6.35029
current_st = current_kg / st_mod
total_kg_loss = start_kg - current_kg
total_st_loss = total_kg_loss / st_mod
#bmi
bmi = current_kg / (height_m * height_m)
start_bmi = start_kg /(height_m * height_m)

info_string = f'''## I am currently {current_kg}kg, which is {current_st:.2f} stone.
So, I have **lost {total_kg_loss:.2f}kg** since 24/01/2025, which is **{total_st_loss:.2f} stone**.  
_My BMI is {bmi:.1f}, down from a BMI of {start_bmi:.1f}._'''
st.markdown(info_string)

#plt.figure(figsize=(8,8))
fig,ax1 = plt.subplots(figsize=(8,8))

#Waist plot
sns.lineplot(data=df, x='date', y='waist_cm',ax=ax1, color='tab:red')#, label='Waist size(cm)')
ax1.set_ylabel('Waist size(cm)', color='tab:red')
ax1.tick_params(axis='y',labelcolor='tab:red')

#Weight plot
ax2 = ax1.twinx()
sns.lineplot(data=df_weights_only, x='date', y='weight_kg',ax=ax2,color = 'tab:blue')#, label='Weight(kg)')
ax2.set_ylabel('Weight(kg)', color = 'tab:blue')
ax2.tick_params(axis='y',labelcolor='tab:blue')

#Cosmetics
fig.autofmt_xdate()
plt.title('Weight-loss and Slimming Progression')
plt.subplots_adjust(bottom=0.2)
#plt.show()
st.pyplot(fig)

#Update info
last_weight_update = df_weights_only['date'].iloc[-1].date()
last_waist_update = df['date'].iloc[-1].date()

update_string = f'''_Weight last updated: {last_weight_update}. 
Waist measurement last updated: {last_waist_update}._'''
st.write(update_string)