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
    enable_scaling_configuration_request = volcenginesdkautoscaling.EnableScalingConfigurationRequest(
        scaling_configuration_id="scc-ybmt16auaugh9zfy****",
        scaling_group_id="scg-ybmssdnnhn5pkgyd****",
    )
    
    try:
        resp = api_instance.enable_scaling_configuration(enable_scaling_configuration_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
