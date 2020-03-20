# covid19-india-impact-dashboard
This is a dashboard to track COVID-19 cases in India. Python Flask App with visuals in Dash

# Demo
[!(https://github.com/devAmoghS/covid19-india-impact-dashboard/blob/master/demo.mp4)]


# About:

CoronaVirus has impacted India and the number of confirmed cases are still growing. 

We can do our bit by building tools and services that can help avoid misinformation and support effective tracking.

In an effort to do the same, I have started building a dashboard by sourcing data from Ministry of Health and Family Welfare, Government of India.

# Changelog:
Current version has:
1. Interactive Table to sort and filter data
2. Bar graphs to visually represent the impacted states
3. Key Performance Indicators

# Description of Files:
1. `parseData_BeautifulSoup.py` - Parser made in BeautifulSoup to scrape data from Ministry of Health & Public Welfare, Govermnent of India

2. `renderDashboard.py` - Dash App that is rendered with visual components(bar graphs, KPIs) to display the dashboard

