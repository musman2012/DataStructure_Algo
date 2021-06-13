- ~~Go through previous projects for finding details about software engineering practices being followed --> Saturday~~
- ~~Go through previous projects for Software design questions (how many users, requests per second etc scaling) --> Saturday~~
- ~~Review Data Structures in Python --> Friday~~
- Practice top 10 coding questions --> Sunday +++ Anything else
- ~~- Trapping rainwater
- ~~- Power of 10 
- ~~- Write a function that adds two fractions together and returns the answer in its reduce form
- ~~Important database concepts (SQL vs NoSQL + Where to use which) --> Thursday~~ 

SDLC --> Agile Questions
Revise everything

-------------------------------------
## Software Design Preparations
### Data Transfer System for Production Industry
- Developed complete data ingestion pipeline to stream real-time data to the cloud using Elastic stack
- Data visualization and analysis using Kibana dashboard, predictive maintenance to be achieved

What was the design of this system?

We deployed logstash on the gateway endpoints, this logstash node was ingestion the data to the Elasticsearch which was deployed on an Ec2 instance. 


### High Performance Network Traffic Filtering Solution
The developed system was able to filter high rate traffic coming (40 Gbps). DPDK was used to bypass Kernel overhead and fast packet processing.

### Requirements:
Whitelists data traffic upto 120 Gbps
Modular design provides support for scaling in terms of rate and number of users


[Design](https://docs.google.com/document/d/e/2PACX-1vSUWctV2mg5TiKOmI1mHUn5K-5EtPTXY9ZRwp7SDt8KTBrDnep0mCSdeZpOn7l2N7ab0vBmyFCaU-Ea/pub)

GitHub was being used for version control. master branch had the stable deployed code always. New feature development had the following sequence:

Create feature branch out of master branch --> Do the development on feature branch --> Test feature on feature brach --> merge with dev branch --> Testing complete code --> merge with master branch

Development options and details in E:\Interview Prep\MetaSwitch\Usman_Presentation

### Serendipity

A file storage System, which was Redundant, Distributed, and Encrypted. We have used Python language as backend as well as for frontend.

Application server + Multiple Storage Servers

Application server also had a SQL DB which has details about users, all the files the user has, and locations of chunks for each file using its file ID (Filename as f_ID).

Application server had a Reciever/Sender (used to receive requests and send responses to the users), Message Controller (checking which operation to take place), and a FileSystemManager (which is used to set and fetch the details of chunks). The location information of chunks was provided to the client to directly upload/download from storage servers.

### Yorkshire & Humber Care Record
BigQuery to fetch data from Google Cloud Platform, Python for Backend and D3.JS for front-end

The data was stored on Google cloud storage and was fetched using Google BigQuery.
