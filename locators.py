from selenium.webdriver.common.by import By


class Header:
    button_order_up = [By.CLASS_NAME, 'Button_Button__ra12g']
    logo_yandex = [By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']


class MainPage:
    home_page = [By.CLASS_NAME, 'Home_HomePage__ZXKIX']
    button_order_down = [By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]']
    question_0 = [By.ID, 'accordion__heading-0']
    question_1 = [By.ID, 'accordion__heading-1']
    question_2 = [By.ID, 'accordion__heading-2']
    question_3 = [By.ID, 'accordion__heading-3']
    question_4 = [By.ID, 'accordion__heading-4']
    question_5 = [By.ID, 'accordion__heading-5']
    question_6 = [By.ID, 'accordion__heading-6']
    question_7 = [By.ID, 'accordion__heading-7']
    answer_0 = [By.ID, 'accordion__panel-0']
    answer_1 = [By.ID, 'accordion__panel-1']
    answer_2 = [By.ID, 'accordion__panel-2']
    answer_3 = [By.ID, 'accordion__panel-3']
    answer_4 = [By.ID, 'accordion__panel-4']
    answer_5 = [By.ID, 'accordion__panel-5']
    answer_6 = [By.ID, 'accordion__panel-6']
    answer_7 = [By.ID, 'accordion__panel-7']


class RentPage:
    header_for_whole_scooter = [By.XPATH, '//div[contains(text(),"Для кого самокат")]']
    input_name = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[1]/input[1]']
    input_surname = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/input[1]']
    input_address = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[3]/input[1]']
    input_metro_station = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/input[1]']
    drop_down_metro_station = [By.CLASS_NAME, 'select-search__select']
    select_metro_station = [By.XPATH, '//li[1]']
    input_phone = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[5]/input[1]']
    button_onward = [By.XPATH, '//button[contains(text(),"Далее")]']
    header_about_rent = [By.XPATH, '//div[contains(text(),"Про аренду")]']
    input_data = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]']
    date_selected = [By.CLASS_NAME, 'react-datepicker__day--selected']
    input_rental_period = [By.CLASS_NAME, 'Dropdown-root']
    drop_down_rental_period = [By.CLASS_NAME, 'Dropdown-menu']
    input_comment = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[4]/input[1]']
    button_order = [By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[3]/button[2]']
    pop_up_confirm = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    button_yes = [By.XPATH, '//button[contains(text(),"Да")]']
    pop_up_order_processed = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    button_view_status = [By.XPATH, '//button[contains(text(),"Посмотреть статус")]']
