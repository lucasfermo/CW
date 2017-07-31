import math,os, sys,random,time,turtle,operator
import datetime

def generate_bc(url,separator):
    crumbList=[]
    extension=["html","html","php","asp","index","www","https,pi,&,="]
    for i in range(len(url)):
        if url[i] =="/":
            start=i+1
            temp=""
            for j in range(i+1,len(url)):
                if j==len(url)-1:
                    temp+=url[j]
                    if temp not in extension:
                        crumbList.append(temp)

                elif url[j].isalpha() or url[j]=="-":
                    temp+=url[j]
                elif url[j]=="/":
                    if temp not in extension:
                        crumbList.append(temp)
                    break

                else:
                    if temp not in extension:
                        crumbList.append(temp)
                    break

    words=["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    for i in range(len(crumbList)):
        if len(crumbList[i])==0:
            crumbList.pop(i)
    if len(crumbList)==0:
        final="<span class='active'>HOME</span>"
    else:
        final='<a href="/">HOME</a> {} '.format(separator)

    directory=""
    for i in range(len(crumbList)):
        if i==len(crumbList)-1 and len(crumbList)!=1:
            if len(crumbList[i])>29:
                temp=crumbList[i].split("-")
                for k in words:
                    if k in temp:
                        temp.remove(k)

                acr=""
                for j in range(len(temp)):
                    acr+=temp[j][0].upper()
                final+="<a href='{}/{}/'>{}</a>{}".format(directory,crumbList[i],
                acr,separator)
                directory+="/"+crumbList[i]+""
            else:
                final+="<span class='active'>{}</span>".format(crumbList[i].upper())
        else:
            if len(crumbList[i])>0 and len(crumbList[i])<=29:
                final+="<a href='{}/{}/'>{}</a>{}".format(directory,crumbList[i],
                crumbList[i].upper(),separator)
                directory+="/"+crumbList[i]+""
            if len(crumbList[i])>29:
                temp=crumbList[i].split("-")
                for k in words:
                    if k in temp:
                        temp.remove(k)
                acr=""
                for j in range(len(temp)):
                    acr+=temp[j][0].upper()
                final+="<a href='{}/{}/'>{}</a>{}".format(directory,crumbList[i],
                acr,separator)
                directory+="/"+crumbList[i]+""
    final=final.replace(" ","")
    return final


print(generate_bc("https://www.twitter.de",  ">>>"))
