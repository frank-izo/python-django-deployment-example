from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\izzo\Anaconda3\pkgs\geckodriver-0.24.0-h21ff451_1\Scripts\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
