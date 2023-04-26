#### Run Tests
``` 
pytest tests
```
#### Tests are carried out in parallel, in several browsers at once (you can also specify which one to use in the tests), and by creating xml, html, tracing, Allure reports and screenshots.
### By default, what pytest.ini uses:
Launch of 3 browsers: chromium, firefox, webkit
``` 
--browser chromium --browser firefox --browser webkit
``` 
Parallel running of tests
``` 
-n 3
``` 
Creation of xml, html, Allure reports
``` 
--junitxml=reports/report.xml
--alluredir reports/allure_report/
--html=reports/html_report/report.html
``` 
