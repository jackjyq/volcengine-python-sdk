# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkautoscaling
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
    api_instance = volcenginesdkautoscaling.AUTOSCALINGApi()
    modify_lifecycle_hook_request = volcenginesdkautoscaling.ModifyLifecycleHookRequest(
        lifecycle_hook_id="sgh-ybrzhc5ht08hc******",
        lifecycle_hook_policy="CONTINUE",
        lifecycle_hook_timeout=30,
        lifecycle_hook_type="SCALE_IN",
    )
    
    try:
        resp = api_instance.modify_lifecycle_hook(modify_lifecycle_hook_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
