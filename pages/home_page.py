from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.video_inst = (
            By.CSS_SELECTOR,
            "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div.home-card.pointer > div.home-card__top"
        )

        # ✅ УПРОЩЁННЫЕ И СТАБИЛЬНЫЕ СЕЛЕКТОРЫ
        self.fullscreen_btn = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen")
        self.fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen-exit")

        self.profile_icon = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar")
        self.exit_btn = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(4)")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog button:nth-child(2)")


    # ✅ ВАЖНО: ИСПОЛЬЗУЕМ ТОЛЬКО self.video_inst
    def click_video_inst(self):
        self.wait.until(EC.element_to_be_clickable(self.video_inst)).click()

        # ✅ ПЫТАЕМСЯ ПЕРЕКЛЮЧИТЬСЯ В IFRAME, ЕСЛИ ОН ЕСТЬ
        # noinspection PyBroadException
        try:
            iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            self.driver.switch_to.frame(iframe)
        except:
            pass  # iframe нет — значит остаёмся в основном DOM

        self.wait.until(EC.presence_of_element_located(self.fullscreen_btn))

    def click_fullscreen_btn(self):
        video = self.wait.until(EC.visibility_of_element_located(self.video_inst))
        ActionChains(self.driver).move_to_element(video).perform()
        self.wait.until(EC.element_to_be_clickable(self.fullscreen_btn)).click()


    def click_fullscreen_exit(self):
        self.wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()


    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()


    def click_exit_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.exit_btn)).click()


    def click_confirm_exit(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_exit)).click()
