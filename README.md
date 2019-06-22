 ## what is this about
This repos contains both some experiement showing annoying bugs in enamlx TableView and ways to work around then and have a working Qt grid in enaml.

## what's in it

Directories table_view 2/3/4 contain working programm that show working TableView while supporting deletion, including deletion of currectly "in-view" items and multiple item selection

They contain a small readme that explain the sample the encoutered bugs and the strategy used to work around them.

## wishes :)

Some enamlx TableView properties seems poorly named :
 * visible_row / table.visible_rows !!! : visible_row is the first row that can be  visible in the grid, visible_rowS is the number of rows the tableView will manage (probably more than it will display)  
 What about : first_item_to_display, nb_items_in_grid ? (item being the name of the property of the TableView that contain the displayed 'record')
 * `row` should probaly be named `row_id` because it is in fact a unique row identifier and row means more "the whole row".
  
> ##### Note for other developers :
>
>    It is convenient that `row` is mappable to a property of the undelying container, making the link between the undelying container and the displayed row. 
>    For instance when displaying items from a list (an Atom ContainerList) it can be the index in the list.
>    When the grid is displaying a portion of the underlying container from the 100th element to the 120th, the `row` property for each TableViewRow contains 100, 101, 102   
>    You could also use loop_index to store on the row a reference to the item diplayed.
>    Example use both 
