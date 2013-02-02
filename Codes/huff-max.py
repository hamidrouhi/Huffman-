#!/usr/bin/python
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

