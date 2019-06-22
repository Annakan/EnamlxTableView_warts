# About this example

Here we are still looping over a "range of intergers" as per example 1

## Flaws

* selected property is completely broken (off by one, try to CTRL+click)
* The spinner is now obviously broken, uncomment lines 83/84 in the table_view.enaml to see it.

## Improvements
* you can now select select multiple lines
* ...And remove them
* Go to the last line, hit suppress =>  No crash
* When suppressing at the end, we have a delay in and sometimes "empyt row flashing", 
  probably indicating that we somehow trigger an unecessary  flurry of subscriptions. 

## Comments

### Conflicted onwership and non atomicity of changes 
We start to protect ourselves agains destroying a row that is visible or acting on a row that has been destroyed ;
```python 
row <<  table.visible_row + loop_index if table.visible_row + loop_index < max_row else -1
```

because the more natural this : 
```python
row <<  model.people.index(person)
```
is not working (the person can be destroyed while the row is refreshed ... 
GUI threads ? too strong or toow weak ownership between enaml, enamlx and Qt ?)

See the block of code lines 51-60


### Selection handling

We can't rely on enamlx tableview selection management

We have to pass the underlying widget (qt)  `selectedIndexes` property **when** the remove button is clicked
and then extract the row value and then delete the objects . 
Ugly, pobably inneficient but working.
```python
 model.remove_persons(table.proxy.widget.selectedIndexes())
 table.looper.refresh_items() 
```
The interpretation of the `selectedIndexes`  is a wonly affair :
* First we have to extract the unique rowids : it is possible to have two cells selected on the same row 
plus two other celles in different rows and columns, in that case we only retrieve three distincts rowids.
* Then we have to sort them in reverse numerical order to have a safe removal of the objects in the underlaying container list)

