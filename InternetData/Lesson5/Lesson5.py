# https://gb.ru/lessons/184652/homework
# Selenium. Develop a program that collects letters from Inbox of a mailbox and adds it to DB
# From, Date, Subject, Letter text

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Number of read letters
letters_limit = 15


# gather letters from mail.ru mailbox
def gather_letters():

    letters_list = []
    driver=webdriver.Edge()

    driver.get('https://mail.ru/')

    try:
        # Wait appearing a login button
        wait = WebDriverWait(driver, 7)
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "ph-login")]')))

        if login_button:
            login_button.click()

        # Switch to iframe
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='ag-popup__frame__layout__iframe']")))
        mail_login = driver.find_element(By.XPATH, '//div[@data-test-id="mail.ru"]')

        if mail_login:
            # Select mail ru account
            mail_login.click()

            # User name filling for mail.ru
            login_name = driver.find_element(By.NAME, 'username')
            # login_name = driver.find_element(By.XPATH, '//input[@placeholder="Account name"]')
            login_name.send_keys('study.ai_172')

            # Press 'Enter password' button once has appeared
            wait = WebDriverWait(driver, 5)
            mail_pw = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
            mail_pw.click()

            pw_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
            pw_field.send_keys('NextPassword172#')
            pw_field.send_keys(Keys.ENTER)

            # Wait for appearing Compose button
            wait = WebDriverWait(driver, 7)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'compose-button__txt')))

            # Get letters list
            letters = driver.find_elements(By.XPATH, '//a[contains(@class, "js-letter-list-item")]')
            driver.get(letters[0].get_attribute('href'))

            counter = 0 # Limits the number of added letters just in case
            for letter in letters:

                # Wait for loading the letter (Delete button on a header)
                wait = WebDriverWait(driver, 7)
                wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-title-shortcut="Del"]')))

                title_field = wait.until(EC.presence_of_element_located((By.XPATH, '//h2[@class="thread-subject"]'))).text
                date_field = driver.find_element(By.XPATH, '//div[@class="letter__date"]').text
                from_field = driver.find_element(By.XPATH, '//span[contains(@class,"letter-contact")]').text

                # Attempt to get all text as a text
                # -----------------------
                # content = driver.find_elements(By.XPATH, '//a[contains(@style,"text-decoration")]')
                # text_field = ""
                # for chunk in content:
                #     if chunk and chunk.text:
                #         text_field = text_field + chunk.text + '\n'
                #
                # print (f"{date_field}: {from_field} - {title_field}")
                # print(f"TEXT :{text_field}")

                # Attempt to get a whole HTML for the mail body
                body = driver.find_element(By.CLASS_NAME, 'letter-body')
                body_field = body.get_attribute("outerHTML")

                print(f"{date_field}: {from_field} - {title_field}")
                print(f"TEXT :{body_field}")

                letter_item = {'date': date_field, 'from': from_field,
                               'title': title_field, 'body': body_field}

                letters_list.append(letter_item)

                counter = counter + 1
                if counter >= letters_limit:
                    break

                # Next letter by Next icon
                next_btn = driver.find_element(By.XPATH, '//span[@data-title-shortcut="Ctrl+↓"]')
                if next_btn:
                    next_btn.click()
                else:
                    break

    except Exception as e:
        print(e)
        exit(-1)
    finally:
        driver.quit()

    return letters_list


# Fill Mongo Db with the letters
def fill_db(letters_list):
    from pymongo import MongoClient
    from pymongo.errors import DuplicateKeyError

    # Connecting to Database to store the data
    client = MongoClient("127.0.0.1", 27017)
    db = client['MailLettersDB']
    mails_collection = db.mail_ru_mails

    # Insert to the collection
    added = 0
    for letter in letters_list:
        try:
            mails_collection.insert_one(letter)
            added = added + 1
        except DuplicateKeyError as e:
            print(f'Duplicated record found: ' + letter['title'])

    print(f'\nAdded {added} mails!\n')


mails = gather_letters()

if len(mails) > 0:
    fill_db(mails)
