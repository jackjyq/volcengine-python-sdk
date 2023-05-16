# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
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
    api_instance = volcenginesdkecs.ECSApi()
    import_key_pair_request = volcenginesdkecs.ImportKeyPairRequest(
        key_pair_name="ssh_key_pair",
        public_key="ssh-rsa AaaAAB3NzaC1yc2EAAAADAQ******",
    )

    try:
        resp = api_instance.import_key_pair(import_key_pair_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)