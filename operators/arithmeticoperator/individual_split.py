head_count=5
bill_amount=250
#gst_percentage=18%
gst=(8/100)*bill_amount
bill_amount=bill_amount+gst
individual_split=bill_amount/head_count

print(individual_split)
