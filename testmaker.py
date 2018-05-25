#!Python 3
import os
import requests
import bs4 as bs
import csv
import re
import time
import math

with open("fra_formulas.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    f = open("test.txt","a")
    for row in reader:
        formula = (row['Formula'])
        f.write(formula + "\n\n\n\n")
f.close() 
