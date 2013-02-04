#!/usr/bin/python
#
# hrouhi.kh(At)gmail(.)com
#


def heap_gen(L):
	global tree,parent
	tree=list(Data)
	while len(tree)>1:
		LeftChild=min(tree)
		index=tree.index(LeftChild)
		LeftChidindex=list(tree[index])
		del tree[index]
		RightChild=min(tree)
		index=tree.index(RightChild)
		RightChildindex=list(RightChild)
		del tree[index]
		parent=(LeftChidindex[0]+RightChildindex[0],LeftChild,RightChild)
		tree.append(parent)
	return tree[0]

def codes(huffheap, hbeats = ''):
	global probs,var_list_
	if len(huffheap) == 2:
		print huffheap[1], hbeats
		Prob_i=int(data_for_get_avrg_len[huffheap[1]])
		Num_i=len(hbeats)
		Nbar=float(Prob_i*Num_i)
		Var_i=float(Prob_i*((Num_i-Nbar)** 2 ))
		probs.append(Nbar)
		var_list_.append(Var_i)
	else:
		codes(huffheap[1], hbeats + '0')
		codes(huffheap[2], hbeats + '1')
	
def avrg_len(probs):	
	Z_n_=sum(probs)
	return Z_n_

def variance_of_codes(var_list_):
	Z_var_=sum(var_list_)
	return Z_var_

def get_probs():
	print "Symbolls : "
	Symbolls=int(raw_input("++>"))
	for i in range(1,Symbolls):
		print "Symboll %d :"%i
		Char=str(raw_input("symboll  ==> : "))
		Num=float(raw_input("probability ==> : "))
		print
		data=Num,Char
		Data.append((tuple(data)))
		data_for_get_avrg_len[Char]=Num
		if i==Symbolls:break
	huffheap = heap_gen(Data)
	codes(huffheap)

if __name__ == '__main__':
	Data=[];probs=[];var_list_=[]
	data_for_get_avrg_len={}
	try:	
		get_probs()
	except ValueError:
		print "Enter num of symbolls !"
	except KeyboardInterrupt:
		print "Oops , try again!!!"
	av_len_=avrg_len(probs)
	var_all_code_=variance_of_codes(var_list_)
	print "\nLenght: ",av_len_," bit\n"
	print "Total var: ",var_all_code_," bit/symbol\n"

