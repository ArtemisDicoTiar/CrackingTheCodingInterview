# Arrays and Strings

## Hash Tables

* Highly efficient for **look up** values using keys

### Implementation
* Requirements: Linked lists, hash code function.

~~~
# Insert key and value
1. compute key's hash code with hash function.
(different key may have same hash code)
(b/c infinite # of keys -> finite # of integers)

2. Map hashcode -> index of array
eg. 
hash(key) % array_length
This index becomes the place to insert value.

3. Insert the value into the index

** Caution
The reason for using linked list:
If hash code collides -> append to linked list.
~~~

* Time complexity
    * key -> value access: O(1)
    * linked list iteration (hash code collision): worst -> O(n) 
* Appendix
    * binary search tree can also be used instead of linked list.
        * This case the worst time complexity becomes O(log N)
        * Advantage: 
            * uses less space (better Space Complexity)
            * can iterate through keys in order.

## ArrayList & Resizable Arrays
* Depending on the programming language, the arrays can be automatically resizable.
(available: Python, JavaScript / Unavailable: Java, C/C++)

### How to build dynamic resizable array (ArrayList)
Example: String data
* Access Time Complexity: O(1)
* Size Doubling (when the array is full): O(n) (worst)
    * resizing factor can vary.
* -> Rarely happens -> amortised insertion: O(1)
    * Why?
    * Let the array size is N.
    * Compute how many elements are copied every stage.
        * first: 1
        * second: 2
        * third: 4
        * ...
        * previous capacity increase: n/2
        * final: n
    * therefore, increase to capacity of K -> k/2 should be copied.
    * total: n/2 + n/4 + n/8 + *** + 4 + 2 + 1 ~= n (<n)
~~~Java
ArrayList <String> merge(String[] words, String[] more) {
    ArrayList <String> sentence = new ArrayList<String>();
    for (String w: words) sentence.add(w);
    for (String w: more) sentence.add(w);
    return sentence;
} 
~~~

## StringBuilder
Concatenating list of string 
* python can be done just by adding list with + operator
* However, C/C++ or Java requires some function to concat.


Example Code
* Time Complexity: O(xn^2)
    * Why:
    * first iteration: copy x characters
    * second iteration: copy 2x characters
    * third iteration: 3x
    * total: x + 2x + 3x + *** + nx
~~~Java
String joinWords(String[] words) {
    String sentence = "";
    for (String w: words) {
        sentence = sentence + w;
    }
    return sentence;
}
~~~

Fixed version: use resizable array for all strings -> when necessary
~~~Java
String joinWords (Stirng[] words) {
    StringBuilder sentence = new StringBuilder();
    for (String w: words) {
        sentence.append(w);
    }
    return sentence.toString();
}
~~~


