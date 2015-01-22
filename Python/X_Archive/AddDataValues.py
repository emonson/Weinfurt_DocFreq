# This does most of it, but since 125 is doubled in original html doc, had to
# hand-reduce after that point and remove very last entry

f = open('LongVersion_noCTabs_rev4.html','r')
whole4 = f.read()
whole_fsp = whole4.split('</font>')

for ii,xx in enumerate(whole_fsp[1:len(whole_fsp)]):
	if xx[-1] != ' ':
		whole_fsp[ii+1] += ' '
	whole_fsp[ii+1] += '(${lo_' + str(ii) + '}, ${sh_' + str(ii) + '}) </font>'
	
whole5 = ''.join(whole_fsp)
fout = open('junk3.html','w')
fout.write(whole5)
fout.close()