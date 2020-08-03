# Mybatis

## foreach

### update in foreach

```
<foreach collection="list" item="i" index="index" open="" separator=";" close="">
    UPDATE TABLE_NAME
    SET COLUMN1 = #{i.column1}
    , COLUMN2 = #{i.column2}
    WHERE WHERE_COLUMN1 = #{i.whereColumn1}
    AND WHERE_COLUMN2 = #{i.whereColumn2}
</foreach>
```
