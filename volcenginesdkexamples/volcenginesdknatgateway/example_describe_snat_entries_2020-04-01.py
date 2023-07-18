# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdknatgateway
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdknatgateway.NATGATEWAYApi()
    describe_snat_entries_request = volcenginesdknatgateway.DescribeSnatEntriesRequest(
        nat_gateway_id="ngw-2fedgzyvtzaio59gp675l****",
        snat_entry_ids=["snat-2fedi22b12iv459gp68****", "snat-2fedhzdlyknb459gp676o****"],
    )
    
    try:
        resp = api_instance.describe_snat_entries(describe_snat_entries_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
