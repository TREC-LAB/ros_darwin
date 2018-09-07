I do not like they way urdf works.
```
-- XML --     |    -- URDF --
<parent>      |    <link name = "parent">
  <child>     |    </link>
  </child>    |    <link name = "child">
</parent>     |    </link>
              |    <joint>
              |     <parent link="parent" />
              |     <parent link="child" />
              |    </joint>
```
Therefore, I would like to suggest another way to show the urdf files.
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




