f = open('LongVersion_noCTabs_rev2.html', 'r')
whole = f.read()
whole_s1 = whole.split('${s_1')

for ii, xx in enumerate(whole_s1):
    whole_s1[ii] += ('${s_' + str(ii))
    

whole2 = ''.join(whole_s1)
fout = open('junk.html','w')
fout.write(whole2)
fout.close()

whole_c1 = whole2.split('${c_1')

for ii, xx in enumerate(whole_c1):
    whole_c1[ii] += ('${c_' + str(ii))
    

whole3 = ''.join(whole_c1)
fout = open('junk2.html','w')
fout.write(whole3)
fout.close()

#################

f = open('LongVersion_noCTabs_rev4.html','r')
whole4 = f.read()
whole_fsp = whole4.split('</font>')

for ii,xx in enumerate(whole_fsp[1:len(whole_fsp)]):
	if whole_fsp[ii][-1] != ' ':
		whole_fsp[ii][-1] += (' ')
	whole_fsp[ii] += ('(${lo_' + str(ii) + '}, ${sh_' + str(ii) + '}) </font>')
	
whole5 = ''.join(whole_fsp)
fout = open('junk3.html','w')
fout.write(whole5)
fout.close()