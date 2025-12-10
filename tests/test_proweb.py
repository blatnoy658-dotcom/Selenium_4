from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver_chrome)

    login_page.enter_phone_number("my@proweb.uz")
    login_page.click_btn_next()

    login_page.enter_password("proweb3106632")
    login_page.click_btn_submit()

    # noinspection PyBroadException
    try:
        login_page.click_btn_sessions()
        login_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_chrome)
    home_page.click_video_inst()
    home_page.click_fullscreen_btn()
    home_page.click_fullscreen_exit()

    home_page.click_profile_icon()
    home_page.click_exit_btn()
    home_page.click_confirm_exit()


def test_login_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver_edge)

    login_page.enter_phone_number("my@proweb.uz")
    login_page.click_btn_next()

    login_page.enter_password("proweb3106632")
    login_page.click_btn_submit()

    # noinspection PyBroadException
    try:
        login_page.click_btn_sessions()
        login_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_edge)
    home_page.click_video_inst()
    home_page.click_fullscreen_btn()
    home_page.click_fullscreen_exit()

    home_page.click_profile_icon()
    home_page.click_exit_btn()
    home_page.click_confirm_exit()
