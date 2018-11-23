import SinglyLinkedList as ll
import NodeofList as node
import listvar as glob
import datetime
import verifier as vf

class goofy_coin:

    def __init__(self,pub_key,start_amount,sign):
        glob.goofy_list = ll.SinglyLinkedList()
        genesis = node.ListNode(start_amount)
        genesis.me = pub_key
        genesis.id = datetime.datetime.now()
        genesis.signature=sign
        genesis.is_minted=True
        glob.goofy_list.add_node(genesis)

    def makecoin(self,pub_key,value, sign):
        temp_block = node.ListNode(value)
        temp_block.given_to=pub_key
        temp_block.me = pub_key
        temp_block.value = value
        temp_block.id = datetime.datetime.now()
        temp_block.signature=sign
        temp_block.is_minted=True
        glob.goofy_list.add_node(temp_block)

    def transaction(self, from_person, to_person, value, pri_key_sen):
        #### NODE OF GIVING TO OTHER ####
        temp_block = node.ListNode(value)
        temp_block.me = to_person
        temp_block.value = value
        temp_block.id = datetime.datetime.now()
        #### NODE OF GIVING TO MYSELF ####
        temp_block2 = node.ListNode(value)
        temp_block2.me = from_person
        temp_block2.id = datetime.datetime.now()

        #glob.goofy_list.add_node(temp_block)
        currnode = glob.goofy_list.head
        flag = 0
        while currnode is not None:
            if str(currnode.me) == str(from_person):
                if currnode.value >= value and currnode.spent == False:
                    flag = 1
                    temp_block.parent = currnode
                    temp_block.signature = pri_key_sen.sign(str(from_person)+" "+str(to_person)+" "+str(value),'')
                    temp_block2.parent = currnode
                    temp_block.from_person=currnode.me
                    temp_block2.signature = pri_key_sen.sign(str(from_person)+" "+str(from_person)+" "+str(currnode.value-value),'')
                    currnode.given_to = to_person
                    if currnode.value != value:
                        temp_block2.value= currnode.value-value
                        temp_block2.from_person=currnode.me
                        glob.goofy_list.add_node(temp_block)
                        glob.goofy_list.add_node(temp_block2)
                    else:
                        glob.goofy_list.add_node(temp_block)
                    currnode.spent=True
                    break
            currnode=currnode.next

        if flag == 0:
            print "Transaction Failed"


    def print_goofy_list(self):
        glob.goofy_list.print_list()

    def search_goofy_list(self,value):
        return glob.goofy_list.search_list(value)

    def transaction_verify(self, id_of_tr):
        currnode = glob.goofy_list.head
        flag =0
        while currnode is not None:
            if str(id_of_tr) == str(currnode.id):
                vf.verify_transaction(currnode)
                flag =1
                break
            currnode=currnode.next
        if flag == 0:
            print "Invalid Transaction Id"



################################## TEST CODE ##################################
# g=goofy_coin()
# g.makecoin(23)
# g.makecoin(212)
# g.transaction("##GOOFY##","Sunchit",284)
# g.transaction("Sunchit","Sameer",28)
# g.print_goofy_list()
#
# print g.search_goofy_list(123)
# print "HERE"
###############################################################################
