import os,sys
# takes pdf and writes it to myfile in the same folder

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
dirs = os.listdir(path)
for file_ in dirs:
	if not file_[:-4] in os.listdir('/home/revatidamle/pdftotext/'):
		print file_
		a=to_txt("/home/revatidamle/thesis/"+file_)
		f=open("/home/revatidamle/pdftotext/"+file_[:-4],"w")
		f.write(a)
		f.close()
