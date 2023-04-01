---
title: Website for extracting data from transporting customs document
date: 2020-01-30
description: https://github.com/vittoriomta
---
I've built for my department team a website to upload the T1 documents and automatically create an excel file with all the data in it.

The T1 shipping note is  **a customs document used in the cross-border movement of goods for transporting customs goods from one customs office to another** . Basically, the T1 note is used to carry non-EU goods within the EU territory.

For run the project, clone the Github repository and then run:

```{r
pip install -r requirements.txt
```

Then enter the /app folder and run ``python3 app.py``:

The website basically have two main function for uplaoding the files, the first one is for all the PDF documents of T1 (atm scanned pdf will not work).

The second command if for upload the 'Master.xls' file where in the second column you can save all the containers in order for later to match with the data extracted (optional).

After loading the files go to /extractor in the url and you will find four options:

- Raw Data.xls: If you loaded the pdf this function will open each one and extract all the files inside and will create an excel file will all the most important data in the document divided in each column.
- Sorted Data.xls: If you loaded the master file, this function will look at the master and sort all the data from the Raw Data.xls and create another excel file with all the data sorted.
- T1.pdf: This function will create one merged pdf file sorted by the order of Sorted Data.xls.
- Merged_master.xls: The last function will paste all the data extracted and generate another master file with all the data finded (otherwise the rows will be empty) and you'll be able to easily look at the data extracted

If you go back to the main page '/' there is a button for deleting the files imported and created so you can run it again.

For our team is been a great improvement beacuse we spend a lot of time for creating the documents of our train's departure.

From 40/45 minuts of work time we reduced to about 10 minutes with this applications. If you work with this kind of document (Europe probably), this website will defintely be usefull.

Planning in the near future to implement a function for scanned documents and IMA documents.

Let me know through email for any kinds of bugs.
