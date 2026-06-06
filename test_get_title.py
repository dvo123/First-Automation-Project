
def test_get_title(driver):

    print('This web title is: ', driver.title)

    driver.get("https://www.google.com")
    print('This web title is: ', driver.title)

    driver.back()
    print('This web title is: ', driver.title)