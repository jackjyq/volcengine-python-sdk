# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
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
    api_instance = volcenginesdkecs.ECSApi()
    delete_tags_request = volcenginesdkecs.DeleteTagsRequest(
        resource_ids=["i-l8u0p77yseabkpak****", "i-l8u0p7xyseabkbak****"],
        resource_type="instance",
        tag_keys=["k1"],
    )
    
    try:
        resp = api_instance.delete_tags(delete_tags_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
