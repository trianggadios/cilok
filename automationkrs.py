from selenium import webdriver
import time

npmMahasiswa = '1184011'
password = '130500'
kelas = "B"
Semester = "Semester 3"

if (kelas == "A"):
    khelas = 0
elif (kelas == "B"):
    khelas = 1
elif (kelas == "C"):
    khelas = 2
else:
    print("Kelas tidak ada!")

smester = []

asd='wokwok'
#perubahan



if (Semester == "Semester 1"):
    smester.append(0,15)
elif (Semester == "Semester 3"):
    smester = [16+khelas:37]
elif (Semester == "Semester 5"):

Semester5 = [38+khelas:56]
Semester7 = [57+khelas]

url = 'http://siap.poltekpos.ac.id/siap/besan.depan.php'

driver = webdriver.Chrome('/home/burger-man/Downloads/chromedriver')
driver.get(url)

driver.find_element_by_name('user_name').send_keys(npmMahasiswa)
driver.find_element_by_name('user_pass').send_keys(password)
asd=12345
driver.find_element_by_name('login').click()

time.sleep(5)

driver.find_element_by_link_text("Pengisian KRS").click()
driver.find_element_by_xpath("//input[@value='Tambah KRS']").click()

driver.find_element_by_xpath("//input[@value='16856']").click()
driver.find_element_by_xpath("//input[@value='16855']").click()
driver.find_element_by_xpath("//input[@value='16853']").click()
driver.find_element_by_xpath("//input[@value='16854']").click()
driver.find_element_by_xpath("//input[@value='16900']").click()
driver.find_element_by_xpath("//input[@value='16857']").click()
driver.find_element_by_xpath("//input[@value='16852']").click()
driver.find_element_by_xpath("//input[@value='16848']").click()

awe = driver.find_elements_by_name("JDWL[]")
checkboxValue = []
for i in awe:
    checkboxValue.append(i.get_attribute("value"))

perulangan =
for i in range []:
    print(checkboxValue[])
    perulangan = perulangan + 3
print(checkboxValue[i])

asd = driver.find_elements_by_xpath("//table[@class='box']/tbody/tr")
daftar = []
for i in asd:
    if len(i.text) < 60 and len(i.text) > 10:
        daftar.append(i.text)
        print(i.text)
print(len(daftar))
