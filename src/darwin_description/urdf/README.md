I do not like they way urdf works.
```
-- XML :-) -- |    -- URDF's XML :-( --
<parent>      |    <link name = "parent">
  <child>     |    </link>
  </child>    |    <link name = "child">
</parent>     |    </link>
              |    <joint>
              |     <parent link="parent" />
              |     <parent link="child" />
              |    </joint>
```
Therefore, I would like to suggest another way to write urdf files.
```
<link name = "parent">
</link>
  <joint>
    <parent link="parent" />
    <parent link="child" />
  </joint>
  <link name = "child">
  </link>
```
I want the urdf have tree structure but I need to use their tags. Therefore, we can only change the indent to make it like tree structure. Please note the difference between XML and the way I indent. The close tag </> is before the child in URDF, yet the close tag should be after child in XML. To show the tree structure better, I hope there is a editor can show the follwing structure for me. 
```
<link name = "parent">
</link>
| <joint>
| | <parent link="parent" />
| | <parent link="child" />
| </joint>
| <link name = "child">
| </link>
```
From this structure, you can understand the whole urdf structure easily. And that's where [XML Copy Editor](http://xml-copy-editor.sourceforge.net/) shows up!



