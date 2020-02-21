class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def is_unival(self):
    	if self.val==None:
    		return True
    	
    	return self.left.is_unival() and
    			(self.left.val == self.val if self.left.val else True) and
    			self.right.is_unival() and
    			(self.right.val == self.val if self.right.val else True)
    			
def number_of_unival_nodes(node):
	left = number_of_unival_nodes(node.left)
	right = number_of_unival_nodes(node.right) 
	
	if node.is_unival():
		return 1 + left + right
	else:
		return left + right
	
	
