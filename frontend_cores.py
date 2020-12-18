import os
import re
import pandas as pd
from mturk_cores import print_log


def load_frontend_xml(xml_path):
    """
    Load frontend setting from '.xml' file.
    Example: xml_path = "./frontend/xml_examples/my_question.xml"
    """
    frontend_setting = open(xml_path, "r").read()
    return frontend_setting



def load_frontend_setting(url, height=800):
    """
    Load frontend setting from online url.
    Example: url = "https://huashen218.github.io/images/c_change_tweet_t_000001.html"
    """
    frontend_setting = """<?xml version="1.0" encoding="UTF-8"?>\n
    <ExternalQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd">\n
    <ExternalURL>{{url}}</ExternalURL>\n
    <FrameHeight>{{height}}</FrameHeight>\n
    </ExternalQuestion>""".replace("{{url}}", url).replace("{{height}}", str(height))
    return frontend_setting



def generate_htmls(csv_file_path, html_template_path, html_save_path):
    data = pd.read_csv(csv_file_path, encoding='utf-8')

    with open(html_template_path, "r", encoding = "utf-8") as file:
        template = file.read()
    
    for i in range(5):	
        s = data["original-txt"][i]
        file_name = "c_change_tweet_t_" + str(i).zfill(6) + ".html"
        file_dir = os.path.join(html_save_path, file_name)
        with open(file_dir, "w", encoding = "utf-8") as file:
            changed = s.encode('utf-8').decode('unicode-escape')
            hashtag = re.sub(r"(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)", r'<span class="hashtag">#\1</span>', changed)
            final = template.replace("{{message}}", hashtag)
            final_w_id = final.replace("{{tweetID}}", str(i))
            file.write(final_w_id)
        print_log("INFO", f"Saved file: {file_dir}")
        



def main():
    """
    Generate and save html files.
    """
    # Step1: generate htmls
    csv_data_path= "./frontend/html_template_data/dataset.csv"
    html_template_path = "./frontend/html_template_data/template.html"
    html_save_path = "./frontend/html_files/"

    generate_htmls(csv_data_path, html_template_path, html_save_path)

    # Step2: push htmls to Github
    # push htmls to Github Pages, currently manual.

if __name__ == '__main__':
    main()

