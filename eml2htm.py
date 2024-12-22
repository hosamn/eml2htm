import email
import os
# from bs4 import BeautifulSoup

def eml_to_html(eml_file):
    with open(eml_file, 'r') as file:
        msg = email.message_from_file(file)
        html_content = None
        
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                html_content = part.get_payload(decode=True)
        
        if html_content:
        #     soup = BeautifulSoup(html_content, 'html.parser')
        #     html_text = soup.get_text()
        #     return html_text
            return html_content
        else:
            return None


# To walk a sub dir:
root_path = r"C:/emails/"
for root, dirs, files in os.walk(root_path):
    print(len(files), files)
    eml_files = [root_path+f for f in files if f.endswith('.eml')]
    break  # break after reporting current dir files and don't go any deeper



# Usage
for eml_file in eml_files:
    htm_file = eml_file + ".htm"
    html_content = eml_to_html(eml_file)

    if html_content:
        # print(html_text)
        # with open(htm_file,'w', encoding="utf8") as o:
        with open(htm_file,'wb') as o:
            o.write(html_content)
    else:
        print('No HTML content found in the EML file.')