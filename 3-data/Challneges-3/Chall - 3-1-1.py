import pandas as pd
import streamlit as st
campus_students = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/delimited/campus-students.csv")
online_students = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/delimited/online-students.csv")

# Remember the lengths
campus_len = len(campus_students)
online_len = len(online_students)

# Concatenate
students = pd.concat([campus_students, online_students], ignore_index=True)

# Now assign types based on position
students['type'] = ['campus'] * campus_len + ['online'] * online_len