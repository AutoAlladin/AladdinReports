
from templates.temp import *
from db.Utils import get_MD_collection, get_result



if __name__ =="__main__" :
    coll = get_MD_collection()
    db_result = get_result(coll, id="5a65fdfdf7764837a4554458")
    tBase = prepare_temlate('baseinfo.html')
    tRun = prepare_temlate('run_info.html')
    tRes = prepare_temlate('all_result.html')

    params1 = {
        "name": db_result["run_info"]["user"],
        "ip": db_result["run_info"]["ip"]
    }

    params3 = dict(items="")

    tIt = prepare_temlate('items.html')
    tTxt = ""

    if db_result["results"] is not None:
            for items in db_result["results"]:
                tTxt = get_report(tIt, params3)


    params3 = dict(items=tTxt)


    txtRes = get_report(tRes, params3)
    txtRun = get_report(tRun, params1)

    params2 = dict(
        _id=db_result["_id"],
        test_name=db_result["test_name"],
        test_timestamp=db_result["test_timestamp"],
        test_result=db_result["test_result"],
        run_info=txtRun,
        results=txtRes,
        items=tTxt
    )
    print(get_report(tBase, params2))







