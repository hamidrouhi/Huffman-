#!/usr/bin/python
#
# hrouhi.kh(At)gmail(.)com
#


def heap_gen(L):
	global tree,parent
	tree=list(Data)
	while len(tree)>1:
		LCh=min(tree)
		index=tree.index(LCh)
		LChL=list(tree[index])
		del tree[index]
		RCh=min(tree)
		index=tree.index(RCh)
		RChL=list(RCh)
		del tree[index]
		parent=(LChL[0]+RChL[0],LCh,RCh)
		tree.append(parent)
	return tree[0]

def codes(huffheap, hbeats = ''):
	global probs,var_list_
	if len(huffheap) == 2:
		print huffheap[1], hbeats
		Pi=int(data_for_get_avrg_len[huffheap[1]])
		Ni=len(hbeats)
		Nbar=float(Pi*Ni)
		Vi=float(Pi*((Ni-Nbar)** 2 ))
		probs.append(Nbar)
		var_list_.append(Vi)
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
	print "Symbolss : "
	Symbs=int(raw_input("++>"))
	for i in range(l,Symbs+1):
		print "Symbol %d :"%i
		Char=str(raw_input("symbol  ==> : "))
		Num=float(raw_input("probability ==> : "))
		print
		data=Num,Char
		Data.append((tuple(data)))
		data_for_get_avrg_len[Char]=Num
		if i==Symbs:break
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

