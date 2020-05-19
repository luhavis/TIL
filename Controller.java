// Template For Json ModelAndView
@RequestMapping("")
public ModelAndView main(@RequestParam Map pMap, HttpServletRequest req, HttpServletResponse res) {
    ModelAndView mav = new ModelAndView("jsonView");
    int totalCnt = 0;
    List resultList = new ArrayList();

    PaginationInfo paginationInfo = new PaginationInfo();
    paginationInfo.setTotalRecordCount(totalCnt);
    paginationInfo.setCurrentPageNo(PmapUtil.nvl(pMap, "searchPageIndex", 1));
    paginationInfo.setRecordCountPerPage(PmapUtil.nvl(pMap, "searchRecordCountPerPage", 10));
    paginationInfo.setPageSize(10);

    pMap.put("firstIndex", paginationInfo.getFirstRecordIndex());
    pMap.put("lastIndex", paginationInfo.getLastRecordIndex());
    pMap.put("recordCountPerPage", paginationInfo.getRecordCountPerPage());
    
    if (totalCnt > 0) 
        resultList = examService.getList(pMap);
    
    mav.addObject("totalCnt", totalCnt);
    mav.addObject("resultList", resultList);
    mav.addObject("paginationInfo", paginationInfo);
}


