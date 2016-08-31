## Music Builder

Here we'll build the picture generator app. The input will be a dictionary in the form:

```python
music_example = {
	'time_sig': [4, 4],
	'measures': 2,
	'rhythm': [0.5, 0.5, 0.5, 0.5]
	'pattern': 'RLRL RLRR LRLRL RLL',
}
```

* `time_sig` is a two integer vector representing the numerator then the denominator
* `measures` is how many measures in the rudiment
* `rhythm` is the length of each note relative to the time signature.
* `pattern` is the hand pattern, white space will be trimmed. It's length must be an integer multiple of the rhythm vector's length (if longer than the rhythm vector, the rhythm vector will be repeated to match the length). If the combined `pattern` + `rhythm` length is less than the time specified by `meaurses`, it will also be duplicated. 