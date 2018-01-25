import sys
import os
import webbrowser

from reports.switch import get_report


def mn(args):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    subdirs= [x[0] for x in os.walk(os.path.dirname(os.path.abspath(__file__)))
                   if not x[0].startswith("_")
                        and not x[0].startswith(".")
                        and x[0].find(".git")==-1
              ]
    sys.path.extend(subdirs)

if __name__ =="__main__" :
    mn(sys.argv)

    from db.Utils import get_MD_collection
    coll = get_MD_collection()
    #db_result = get_result(coll, id="5a65fdfdf7764837a4554458")

    a = get_report(coll, 'main_page')

    with open('report.html', 'w') as f:
        f.write(a)

    webbrowser.open_new_tab('report.html')









