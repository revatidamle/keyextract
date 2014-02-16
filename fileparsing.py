import os,sys
import csv
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
def to_txt(pdf_path):
    input_ = file(pdf_path, 'rb')
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    process_pdf(manager, converter, input_)
    return output.getvalue() 
path="/home/revatidamle/thesis"
dirs = os.listdir(path)	# listdir returns the list of all files in the given directory path
for file_ in dirs:
	if not file_[:-4] in os.listdir('/home/revatidamle/pdftotext/'):
		print file_
		a=to_txt("/home/revatidamle/thesis/"+file_)
		f=open("/home/revatidamle/pdftotext/"+file_[:-4],"w")
		f.write(a)
		f.close()
new_dict=dict()
for file1 in os.listdir("/home/revatidamle/pdftotext/"):
	f=open("/home/revatidamle/pdftotext/"+file1,"r")
	string=f.read()
	list_=string.split()
	for i in list_:
		if i in new_dict:
			new_dict[i]=new_dict[i]+1;
		else:
			new_dict[i]=1;

f1=open("/home/revatidamle/res.txt","w")
writer = csv.writer(open('res.txt', 'wb'))
for key, value in new_dict.items():
   writer.writerow([key, value])	
