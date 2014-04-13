import os,sys
import csv
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import math
from collections import OrderedDict
#print sys.argv[1],sys.argv[1]

#------------------------------------------converting from pdf to text----------------------------------
def to_txt(pdf_path):
    input_ = file(pdf_path, 'rb')
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    process_pdf(manager, converter, input_)
    return output.getvalue()


#-----------------------------term frequency calculations-------------------------------------------

def termFrequency(term, document):
    normalizeDocument = document.lower().split()
    return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))

#----------------------inverse document frequency clculations--------------------------------------
def inverseDocumentFrequency(term, allDocuments):
    numDocumentsWithThisTerm = 0
    for doc in allDocuments:
        if term.lower() in allDocuments[doc].lower().split():
            numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1

    if numDocumentsWithThisTerm > 0:
        return 1.0 + math.log(float(len(allDocuments)) / numDocumentsWithThisTerm)
    else:
        return 1.0

#---------------------------------------------------------------------------------------------------
if __name__=='__main__':
    all_docs=dict();
    path=sys.argv[1] #/home/revatidamle/thesis
    dirs = os.listdir(path) # listdir returns the list of all files in the given directory path
    for file_ in dirs:
        if not file_[:-4] in os.listdir(sys.argv[2]):#/home/revatidamle/pdftotext/
            a=to_txt(path+file_) 
            f=open(sys.argv[2]+file_[:-4],"w")
            all_docs[file_[:-4]]=a;
            f.write(a)
            f.close()
        else:
            f=open(os.path.join(sys.argv[2],file_[:-4]),"r")
            all_docs[file_[:-4]]=f.read();
            f.close()
    inp = raw_input("enter search query");
    input_list=inp.split();
    for wrd in input_list:
        new =dict();
        idf=inverseDocumentFrequency(wrd,all_docs);
        for file_ in os.listdir(sys.argv[2]):
	   if (idf*termFrequency(wrd,all_docs[file_])!=0) :                
		 new[file_]=[idf *termFrequency(wrd,all_docs[file_])];          # calculating tfdif
        print "------------------------"
	print list(reversed(sorted(new.items(),key=lambda x: x[1])))          #sorting the list in descending order ; lambda used to use second value of the 										        tuple for sorting
