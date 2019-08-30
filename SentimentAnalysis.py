# -*- coding: utf-8 -*-
"""
Anne Marie Pruett
"""
import numpy as np
import matplotlib.pyplot as mplot
import csv as csv
import collections

#read csv lexicon and create a dictionary named lex with words and their scores
#take out null values
read = csv.reader(open('sentiment_lex.csv'))

lex={row[0]:row[1:] for row in read if row and row[0]}



#initialize dictionaries wordList and wordCount
wordList={}
wordCount={}
#list of a series list and a list of b series scripts
aScripts=("a101script.txt","a102script.txt","a103script.txt","a104script.txt",
          "a105script.txt","a106script.txt","a107script.txt","a108script.txt",
          "a109script.txt","a110script.txt","a111script.txt","a112script.txt",
          "a113script.txt","a114script.txt","a115script.txt","a116script.txt",
          "a117script.txt","a118script.txt","a119script.txt","a120script.txt",
          "a121script.txt","a122script.txt")
bScripts=("bg101script.txt","bg102script.txt","bg103script.txt","bg104script.txt",
         "bg105script.txt","bg106script.txt","bg107script.txt","bg108script.txt",
         "bg109script.txt","bg110script.txt","bg111script.txt","bg112script.txt",
         "bg113script.txt")

#go through all a series scripts and take out punctuation and numbers 
data2=[]
wordCount=collections.Counter()
for filename in aScripts:
    file=open("data_ch2/"+filename,"r")
    data=file.read()
    data=data.replace("\n"," ")
    data=data.replace("."," ")
    data=data.replace(","," ")
    data=data.replace("?"," ")
    data=data.replace("!"," ")
    data=data.split(" ")
    for d in data:
        if d.isdigit()==False:
            data2.append(d.lower())
#get count of remaining words and make dictionary of words and their counts
    wordList=collections.Counter(data2)
#make copy of dictionary so can edit
wordCount=dict(wordList)
#if key is not in lex dictionary then delete from wordCount
for key in wordList.keys():
    if key not in lex.keys():
        del wordCount[key]

#create list to hold x and y values for first graph
x=[1,2,3,4,5]
y=[0,0,0,0,0]
#add all counts of words within certain interval of sentiment scores and make them y values
for key in wordCount.keys():
    if float(lex[key][0])<-0.6:#Neg Sentiment on bar graph
        y[0]=y[0]+int(wordCount[key])
    elif float(lex[key][0])<-0.2:#WNeg Sentiment on bar graph
        y[1]=y[1]+int(wordCount[key])
    elif float(lex[key][0])<0.2:#Nue Sentiment on bar graph
        y[2]=y[2]+int(wordCount[key])
    elif float(lex[key][0])<0.6:#WPos Sentiment on bar graph
        y[3]=y[3]+int(wordCount[key]) 
    else:#Ps Sentiment on bar graph
        y[4]=y[4]+int(wordCount[key])
 
#go through all a series scripts and take out punctuation and numbers        
data22=[]
wordCount2=collections.Counter()
for filename in bScripts:
    file=open("data_ch2/"+filename,"r")
    data2=file.read()
    data2=data2.replace("\n"," ")
    data2=data2.replace("."," ")
    data2=data2.replace(","," ")
    data2=data2.replace("?"," ")
    data2=data2.replace("!"," ")
    data2=data2.split(" ")
    for d in data2:
        if d.isdigit()==False:
            data22.append(d.lower())
#get count of remaining words and make dictionary of words and their counts
    wordList2=collections.Counter(data22)
#make copy of dictionary so can edit
wordCount2=dict(wordList2)
#if key is not in lex dictionary then delete from wordCount
for key in wordList2.keys():
    if key not in lex.keys():
        del wordCount2[key]


#create list to hold x2 and y2 values for second graph   
x2=[1,2,3,4,5]
y2=[0,0,0,0,0]
#add all counts of words within certain interval of sentiment scores and make them y2 values
for key in wordCount2.keys():
    if float(lex[key][0])<-0.6:#Neg Sentiment on bar graph
        y2[0]=y2[0]+int(wordCount2[key])
    elif float(lex[key][0])<-0.2:#WNeg Sentiment on bar graph
        y2[1]=y2[1]+int(wordCount2[key])
    elif float(lex[key][0])<0.2:#Nue Sentiment on bar graph
        y2[2]=y2[2]+int(wordCount2[key])
    elif float(lex[key][0])<0.6:#WPos Sentiment on bar graph
        y2[3]=y2[3]+int(wordCount2[key]) 
    else:#Pos Sentiment on bar graph
        y2[4]=y2[4]+int(wordCount2[key])
    
#make y and y2 log of y and y2 
y=np.log10(y) 
y2=np.log10(y2)
 

#ask user for input and save as variable
series=input("Enter series name:")
#print graph of selected series or message
if series=="a" or series=="A":
    mplot.bar(x,y)
    mplot.title("Sentiment Analysis Series A")     
    mplot.xticks(x,["Neg","WNeg","Nue","WPos","Pos"]) 
    mplot.xlabel("Sentiment")
    mplot.ylabel("log Word Count")
    mplot.show()
elif series=="b" or series=="B":
    mplot.bar(x2,y2)
    mplot.title("Sentiment Analysis Series B")
    mplot.xlabel("Sentiment")
    mplot.ylabel("log Word Count")
    mplot.xticks(x,["Neg","WNeg","Nue","WPos","Pos"]) 
    mplot.show()
else:
    Cprint("I only know shows a and b")



