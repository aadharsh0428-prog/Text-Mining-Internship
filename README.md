# Text-Mining-Internship

This repository consists of the script that extracts topics from the given csv files as mentioned in the dataset and <br>
an .ipynb notebook which has the pre processsing of the text and the application of an Unsupervised Learning Algorithm to <br>
demonstrate clustering. <br>

1.Clone the repository using git clone https://github.com/aadharsh0428-prog/Text-Mining-Internship.git <br>
2.Download and extract the dataset from [here](https://cordis.europa.eu/data/cordis-h2020projects-csv.zip). <br>

### Run Requirements. 
This will install all the dependencies need to run the project.

```
$> cd Text-Mining-Internship-main
$> pip install -r requirements.txt
```

### How to run scripts to get text file.

After cloning the repository place the extracted data folder as well. The directory structure is as below <br>

```bash
Text-Mining-Internship-main/
 |--csv
 |   |--euroSciVoc.csv
 |   |--legalBasis.csv
 |   |--organization.csv
 |   |--project.csv
 |   |--topics.csv
 |   |--webItem.csv
 |   |--webLink.csv
 |   |--cordis_programmes_topics.py
 |--Text Mining Analysis.ipynb
 |--requirements.txt
```
```
$> mv ~/Text-Mining-Internship-main/cordis_programmes_topics.py ~/Text-Mining-Internship-main/csv/cordis_programmes_topics.py
$> cd csv
$> python3 cordis_programmes_topics.py --input <filename.csv>
```
After running the above script to get the topics run the Python Notebook to visualize the results.
