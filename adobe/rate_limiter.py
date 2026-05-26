"""

Design a rate limiter that allows at most `N` requests per `T` seconds per user.

First line:
`N T`

where:

* **N** = maximum allowed requests
* **T** = time window in seconds

Next lines contain requests:
`username timestamp`

---

### Sample Input

```text
3 10
alice 1
alice 2
alice 5
alice 8
alice 12
alice 15

```

### Sample Output:

```text
True
True
True
False
True
True

```

---

### Another Sample:

```text
2 5

alice 1
bob 2
alice 3
bob 4
alice 5
bob 6
alice 7
bob 8

```

### Output::

```text
True
True
True
True
False
False
True
True

```


=========== Solution: =================

dictionary of key = user-id
value = list of time stamps

After I read the first row, I get the allowed max size of the list and time window

configuration.

Read each line -

get list the user,

if list len is less than max, append to end and say True or Allowed
if list len is equal to max, check the time stamp of first item in the list, compare with current time stamp - time window
 if greater-equal, remove first item, add current item to end and say True or Allowed
 else, fail and say false

 alice 1 - [1] True
 alice 2 - [1, 2] True
 alice 5 - [1, 2, 5] True
 alice 8 - [1, 2, 5] False
 alice 11 - [2, 5, 11] True
 alice 12
"""
