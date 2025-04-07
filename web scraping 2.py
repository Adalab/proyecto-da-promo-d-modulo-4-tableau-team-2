import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import math
import os
df = pd.read_csv('Final-data/final_final.csv')
crime_keywords = ["cannibalism", "rape", "sexual abuse", "child abuse", "pedophilia", "necrophilia", 
                  "torture", "kidnapping", "arson", "robbery", "burglary", "incest", "animal cruelty", 
                  "stalking", "hate crime", "terrorism", "domestic violence", "human trafficking"]