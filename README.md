# pairfinder

https://pairfinder.herokuapp.com/

A web app for pairing people together based on shared preferences. The matching found will be a [maximum cardinality matching](https://en.wikipedia.org/wiki/Maximum_cardinality_matching).


### Example
Given the following table:
|Name|Pref1|Pref2|Pref3|Pref4|
|----|-----|-----|-----|-----|
|A   |x    |     |x    |     |
|B   |     |x    |     |x    |
|C   |     |x    |     |     |
|D   |x    |     |     |x    |

A will be matched with D (both share Pref1), and B will be matched with C (both share Pref2). Although B and D is a valid pairing (both share Pref4) they will never be put together, since pairing B and D will leave A and C unmatched. 


### Todos
* [ ] Implement file upload validation
* [ ] Allow for file to automatically populate table upon upload (in progress)

