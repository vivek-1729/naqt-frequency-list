import requests, pdftotext, pickle
with open('pdfs/19','rb') as file:
    links = pickle.load(file)
url = links[0]
# https://quizbowlpackets.com/1980/
# https://quizbowlpackets.com/2155/
# https://quizbowlpackets.com/2344/
response = requests.get(url)
my_raw_data = response.content

with open("my_pdf.pdf", 'wb') as my_data:
    my_data.write(my_raw_data)

memory_file = open("my_pdf.pdf", 'rb')
pdf = pdftotext.PDF(memory_file)
# Iterate over all the pages
final = []
for page in pdf:
    pageSplit = page.split('ANSWER: ')
    answers = pageSplit[1::2]
    for element in answers:
        if '<' in element:
            answer = element.split('<')[0]
        else:
            answer = element.split('\n')[0]
        final.append(answer)
print(final)