import NodeofList as node

class SinglyLinkedList:

    def __init__(self): # FINAL
        self.head=None
        self.tail=None
        return

    def add_node(self, item): # HAVE TO MODIFY TO SUIT NEEDS
        if not isinstance(item,node.ListNode):
            item = node.ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next=item
        self.tail=item
        return

    def list_len(self): # FINAL
        count =0;
        currnode = self.head
        while currnode is not None:
            count =count + 1
            currnode=currnode.next
        return count

    def print_list(self): # MAY NEED MODIFICATION
        currnode = self.head
        while currnode is not None:
            print "________________"
            print "VALUE : "+str(currnode.value)
            print "PARENT LINK: "+str(currnode.parent)
            print "TAKEN FROM : "+str(currnode.from_person)
            print "OWNER : "+str(currnode.me)
            print "GIVEN TO : "+str(currnode.given_to)
            print "IS SPENT : "+str(currnode.spent)
            print "TRANSACTION ID : "+str(currnode.id)
            print "IS MINTED : "+str(currnode.is_minted)
            print "SIGNATURE : "+str(currnode.signature)
            print "________________"
            currnode=currnode.next
        return

    def search_list(self,value): # MAY NEED MODIFICATION
        currnode = self.head

        node_id=0;
        answer=[]

        while currnode is not None:
            if currnode.has_value(value):
                answer.append(node_id)
            currnode=currnode.next
            node_id=node_id+1

        return answer

####################################### TEST CODE ##################################
# node1 =node.ListNode(15)
# node2 =node.ListNode("china")
# item3 = 23
#
# alist= SinglyLinkedList()
# print("List Length : %i" % alist.list_len())
#
# for curr_item in [node1, node2, item3]:
#     alist.add_node(curr_item)
#     print("List Length : %i" % alist.list_len())
#     alist.print_list()
#
# x=alist.search_list(23)
# print x
####################################################################################
