"""
=========================== Concept question = 2 ===============================

Precision = TP/(TP + FP) = Out of whatever we claimed as true, how many are actually true
Recaall = TP/(TP + FN) = Out of whatever were actually true, how many did we catch


Fraud = true
No Fraud = False

100 Transactions - 2 are True and 98 are False
Our classifier catches 1 and leaves another - TP is 1, FN is 1, 98 = Transactions

Precision = 1/(1 + 0) = 100%
Recall = 1/(1 + 1) = 50%

=========================== Coding question = 1 ===============================


A: 150
B: 190
C: 300
D: 400

constraint 0: you can only read the elements sequentially, i.e. pop(0)
you are allowed to keep state.
constraint 1: All elements of a certain class, regardless of the position in the stream, should have an equal possibility of getting selected


Possible algorithm - 1:

1. first I start filling by category i.e. until the elements get to the limit
2. if I start encountering elements after filling , I do a electronic toss and put it in based on that.

3 = A

A B B A C D A A B B A B A
0 1 2

A0, A3, A6,

encountered_count_dict ={
A: 3,
B: ..

}

Algo 1:

1. Fill it up till the limit

2. After filling to add new elements, A7 - electronic toss of (1/4-dict) true = 25% suppose we have 1/4

if success, I push it into the output array and update the count in the dictionary; else you still update

=========
Assume just A, 5 As, and 2 as the limit - calculate the fairness

1. First A is 100% prob of insertion - 1/3 of removal
2. Second A is 100% prob of insertion (1/3 of previous being removed) * 1/4 of removing this one
3. Third A is 1/3 of insertion
4. Fourth will have 1/4 of insertion
5. Fifth will have 1/5th of insertion


Suppose the limit is 3, and we have encounterd 4

So each element has to have a 3/4 probability of being present. - fairness
My algorithm is doing is we are only checking the first in the queue and the most recently encountered.
Improvement - Instead of doing the electronic toss on 1/4 and pushing out - we do it for 3/4 on all elements
Whatever is in the queue and the newly encounterd one

take the n + 1 elements - randomly sort them and do n/(n+1) electronic toss and start pushing the elements in till it gets full


n/n+1 = 150/151 = then it may favor the early ones - randomly sort

"""

def randomize(input: list[int]) -> list[int]:
    pass

def insert_into_output(element, output, ratio_dict):

    category = element["category"]
    category_max = ratio_dict[category]

    if not output[category] or len(output[category]) < category_max:
        # inserting while empty or less
        output[category].append(element)
    else:
        # here we have determined that the output[category] is full
        intermediate = output[category].append(element)
        randomize(intermediate)
        for candidate in intermediate:
            electronic_toss


def sample_elements(input, ratio_dict):

    output = {

    }

    for element in input:
        #
        insert_into_output(element, output, ratio_dict)

    return output


#----
