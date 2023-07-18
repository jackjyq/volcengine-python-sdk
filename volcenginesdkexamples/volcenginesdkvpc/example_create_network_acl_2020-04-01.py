# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    create_network_acl_request = volcenginesdkvpc.CreateNetworkAclRequest(
        network_acl_name="acl-1",
        vpc_id="vpc-bp1opxu1zkhn00gzv****",
    )
    
    try:
        resp = api_instance.create_network_acl(create_network_acl_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
