from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PIL import Image, ImageGrab
import time
from selenium.webdriver.common.action_chains import ActionChains
from io import BytesIO
from pynput.keyboard import Key, Controller
import datetime
import sqlite3

mounths = {a[0]:a[1] for a in (('января', 1), ('февраля', 2), ('марта',3), ('апреля', 4), ('мая', 5), ('июня', 6), ('июля', 7), ('августа',8), ('сентября',9), ('октября', 10), ('ноября', 11), ('декабря', 12))}
print(mounths)

def holibd(mounth):
    base = sqlite3.connect('orders.db')
    cur = base.cursor()
    cur.execute("select HOL from holidays where day=?;", (mounth,))
    return (cur.fetchone()[0])

def to_time(day_txt, post_tm):
    day, mounth = int(day_txt.split()[0]), mounths[day_txt.split()[1]]
    timee = (post_tm.split()[2])
    processed_time = timee.split(":")
    hour, min= map(int, processed_time)
    time_obj = datetime.timedelta(hours=hour, minutes=min)
    return time_obj

ggs = ["(суббота)", "(среда)", "(понедельник)"]

timedelta =(datetime.datetime.now()- to_time("29 февраля (четверг)", "сегодня в 21:12")).time()


spisok = []
def main_function():
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://vk.com/")
        login_pol = wd(driver, 10).until(ec.presence_of_element_located((By.ID, "index_email")))
        login_pol.clear(); login_pol.send_keys("89212405502")
        login_pol.send_keys(Keys.RETURN)

        wd(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/form/div[3]/button"))).click()

        wd(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[4]"))).click()

        parol = wd(driver, 7).until(ec.presence_of_element_located((By.NAME, "password")))
        parol.clear(); parol.send_keys("w#y^6TQ4ir3AeG")
        parol.send_keys(Keys.RETURN)

        messages = wd(driver, 5).until(ec.element_to_be_clickable((By.ID, "l_msg"))).click()
        time.sleep(4)
        stroiteli = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/ul/li[1]"))).click()
        users = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[3]/div/span[2]/button"))).click()
        for x in range(2, 39):
            try:
                user =wd(driver, 5).until(ec.presence_of_element_located((By.XPATH, f"/html/body/div[7]/div/div[2]/div/div[2]/div/div/section/div[2]/div[3]/div/div/ul/li[{x}]/div[1]/div/div[2]/div[1]/a/span")))
                spisok.append(user.text)
            except TimeoutException:
                pass
        for x in range(2):
            driver.back()
        group = wd(driver, 5).until(ec.element_to_be_clickable((By.ID, "l_gr"))).click()
        time.sleep(4)
        shed_group = wd(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/a"))).click()
        time.sleep(4)
        driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)
        shedule = wd(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/img[2]"))).click()
        time.sleep(9)
        day_text, post_time = wd(driver, 5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[4]/div"))).text, wd(driver, 5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/div[2]/span/span"))).text
        week =day_text.split()[2]
        day_text = day_text.split()[0] + ' ' + day_text.split()[1]
        message = day_text + ' - ' + holibd(day_text)
        if week in ggs:
            message += '\nФизика нуу это два, похуйX_X'
        print(day_text, post_time)
        print(post_time.split()[0])
        if (datetime.datetime.now() - to_time(day_text, post_time)).time() < datetime.time(0, 10, 0) and post_time.split()[0] == "сегодня":
            
            photo = ImageGrab.grab((250, 130, 1400, 930))
            bytes_str = BytesIO()
            photo.save("schedule.png")
            time.sleep(2)
            for x in range(3):
                driver.back()
            messages = wd(driver, 5).until(ec.element_to_be_clickable((By.ID, "l_msg"))).click()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,250)")
            saved = wd(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/ul/li[2]/div[2]/div/div[2]/div[1]"))).click()
            line = wd(driver, 5).until(ec.presence_of_element_located((By.ID, "im_editable0")))
            time.sleep(2)
            chains = ActionChains(driver)

            pho = wd(driver, 5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/div[2]/div[4]/div[4]/div[4]/div[1]/div[2]/div/div/div/div/a[1]")))
            screb = wd(driver,
            5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/div[2]/div[4]/div[4]/div[4]/div[1]/div[2]/div/div/a/span")))
            chains.move_to_element(screb)

            chains.click(pho).perform()
            time.sleep(2)
            upl = wd(driver, 5).until(ec.element_to_be_clickable((By.ID, 'photos_choose_upload_area_label268346656_-3'))).click()
            keyboard = Controller()
            keyboard.type(r"C:\Users\Admin\Documents\programming\projects\vk_bot\schedule.png")
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            line = wd(driver, 5).until(ec.presence_of_element_located((By.ID, "im_editable0")))
            line.clear()
            line.send_keys(message)
            line.send_keys(Keys.RETURN)
            time.sleep(2)
    finally:
        driver.close()

def main_execute():
    main_function()

if __name__ == "__main__":
    main_execute()