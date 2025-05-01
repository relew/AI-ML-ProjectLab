# How Be TrackLess
A repo with the code, data and models needed for developing an anti-tracking chrome extension

## About
### Utilizing NLP for improved anti-tracking in web browsers
### Abstract 
Online tracking remains a significant privacy concern for internet users. Current solutions while effective have limitations in terms of coverage maintenance and precision. This workshop aims to leverage the power of LLMs to create a more robust adaptive and efficient anti-tracking system. We will explore the architecture of an LLM-based anti-tracking system developing the data pipeline and exploring how these models can be fine-tuned to analyze network requests page content and user interactions in real-time. The system's ability to understand the semantic context of web elements allows for more accurate identification of tracking attempts reducing false positives while improving detection rates of sophisticated trackers. A key focus will be on the practical challenges of implementing such a system within the constraints of a web browser environment. We'll discuss strategies for optimizing LLM inference to meet the real-time demands of browsing balancing accuracy with performance.

### Code and Data
Please clone the repo in your local machine to get the code and data required for this project.
```
git clone https://github.com/humeranoor/llm-anti-tracking
```

### Trained Model
- Download the [original pre-trained model](https://drive.google.com/file/d/1FuDfbfiNawnfvTQJ5MZLdzBh5xGt1Bfq/view?usp=drive_link) and save to the ./original_distilbert folder.

### Setting up the Machine
1. Create virtual environment:

```
python -m venv trackless-venv
source trackless-venv/bin/activate  # macOS/Linux
```

2. Install Python Packages: 
```
cd trackless-easy/
pip install -r requirements.txt
```


HOW TO RUN

### INPUTS
easyprivacy - manual refreshment needed
from https://easylist.to/ website download EasyPrivacz in a .txt format

# METHDODOLGY:

ditilBERT-base-uncased pre-trained model used
adamw-torch used for optimization


# STEP vy STEP
first tstep generated train data: python data_generator.py
first tstep generated test data: python data_generator.py

second tstep trauin_model data: python train_model.py
third tstep test model: python test_model.py

# evaluate model
metrics and confusion matrix

### Usage
#### through rest api
    One way to use this model is through the provided Flask-based REST API. By running the app.py script, you can expose an HTTP endpoint (/predict) that accepts POST requests with a URL in JSON format. The API returns whether the given URL is classified as a tracker along with a confidence score. This setup enables easy integration with web frontends, browser extensions, or other external applications that need to interact with the model in real time. You can test it locally using tools like curl or Postman.&&&

    python app.py

#### through chore extension 







### test predict

curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"url": "https://tracking.badsite.com/ads?id=123"}'