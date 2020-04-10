<!-- Generated by documentation.js. Update this documentation by updating the source code. -->

### Table of Contents

-   [DataFrame][1]
    -   [toDSV][2]
    -   [toCSV][3]
    -   [toTSV][4]
    -   [toPSV][5]
    -   [toText][6]
    -   [toJSON][7]
    -   [toDict][8]
    -   [toArray][9]
    -   [toCollection][10]
    -   [show][11]
    -   [dim][12]
    -   [transpose][13]
    -   [count][14]
    -   [countValue][15]
    -   [push][16]
    -   [replace][17]
    -   [distinct][18]
    -   [unique][19]
    -   [listColumns][20]
    -   [select][21]
    -   [withColumn][22]
    -   [restructure][23]
    -   [renameAll][24]
    -   [rename][25]
    -   [castAll][26]
    -   [cast][27]
    -   [drop][28]
    -   [chain][29]
    -   [filter][30]
    -   [where][31]
    -   [find][32]
    -   [map][33]
    -   [reduce][34]
    -   [reduceRight][35]
    -   [dropDuplicates][36]
    -   [dropMissingValues][37]
    -   [fillMissingValues][38]
    -   [shuffle][39]
    -   [sample][40]
    -   [bisect][41]
    -   [groupBy][42]
    -   [sortBy][43]
    -   [union][44]
    -   [join][45]
    -   [innerJoin][46]
    -   [fullJoin][47]
    -   [outerJoin][48]
    -   [leftJoin][49]
    -   [rightJoin][50]
    -   [diff][51]
    -   [head][52]
    -   [tail][53]
    -   [slice][54]
    -   [getRow][55]
    -   [setRow][56]
    -   [setDefaultModules][57]
    -   [fromDSV][58]
    -   [fromText][59]
    -   [fromCSV][60]
    -   [fromTSV][61]
    -   [fromPSV][62]
    -   [fromJSON][63]

## DataFrame

[src/dataframe.js:11-1243][64]

DataFrame data structure providing an immutable, flexible and powerfull way to manipulate data with columns and rows.

**Parameters**

-   `data` **([Array][65] \| [Object][66] \| [DataFrame][67])** The data of the DataFrame.
-   `columns` **[Array][65]** The DataFrame column names.
-   `options` **[Object][66]** Additional options. Example: modules. (optional, default `{}`)

### toDSV

[src/dataframe.js:313-315][68]

Convert the DataFrame into a text delimiter separated values. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `sep` **[String][69]** Column separator. (optional, default `' '`)
-   `header` **[Boolean][70]** Writing the header in the first line. If false, there will be no header. (optional, default `true`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toDSV()
df.toDSV(';')
df.toDSV(';', true)
// From node.js only
df.toDSV(';', true, '/my/absolute/path/dataframe.txt')
```

Returns **[String][69]** The text file in raw string.

### toCSV

[src/dataframe.js:328-330][71]

Convert the DataFrame into a comma separated values string. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `header` **[Boolean][70]** Writing the header in the first line. If false, there will be no header. (optional, default `true`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toCSV()
df.toCSV(true)
// From node.js only
df.toCSV(true, '/my/absolute/path/dataframe.csv')
```

Returns **[String][69]** The csv file in raw string.

### toTSV

[src/dataframe.js:343-345][72]

Convert the DataFrame into a tab separated values string. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `header` **[Boolean][70]** Writing the header in the first line. If false, there will be no header. (optional, default `true`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toCSV()
df.toCSV(true)
// From node.js only
df.toCSV(true, '/my/absolute/path/dataframe.csv')
```

Returns **[String][69]** The csv file in raw string.

### toPSV

[src/dataframe.js:358-360][73]

Convert the DataFrame into a pipe separated values string. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `header` **[Boolean][70]** Writing the header in the first line. If false, there will be no header. (optional, default `true`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toPSV()
df.toPSV(true)
// From node.js only
df.toPSV(true, '/my/absolute/path/dataframe.csv')
```

Returns **[String][69]** The csv file in raw string.

### toText

[src/dataframe.js:375-377][74]

Convert the DataFrame into a text delimiter separated values. Alias for .toDSV. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `sep` **[String][69]** Column separator. (optional, default `' '`)
-   `header` **[Boolean][70]** Writing the header in the first line. If false, there will be no header. (optional, default `true`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toText()
df.toText(';')
df.toText(';', true)
// From node.js only
df.toText(';', true, '/my/absolute/path/dataframe.txt')
```

Returns **[String][69]** The text file in raw string.

### toJSON

[src/dataframe.js:389-391][75]

Convert the DataFrame into a json string. You can also save the file if you are using nodejs.

**Parameters**

-   `args` **...any** 
-   `asCollection` **[Boolean][70]** Writing the JSON as collection of Object. (optional, default `false`)
-   `path` **[String][69]?** The path to save the file. /!\\ Works only on node.js, not into the browser.

**Examples**

```javascript
df.toJSON()
// From node.js only
df.toJSON('/my/absolute/path/dataframe.json')
```

Returns **[String][69]** The json file in raw string.

### toDict

[src/dataframe.js:399-406][76]

Convert DataFrame into dict / hash / object.

**Examples**

```javascript
df.toDict()
```

Returns **[Object][66]** The DataFrame converted into dict.

### toArray

[src/dataframe.js:415-419][77]

Convert DataFrame into Array of Arrays. You can also extract only one column as Array.

**Parameters**

-   `columnName` **[String][69]?** Column Name to extract. By default, all columns are transformed.

**Examples**

```javascript
df.toArray()
```

Returns **[Array][65]** The DataFrame (or the column) converted into Array.

### toCollection

[src/dataframe.js:428-432][78]

Convert DataFrame into Array of dictionnaries. You can also return Rows instead of dictionnaries.

**Parameters**

-   `ofRows` **[Boolean][70]?** Return a collection of Rows instead of dictionnaries.

**Examples**

```javascript
df.toCollection()
```

Returns **[Array][65]** The DataFrame converted into Array of dictionnaries (or Rows).

### show

[src/dataframe.js:444-473][79]

Display the DataFrame as String Table. Can only return a sring instead of displaying the DataFrame.

**Parameters**

-   `rows` **[Number][80]** The number of lines to display. (optional, default `10`)
-   `quiet` **[Boolean][70]** Quiet mode. If true, only returns a string instead of console.log(). (optional, default `false`)

**Examples**

```javascript
df.show()
df.show(10)
const stringDF = df.show(10, true)
```

Returns **[String][69]** The DataFrame as String Table.

### dim

[src/dataframe.js:481-483][81]

Get the DataFrame dimensions.

**Examples**

```javascript
const [height, weight] = df.dim()
```

Returns **[Array][65]** The DataFrame dimensions. [height, weight]

### transpose

[src/dataframe.js:492-507][82]

Transpose a DataFrame. Rows become columns and conversely. n x p => p x n.

**Parameters**

-   `tranposeColumnNames`  
-   `transposeColumnNames` **[Boolean][70]** An option to transpose columnNames in a rowNames column. (optional, default `false`)

**Examples**

```javascript
df.transpose()
```

Returns **ÐataFrame** A new transposed DataFrame.

### count

[src/dataframe.js:515-517][83]

Get the rows number.

**Examples**

```javascript
df.count()
```

Returns **Int** The number of DataFrame rows.

### countValue

[src/dataframe.js:528-530][84]

Get the count of a value into a column.

**Parameters**

-   `valueToCount`  The value to count into the selected column.
-   `columnName` **[String][69]** The column to count the value. (optional, default `this.listColumns()[0]`)

**Examples**

```javascript
df.countValue(5, 'column2')
df.select('column1').countValue(5)
```

Returns **Int** The number of times the selected value appears.

### push

[src/dataframe.js:539-541][85]

Push new rows into the DataFrame.

**Parameters**

-   `rows` **([Array][65] | Row)** The rows to add.

**Examples**

```javascript
df.push([1,2,3], [1,4,9])
```

Returns **[DataFrame][67]** A new DataFrame with the new rows.

### replace

[src/dataframe.js:552-565][86]

Replace a value by another in all the DataFrame or in a column.

**Parameters**

-   `value`  The value to replace.
-   `replacement`  The new value.
-   `columnNames` **([String][69] \| [Array][65])** The columns to apply the replacement. (optional, default `this.listColumns()`)

**Examples**

```javascript
df.replace(undefined, 0, 'column1', 'column2')
```

Returns **[DataFrame][67]** A new DataFrame with replaced values.

### distinct

[src/dataframe.js:574-579][87]

Compute unique values into a column.

**Parameters**

-   `columnName` **[String][69]** The column to distinct.

**Examples**

```javascript
df.distinct('column1')
```

Returns **[DataFrame][67]** A DataFrame containing the column with distinct values.

### unique

[src/dataframe.js:589-591][88]

Compute unique values into a column.
Alias from .distinct()

**Parameters**

-   `columnName` **[String][69]** The column to distinct.

**Examples**

```javascript
df.unique('column1')
```

Returns **[DataFrame][67]** A DataFrame containing the column with distinct values.

### listColumns

[src/dataframe.js:599-601][89]

List DataFrame columns.

**Examples**

```javascript
df.listColumns()
```

Returns **[Array][65]** An Array containing DataFrame columnNames.

### select

[src/dataframe.js:610-615][90]

Select columns in the DataFrame.

**Parameters**

-   `columnNames` **...[String][69]** The columns to select.

**Examples**

```javascript
df.select('column1', 'column3')
```

Returns **[DataFrame][67]** A new DataFrame containing selected columns.

### withColumn

[src/dataframe.js:626-635][91]

Add a new column or set an existing one.

**Parameters**

-   `columnName` **[String][69]** The column to modify or to create.
-   `func` **[Function][92]** The function to create the column. (optional, default `(row,index)=>undefined`)

**Examples**

```javascript
df.withColumn('column4', () => 2)
df.withColumn('column2', (row) => row.get('column2') * 2)
```

Returns **[DataFrame][67]** A new DataFrame containing the new or modified column.

### restructure

[src/dataframe.js:646-648][93]

Modify the structure of the DataFrame by changing columns order, creating new columns or removing some columns.

**Parameters**

-   `newColumnNames` **[Array][65]** The new columns of the DataFrame.

**Examples**

```javascript
df.restructure(['column1', 'column4', 'column2', 'column3'])
df.restructure(['column1', 'column4'])
df.restructure(['column1', 'newColumn', 'column4'])
```

Returns **[DataFrame][67]** A new DataFrame with restructured columns (renamed, add or deleted).

### renameAll

[src/dataframe.js:657-662][94]

Rename each column.

**Parameters**

-   `newColumnNames` **[Array][65]** The new column names of the DataFrame.

**Examples**

```javascript
df.renameAll(['column1', 'column3', 'column4'])
```

Returns **[DataFrame][67]** A new DataFrame with the new column names.

### rename

[src/dataframe.js:672-677][95]

Rename a column.

**Parameters**

-   `columnName` **[String][69]** The column to rename.
-   `replacement` **[String][69]** The new name for the column.

**Examples**

```javascript
df.rename('column1', 'columnRenamed')
```

Returns **[DataFrame][67]** A new DataFrame with the new column name.

### castAll

[src/dataframe.js:686-699][96]

Cast each column into a given type.

**Parameters**

-   `typeFunctions` **[Array][65]** The functions used to cast columns.

**Examples**

```javascript
df.castAll([Number, String, (val) => new CustomClass(val)])
```

Returns **[DataFrame][67]** A new DataFrame with the columns having new types.

### cast

[src/dataframe.js:710-714][97]

Cast a column into a given type.

**Parameters**

-   `columnName` **[String][69]** The column to cast.
-   `typeFunction`  
-   `ObjectType` **[Function][92]** The function used to cast the column.

**Examples**

```javascript
df.cast('column1', Number)
df.cast('column1', (val) => new MyCustomClass(val))
```

Returns **[DataFrame][67]** A new DataFrame with the column having a new type.

### drop

[src/dataframe.js:723-728][98]

Remove a single column.

**Parameters**

-   `columnName` **[String][69]** The column to drop.

**Examples**

```javascript
df.drop('column2')
```

Returns **[DataFrame][67]** A new DataFrame without the dropped column.

### chain

[src/dataframe.js:743-748][99]

Chain maps and filters functions on DataFrame by optimizing their executions.
If a function returns boolean, it's a filter. Else it's a map.
It can be 10 - 100 x faster than standard chains of .map() and .filter().

**Parameters**

-   `funcs` **...[Function][92]** Functions to apply on the DataFrame rows taking the row as parameter.

**Examples**

```javascript
df.chain(
     row => row.get('column1') > 3, // filter
     row => row.set('column1', 3),  // map
     row => row.get('column2') === '5' // filter
)
```

Returns **[DataFrame][67]** A new DataFrame with modified rows.

### filter

[src/dataframe.js:758-772][100]

Filter DataFrame rows.

**Parameters**

-   `condition` **([Function][92] \| [Object][66])** A filter function or a column/value object.

**Examples**

```javascript
df.filter(row => row.get('column1') >= 3)
df.filter({'column2': 5, 'column1': 3}))
```

Returns **[DataFrame][67]** A new filtered DataFrame.

### where

[src/dataframe.js:783-785][101]

Filter DataFrame rows.
Alias of .filter()

**Parameters**

-   `condition` **([Function][92] \| [Object][66])** A filter function or a column/value object.

**Examples**

```javascript
df.where(row => row.get('column1') >= 3)
df.where({'column2': 5, 'column1': 3}))
```

Returns **[DataFrame][67]** A new filtered DataFrame.

### find

[src/dataframe.js:795-797][102]

Find a row (the first met) based on a condition.

**Parameters**

-   `condition` **([Function][92] \| [Object][66])** A filter function or a column/value object.

**Examples**

```javascript
df.find(row => row.get('column1') === 3)
df.find({'column1': 3})
```

Returns **Row** The targeted Row.

### map

[src/dataframe.js:806-811][103]

Map on DataFrame rows. /!\\ Prefer to use .chain().

**Parameters**

-   `func` **[Function][92]** A function to apply on each row taking the row as parameter.

**Examples**

```javascript
df.map(row => row.set('column1', row.get('column1') * 2))
```

Returns **[DataFrame][67]** A new DataFrame with modified rows.

### reduce

[src/dataframe.js:825-829][104]

Reduce DataFrame into a value.

**Parameters**

-   `func` **[Function][92]** The reduce function taking 2 parameters, previous and next.
-   `init`  The initial value of the reducer.

**Examples**

```javascript
df.reduce((p, n) => n.get('column1') + p, 0)
df2.reduce((p, n) => (
         n.set('column1', p.get('column1') + n.get('column1'))
          .set('column2', p.get('column2') + n.get('column2'))
))
```

Returns **any** A reduced value.

### reduceRight

[src/dataframe.js:839-843][105]

Reduce DataFrame into a value, starting from the last row (see .reduce()).

**Parameters**

-   `func` **[Function][92]** The reduce function taking 2 parameters, previous and next.
-   `init`  The initial value of the reducer.

**Examples**

```javascript
df.reduceRight((p, n) => p > n ? p : n, 0)
```

Returns **any** A reduced value.

### dropDuplicates

[src/dataframe.js:852-858][106]

Return a DataFrame without duplicated columns.

**Parameters**

-   `columnNames` **...[String][69]** The columns used to check unicity of rows. If omitted, unicity is checked on all columns.

**Examples**

```javascript
df.dropDuplicates('id', 'name')
```

Returns **[DataFrame][67]** A DataFrame without duplicated rows.

### dropMissingValues

[src/dataframe.js:867-881][107]

Return a DataFrame without rows containing missing values (undefined, NaN, null).

**Parameters**

-   `columnNames` **[Array][65]** The columns to consider. All columns are considered by default.

**Examples**

```javascript
df.dropMissingValues(['id', 'name'])
```

Returns **[DataFrame][67]** A DataFrame without rows containing missing values.

### fillMissingValues

[src/dataframe.js:891-893][108]

Return a DataFrame with missing values (undefined, NaN, null) fill with default value.

**Parameters**

-   `replacement`  The new value.
-   `columnNames` **[Array][65]** The columns to consider. All columns are considered by default.

**Examples**

```javascript
df.fillMissingValues(0, ['id', 'name'])
```

Returns **[DataFrame][67]** A DataFrame with missing values replaced.

### shuffle

[src/dataframe.js:901-912][109]

Return a shuffled DataFrame rows.

**Examples**

```javascript
df.shuffle()
```

Returns **[DataFrame][67]** A shuffled DataFrame.

### sample

[src/dataframe.js:921-935][110]

Return a random sample of rows.

**Parameters**

-   `percentage` **[Number][80]** A percentage of the orignal DataFrame giving the sample size.

**Examples**

```javascript
df.sample(0.3)
```

Returns **[DataFrame][67]** A sample DataFrame

### bisect

[src/dataframe.js:944-961][111]

Randomly split a DataFrame into 2 DataFrames.

**Parameters**

-   `percentage` **[Number][80]** A percentage of the orignal DataFrame giving the first DataFrame size. The second takes the rest.

**Examples**

```javascript
const [30DF, 70DF] = df.bisect(0.3)
```

Returns **[Array][65]** An Array containing the two DataFrames. First, the X% DataFrame then the rest DataFrame.

### groupBy

[src/dataframe.js:974-976][112]

Group DataFrame rows by columns giving a GroupedDataFrame object. See its doc for more examples.

**Parameters**

-   `args` **...any** 
-   `columnNames` **...[String][69]** The columns used for the groupBy.

**Examples**

```javascript
df.groupBy('column1')
df.groupBy('column1', 'column2')
df.groupBy('column1', 'column2').listGroups()
df.groupBy('column1', 'column2').show()
df.groupBy('column1', 'column2').aggregate((group) => group.count())
```

Returns **GroupedDataFrame** A GroupedDataFrame object.

### sortBy

[src/dataframe.js:989-1053][113]

Sort DataFrame rows based on column values. The row should contains only one variable type. Columns are sorted left-to-right.

**Parameters**

-   `columnNames` **([String][69] \| [Array][65]&lt;[string][69]>)** The columns giving order.
-   `reverse` **[Boolean][70]** Reverse mode. Reverse the order if true. (optional, default `false`)
-   `missingValuesPosition` **[String][69]** Define the position of missing values (undefined, nulls and NaN) in the order. (optional, default `'first'`)

**Examples**

```javascript
df.sortBy('id')
df.sortBy(['id1', 'id2'])
df.sortBy(['id1'], true)
```

Returns **[DataFrame][67]** An ordered DataFrame.

### union

[src/dataframe.js:1062-1075][114]

Concat two DataFrames.

**Parameters**

-   `dfToUnion` **[DataFrame][67]** The DataFrame to concat.

**Examples**

```javascript
df.union(df2)
```

Returns **[DataFrame][67]** A new concatenated DataFrame resulting of the union.

### join

[src/dataframe.js:1086-1095][115]

Join two DataFrames.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.
-   `how` **[String][69]** The join mode. Can be: full, inner, outer, left, right. (optional, default `'inner'`)

**Examples**

```javascript
df.join(df2, 'column1', 'full')
```

Returns **[DataFrame][67]** The joined DataFrame.

### innerJoin

[src/dataframe.js:1107-1109][116]

Join two DataFrames with inner mode.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.

**Examples**

```javascript
df.innerJoin(df2, 'id')
df.join(df2, 'id')
df.join(df2, 'id', 'inner')
```

Returns **[DataFrame][67]** The joined DataFrame.

### fullJoin

[src/dataframe.js:1120-1122][117]

Join two DataFrames with full mode.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.

**Examples**

```javascript
df.fullJoin(df2, 'id')
df.join(df2, 'id', 'full')
```

Returns **[DataFrame][67]** The joined DataFrame.

### outerJoin

[src/dataframe.js:1133-1135][118]

Join two DataFrames with outer mode.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.

**Examples**

```javascript
df2.outerJoin(df2, 'id')
df2.join(df2, 'id', 'outer')
```

Returns **[DataFrame][67]** The joined DataFrame.

### leftJoin

[src/dataframe.js:1146-1148][119]

Join two DataFrames with left mode.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.

**Examples**

```javascript
df.leftJoin(df2, 'id')
df.join(df2, 'id', 'left')
```

Returns **[DataFrame][67]** The joined DataFrame.

### rightJoin

[src/dataframe.js:1159-1161][120]

Join two DataFrames with right mode.

**Parameters**

-   `dfToJoin` **[DataFrame][67]** The DataFrame to join.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the join.

**Examples**

```javascript
df.rightJoin(df2, 'id')
df.join(df2, 'id', 'right')
```

Returns **[DataFrame][67]** The joined DataFrame.

### diff

[src/dataframe.js:1171-1173][121]

Find the differences between two DataFrames (reverse of join).

**Parameters**

-   `dfToDiff` **[DataFrame][67]** The DataFrame to diff.
-   `columnNames` **([String][69] \| [Array][65])** The selected columns for the diff.

**Examples**

```javascript
df2.diff(df2, 'id')
```

Returns **[DataFrame][67]** The differences DataFrame.

### head

[src/dataframe.js:1183-1185][122]

Create a new subset DataFrame based on the first rows.

**Parameters**

-   `nRows` **[Number][80]** The number of first rows to get. (optional, default `10`)

**Examples**

```javascript
df2.head()
df2.head(5)
```

Returns **[DataFrame][67]** The subset DataFrame.

### tail

[src/dataframe.js:1195-1197][123]

Create a new subset DataFrame based on the last rows.

**Parameters**

-   `nRows` **[Number][80]** The number of last rows to get. (optional, default `10`)

**Examples**

```javascript
df2.tail()
df2.tail(5)
```

Returns **[DataFrame][67]** The subset DataFrame.

### slice

[src/dataframe.js:1210-1218][124]

Create a new subset DataFrame based on given indexs. Similar to Array.slice.

**Parameters**

-   `startIndex` **[Number][80]** The index to start the slice (included). (optional, default `0`)
-   `endIndex` **[Number][80]** The index to end the slice (excluded). (optional, default `this.count()`)

**Examples**

```javascript
df2.slice()
df2.slice(0)
df2.slice(0, 20)
df2.slice(10, 30)
```

Returns **[DataFrame][67]** The subset DataFrame.

### getRow

[src/dataframe.js:1227-1229][125]

Return a Row by its index.

**Parameters**

-   `index` **[Number][80]** The index to select the row. (optional, default `0`)

**Examples**

```javascript
df2.getRow(1)
```

Returns **Row** The Row.

### setRow

[src/dataframe.js:1238-1242][126]

Modify a Row a the given index.

**Parameters**

-   `index` **[Number][80]** The index to select the row. (optional, default `0`)
-   `func`   (optional, default `row=>row`)

**Examples**

```javascript
df2.setRowByIndex(1, row => row.set("column1", 33))
```

Returns **[DataFrame][67]** A new DataFrame with the modified Row.

### setDefaultModules

[src/dataframe.js:18-20][127]

Set the default modules used in DataFrame instances.

**Parameters**

-   `defaultModules` **...[Object][66]** DataFrame modules used by default.

**Examples**

```javascript
DataFrame.setDefaultModules(SQL, Stat)
```

### fromDSV

[src/dataframe.js:35-37][128]

Create a DataFrame from a delimiter separated values text file. It returns a Promise.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.
-   `sep` **[String][69]** The separator used to parse the file.
-   `header` **[Boolean][70]** A boolean indicating if the text has a header or not. (optional, default `true`)

**Examples**

```javascript
DataFrame.fromDSV('http://myurl/myfile.txt').then(df => df.show())
// In browser Only
DataFrame.fromDSV(myFile).then(df => df.show())
// From node.js only Only
DataFrame.fromDSV('/my/absolue/path/myfile.txt').then(df => df.show())
DataFrame.fromDSV('/my/absolue/path/myfile.txt', ';', true).then(df => df.show())
```

### fromText

[src/dataframe.js:52-54][129]

Create a DataFrame from a delimiter separated values text file. It returns a Promise. Alias of DataFrame.fromDSV.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.
-   `sep` **[String][69]** The separator used to parse the file.
-   `header` **[Boolean][70]** A boolean indicating if the text has a header or not. (optional, default `true`)

**Examples**

```javascript
DataFrame.fromText('http://myurl/myfile.txt').then(df => df.show())
// In browser Only
DataFrame.fromText(myFile).then(df => df.show())
// From node.js only Only
DataFrame.fromText('/my/absolue/path/myfile.txt').then(df => df.show())
DataFrame.fromText('/my/absolue/path/myfile.txt', ';', true).then(df => df.show())
```

### fromCSV

[src/dataframe.js:68-70][130]

Create a DataFrame from a comma separated values file. It returns a Promise.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.
-   `header` **[Boolean][70]** A boolean indicating if the csv has a header or not. (optional, default `true`)

**Examples**

```javascript
DataFrame.fromCSV('http://myurl/myfile.csv').then(df => df.show())
// For browser only
DataFrame.fromCSV(myFile).then(df => df.show())
// From node.js only
DataFrame.fromCSV('/my/absolue/path/myfile.csv').then(df => df.show())
DataFrame.fromCSV('/my/absolue/path/myfile.csv', true).then(df => df.show())
```

### fromTSV

[src/dataframe.js:84-86][131]

Create a DataFrame from a tab separated values file. It returns a Promise.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.
-   `header` **[Boolean][70]** A boolean indicating if the tsv has a header or not. (optional, default `true`)

**Examples**

```javascript
DataFrame.fromTSV('http://myurl/myfile.tsv').then(df => df.show())
// For browser only
DataFrame.fromTSV(myFile).then(df => df.show())
// From node.js only
DataFrame.fromTSV('/my/absolue/path/myfile.tsv').then(df => df.show())
DataFrame.fromTSV('/my/absolue/path/myfile.tsv', true).then(df => df.show())
```

### fromPSV

[src/dataframe.js:100-102][132]

Create a DataFrame from a pipe separated values file. It returns a Promise.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.
-   `header` **[Boolean][70]** A boolean indicating if the psv has a header or not. (optional, default `true`)

**Examples**

```javascript
DataFrame.fromPSV('http://myurl/myfile.psv').then(df => df.show())
// For browser only
DataFrame.fromPSV(myFile).then(df => df.show())
// From node.js only
DataFrame.fromPSV('/my/absolue/path/myfile.psv').then(df => df.show())
DataFrame.fromPSV('/my/absolue/path/myfile.psv', true).then(df => df.show())
```

### fromJSON

[src/dataframe.js:114-116][133]

Create a DataFrame from a JSON file. It returns a Promise.

**Parameters**

-   `args` **...any** 
-   `pathOrFile` **([String][69] | File)** A path to the file (url or local) or a browser File object.

**Examples**

```javascript
DataFrame.fromJSON('http://myurl/myfile.json').then(df => df.show())
// For browser only
DataFrame.fromJSON(myFile).then(df => df.show())
// From node.js only
DataFrame.fromJSON('/my/absolute/path/myfile.json').then(df => df.show())
```

[1]: #dataframe

[2]: #todsv

[3]: #tocsv

[4]: #totsv

[5]: #topsv

[6]: #totext

[7]: #tojson

[8]: #todict

[9]: #toarray

[10]: #tocollection

[11]: #show

[12]: #dim

[13]: #transpose

[14]: #count

[15]: #countvalue

[16]: #push

[17]: #replace

[18]: #distinct

[19]: #unique

[20]: #listcolumns

[21]: #select

[22]: #withcolumn

[23]: #restructure

[24]: #renameall

[25]: #rename

[26]: #castall

[27]: #cast

[28]: #drop

[29]: #chain

[30]: #filter

[31]: #where

[32]: #find

[33]: #map

[34]: #reduce

[35]: #reduceright

[36]: #dropduplicates

[37]: #dropmissingvalues

[38]: #fillmissingvalues

[39]: #shuffle

[40]: #sample

[41]: #bisect

[42]: #groupby

[43]: #sortby

[44]: #union

[45]: #join

[46]: #innerjoin

[47]: #fulljoin

[48]: #outerjoin

[49]: #leftjoin

[50]: #rightjoin

[51]: #diff

[52]: #head

[53]: #tail

[54]: #slice

[55]: #getrow

[56]: #setrow

[57]: #setdefaultmodules

[58]: #fromdsv

[59]: #fromtext

[60]: #fromcsv

[61]: #fromtsv

[62]: #frompsv

[63]: #fromjson

[64]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L11-L1243 "Source code on GitHub"

[65]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array

[66]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object

[67]: #dataframe

[68]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L313-L315 "Source code on GitHub"

[69]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String

[70]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean

[71]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L328-L330 "Source code on GitHub"

[72]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L343-L345 "Source code on GitHub"

[73]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L358-L360 "Source code on GitHub"

[74]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L375-L377 "Source code on GitHub"

[75]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L389-L391 "Source code on GitHub"

[76]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L399-L406 "Source code on GitHub"

[77]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L415-L419 "Source code on GitHub"

[78]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L428-L432 "Source code on GitHub"

[79]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L444-L473 "Source code on GitHub"

[80]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number

[81]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L481-L483 "Source code on GitHub"

[82]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L492-L507 "Source code on GitHub"

[83]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L515-L517 "Source code on GitHub"

[84]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L528-L530 "Source code on GitHub"

[85]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L539-L541 "Source code on GitHub"

[86]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L552-L565 "Source code on GitHub"

[87]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L574-L579 "Source code on GitHub"

[88]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L589-L591 "Source code on GitHub"

[89]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L599-L601 "Source code on GitHub"

[90]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L610-L615 "Source code on GitHub"

[91]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L626-L635 "Source code on GitHub"

[92]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function

[93]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L646-L648 "Source code on GitHub"

[94]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L657-L662 "Source code on GitHub"

[95]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L672-L677 "Source code on GitHub"

[96]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L686-L699 "Source code on GitHub"

[97]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L710-L714 "Source code on GitHub"

[98]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L723-L728 "Source code on GitHub"

[99]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L743-L748 "Source code on GitHub"

[100]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L758-L772 "Source code on GitHub"

[101]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L783-L785 "Source code on GitHub"

[102]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L795-L797 "Source code on GitHub"

[103]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L806-L811 "Source code on GitHub"

[104]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L825-L829 "Source code on GitHub"

[105]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L839-L843 "Source code on GitHub"

[106]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L852-L858 "Source code on GitHub"

[107]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L867-L881 "Source code on GitHub"

[108]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L891-L893 "Source code on GitHub"

[109]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L901-L912 "Source code on GitHub"

[110]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L921-L935 "Source code on GitHub"

[111]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L944-L961 "Source code on GitHub"

[112]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L974-L976 "Source code on GitHub"

[113]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L989-L1053 "Source code on GitHub"

[114]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1062-L1075 "Source code on GitHub"

[115]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1086-L1095 "Source code on GitHub"

[116]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1107-L1109 "Source code on GitHub"

[117]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1120-L1122 "Source code on GitHub"

[118]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1133-L1135 "Source code on GitHub"

[119]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1146-L1148 "Source code on GitHub"

[120]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1159-L1161 "Source code on GitHub"

[121]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1171-L1173 "Source code on GitHub"

[122]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1183-L1185 "Source code on GitHub"

[123]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1195-L1197 "Source code on GitHub"

[124]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1210-L1218 "Source code on GitHub"

[125]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1227-L1229 "Source code on GitHub"

[126]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L1238-L1242 "Source code on GitHub"

[127]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L18-L20 "Source code on GitHub"

[128]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L35-L37 "Source code on GitHub"

[129]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L52-L54 "Source code on GitHub"

[130]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L68-L70 "Source code on GitHub"

[131]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L84-L86 "Source code on GitHub"

[132]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L100-L102 "Source code on GitHub"

[133]: https://git@github.com/:Gmousse/dataframe-js/blob/ec685babaf21f5c5c74b51405f3b5344642b8849/src/dataframe.js#L114-L116 "Source code on GitHub"