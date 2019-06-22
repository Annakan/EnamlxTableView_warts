# About this example

Here we are looping over the underlying container and that seems more natural

## Flaws

* `selection` property is completely broken (always off by one, try to CTRL+click disjoint row/cells etc ...)
* The spinner is still obviously broken, uncomment lines 83/84 in the table_view.enaml to see it.

## Improvements
* you can now select select multiple lines
* ...And remove them
* Go to the last line, hit suppress =>  No crash
* Select ajdjacent or disjoint cells and suppres = > no crash
* When suppressing at the end, we have a delay in and sometimes "empyt row flashing", 
  probably indicating that we somehow trigger an unecessary  flurry of subscriptions. 

## Comments

### Conflicted onwership and non atomicity of changes 
We still have to protect ourselves agains destroying a row that is visible or acting on a row that has been destroyed ;
```python 
row <<  table.visible_row + loop_index if table.visible_row + loop_index < max_row else -1
```

### Selection handling

We still can't rely on enamlx tableview selection management.

Here we try to insulate the "model" code from accessing the widget through a `selected` property/attr 

```python
# the following is nice but not working because no subscription will be taken on the items from the iterable
# attr selected_rows << {index for index in (s_index.row() for s_index in self.proxy.widget.selectedIndexes()) }
attr selected_rows << {items[index] for index in (s_index.row() for s_index in self.proxy.widget.selectedIndexes()) if index < len(model.people)}
```

I don't know what strategy is the most efficient (range or container, selected property or passing the selection info from the widget)
