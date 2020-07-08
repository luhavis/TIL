
## for ModelAndView (VIEW)

```java
@RequestMapping("/{siteid}/$REQUEST_URL$")
public ModelAndView $METHOD_NAME$(HttpServletRequest request) throws Exception {
    ModelAndView mav = new ModelAndView(comSkin.getSkinDir(request.getRequestURI())+"/$REQUEST_URL$");
    return mav;
}
$END$
```

## for ModelAndView (Json)

```java
@RequestMapping("/{siteid}/$REQUEST_URL$")
public ModelAndView $METHOD_NAME$(@PathVariable("siteid") String siteid, @RequestParam Map<String, Object> pMap, HttpServletRequest request) throws Exception {
    ModelAndView mav = new ModelAndView("jsonView");
    ComPmapUtil.keepParametersObject(pMap, mav);

    int totalCnt = 0;

    /** paging start */
    PaginationInfo paginationInfo = ComFunc.commonPageInfo(totalCnt, pMap);
    /** paging end */

    List resultList = null;
    if(totalCnt>0)
        resultList = null;

    mav.addObject("totalCnt", totalCnt);
    mav.addObject("paginationInfo", paginationInfo);
    mav.addObject("resultList", resultList);

    return mav;
}
$END$
```

## for Mybatis (Count)

```xml
<select id="$ID$" parameterType="$PARAMETER_TYPE$" resultType="$RESULT_TYPE$">
SELECT COUNT(*)
FROM $TABLE_NAME$
</select>
```


## for Mybatis (List)

```xml
<select id="$ID$" parameterType="$PARAMETER_TYPE$" resultType="$RESULT_TYPE$">
SELECT 
FROM $TABLE_NAME$
LIMIT #{recordCountPerPage} OFFSET #{firstIndex}
</select>
```
