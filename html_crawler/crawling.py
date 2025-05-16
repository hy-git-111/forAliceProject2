from selenium import webdriver
from selenium.webdriver.common.by import By
from html_crawler.base_page import BasePage
import time, os
from file_manage import save_data_overwrite

class CrawlingPage(BasePage):
    def login(self, ID: str, PASSWORD: str):
        self.click_element((By.CSS_SELECTOR, "ul > li:nth-child(2) > a"))
        self.input_text((By.CSS_SELECTOR, "fieldset:nth-child(1) > input"), ID)
        self.input_text((By.CSS_SELECTOR, "fieldset:nth-child(2) > input"), PASSWORD)
        self.click_element((By.CLASS_NAME, "btn-primary"))

    def publish_article(self, title, description, article):
        self.input_text((By.CLASS_NAME, "form-control-lg"), title)
        self.input_text((By.CSS_SELECTOR, "fieldset:nth-child(2) > input"), description)
        self.input_text((By.CSS_SELECTOR, "fieldset:nth-child(3) > textarea"), article)
        self.click_element((By.CLASS_NAME), "btn-primary")

    def get_html_tags(self):
        tags = self.driver.execute_script("""
            return (function getNodePath(node, depth = 0) {
                if (!node) return '';
                const indent = ' '.repeat(depth * 2);
                let result = '';

                if (node.nodeType === 1) {
                    result += indent + '<' + node.tagName.toLowerCase();
                    for (let i = 0; i < node.attributes.length; i++) {
                        const attr = node.attributes[i];
                        result += ' ' + attr.name + '="' + attr.value + '"';
                    }
                    result += '>' + '\\n';
                    for (let i = 0; i < node.childNodes.length; i++) {
                        result += getNodePath(node.childNodes[i], depth + 1);
                    }
                    result += indent + '</' + node.tagName.toLowerCase() + '>' + '\\n';
                } else if (node.nodeType === 3) {
                    const text = node.textContent.trim();
                    if (text) {
                        result += indent + '"' + text + '"' + '\\n';
                    }
                }
                return result;
            })(document.body);
        """)

        return tags

    def capture_page(self, title, click_1=None, click_2=None, click_3 = None): 
        url = "http://localhost:4100/"
        self.driver.get(url)
        self.login("5@5", "5")
        
        if click_1:
            self.click_element(click_1)
            self.wait_for_page_load()
            time.sleep(1)
            if click_2:
                self.click_element(click_2)
                self.wait_for_page_load()

                if click_3:
                    self.publish_article("타이틀", "요약", "내용")
                    self.wait_for_page_load()

        html_data = (f"<!-- {title} -->\n{self.get_html_tags()}")
        return html_data

def capture_page(title, click_1=None, click_2=None, click_3=None):
    driver = webdriver.Chrome()
    crawling = CrawlingPage(driver)

    try:
        html_data = crawling.capture_page(title, click_1, click_2, click_3)
        filename = title + ".html"
        save_data_overwrite(html_data, "html_data", filename)
    finally:
        time.sleep(1)
        driver.quit()
    

        


