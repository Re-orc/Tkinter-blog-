'''
from pywinauto.application import Application
app = Application()
kakao = app.connect(path = 'KakaoTalk')
#kakao.카카오톡.print_control_identifiers()

kakao['카카오톡']['ContactListView_0x00040274'].child_window(best_match='').click
#kakao.카카오톡.child_window(best_match='ChatRoomListView_0x000402f2').click()
'''
from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from pywinauto import application
import time, random, os, threading

class UI_Blog(threading.Thread):

    def __init__(self):
        super(UI_Blog,self).__init__()
        self.root = Tk()
        self.root.title('블로그')
        self.root.geometry('500x80')
        self.root.resizable(False,False)
        self.num = 0
        self.OsNum = len(os.listdir(os.path.expanduser('~\\DeskTop\\사진')))
        self.start()
        
        
        #Label
        label = Label(self.root,text = '제목을 입력해주세요')
        label.place(relx=0.0,rely=0.1)
        label2 = Label(self.root,text = '\t파일 경로')
        label2.place(relx=0.0,rely=0.54)
        
        #Text
        self.Text1 = Entry(self.root)
        self.Text1.place(relx=0.3,rely=0.12)
        self.Text2 = Entry(self.root)
        self.Text2.place(relx=0.3,rely=0.55)
        
        #Button
        button1 = Button(self.root,text = 'Start',width=4,command = self.UI_Title)
        button1.place(relx=0.7,rely=0.09)
        button2 = Button(self.root,text = '계속',width=5,heigh=2,command = self.first)
        button2.place(relx=0.85,rely=0.2)
        button3 = Button(self.root,text='찾기',width=4,command = self.file)
        button3.place(relx=0.7,rely=0.5)

    def file(self):
        self.Text2.delete('0',END)#버튼 클릭시 삭제 
        self.filename = filedialog.askopenfilename(initialdir = os.path.expanduser('~\\Desktop\\'),title='열기',filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        self.Text2.insert(END,self.filename)#버튼 클릭시 Text2에 경로 삽입

    def UI_Title(self):    
        self.title= self.Text1.get()
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=700,825')
        self.driver = webdriver.Chrome('./chdr',options=options)
        self.driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/')
        

    def first(self):
        self.filelist = list(filter(lambda x:x != self.filename.split('/')[-1], os.listdir(os.path.expanduser('~\\Desktop\\사진'))))
        self.f = open(self.filename,encoding='utf-8',mode='r')
        self.ID = self.driver.page_source
        self.num2 = 0
        id_pwd = self.ID.split('isLogin : "')[1].split('"')[0]
        self.driver.get('https://blog.naver.com/'+id_pwd+'?Redirect=Write&useSmartEditorVersion=2')
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_id('mainFrame'))#전체 iframe
        time.sleep(1)
        self.driver.find_element_by_name('post.title').clear()
        time.sleep(0.5)
        self.driver.find_element_by_name('post.title').send_keys(self.title)
        i = ','.join(os.listdir(os.path.expanduser('~\\DeskTop\\사진')))
        while self.num <= self.OsNum:
        #for i in os.listdir(os.path.expanduser('~\\DeskTop\\사진')):
            if not i.endswith('.txt'):
                time.sleep(1)
                self.driver.find_element_by_class_name('se2_photo').click()#사진클릭
                time.sleep(1)
                self.driver.find_element_by_class_name('se2_center').click()#가운데정렬
                time.sleep(0.5)
                self.driver.switch_to.window(self.driver.window_handles[1])#탭 선택
                time.sleep(3)
                self.driver.find_element_by_class_name('npe_alert_btn_close').click()
                time.sleep(3)
                self.driver.find_element_by_class_name('npu_btn_icon ').click()
                time.sleep(3)
                app = application.Application(backend='uia')
                app.connect(title_re='열기')                
                app.열기.edit.set_edit_text(os.path.expanduser('~\\DeskTop\\사진\\'+self.filelist[self.num2]))
                app.열기['열기(&0)'].click()
                time.sleep(3)
                self.driver.find_elements_by_class_name('npu_btn_title')[5].click() 
                time.sleep(5)
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(0.5)
                self.driver.switch_to.frame(self.driver.find_element_by_id('mainFrame'))#메인 프레임
                time.sleep(1)
                self.driver.switch_to.frame(self.driver.find_element_by_id('se2_iframe'))#입력창 프레임
                time.sleep(1)
                self.driver.find_elements_by_class_name('se2_inputarea')[0].send_keys('\n')
                
                self.lines = self.f.readline()
                self.driver.find_elements_by_class_name('se2_inputarea')[0].send_keys(self.lines)
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame(self.driver.find_element_by_id('mainFrame'))#전체 iframe
                self.num+=1
                self.num2+=1

        self.driver.execute_script("window.scrollTo(0,1000);")
        time.sleep(1)
        self.driver.find_element_by_id('btn_submit').click()
        time.sleep(3)
        self.driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/')
        self.OsNum+=self.OsNum
        chdr = app.connect(path ='chdr.exe')
        chdr.kill()

                
    
if __name__ == '__main__':
    ui_blog = UI_Blog()
    ui_blog.root.mainloop()


'''
import requests

data = {}

with requests.Session() as s:
    
#https://forms.office.com/Pages/ResponsePage.aspx?id=vnSfnWt49kiOGIPPei7vfPBDAkcg3RdBh87XLyYBkaRURDZaVVBaTks4NUc2OUxSTTMzSVJJTktBVS4u





prices = [498,501,470,489]
answer =[]
for i in range(len(prices)):
    answer.append(prices[i:len(prices)].index(min(prices)))

a = [1,2,3]

print(''.join(map(str,a))*2+str(a[0]))
    

def get_input():
# Get X and Y coordinates from the user.
    x1 = input('값을 입력해주세요:').split()
 
    return x1


#Formula for the slope of the line
def calculate_slope(*a):
    m = (int(a[3])-int(a[2]))/(int(a[1])-int(a[0]))
    return m
#print(calculate_slope)


#Calculate the slope of the line
#slope_line= calculate_slope(x1,y1,x2,y2)


#Calculate the slope of the line
slope_line= calculate_slope(*get_input())
          
 # Display the slope to the user.
print("The slope of the line is {:.1f}".format(slope_line))



def solution(numbers):
    nums = [str(n) for n in numbers]
    longest = max([len(n) for n in nums], default=0)
    nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
    return str(int(''.join(nums)))


S=[3, 30, 34, 5, 9]
print(int("".join([str(10**(len(i))-int(i)) for i in sorted([str(10**(len(str(i)))-i) for i in S])])))
    

s = 'azcbobobegghakl'
SampleString= 'bob'
InstancesFound = [i for i in range(len(s)-len(SampleString)) if s[i: i+3] == SampleString ]

        
print('Number of times bob occurs is:', len(InstancesFound))



import wx
import requests
import urllib3
from selenium import webdriver


class Reservation(wx.Frame):


    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Reservation')
        self.panel = wx.Panel(self, wx.ID_ANY)

        #label
        bmp = wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER,(16,16))
        inputOneIco = wx.StaticBitmap(self.panel, wx.ID_ANY,bmp)
        labelOne = wx.StaticText(self.panel, wx.ID_ANY,'아이디')
        self.inputTxtOne = wx.TextCtrl(self.panel, wx.ID_ANY,'') 
        inputTwoIco = wx.StaticBitmap(self.panel, wx.ID_ANY,bmp)
        labelTwo = wx.StaticText(self.panel, wx.ID_ANY,'암호   ')
        self.inputTxtTwo = wx.TextCtrl(self.panel,style=wx.TE_PASSWORD)

        #button
        okBtn = wx.Button(self.panel, wx.ID_ANY,'확인')
        cancelBtn = wx.Button(self.panel, wx.ID_ANY,'종료')
        self.Bind(wx.EVT_BUTTON,self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON,self.onCancel, cancelBtn)

        #
        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)

        #
        inputOneSizer.Add(inputOneIco, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)
        inputOneSizer.Add(self.inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)

        inputTwoSizer.Add(inputTwoIco, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.inputTxtTwo, 1, wx.ALL|wx.EXPAND, 5)
        #
        btnSizer.Add(okBtn, 0, wx.ALL,5)
        btnSizer.Add(cancelBtn, 0, wx.ALL,5)
        #
        topSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)

    def reserved(self):
        driver = webdriver.Chrome('')
        
    def Login(self):
        
        urllib3.disable_warnings()
        LOGIN_INFO ={
                     'userid':self.ID,
                     'userpw':self.passwrd,
                    }
        with requests.Session() as s:
            url = s.post('https://www.best.or.kr/member/login#',data=LOGIN_INFO,verify=False)
            print(url.status_code)
            return url.status_code

    def onOK(self,event):
        self.ID = self.inputTxtOne.GetValue()
        self.passwrd  = self.inputTxtTwo.GetValue()
        url_status = self.Login()
        if url_status == 200:
            wx.MessageBox('로그인 되었습니다.')
        else:
            wx.MessageBox('다시 입력해주세요')
            

        
    def onCancel(self,event):
        self.closeProgram()

    def closeProgram(self):
        self.Close()

    

if __name__ in '__main__':
    app = wx.App()
    fram = Reservation().Show()
    app.MainLoop()
    
    



class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
        
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()    # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'
    def b(self):
        return self.hello



a = Student()
print(a.hello)
c = a.b()
print(c)


import random

a = random.sample(range(1,55),54)
def b():
    
    b = random.sample(range(0,len(a)),1)
    print(a.pop(b[0]))
    print(a)
b()

    


mylist = [ [1,2,3], [4,5,6], [7,8,9] ]

for i in range(3):
    for j in range(3):
        a = mylist[j].pop()
        if j == 0:
            mylist[1].insert(0,a)
        elif j == 1:
            mylist[2].insert(0,a)
        else:
            mylist[0].insert(0,a)

    print(mylist)

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8) #zeros 행 512 열 512의 0으로 채우고
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

a = []
c=None
while True:   
    b =input('입력하세요: ')
    if b == '':
        break
    a.append(int(b))
    a.sort(),a.reverse()
    
if len(a) == 4:
    c = 0.5*a[0]+0.3*a[1]+0.2*a[2]+0.1*a[3]
elif len(a) == 3:
    c = 0.7*a[0]+0.2*a[1]+0.1*a[2]
elif len(a) == 2:
    c = 0.9*a[0]+0.1*a[1]
else:
    print(a)
print(c)

'''        
#n = int(input('입력하세요 :'))
#m1 = list(int(input('입력하세요: ')))    
    
    

'''
import requests
from bs4 import BeautifulSoup

LOGIN_INFO = { 'id':'k_s_y25',
               'pw':'tkddyd5278!!',
             }


with requests.Session() as s:
    url = s.post('https://nid.naver.com/nidlogin.login',data=LOGIN_INFO,allow_redirects=False)
    redirect_url = url.headers
    print(redirect_url)
    #sd = s.get(redirect_url,headers=headers)
   
    #print(sd)
    url1 = s.get('http://mail.naver.com/?n=1531810188592&v=f')
    soup = BeautifulSoup(url1.text, 'html.parser')
    total = soup.select('#cont_flex_area > div.divList.unselectable')
    print(total) 

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#pytesseract 경로 설정
img = cv2.imread('captcha.jpg',cv2.IMREAD_GRAYSCALE )
#opencv 이미지 불러오기 및 컬러 설정
(thresh, bw_img) = cv2.threshold(img,255,100 ,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('first',bw_img)
#opencv 이미지 보여주기 firts란 이름으로
test = pytesseract.image_to_string(bw_img, lang='eng')
#pytesseract 영어로
print(test)
cv2.waitKey(0),cv2.destroyAllWindows()
#opencv 아무키나 입력하면 꺼짐


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
im = Image.open('bb.png')
test = pytesseract.image_to_string(im,lang='kor')

print(test)



#pytesseract 이용해서 tesseract.exe를 실행하기위한 경로설정
#tessdata_dir_config = '--tessdata-DIR"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"'



import requests
from bs4 import BeautifulSoup

login_info = {
        'id':'k_s_y25',
        'pw':'tkddyd5278!!'
    }
with requests.Session() as s:
    url = s.post('https://www.naver.com',data=login_info)
    total = s.get('http://mail.naver.com/?n=1530178740789&v=f',data=login_info).text
    soup = BeautifulSoup(total,'html.parser')
    print(soup)




a = 17/3
print(round(a,4))

a = [1,2,3,4]
b = ['a','b','c','d']
c = list(zip(a,b))
print(c)

import requests
from bs4 import BeautifulSoup

header = {'User-Agent':('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
          '(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'),
          'Referer':'http://icis.me.go.kr/pageLink.do'}
          
url = requests.get('http://icis.me.go.kr/search/searchTypeView6.do',params={'bplcID':'144400363'})
soup = BeautifulSoup(url.text,'html.parser')
total = soup.select('.view_table')
for i in total:
    a = i.find_all('td')
    for d in a:
        print(d.text.strip().replace('\n',''))


import json

with open('cctv.json',encoding='utf-8') as data_file:
    data = data_file.readline()
    print(data)

import requests
import json
import time
while True:
    url = requests.get('https://api.bithumb.com/public/ticker/all')
    url = json.loads(url.text)
    a = url['data']['BTC']['sell_price']
    b = url['data']['ETC']['sell_price']
    c = ''
    for i in a:
        c+=i
    print(c)
    if a > '8347000' and b > '16760':
        print('파셈')
    elif a < '8347000' and b < '16750':
        print('사셈')
    else:
        print('ㅅㄱ',a,b)
    time.sleep(5)


import requests
from bs4 import BeautifulSoup
LOGIN_INFO = {
    'm_id':'adifuld',
    'm_pass':'ccc12345'
    }
with requests.Session() as s:
    #s = requests.Session()
    login_req = s.post('http://www.hojubada.com/board.php?board=kkkmain',data=LOGIN_INFO)
    print(login_req)
    header = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
              '(KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'),
    'Referer': 'http://www.hojubada.com/board.php?board=guinfree&backstepnum=2&itnocache=1528521344' }
    url = s.get('http://www.hojubada.com/member.php?mboard=memberboard&exe=mypage',)
    soup = BeautifulSoup(url.text, 'html.parser')
    print(soup)
    #total = soup.select('#mp_def_main > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1)')
    #print(total)

    

b = str(input('입력: '))
def get_complement_dna(dna):
    a=','
    c =list(a.join(dna).replace(',','').upper())
    print(c)
    dic={'A':'T','T':'A','G':'C','C':'G'}
    d=''
    for i in range(len(c)):
        d += dic[c[i]]

    print(d)


get_complement_dna(b)
'''
