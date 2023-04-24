#### Run Tests
``` 
pytest tests
```

### By default, the launch will occur according to the settings in pytest.ini: 
In the reports/ folder there will be html, xml, allure and trace reports. The screenshots/ folder will contain the final test results


``` 
addopts = --junitxml=reports/report.xml --alluredir reports/allure_report/ --html=reports/html_report/report.html -n 3
headless = False
```


#### Can change the browsers involved in the work in conftest.py -> get_browser -> params = []
``` 
@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def get_browser(get_playwright, request):
```