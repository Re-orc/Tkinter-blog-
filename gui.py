from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import tkinter as tk
import os

class test():

    def Window(self):
        self.window = tk.Tk()
        self.text = tk.StringVar()
        self.window.title('연습용')
        self.window.geometry('500x180')
        self.window.resizable(False,False)

    def Label(self):
        label = tk.Label(self.window,text = '검색어입력하세요',width=15,height=2)
        label.place(relx=0.0,rely=0.0)
        
    def textvar(self):
        self.Text = tk.Entry(self.window)#, textvariable=)
        self.Text1 = tk.Text(self.window)
        self.Text1.config(width=60,height=10)
        #self.Text1.insert(tk.END,'')#textbox 출력
        self.Text.place(relx=0.22,rely=0.04)
        self.Text1.place(relx=0.01,rely=0.2)
        #self.Text2 = tk.Entry(self.window)
        #self.Text2.place(relx=0.25,rely=0.19)

    def StartButton(self):
        button = tk.Button(self.window,text ='Start',width=5,height=1,command=self.print_content)#command 눌렀을때 이벤트발생
        
        button.place(relx=0.52,rely=0.03)
           

        #starButton 눌렀을때 출력
    def print_content(self):
        content = self.Text.get()
        #content2 = self.Text2.get()
        driver = webdriver.Chrome('./chdr')
        driver.get('https://search.naver.com/search.naver?where=post&sm=tab_jum&query='+content)
        for i in range(len(driver.find_elements_by_partial_link_text('blog.naver.com'))):
            driver.find_elements_by_partial_link_text('blog.naver.com')[i].click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(10)
            try:
                driver.switch_to_frame(driver.find_element_by_id('mainFrame'))
            except NoSuchElementException:
                driver.switch_to_frame(driver.find_element_by_id('screenFrame'))
                driver.switch_to_frame(driver.find_element_by_id('mainFrame'))

            source = driver.page_source
            total = BeautifulSoup(source, 'html.parser')
            if total.select('.se-fs-'):
                a = total.select('.se-fs-')
            else:
                a = total.select('.se_textarea')

            c = ''
            for i in a:
                c += i.text+'\n'
            with open(os.path.expanduser('~\\DeskTop')+'/blog글.txt',encoding='utf-8',mode ='a') as f:
                f.writelines(c)
                f.closed

          
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
        driver.close()
        self.Text1.insert(tk.END,'끝났습니다.\n')

        
if __name__ in '__main__':
    inter = test()
    inter.Window()
    inter.Label()
    inter.StartButton()
    inter.textvar()
    inter.window.mainloop()
