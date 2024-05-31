import asyncio

import time
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from download import test_download

class DownloadGuiApp(toga.App):
    def __init__(self):
        super().__init__(formal_name='Download Gui App', app_id='com.example.downloadgui')

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # the main text box
        self._logbox = toga.MultilineTextInput(style=Pack(flex=1, font_family="monospace", font_size=10))
        self._logbox.readonly = True
        main_box.add(self._logbox)
        
        # the upload button
        self._start_button = toga.Button(f'Start Test...', on_press=self.download_test, enabled=True)
        main_box.add(self._start_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        self.main_window.show()


    def log(self, message:str=''):
        self._logbox.value += f'{message}\n'
        self._logbox.scroll_to_bottom()


    async def download_test(self, widget):
        self._start_button.enabled = False
        self.log("> starting test")
        t1 = time.time()
        await test_download( url = 'http://ipv4.download.thinkbroadband.com/200MB.zip')
        t2 = time.time()
        self.log(f"> test complete in {t2-t1:.2f}s")
        self._start_button.enabled = True


def main():
    return DownloadGuiApp()



if __name__ == '__main__':
    app = main()
    app.main_loop()