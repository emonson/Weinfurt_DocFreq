import random
import math
import datetime
from string import Template
import xlrd

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch 

# Misc setup routines

def labelsList():
    return """
        138b
        200
        201
        202
        203
        204
        205
        206
        207
        208
        209
        data001
        data002
        data003
        data003a
        data004
        data005
        data006
        data007
        data008
        data009
        data010
        data011
        data012
        data013
        data014
        data015
        data016
        data017
        data017a
        data018
        data019
        data020
        data021
        data021a
        data022
        data023
        data024
        data025
        data026
        data026a
        data027
        data028
        data029
        data030
        data031
        data032
        data033
        data034
        data035
        data035a
        data035b
        data035c
        data035d
        data036
        data036a
        data036b
        data036c
        data037
        data038
        data038a
        data038b
        data039
        data040
        data041
        data042
        data043
        data044
        data044a
        data045
        data046
        data047
        data048
        data049
        data050
        data051
        data051a
        data052
        data053
        data054
        data055
        data055a
        data056
        data056a
        data057
        data058
        data059
        data059a
        data059b
        data060
        data061
        data062
        data062a
        data063
        data063a
        data063b
        data064
        data064a
        data065
        data066
        data067
        data068
        data068a
        data068b
        data069
        data069a
        data070
        data071
        data071a
        data072
        data073
        data074
        data075
        data076
        data077
        data078
        data078a
        data079
        data079a
        data080
        data081
        data082
        data083
        data084
        data085
        data086
        data087
        data088
        data089
        data090
        data091
        data092
        data092a
        data093
        data094
        data095
        data095a
        data096
        data097
        data097a
        data098
        data098a
        data099
        data099a
        data100
        data100a
        data100b
        data101
        data101a
        data102
        data103
        data104
        data105
        data106
        data107
        data108
        data108a
        data109
        data109a
        data110
        data111
        data111a
        data112
        data113
        data114
        data115
        data116
        data117
        data118
        data119
        data119a
        data120
        data121
        data121a
        data122
        data123
        data123a
        data123b
        data124
        data125
        data125a
        data126
        data126a
        data127
        data128
        data129
        data130
        data131
        data132
        data132a
        data133
        data133a
        data134
        data135
        data135a
        data136
        data137
        data137a
        data138
        data138a
        data139
        data139a
        data140
        data140a
        data141
        data142
        data142a
        data143
        data144
        data145
        data146
        """.split()
        
def myPages(canvas, doc): 
    canvas.saveState() 
    canvas.setFillColor('#a0a0a0')
    canvas.setFont('Helvetica-Oblique',10) 
    canvas.drawString(1.0*inch, 0.65*inch, "%s" % pageinfo) 
    canvas.drawCentredString(pageWidth/2.0, 0.65*inch, "%s" % dateNow)
    canvas.setFont('Helvetica',10) 
    canvas.drawString(pageWidth-1.0*inch, 0.65*inch, "%d" % doc.page) 

    # Color scale boxes
    canvas.setFillColor(shortColor1) 
    canvas.rect(pageWidth-0.7*inch, 0.65*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 
    canvas.setFillColor(shortColor2) 
    canvas.rect(pageWidth-0.7*inch, 0.75*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 
    canvas.setFillColor(shortColor3) 
    canvas.rect(pageWidth-0.7*inch, 0.85*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 

    # Color scale text labels
    canvas.setFillColor('#000000') 
    canvas.setFont('Helvetica',6) 
    canvas.drawString(pageWidth-0.55*inch, 0.6*inch, "%d" % int(100*short_max*0.00)) 
    canvas.drawString(pageWidth-0.55*inch, 0.7*inch, "%d" % int(100*short_max*0.33)) 
    canvas.drawString(pageWidth-0.55*inch, 0.8*inch, "%d" % int(100*short_max*0.66)) 
    canvas.drawString(pageWidth-0.55*inch, 0.9*inch, "%d" % int(100*short_max*1.00)) 
    canvas.drawString(pageWidth-0.715*inch, 1.01*inch, "%s" % ('Short %')) 

    # Color scale label ticks
    canvas.setLineWidth(0.35) 
    canvas.setStrokeColor('#000000') 
    # canvas.setDash(0.5, 0.5)
    canvas.line(pageWidth-0.7*inch, 0.62*inch, pageWidth-0.57*inch, 0.62*inch) 
    canvas.line(pageWidth-0.7*inch, 0.72*inch, pageWidth-0.57*inch, 0.72*inch) 
    canvas.line(pageWidth-0.7*inch, 0.82*inch, pageWidth-0.57*inch, 0.82*inch) 
    canvas.line(pageWidth-0.7*inch, 0.92*inch, pageWidth-0.57*inch, 0.92*inch) 

    # Text scale letters
    longStr = 'eE'
    scaleOffset = 1.25*inch	
    scaleUpset = 0.68*inch
    canvas.setFillColor('#000000') 
    canvas.setFont('Helvetica',8) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.32*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',10) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.45*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',12) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.60*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',14) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.770*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',6) 

    # Text scale text labels
    canvas.setFillColor('#000000') 
    canvas.drawString(scaleOffset-0.55*inch, 1.275*inch-scaleUpset, "%d" % (0)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.405*inch-scaleUpset, "%d" % (25)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.550*inch-scaleUpset, "%d" % (50)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.715*inch-scaleUpset, "%d" % (75)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.905*inch-scaleUpset, "%d" % (100)) 
    canvas.drawString(scaleOffset-0.715*inch, 2.02*inch-scaleUpset, "%s" % ('Long %')) 

    # Text scale label ticks
    canvas.setLineWidth(0.35) 
    canvas.setStrokeColor('#000000') 
    # canvas.setDash(0.5, 0.5)
    canvas.line(scaleOffset-0.665*inch, 1.30*inch-scaleUpset, scaleOffset-0.57*inch, 1.30*inch-scaleUpset) 
    canvas.line(scaleOffset-0.685*inch, 1.425*inch-scaleUpset, scaleOffset-0.57*inch, 1.425*inch-scaleUpset) 
    canvas.line(scaleOffset-0.7*inch, 1.575*inch-scaleUpset, scaleOffset-0.57*inch, 1.575*inch-scaleUpset) 
    canvas.line(scaleOffset-0.715*inch, 1.745*inch-scaleUpset, scaleOffset-0.57*inch, 1.745*inch-scaleUpset) 
    canvas.line(scaleOffset-0.715*inch, 1.935*inch-scaleUpset, scaleOffset-0.57*inch, 1.935*inch-scaleUpset) 

    canvas.restoreState()

#
# Set whether data values are printed and output file name
#
WRITE_DATA_VALUES = True
outfileName = 'DocFreq_Prelim_rev6k.pdf'

shortColorGiven = '#000000'
shortColorProblem = '#ff0000'
# Brown to yellow-orange
# shortColor1 = '#eac79d'		# low freq
# shortColor2 = '#b86944'		# med freq
# shortColor3 = '#741e14'		# high freq
# CB 3-class seq PuRd
# shortColor1 = '#e7e1df'		# low freq
# shortColor2 = '#c994c7'		# med freq
# shortColor3 = '#dd1c77'		# high freq
# from CB 4-class seq PuRd
# shortColor1 = '#d7b5d8'		# low freq
# shortColor2 = '#df65b0'		# med freq
# shortColor3 = '#ce1256'		# high freq
# from CB 3-class seq RdPu
# shortColor1 = '#fde0dd'		# low freq
# shortColor2 = '#fa9fb5'		# med freq
# shortColor3 = '#c51b8a'		# high freq
# from CB 4-class seq OrRd == GOOD
# shortColor1 = '#fdcc8a'		# low freq
# shortColor2 = '#fc8d59'		# med freq
# shortColor3 = '#d7301f'		# high freq
# from CB 4-class seq OrRd
# shortColor1 = '#f2c384'		# low freq
# shortColor2 = '#de703e'		# med freq
# shortColor3 = '#9e1506'		# high freq
# from CB 4-class seq OrRd
shortColor1 = '#000000'		# low freq
shortColor2 = '#000000'		# med freq
shortColor3 = '#000000'		# high freq

if WRITE_DATA_VALUES:
    outfileName = outfileName.replace('Prelim','PrelimData')

pageinfo = "Size/Color v6 (Preliminary Data)" 
dateNow = datetime.datetime.now().strftime("%d %b %Y")
styles = getSampleStyleSheet()
pageWidth, pageHeight = letter
doc = SimpleDocTemplate(outfileName, pagesize = letter)
# Story = [Spacer(1,1*inch)] 
Story = [] 

style = styles["Normal"]
# style.fontName = "Times-Roman"
style.fontName = "Helvetica"
style.bulletFontName = "Helvetica"
style.fontSize = 11
style.allowWidows = 0
style.allowOrphans = 0

def MapDataToFontSize(val):
    # Map combined (normalized to 1) data measure onto desired range and resolution 
    #   to return a font size
    # Here want sizes to range from 8 to 16 by two...
    if (val >= 0) & (val < 0.245):
        return 8
    elif (val >= 0.245) & (val < 0.495):
        return 10
    elif (val >= 0.495) & (val < 0.745):
        return 12
    elif (val >= 0.745) & (val <= 1.00):
        return 14
    else:
        return -1            # problem

def MapDataToColor(longVal, shortVal):
    # Map normalized data values into integers which can index color lookup matrix
    # Here calculating whether short data values are statistically same, greater or less than long
    if abs(shortVal - longVal) <= 0.2:
        return '#000000'    # black
    elif (shortVal - longVal) > 0.2:
        return '#8f0000'    # red
    else:
        return '#00008f'    # blue

def MapShortDataToColor(shortVal, shortMax):
    # Map normalized data values into colors
    # Here calculating based on short data fraction of max value (renormalizing)
    val = shortVal/shortMax
    
    if (val < 0):
        return shortColorGiven            # given
    elif (val >= 0) & (val < 0.33):
        return shortColor1
    elif (val >= 0.33) & (val < 0.66):
        return shortColor2
    elif (val >= 0.66) & (val <= 1.0):
        return shortColor3
    else:
        return shortColorProblem            # problem

def LabelConvert(label, type):
    if type == 1:           # Text
        return str(label)
    elif type == 2:         # Integer
        return str(int(label))
    

# Read in long version data
long_book = xlrd.open_workbook('long forms.xls')
long_sheet = long_book.sheet_by_index(0)
long_ids = long_sheet.col_values(1,1)
long_id_types = long_sheet.col_types(1,1)
long_selected = long_sheet.col_values(2,1)
long_ntotal = long_sheet.col_values(4,1)

# Some data labels are formatted as integers in Excel, so convert these to strings w/o decimals
long_labels = map(LabelConvert, long_ids, long_id_types)

labels_list = labelsList()
long_data = {}
for ii, id in enumerate(long_labels):
    long_data[id] = float(long_selected[ii])/float(long_ntotal[ii])
    labels_list.remove(id)

# Duplicate data for sentences which are combined in the long form
long_data['data137a'] = long_data['data137']
labels_list.remove('data137a')
long_data['data138a'] = long_data['data138']
labels_list.remove('data138a')
long_data['data139a'] = long_data['data139']
labels_list.remove('data139a')
long_data['data140a'] = long_data['data140']
labels_list.remove('data140a')

# Check that all labels assigned
if len(labels_list) > 0:
    print "ERROR: Not all labels use for long form data! \n"

# Read in short version data
short_book = xlrd.open_workbook('short forms.xls')
short_sheet = short_book.sheet_by_index(0)
short_ids = short_sheet.col_values(1,1)
short_id_types = short_sheet.col_types(1,1)
short_selected = short_sheet.col_values(2,1)
short_given = short_sheet.col_values(3,1)
short_ntotal = short_sheet.col_values(4,1)

# Some data labels are formatted as integers in Excel, so convert these to strings w/o decimals
short_labels = map(LabelConvert, short_ids, short_id_types)

labels_list = labelsList()
short_data = {}
for ii, id in enumerate(short_labels):
    short_data[id] = float(short_selected[ii])/float(short_ntotal[ii])
    # Option to choose all "Given" sentences as selected
    if short_given[ii] == 'Yes':
        short_data[id] = -1.0
    labels_list.remove(id)

# Duplicating data for sentences which are combined in short form
# Some of these we may want to set to zero instead of duplicating
short_data['data017a'] = short_data['data017']
labels_list.remove('data017a')
short_data['data021a'] = short_data['data021']
labels_list.remove('data021a')
short_data['data038a'] = short_data['data038']
labels_list.remove('data038a')
short_data['data038b'] = short_data['data038']
labels_list.remove('data038b')
short_data['data078a'] = short_data['data078']
labels_list.remove('data078a')
short_data['data079a'] = short_data['data079']
labels_list.remove('data079a')
short_data['data125a'] = short_data['data125']
labels_list.remove('data125a')
short_data['data126a'] = short_data['data126']
labels_list.remove('data126a')
short_data['data132a'] = short_data['data132']
labels_list.remove('data132a')
short_data['data135a'] = short_data['data135']
labels_list.remove('data135a')

# Check that all labels assigned
if len(labels_list) > 0:
    print "ERROR: Not all labels use for short form data! \n"


# Build up dictionary of font sizes and colors from the data
dict = {}
dict['spAfTitle'] = 24
dict['spBefSeq'] = 18
dict['spBefHds'] = 28
dict['seqLftInd'] = 16
dict['bulInd'] = 16
dict['bulTxtInd'] = 32

fmax = -1
fmin = 10000

labels_list = labelsList()
short_max = max(short_data.values())
# Build up dictionaries for later use in Template(w)
for id in labels_list:
    
    # Font size is based on "long form" data
    fontSize = MapDataToFontSize(long_data[id])
    dict['s_' + id] = fontSize
    if fontSize > fmax: fmax = fontSize
    if fontSize < fmin: fmin = fontSize
    
    # Statistically compare long and short data to generate a color
    dict['c_' + id] = MapShortDataToColor(short_data[id], short_max)
    
    # if doing data labels
    if WRITE_DATA_VALUES:
		# if doing data labels
		dict['lo_' + id] = '%d' % (int(100*long_data[id]))
		# dict['sh_' + id] = '%3.2f' % (fontSize)
		if (short_data[id] >= 0):
			dict['sh_' + id] = '%d' % (int(100*short_data[id]))
		else:
			dict['sh_' + id] = '-'
    
# Set paragraph leading based on font size bounds
style.spaceAfter = 7
style.leading = fmax*1.1
doc.bottomMargin = 1.25*inch

# Read in template document
f = open('LongVer_newLabelsPrelim3_rev6.html','r')
# If doing data labels
# f = open('LongVer_newLabelsDataPrelim3_rev5.html','r')

w = f.read()
f.close()

if WRITE_DATA_VALUES:
	whole_fsp = w.split('</font>')
	
	for ii,xx in enumerate(whole_fsp[1:-1]):
		# Make sure there is a space at the end of the sentence
		if xx[-1] != ' ':
			whole_fsp[ii+1] += ' '
			
		# Get the data label from each line
		dlStart = xx.find('${s_')
		dlEnd = xx.find('} color=${')
		dLabel = xx[dlStart+4:dlEnd]
		
		# Add data values piece & re-add </font> since removed with .split()
		whole_fsp[ii+1] += '(${lo_' + dLabel + '},${sh_' + dLabel + '}) </font>'
		
	w = ''.join(whole_fsp)


t = Template(w)
wsub = t.substitute(dict)
wlines = wsub.splitlines()

# Now, iterate through lines, detecting whether starts with '<para' or ends with '</para>'
# and construct paragraphs, appending them to the story, then build the PDF doc.
textList = []
for line in wlines:
    textList.append(line)
    if line.endswith('</para>'):
        p = Paragraph(''.join(textList), style)
        # print ''.join(textList)
        Story.append(p) 
        del textList[:] 
    
doc.build(Story, onFirstPage=myPages, onLaterPages=myPages)



