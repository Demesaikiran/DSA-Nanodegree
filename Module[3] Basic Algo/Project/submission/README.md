# Problem vs Algorithm
This project includes 7 code bases.

## Problem 1- Finding the square root of an integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

- Analysis of the algorithm: It is purely excluding half the length of the list so it turns out to be T(n) = T(n / 2) + C. It is similar to the `Binary search Algorithm` 

- We are just using a variable which is of constant order. 

- Time Complexity: O(log(n))
- Space Complexity: O(1) 


## Problem 2- Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

- The approach went like this, find a pivot element (using `binary search`) such that there are two sorted arrays. Check in which array does the target element reside. Then apply Binary Search on that array to find its position.

- Assumptions: There are no duplicates in the array
- We are not using extra calculation space other than input list. So we can consider it as constant order space.
- Thus if we isolate the number of iterations in relation to the input space (n), we obtain log(n) = recursive_depth

- Time Complexity: O(log(n))
- Space Complexity: O(1) and the input space is `O(n)`

## Problem 3- Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

- For `merge` operation it is taking about O(log(n)) and for making 
- As for the space complexity, if we hold the assumption that python gets automatically rid of each previous step auxiliary created arrays, then the space complexity is of O(n) (we have always arrays tat amount to the length of the input array).

- The algorithm that is implemented is merge sort in the code base.

- Time Complexity: O(nlog(n)).
- Space Complexity: O(n)

## Problem 4- Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

**Note**: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

- Here we are traversing from left to right with a mediator variable 'traverse'. Now, there are three cases when we see a '0' for traverse variable then we swap with the 'left' index variable. 
- Similarly with the 'right' index variable. We are traversing only once using the variable 'traverse'.
- In this code base we are processing the calcuations or any updation in the list itself. So the space complexity will be the length of the input list. other than that the space complexity is constant order

- Time complexity: O(n)
- Space complexity: O(1) // Excluding the input list length

## Problem 5- Autocomplete with Tries
To implement the autocomplete feature for words using Trie datastructure. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"]

- I have implemented a `Trie` Data structure with insert word, find prefix and, match prefix functionalities. Find_words function will find all words in a given prefix and return all matching words in a list format.


- Inserting a node will make O(n) complexity
- Finding the required stringtakes O(len(n)), n is the length of the string
- Find_words takes O(T) where T is the number of nodes in the trie.

- The above mentioned complexites makes the entire time complexity

- We are using `n` nodes in the Trie and space that takes is `O(n)`. find_words takes `O(n)` where n is the number of nodes in the Trie.  For instance, if all words in a dictionary are starting with a and search string is also a then it has to visit every node which is a linear operation.

## Problem 6- Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

- The approach of solving the required problem is first taking both `min` and `max` elements same that is first element and then uses `linear search` algorithm to check if the current element is greater or lesse than the min and max values and updating them accordingly.

- Time Complexity = `O(n)`, Since we iterate through each item once in the array.
- We are using input space as O(n) and the auxiliary space as O(1). Hence totally we are using `O(n)` space complexity

## Problem 7- HTTPRouter using a Trie


We are going to implement an HTTPRouter like we would find in a typical web server using the `Trie data structure` we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

The RouteTrie stores handlers under path parts.

- If the path is not found in the `Trie`, not found handler will be initiated and returns.

- In the worst case when we have a path with no common folders between them, a node for each path block will be created, resulting in a space complexity of O(n).

- The `time complexity` of searching, inserting, and deleting from a trie depends on the length of the word a that’s being searched for, inserted, or deleted, and the number of total words, `n`, making the runtime of these operations `O(a * n)`. Of course, for the longest word in the trie, inserting, searching, and deleting will take more time and memory than for the shortest word in the trie.

- Splitting a string to store individual parts of the path is dependent on the length of the string and the depth or level of the path, which could be quite large on a site with many pages. In any case, using a dictionary should be `O(n)`  which describes the `space complexity` where n is the count or number of components in the path.