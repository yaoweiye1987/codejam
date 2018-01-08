class ListNode(object):
  def __init__(self, x):
    self.val = x 
    self.next = None 

dummy = ListNode(0) 
dummy.next = ListNode(1) 

print (dummy.next.val) 

