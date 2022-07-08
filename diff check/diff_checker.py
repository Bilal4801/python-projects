import json
import argparse, textwrap
import difflib                    						 # unified_diff,  ndiff, first_set.symmetric_difference(second_set)
from difflib import Differ, unified_diff, ndiff
import re

def sentence_maker(paragraph):
	return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)

def word_checker(input1, input2):
	st1 = ""
	st2 = ""
	lst1 = []
	lst2 = []
	wd_lst3 = []
	wd_lst4 = []		  				  		 				 # re.search(r"\bisn't\b", "it isn't bad") r word level search in re
	f_str = input1.splitlines(keepends=True)				 			 # using set you can find the difference between two strings
	s_str = input2.splitlines(keepends=True)

	# print(f_str)
	# print(s_str)
	# exit()
	for new1 in f_str:
		# print(len(new1))

		if len(new1) == 1:
			continue
		elif len(new1) > 1:
			lst1.append(new1)
		else:
			print('no newline in sentences')	

	for i in lst1:
		st1 +=i
	str1 = st1.replace('\n', '阿薩德')
	str1 = str1.strip()

	# print(str1)
	# exit()	

	for new2 in s_str:
		if len(new2) == 1:
			continue
		elif len(new2) > 1:
			lst2.append(new2)
		else:
			print('no newline in sentences')	

	for j in lst2:
		st2 +=j

	str2 = st2.replace('\n', '阿薩德')
	str2 = str2.strip()
	# print(str2)
	# exit()

	dif = Differ()

# This is for first case
	difference = list(dif.compare(str1.split(), str2.split()))
	diff2 = list(dif.compare(str2.split(), str1.split()))
	# print(difference,'\n')

	for word1,word2 in zip(difference, diff2):	   
		if word1.startswith('-'):      
			var = word1.replace(f'{word1}', f" <b class='diff'>{word1.replace('- ', '')}</b>")
			wd_lst3.append(var)

		elif word1.startswith('+ '):
			continue
			# if word1.endswith("阿薩德"):
			# 	wd_lst3.append("阿薩德")
			


		elif word1.startswith(' '):
			wd_lst3.append(word1)
		else:
			print('no')


		diff2 = list(dif.compare(str2.split(), str1.split()))
	# # print(diff2, '\n')

	for word2 in diff2:
		if word2.startswith('-'):
			new = word2.replace(f'{word2}', f" <b>{word2.replace('- ', '')}</b>")
			wd_lst4.append(new)
		
		if word2.startswith('+'):
			continue

		if word2.startswith(' '):
			wd_lst4.append(word2)	

		# if word2.startswith('-'):
		# 	new = word2.replace(f'{word2}', f" <b class='diff'>{word2.replace('- ', '')}</b>")
		# 	wd_lst4.append(new)
		
		# elif word2.startswith('+'):
		# 	continue
		# 	# if word2 == "+ 阿薩德":
		# 	# 	wd_lst4.append("ukh")#add list 3 there and list 4 opper
		# 	# 	print(word2+"aa")
		# 	# if word2 == '+ ':
		# 	# 	wd_lst4.append("阿薩德")

		# elif word2.startswith(' '):
		# 	wd_lst4.append(word2)
		# else:
		# 	print('no')

	# difference = list(dif.compare(str1.split(), str2.split()))
	# # print(difference,'\n')
	# # exit()

	# for word1 in difference:	   
	# 	if word1.startswith('-'):      
	# 		var = word1.replace(f'{word1}', f" <b>{word1.replace('- ', '')}</b>")
	# 		wd_lst3.append(var)

	# 	if word1.startswith('+'):
	# 		continue

	# 	if word1.startswith(' '):
	# 		wd_lst3.append(word1)

	# wd_lst3_join = ''.join(wd_lst3)
	# lst1_rep = wd_lst3_join.replace('  ', ' ')
	# # print(lst1_rep)

	# diff2 = list(dif.compare(str2.split(), str1.split()))
	# # print(diff2, '\n')

	# for word2 in diff2:
	# 	if word2.startswith('-'):
	# 		new = word2.replace(f'{word2}', f" <b>{word2.replace('- ', '')}</b>")
	# 		wd_lst4.append(new)
		
	# 	if word2.startswith('+'):
	# 		continue

		if word2.startswith(' '):
			wd_lst4.append(word2)

	wd_lst4_join = ''.join(wd_lst4)
	lst2_rep = wd_lst4_join.replace('  ', ' ')		
	return lst1_rep, lst2_rep
		

	wd_lst3_join = ''.join(wd_lst3)
	lst1_rep = wd_lst3_join.replace('  ', ' ')

	wd_lst4_join = ''.join(wd_lst4)
	lst2_rep = wd_lst4_join.replace('  ', ' ')
	
	res1=lst1_rep.replace("阿薩德",'<br>')	
	res2=lst2_rep.replace("阿薩德",'<br>')	
	# print(res1,res2)
	# res1=res1[:-1]
	# res2=res2[:-1]
	
	
	return res1,res2

# Linebase difference checker
def sentence_checker(input_str1, input_str2):
	lst3 = []
	lst4 = []

	str1 = sentence_maker(input_str1)
	str2 = sentence_maker(input_str2)

	d = Differ()
	compr = list(d.compare(str1, str2))

	for sent in compr:
		if sent.startswith('-'):
			rep = sent.replace(f'{sent}', f" <b class='diff'>{sent.replace('- ', '')}</b>")
			lst3.append(rep)

		if sent.startswith('+'):
			continue

		if sent.startswith(' '):
			lst3.append(sent)

	sent_jn1 = ''.join(lst3)		

	comp2 = list(d.compare(str2, str1))
	# print(comp2, '\n')
	for sent2 in comp2:
		if sent2.startswith('-'):
			repl = sent2.replace(f'{sent2}', f" <b class='diff'>{sent2.replace('- ', '')}</b>")
			lst4.append(repl)

		if sent2.startswith('+ '):
			continue

		if sent2.startswith(' '):
			lst4.append(sent2)

	sent_jn2 = ''.join(lst4)		
	return sent_jn1, sent_jn2

def char_checker(s1, s2):
	af_lst1 = []
	af_lst2 = []
	
	# ch_diff = Differ()
	# ch_comp = list(ch_diff.compare(s1, s2))
	ch_comp = list(ndiff(s1, s2))
	# print(ch_comp)
	# exit()

	for char1 in ch_comp:
		if char1.startswith('-'):
			ch_rep1 = char1.replace(f'{char1}', f"<b class='diff'>{char1.replace('- ', '')}</b>")
			af_lst1.append(ch_rep1)

		if char1.startswith('+'): 
			continue

		if char1.startswith(' '):
			af_lst1.append(char1)		

	ch_jn = ''.join(af_lst1)
	sp_rep1 = ch_jn.replace('  ', '')
	return sp_rep1


# Character base difference checker
def character_checker(st1, st2):
	ch_lst1 = []
	ch_lst2 = []

	ch_str1 = sentence_maker(st1)
	ch_str2 = sentence_maker(st2)
	result_list_div1 = []
	for a, b in zip(ch_str1, ch_str2):
		response = char_checker(a,b)
		result_list_div1.append(response)
	result_list_div1 = " ".join(result_list_div1)


	result_list_div2 = []
	for a, b in zip(ch_str1, ch_str2):
		response2 = char_checker(b,a)
		result_list_div2.append(response2)
	result_list_div2 = " ".join(result_list_div2)

	return result_list_div1, result_list_div2