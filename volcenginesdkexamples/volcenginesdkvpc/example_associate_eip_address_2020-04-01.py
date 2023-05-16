# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkvpc.VPCApi()
    associate_eip_address_request = volcenginesdkvpc.AssociateEipAddressRequest(
        allocation_id="eip-2zeewb7ujxscd****",
        instance_id="i-2zebbhyczzaweeval****",
        instance_type="EcsInstance",
    )

    try:
        resp = api_instance.associate_eip_address(associate_eip_address_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)