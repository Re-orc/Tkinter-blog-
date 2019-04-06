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
