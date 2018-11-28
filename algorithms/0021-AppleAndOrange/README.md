# Apple and Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, we have his house, where **s** is the start point, and **t** is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point **a**, and the orange tree is at point **b**.

```
          ============                                   ============                            ============
           apples tree                                       house                               oranges tree
          ============                                   ============                            ============
          
          &&& &&  & &&                                  __- -                                    &&& &&  & &&
      && &\/&\|& ()|/ @, &&                            (                                     && &\/&\|& ()|/ @, &&
      &\/(/&/&||/& /_/)_&/_&                          _))_                                   &\/(/&/&||/& /_/)_&/_&
   &() &\/&|()|/&\/ '%" & ()                          |  |________                        &() &\/&|()|/&\/ '%" & ()
  &_\_&&_\ |& |&&/&__%_/_& &&                .-------"""""   |    """""------.           &_\_&&_\ |& |&&/&__%_/_& &&
&&   && & &| &| /& & % ()& /&&              /.".\            |            /.".\        &&   && & &| &| /& & % ()& /&&
 ()&_---()&\&\|&&-&&--%---()~              /.   .\           |           /.   .\         ()&_---()&\&\|&&-&&--%---()~
     &&     \|||                          /.     .\          |          /.     .\             &&     \|||
             |||                         /.  ___ '.|__....--"T"--....__|.' ___  .\                     |||
             |||                        |   |_|_|  |   _..   |   --.   |  |_|_|  |                     |||
             |||                        |   |_|_|  |  |  |   |   |_|   |  |_|_|  |                     |||
       , -=-~  .-^- _                   |__________|__|..+--"""--....__|_________|               , -=-~  .-^- _

                        apple                          apple                orange                                  orange
====================================================================================================================================
             a -------->                <---------------------------------------->                      b
                   d                    s                                        t
```

When a fruit falls from its tree, it lands **d** units of distance from its tree of origin along the **x-axis**. A negative value of **d** means the fruit fell **d** units to the tree's left, and a positive value of **d** means it falls **d** units to the tree's right.

Given the value of **d** for **m** apples and **n** oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range **[s, t]**)?

For example, Sam's house is between **s = 7** and **t = 10**. The apple tree is located at **a = 4** and the orange at **b = 12**. There are **m = 3** apples and **n = 3** oranges. Apples are thrown **apples = [2, 3, -4]** units distance from **a**, and **oranges = [3, -2, -4]** units distance. Adding each apple distance to the position of the tree, they land at **[4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]**. Oranges land at **[12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]**. One apple and two oranges land in the inclusive range **7 - 10** so we return:
```
(1, 2)
```

# Function Description

Implement the ```countApplesAndOranges``` function. It should return a tuple representing the number of apples and oranges that land on Sam's house.

```countApplesAndOranges``` has the following parameter(s):

* **houseStart:** (**s** in the diagram) integer, starting point of Sam's house location.
* **houseEnd:** (**t** in the diagram)integer, ending location of Sam's house location.
* **applesTreeLocation:** (**a** in the diagram) integer, location of the Apple tree.
* **orangesTreeLocation:** (**b** in the diagram) integer, location of the Orange tree.
* **apples:** integer array, distances at which each apple falls from the tree.
* **oranges:** integer array, distances at which each orange falls from the tree.

# Input and Output Format

```python
countApplesAndOranges(
    house_start = 7,
    house_end = 10,
    apples_tree_location = 4,
    oranges_tree_location = 12 ,
    apple_distances = [2, 3, -4],
    orange_distances = [3, -2, -4]
)
# output:
# (1, 2)
```


# Explanation

* The first apple falls at position **4 + 2 = 6**. 

* The second apple falls at position **4 + 3 = 7**. 

* The third apple falls at position **4 + -4 = 0**. 

* The first orange falls at position **12 + 3 = 15**. 

* The second orange falls at position **12 + -2 = 10**. 

* The third orange falls at position **12 + -4 = 8**. 

* Only one fruit (the second apple) falls within the region between **7** and **10**, so we set **1** as the first item of the returned tuple. 

* Two oranges (second and third) fall within the region between **7** and **10**, so we set **2** as the second item of the returned tuple. 