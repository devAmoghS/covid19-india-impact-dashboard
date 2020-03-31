# covid19-india-impact-dashboard ![GitHub stars](https://img.shields.io/github/stars/devAmoghS/covid19-india-impact-dashboard?style=for-the-badge)  ![GitHub forks](https://img.shields.io/github/forks/devAmoghS/covid19-india-impact-dashboard?label=Forks&style=for-the-badge)
This is a [dashboard](http://covid19dashboard.pythonanywhere.com/) to track COVID-19 cases in India. Python Flask App with visuals in Dash

### Demo
### (Duration: ~ 1 minute)
![COVID-19 India Impact Demo](https://github.com/devAmoghS/covid19-india-impact-dashboard/blob/master/demo.gif)


### About:

CoronaVirus(COVID-19) has impacted India and the number of confirmed cases are still growing. 

We can do our bit by building tools and services that can help provide accurate information from official sources in user-friendly manner and help spread awareness of gravity of situation.

In an effort to do the same, we have started building a dashboard by sourcing data from Ministry of Health and Family Welfare, Government of India.

### Blog
If you want to learn about how this idea got translated into code, you can the blog post here.
![Tracking the COVID-19 outbreak in India using Python](https://medium.com/swlh/tracking-the-covid-19-outbreak-in-india-using-python-c938eb824ba3?source=friends_link&sk=b83073428d916ab0d11aba24e0133453)

### Contributors
[Amogh Singhal](https://www.linkedin.com/in/amogh-singhal/) <br/>
[Sourabh Inani](https://www.linkedin.com/in/sourabh-inani-5b79464a/)

### Installation
1. Use `pipenv` or `virtualenv` to setup a virtual environment for the project
2. Activate the environment
3. Change directory to the location where `requirements.txt` is present.
4. Use the following command: `pip install -r requirements.txt`

#### Feel free to raise a pull request to improve this repository and help our nation fight this pandemic !!!

### Changelog:
Current version has:
1. Interactive Table to sort and filter data
2. Bar graphs to visually represent the impacted states
3. Key Performance Indicators

### Description of Files:
1. `parseData_BeautifulSoup.py` - Parser made in BeautifulSoup to scrape data from Ministry of Health & Public Welfare, Govermnent of India

2. `renderDashboard.py` - Dash App that is rendered with visual components(bar graphs, KPIs) to display the dashboard

#### Huge Shout-out to people at pythonanywhere.com for helping us taking this live
[Giles Thomas](https://www.linkedin.com/in/gilesthomas/)
[Glenn Jones](https://www.linkedin.com/in/glenn-jones-3503b81/)
[Filip Lajszczak](https://www.linkedin.com/in/filip-lajszczak-05562388/)
