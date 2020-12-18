## MTurk Implementation 

This is a code package for implementing MTurk with external website.


### 1. Install Dependencies
Firstly, we need to install boto3 (i.e., Python SDK for AWS) and other dependencies for processing data by:

    $ pip install -r requirement.txt
or

    $ pip install pandas
    $ pip install boto3



### 2. Config the MTurk Task

Main configuration can be set in 'config.json' file. Here is some notes on configuration setting:

- To set 'aws_access_key_id' and 'aws_secret_access_key', an AWS account with credentials can be signed up [here](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/signup-create-iam-user.html).
- Worker qualification requirement details can be found at [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html#ApiReference_QualificationType-IDs).
- We support to save file as '.json' or '.csv' type.


### 3. Core MTurk Functions

Core MTurk functions are within **MTurkManager** class in 'mturk_cores.py' file. This will be used in the HIT processing later.

### 4. Worker Interface Files.

For generating worker interfaces of HITS, please run:

    python frontend_cores.py

The generated htmls (or xmls) pages are saved in 'fontend' folder. 

### 5. Create MTurk HITs.

To create HITs, please run:

    python main_create_hit.py


### 6. Handle HITs Results.

To handle HITs results, we can retrieve, approve and save results into 'json' or 'csv' files by running:

    python main_retrieve_hit.py

Note that we might need to change detailed settings of **Worker Interface**, **Create HITs**, **Retrieve and Save HITs** in the corresponding files (e.g., main_retrieve_hit.py), please look into the file for instruction.