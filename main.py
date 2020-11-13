import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import requests
import math as mt
import cv2
import pyautogui 
import time  
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


engine = pyttsx3.init('sapi5')

def speak(audio):
    print('Добби: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Доброе утро, хозяин!')

    if currentH >= 12 and currentH < 18:
        speak('Добрый день, хозяин!')

    if currentH >= 18 and currentH !=0:
        speak('Добрый вечер, хозяин!')

greetMe()

speak('Добби слушает твои указания')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Слушаю...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print('Хозяин: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Добби не понял, повтори')
        query = myCommand()

    return query
        

if __name__ == '__main__':

    while True:
        #получаем команду с микрофона и сразу ставим в нижний регистр
        query = myCommand();
        query = query.lower()

        
        
        #ютуб
        if 'открой youtube' in query or 'youtube' in query:
            speak('открываю')
            webbrowser.open('www.youtube.com')

        elif 'открой тренды youtube' in query:
            speak('открываю тренды')
            webbrowser.open('https://www.youtube.com/feed/trending')

        elif 'открой мои подписки youtube' in query or 'открой подписки youtube' in query:
            speak('открываю подписки')
            webbrowser.open('https://www.youtube.com/feed/subscriptions')
            
        elif 'открой библиотеку youtube' in query:
            speak('открываю библиотеку')
            webbrowser.open('https://www.youtube.com/feed/library')

        elif 'открой историю youtube' in query or 'что я последнее смотрел на youtube' in query or 'что я последнее смотрела на youtube' in query:
            speak('открываю историю')
            webbrowser.open('https://www.youtube.com/feed/history')

        elif 'открой мои видео в youtube' in query:
            speak('открываю ваши видео')
            webbrowser.open('https://www.youtube.com/feed/my_videos')

        elif 'открой мои покупки в youtube' in query:
            speak('открываю ваши покупки')
            webbrowser.open('https://www.youtube.com/feed/purchases')
            
        elif 'открой понравившиеся видео в youtube' in query:
            speak('открываю ваши понравившиеся видео')
            webbrowser.open('https://www.youtube.com/playlist?list=LLdg_gMmvyZBmkyOi50B7OTg')

        elif 'открой мой аккаунт youtube' in query:
            speak('открываю аккаунт')
            webbrowser.open('https://www.youtube.com/account')
            
        #гугл
        elif 'открой google' in query or 'google' in query:
            speak('открываю')
            webbrowser.open('www.google.co.in')

        elif 'открой google картинки' in query:
            speak('открываю')
            webbrowser.open('https://www.google.ru/imghp?hl=ru&tab=wi&ogbl')

        elif 'открой аккаунт google' in query:
            speak('открываю аккаунт')
            webbrowser.open('https://myaccount.google.com/')

        #инфоормацию по университету
        elif 'открой сайт политеха' in query or 'открой сайт политехничсекого университета' in query:
            speak('открываю сайт Политеха')
            webbrowser.open('https://www.spbstu.ru/')

        elif 'институты в политехе' in query or 'какие бывают институты в политехе' in query:
            speak('институт компьютерных наук и технологий, ')
            speak('институт прикладной математики и механики, ')
            speak('инженерно-строительный институт, ')
            speak('высшая школа техносферной безопасности, ')
            speak('институт энергетики, ')
            speak('университетский политехнический колледж, ')
            speak('гуманитарный институт, ')
            speak('институт промышленного менеджмента, экономики и торговли, ')
            speak('институт биомедицинских систем и биотехнологий, ')
            speak('институт физики, нанотехнологий и телекоммуникаций, ')
            
        elif 'открой расписание пар в институте компьютерных наук и технологий' in query:
            speak('открываю расписание в институте компьютерных наук и технологий')
            webbrowser.open('https://ruz.spbstu.ru/faculty/95/groups')

        elif 'открой расписание пар в институте прикладной математике и механике' in query:
            speak('открываю расписание в институте прикладной математике и механике')
            webbrowser.open('https://ruz.spbstu.ru/faculty/99/groups')

        elif 'открой расписание пар в инженерно-строительном институте' in query:
            speak('открываю расписание в инженерно-строительном институте')
            webbrowser.open('https://ruz.spbstu.ru/faculty/92/groups')

        elif 'открой расписание пар в высшей школе техносферной безопасности' in query:
            speak('открываю расписание в высшей школе техносферной безопасности')
            webbrowser.open('https://ruz.spbstu.ru/faculty/96/groups')
        
        elif 'открой расписание пар в институте энергетике' in query:
            speak('открываю расписание в институте энергетике')
            webbrowser.open('https://ruz.spbstu.ru/faculty/93/groups')

        elif 'открой расписание пар в университетском политехническом колледже' in query:
            speak('открываю расписание в университетском политехническом колледже')
            webbrowser.open('https://ruz.spbstu.ru/faculty/117/groups')

        elif 'открой расписание пар в гуманитарном институте' in query:
            speak('открываю расписание в гуманитарном институте')
            webbrowser.open('https://ruz.spbstu.ru/faculty/101/groups')

        elif 'открой расписание пар в институте промышленного менеджмента, экономики и торговли' in query:
            speak('открываю расписание в институте промышленного менеджмента, экономики и торговли')
            webbrowser.open('https://ruz.spbstu.ru/faculty/100/groups')

        elif 'открой расписание пар в институте биомедицинских систем и биотехнологий' in query:
            speak('открываю расписание в институте биомедицинских систем и биотехнологий')
            webbrowser.open('https://ruz.spbstu.ru/faculty/119/groups')

        elif 'открой расписание пар в институте физики, нанотехнологий и телекоммуникаций' in query:
            speak('открываю расписание в институте физики, нанотехнологий и телекоммуникаций')
            webbrowser.open('https://ruz.spbstu.ru/faculty/98/groups')

        elif 'открой сайт первокурсника' in query:
            speak('открываю сайт первокурсника')
            webbrowser.open('https://www.spbstu.ru/freshman/')

        elif 'открой информацию по общежитию' in query:
            speak('открываю ифнормацию по общежитию')
            webbrowser.open('https://www.spbstu.ru/freshman/dormitory/dormitory.html')

        elif 'открой информацию по банковским картам' in query:
            speak('открываю ифнормацию по банковским картам')
            webbrowser.open('https://www.spbstu.ru/freshman/card/card.html')

        elif 'открой информацию по собранию первокурсников' in query:
            speak('открываю ифнормацию по собранию')
            webbrowser.open('https://www.spbstu.ru/freshman/meeting/meeting.html')

        elif 'открой информацию по пропуску' in query:
            speak('открываю ифнормацию по пропуску')
            webbrowser.open('https://www.spbstu.ru/freshman/skip/skip.html')

        elif 'открой информацию по студенческому билету' in query:
            speak('открываю ифнормацию по студенческому билету')
            webbrowser.open('https://www.spbstu.ru/freshman/studentcard/studentcard.html')

        elif 'открой информацию для первокурсников' in query:
            speak('открываю ифнормацию для первокурсников')
            webbrowser.open('https://www.spbstu.ru/freshman/files/booklet_web.pdf')


            
        #почта
        elif 'открой почту' in query:
            speak('открываю')
            webbrowser.open('www.mail.ru')

        elif "как дела" in query or 'как ты' in query:
            stMsgs = ['Лучше всех', 'Все хорошо']
            speak(random.choice(stMsgs))

        elif 'ничего' in query or 'забей' in query or 'отдыхай' in query:
            speak('Буду ждать')
            speak('Пока')
            sys.exit()
           
        elif 'привет' in query or 'салам' in query:
            if 'привет' in query:
                speak('Привет')
            else:
                speak('Салам алейкум, хозяин')

        #вконтакте
        elif 'войти вконтакт' in query:
            speak('Напиши логин')
            login_ = str(input())
            speak('Напиши пароль')
            password_ = str(input())
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)            
            driver.get ('https://www.vk.com/login')            
            driver.find_element_by_id('email').send_keys(login_)
            driver.find_element_by_id('pass').send_keys(password_)
            driver.find_element_by_id('login_button').click()
            isContinue = True            
            while driver.find_elements_by_xpath("//*[@id='login_message']/div/div"):
                driver.find_element_by_id('email').clear()
                speak('Не удаётся войти. Попробовать снова?')
                answer = myCommand();
                answer = answer.lower()
                if answer == 'да' or answer == 'конечно':
                    speak('Напиши логин')
                    login_ = str(input())
                    speak('Напиши пароль')
                    password_ = str(input())            
                    driver.find_element_by_id('email').send_keys(login_)
                    driver.find_element_by_id('pass').send_keys(password_)
                    driver.find_element_by_id('login_button').click()
                else: 
                    isContinue = False
                    driver.quit()
                    break
            if isContinue == True:
                speak('Напиши код')
                code_ = str(input())            
                code = driver.find_element_by_id('authcheck_code')
                code.send_keys(code_)
                button = driver.find_element_by_id('login_authcheck_submit_btn')
                button.click()
                while driver.find_element_by_id('login_authcheck_submit_btn'):
                    speak('Неверный код. Попробовать снова?')
                    answer = myCommand();
                    answer = answer.lower()
                    if answer == 'да' or answer == 'конечно':
                        code.clear()
                        speak('Напиши код')
                        code_ = str(input())            
                        code.send_keys(code_)
                        button.click()    
                    else: 
                        driver.quit()
                        break

        #одноклассники
        elif 'войти в одноклассники' in query:
            speak('Напиши логин')
            login_ = str(input())
            speak('Напиши пароль')
            password_ = str(input())
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)            
            driver.get ('https://ok.ru/')            
            driver.find_element_by_id('field_email').send_keys(login_)
            driver.find_element_by_id('field_password').send_keys(password_)
            driver.find_element_by_xpath('//*[@id="anonymPageContent"]/div[2]/div/div[3]/form/div[5]/div[1]/input').click()
            #isContinue = True            
            while driver.find_elements_by_xpath('//*[@id="anonymPageContent"]/div[2]/div/div[3]/form/div[3]/div'):
                driver.find_element_by_id('field_email').clear()
                speak('Не удаётся войти. Попробовать снова?')
                answer = myCommand();
                answer = answer.lower()
                if answer == 'да' or answer == 'конечно':
                    speak('Напиши логин')
                    login_ = str(input())
                    speak('Напиши пароль')
                    password_ = str(input())           
                    driver.find_element_by_id('field_email').send_keys(login_)
                    driver.find_element_by_id('field_password').send_keys(password_)
                    driver.find_element_by_xpath('//*[@id="anonymPageContent"]/div[2]/div/div[3]/form/div[5]/div[1]/input').click()
                else: 
                    #isContinue = False
                    driver.quit()
                    break


        #скриншот
        elif 'скрин' in query:
            pyautogui.screenshot('image.png')

        #включает камеру и делает фотку (фото сохраняется в папке с Добби)
        elif 'сделай фото' in query:
            cap = cv2.VideoCapture(0)
            for i in range(30):
                cap.read()  
            ret, frame = cap.read()
            cv2.imwrite('cam.png', frame)   
            cap.release()
            
        #создает папку по указанному пути(главное без ошибок)
        elif 'создай папку' in query:
            speak('Напиши путь')
            a = str(input())
            speak('Как назвать папку')
            b = str(input())
            way = a+b
            os.mkdir(way)
            speak('Сделано')
            
        #удалить папку
        elif 'удали папку' in query:
            speak('Напиши путь')
            a = str(input())
            os.rmdir(a)
            speak('Сделано')

        #время
        elif 'который час' in query or 'время' in query:
            d = datetime.datetime.today()
            res = str(d.hour) + " " + str(d.minute)
            speak(res)

        #дата
        elif 'какое сегодня число' in query or 'дата' in query:
            d = datetime.datetime.today()
            res = str(d.day)
            speak(res)
            
        #создать файл
        elif 'создай файл' in query:
            end_ = '.txt'
            speak('Скажи какой формат?')
            speak('Автоматически стоит формат txt, чтобы был докс скажи один')
            answer = myCommand();
            answer = answer.lower()
            if answer == '1':
                end_ = '.docx'
            speak('Напиши путь')
            s = str(input())
            speak('Как назвать?')
            name = myCommand();
            name = name.lower()
            s+=name+end_
            file = open(s,"w")
            file.close()
            speak('Готово')


        elif 'открой тренды youtube' in query:
            webbrowser.open('www.youtube.com/feed/trending')
        #заполнить файл
        elif 'заполни файл' in query:
            speak('Что написать?')
            text = myCommand();
            speak('В какой файл записать?')
            way = str(input())
            file = open(way, "w")
            file.write(text)
            file.close()
            speak('Записал')

        #удалить файл
        elif 'удали файл' in query:
            speak('Укажи путь')
            way = str(input())
            size_ = os.path.getsize(way)
            if size_== 0:
                os.remove(way)
            else:
                speak('Файл не пустой, уверен?')
                answer = myCommand();
                answer = answer.lower()
                if answer == 'да' or answer == 'конечно':
                    os.remove(way)
                    speak('Закончил')
                else:
                    speak('Правильно, лучше оставить')
            
        #калькулятор
        elif 'посчитай' in query:
            speak('Скажи выражение')
            expression = myCommand()
            expression = expression.lower()
            #корень
            if expression.startswith('корень из'):
                newExp = expression.replace('корень из', '')
                newExp.strip()
                answer = mt.sqrt(int(newExp))
                speak(str(answer))
            #возведение в степень    
            elif expression.startswith('возведи'):
                newExp = expression.replace('возведи','')
                newExp = newExp.replace('число','')
                newExp = newExp.replace('в','')
                newExp = newExp.replace('степень','')
                newExp = newExp.replace('степени','')
                newExp = newExp.strip()
                x,newX,i = [],[],0
                x.extend(newExp)
                while i<len(x):
                    if x[i]!=' ':
                        newX.append(x[i])
                    i+=1
                answer = mt.pow(int(newX[0]),int(newX[1]))
                speak(str(answer))
            else:
                znak = ['+', '-', 'x', '/']
                a,i,str1,str2 = [],0,'',''
                while i<len(expression):
                    if expression[i] in znak:
                        break
                    str1+=expression[i]
                    i+=1
                a.append(str1.rstrip())
                a.append(expression[i])
                i = i+1
                while i<len(expression):
                    str2+=expression[i]
                    i+=1
                a.append(str2.lstrip())

                if a[1] == '+':
                    answer = int(a[0])+int(a[2])
                    speak(str(answer))
                elif a[1] == '-':
                    answer = int(a[0])-int(a[2])
                    speak(str(answer))
                elif a[1] == 'x':
                    answer = int(a[0])*int(a[2])
                    speak(str(answer))
                elif a[1] == '/':
                    answer = int(a[0])/int(a[2])
                    speak(str(answer))

        #погода сейчас
        elif 'скажи погоду' in query or 'как мне сегодня одеться' in query:
            r = requests.get('https://api.ipdata.co?api-key=test').json()
            s_city = r['city']
            appid = "a091291a9ed9a4ac64d93b44076a0252"
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                   params={'q': str(s_city), 'type': 'like', 'units': 'metric', 'APPID': appid})
                data = res.json()
                cities = ["{} ({})".format(d['name'], d['sys']['country'])
                          for d in data['list']]
                city_id = data['list'][0]['id']
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                d = datetime.datetime.today()
                res = str(d.day)
            except Exception:
                myCommand()
            if 'как мне сегодня одеться' in query:
                if data['main']['temp']<5:
                    speak('Надень куртку или пуховик, шарф, шапку, теплые штаны и ботинки')
                elif 5<=data['main']['temp']<=15:
                    speak('Надень кофту или легкую куртку, штаны и кросовки')
                elif 15<data['main']['temp']<=35:
                    speak('Надень шорты и футболку')
                elif data['main']['temp']>35:
                    spaek('На улице ужасно жарко')

                    
                if 'дождь' in data['weather'][0]['description']:
                    speak('Также учти, на улице дождь')
                elif 'облачно' in data['weather'][0]['description']:
                    speak('На улице облачно, может пойти дождь')
            else:
                speak('Сегодня, ' + str(data['weather'][0]['description']) + ' и '+ str(data['main']['temp']) + ' градусов')

    
        elif 'пока' in query:
            speak('Пока')
            sys.exit()

        elif 'что ты умеешь' in query or 'твои возможности' in query:
            speak('Открывать ютуб, гугл и почту. Создавать и удалять папки. Создавать, заполнять и удалять файлы.')
            speak('Разговаривать с тобой. Говорить который час  и какое число. То, что я не знаю, я ищу в гугле и вывожу тебе на экран')


        
        else:
            query = query
            speak('Ищу...')
            webbrowser.open('www.google.com/search?q='+query)
        speak('Что делать дальше?')
