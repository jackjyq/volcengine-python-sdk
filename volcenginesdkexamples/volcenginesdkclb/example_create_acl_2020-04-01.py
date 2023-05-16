# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkclb
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
    api_instance = volcenginesdkclb.CLBApi()
    create_acl_request = volcenginesdkclb.CreateAclRequest(
        acl_name="test",
        description="default",
    )

    try:
        resp = api_instance.create_acl(create_acl_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)