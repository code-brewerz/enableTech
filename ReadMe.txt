Clone Repo
git clone https://github.com/code-brewerz/enableTech.git

Install libraries:
pip install selenium pytest locust softest pytest-html pytest-xdist requests 

Use following command to run with 4 workers

pytest .\testCases\test_saucelabs.py  --browser firefox -n 4
