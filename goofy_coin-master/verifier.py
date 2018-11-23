def verify_transaction(currnode):
    if(currnode.is_minted):
        val = str(currnode.me)+" "+str(currnode.me)+" "+str(currnode.value)
        if currnode.me.verify(val,currnode.signature):
            print "Fully Valid Transaction"
    else:
        val = str(currnode.from_person)+" "+str(currnode.me)+" "+str(currnode.value)
        if currnode.from_person.verify(val,currnode.signature):
            print str(currnode.from_person)+" "+str(currnode.me)+" "+str(currnode.value)
            print "Valid Transaction : Verifying Parent"
            verify_transaction(currnode.parent)
        else:
            print "INVALID"
