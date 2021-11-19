import bw2data as bd
import bw2io as bi
from copy import deepcopy

from .importers import ConsumptionDbImporter


def import_ecoinvent(ei_path, ei_name):
    if ei_name in bd.databases:
        print(ei_name + " database already present!!! No import is needed")
    else:
        ei = bi.SingleOutputEcospold2Importer(ei_path, ei_name)
        ei.apply_strategies()
        ei.match_database(db_name='biosphere3', fields=('name', 'category', 'unit', 'location'))
        ei.statistics()
        ei.write_database()


def create_ecoinvent_33_project(ei33_path, ei33_name="ecoinvent 3.3 cutoff"):
    current_project = deepcopy(bd.projects.current)
    bd.projects.set_current(ei33_name)  # Temporarily switch to ecoinvent 3.3 project
    bi.bw2setup()
    import_ecoinvent(ei33_path, ei33_name)
    bd.projects.set_current(current_project)  # Switch back

        
def import_exiobase_3(ex3_path, ex3_name):
    if ex3_name in bd.databases:
        print("{} database already present!!! No import is needed".format(ex3_name))
    else:
        ex = bi.Exiobase3MonetaryImporter(ex3_path, ex3_name)  # give path to IOT_year_pxp folder
        ex.apply_strategies()
        ex.write_database()


def import_consumption_db(habe_path, co_name, exclude_dbs=(),):
    # TODO add more here once the import is done
    if co_name in bd.databases:
        print(co_name + " database already present!!! No import is needed")
    else:
        co = ConsumptionDbImporter(habe_path, co_name, exclude_dbs)
        co.write_database()
