class Node:
    def __init__(self, val):
        self.val = val
        self.nextNode = None


class stack:
    def __init__(self):
	self.top = None

    def push(self, val):
	if not self.top:
	    self.top = Node(val)
	else:
	    nd = Node(val)
	    nd.nextNode = self.top
	    self.top = nd
	
    def pop(self):
	if not self.top:
    	    return -99999
	ret_obj = self.top
	self.top = self.top.nextNode
	ret_val = ret_obj.val
	del(ret_obj)
	return ret_val

    def isEmpty(self):
	return self.top is None

    def peek(self):
        if not self.top:
 	    return -99999
	return self.top.val


if __name__ == '__main__':
    stk = stack()
    print('This should print True.....answer is: {}'.format(stk.isEmpty()))
    print('This should print -99999.....answer is: {}'.format(stk.peek()))
    stk.push(1)
    stk.push(2)
    stk.push(3)
    print('This should print False.....answer is: {}'.format(stk.isEmpty()))
    print('This should print 3.....answer is: {}'.format(stk.peek()))	
    print('This should print 3.....answer is: {}'.format(stk.pop()))
    print('This should print 2.....answer is: {}'.format(stk.pop()))
    stk.push(55)
    print('This should print 55.....answer is: {}'.format(stk.pop()))
    print('This should print 1.....answer is: {}'.format(stk.pop()))
    print('This should print -99999.....answer is: {}'.format(stk.pop()))
    print('This should print True.....answer is: {}'.format(stk.isEmpty()))
    print('This should print -99999.....answer is: {}'.format(stk.peek()))
