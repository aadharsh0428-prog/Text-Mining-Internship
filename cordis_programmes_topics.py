#!/usr/bin/python
"""Filter the CORDIS csv file to file all programmes and topics"""

import os.path
import csv
import argparse

parser = argparse.ArgumentParser(
    description="Filter the CORDIS csv file to file all programmes and topics",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "--input",
    type=str,
    default="h2020projects.csv",
    help="name of the CSV file where to read the project data from")
parser.add_argument(
    "--output_topics",
    type=str,
    default="topics.txt",
    help="name of the file where to save the topics")
parser.add_argument(
    "--overwrite",
    action="store_true",
    default=False,
    help="overwrite output file if existing")
args = parser.parse_args()

topics = set()

with open(args.input, 'r') as csvfile:
    cordis = csv.reader(csvfile, delimiter=';', quotechar='"')
    if args.input == 'euroSciVoc.csv' or args.input == 'legalBasis.csv' or args.input == 'topics.csv':
        for row in cordis:
            topics.add(row[2])
    if args.input == 'organization.csv':
        for row in cordis:
            topics.add(row[4])
    if args.input == 'project.csv' or args.input == 'webItem.csv':
        for row in cordis:
            topics.add(row[3])
    if args.input == 'webLink.csv':
        for row in cordis:
            topics.add(row[6])
    

with open(args.output_topics, 'w') as topicsfile:
    for x in sorted(topics):
        topicsfile.write(x + '\n')

