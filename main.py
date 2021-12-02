from flask import Flask, render_template , request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine=pp.init() #.init func call & return engine module
voices=engine.getProperty('voices') #all voices at voices
print(voices)
engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word) #speak sentence
    engine.runAndWait()


#pyttsx3 for chatbot speak
bot = ChatBot("My Bot")
convo = {
     'hello',
     'hii there!',
     'What is your name?',
     'I am you assistant how may I help you ',
     'how are you?',
     'I am doing great these days',
     'thankyou',
     'In which city you live ?',
     'I live in cloud , I hope you are happy with me',
     'Which language you talk?',
     'I mostly talk in english',
 }

trainer=ListTrainer(bot)#trainer obj
# now training the bot with the help of trainer
#
trainer.train(convo)
# answer= bot.get_response("Which language you talk")
# print(answer)

# print("talk to bot")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)
#start make window.......
main =Tk()

#set the hight and width of window
main.geometry("500x650")

#name of bot
main.title("My chat bot")

#icon of chatbot
img = PhotoImage(file="bot.png")#obj of img
photoL = Label(main, image=img)#obj of photo
photoL.pack(pady = 5)#pack label


#Take query : It takes audio as input frome user and converts it to string....
def takeQuery():
    sr = s.Recognizer() #making a obj of our own recognition
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
         try:
             audio = sr.listen(m)
             query = sr.recognize_google(audio, language='eng-in')
             print(query)
             textF.delete(0, END)
             textF.insert(0, query)
             ask_from_bot()
         except Exception as e:
             print(e)
             print("not recognized")

#make a func for command
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you :" + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot: " + str(answer_from_bot))
    speak(answer_from_bot)

    textF.delete(0,END)
    msgs.yview((END))

frame = Frame(main)#frame class take main window of chatbot

sc = Scrollbar(frame)
msgs = Listbox(frame,width=80, height=20,yscrollcommand=sc.set)#obj of listbox into msgs variable

#for scrollbar
sc.pack(side=RIGHT ,fill=Y)
msgs.pack(side=LEFT, fill=BOTH,pady=10)

frame.pack()#for packing frame

#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady = 10)

#creating button in text field
btn=Button(main,text="Ask from bot",font=("Verdana",20),command = ask_from_bot)
btn.pack()


#creating a function for put message to hit enter
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key.....
main.bind('<Return>',enter_function)


def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
main.mainloop()
