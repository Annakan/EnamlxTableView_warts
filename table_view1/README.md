# About this example

This is the original example, minus the threaded update.

## Flaws

* Impossible to select multiple lines
* We can't select one or multiple person to remove (always the last)
* Go to the last line, hit suppress => crash
* The spinner is not really working (a simple change to the loop and it will break and appear on the top left corner) see next example table_view2
* We are strangely looping over "range" and not the underliying person dataset
* 
