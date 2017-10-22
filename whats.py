from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import threading
driver = None


def main():
    global driver
    driver = webdriver.Chrome(os.environ['CHROME_DRIVER'])
    driver.get("https://web.whatsapp.com/")
    answer = raw_input('Is the phone connected successfully? (y/Y) -> ')

    if str(answer).strip().lower() == 'y':
        keep_running = True
        while keep_running:
            try:
                give_options()
            except:
                keep_running = False

        print 'Thanks for using.....'
    else:
        print 'Thanks for using.....'


def give_options():
    answer = int(
        raw_input('1. Send scheduled message\n2. Send quick message\n3. Chat\n-> ').strip())

    if answer == 1:
        interval = int(raw_input('Enter the interval in seconds -> ').strip())
        user_name = raw_input('Enter the user -> ').strip()
        message = raw_input('Enter the message -> ')
        message_after_interval(interval, user_name, message)
    elif answer == 2:
        user_name = raw_input('Enter the user -> ').strip()
        message = raw_input('Enter the message -> ')

        user_name_list = user_name.split(',')

        for user_name in user_name_list:
            if user_name:
                send_message(user_name.strip(), message)
    elif answer == 3:
        user_name = raw_input('Enter the user -> ').strip()
        initialize_chat(user_name)
    else:
        print 'O.o\nWrong Choice!'


def message_after_interval(interval, user_name, message):
    threading.Timer(interval, send_message, args=[user_name, message, True]).start()


def initialize_chat(user_name):
    if open_chat(user_name):
        print 'Chat opened'
        try:
            all_msgs_text_only = driver.find_element_by_xpath(
                '//div[contains(@class, "message-text")]')
            print all_msgs_text_only
        except Exception as e:
            print str(e)


def open_chat(user_name):
    try:
        print 'Searching for user..... ' + user_name
        web_obj = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
        web_obj.send_keys(user_name)
        time.sleep(2)
        elem = driver.find_element_by_xpath('//span[contains(text(),"{0}")]'.format(user_name))
        elem.click()
        return True
    except:
        print 'O.o!\nNo user found..'
        elem = driver.find_element_by_xpath('//button[@class="icon-search-morph"]')
        elem.click()
        return False


def send_message(user_name, message, is_interval=False):
    if open_chat(user_name):
        web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
        web_obj.send_keys(message)

        if is_interval:
            web_obj.send_keys(Keys.RETURN)
        else:
            answer = raw_input('Should i send message (y/Y)? -> ')
            if str(answer).strip().lower() == 'y':
                web_obj.send_keys(Keys.RETURN)
            else:
                web_obj.clear()


if __name__ == '__main__':
    main()
