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
    complete_lifecycle_activity_request = volcenginesdkautoscaling.CompleteLifecycleActivityRequest(
        lifecycle_activity_id="sgha-ybw2idr7kogsnzd9****",
    )
    
    try:
        resp = api_instance.complete_lifecycle_activity(complete_lifecycle_activity_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)