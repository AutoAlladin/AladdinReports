from db.Utils import get_result
from templates.temp import prepare_temlate, get_treport


def get_main_page_report(db_coll):

    db_result = get_result(db_coll,  maxdate=True, name='main_page')

    tBase = prepare_temlate('baseinfo.html')
    tRunInfo = prepare_temlate('run_info.html')
    tRes = prepare_temlate('all_result.html')
    tResItems = prepare_temlate('items.html')

    pResItems = dict(items="")

    pRunInfo = {
        "name": db_result["run_info"]["user"],
        "ip": db_result["run_info"]["ip"]
    }

    txtResItems = ""

    if db_result["results"] is not None:
        for items in db_result["results"]:
            txtResItems += get_treport(tResItems, pResItems)

    pResItems = dict(items=txtResItems)

    txtRes = get_treport(tRes, pResItems)
    txtRun = get_treport(tRunInfo, pRunInfo)

    pBase = dict(
        _id=db_result["_id"],
        test_name=db_result["test_name"],
        test_timestamp=db_result["test_timestamp"],
        test_result=db_result["test_result"],
        run_info=txtRun,
        results=txtRes,
        items=txtResItems
    )
    a = get_treport(tBase, pBase)
    return a


def get_report(col, name):
    if name =="main_page":
        return get_main_page_report(col)

