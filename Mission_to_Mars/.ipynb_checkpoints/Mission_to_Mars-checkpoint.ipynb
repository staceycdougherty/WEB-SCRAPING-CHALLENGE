{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "from flask import Flask, render_template\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [/Users/staceydougherty/.wdm/drivers/chromedriver/mac64/91.0.4472.101/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#visit site\n",
    "url = \"https://redplanetscience.com/\"\n",
    "browser.visit(url)\n",
    "\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "#soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the news name\n",
    "news_title = soup.find_all('div', class_='content_title')[0].text\n",
    "\n",
    "# Get the news paragraph\n",
    "news_p = soup.find_all('div', class_='article_teaser_body')[0].text\n",
    "#print it out to see if it found it\n",
    "#news_title\n",
    "#news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#visit site for picture\n",
    "featured_image_url = \"https://spaceimages-mars.com/\"\n",
    "browser.visit(featured_image_url)\n",
    "    \n",
    "time.sleep(1)\n",
    "    \n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "#soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "relative_image_path = soup.find_all('img')[1][\"src\"]\n",
    "featured_img_url = featured_image_url + relative_image_path\n",
    "    \n",
    "featured_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Values</th>    </tr>    <tr>      <th>Attributes</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 ( Phobos &amp; Deimos )</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>\n"
     ]
    }
   ],
   "source": [
    "#mars facts scraping\n",
    "mars_facts_url = 'https://galaxyfacts-mars.com/'\n",
    "tables = pd.read_html(mars_facts_url)\n",
    "#tables\n",
    "\n",
    "table_df = pd.DataFrame(tables[1])\n",
    "table_df.columns = [\"Attributes\", \"Values\"]\n",
    "table_df.set_index(\"Attributes\", inplace =True)\n",
    "table_df\n",
    "#convert to html table\n",
    "html_table = table_df.to_html()\n",
    "html_table\n",
    "\n",
    "html_table = html_table.replace('\\n', '')\n",
    "print(html_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}\n"
     ]
    }
   ],
   "source": [
    "#mars hemisphere\n",
    "mars_url = 'https://marshemispheres.com/'\n",
    "browser.visit(mars_url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')\n",
    "\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "for i in range(4):\n",
    "    #create empty dictionary\n",
    "    hemispheres = {}\n",
    "    browser.find_by_css('a.product-item h3')[i].click()\n",
    "    element = browser.links.find_by_text('Sample').first\n",
    "    img_url = element['href']\n",
    "    title = browser.find_by_css(\"h2.title\").text\n",
    "    hemispheres[\"img_url\"] = img_url\n",
    "    hemispheres[\"title\"] = title\n",
    "    hemisphere_image_urls.append(hemispheres)\n",
    "    browser.back()\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'img_url': 'https://marshemispheres.com/images/full.jpg', 'title': 'Cerberus Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg', 'title': 'Schiaparelli Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg', 'title': 'Syrtis Major Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}]\n"
     ]
    }
   ],
   "source": [
    "print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:Virtual_Env] *",
   "language": "python",
   "name": "conda-env-Virtual_Env-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
