# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkdirectconnect
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
    api_instance = volcenginesdkdirectconnect.DIRECTCONNECTApi()
    create_direct_connect_connection_request = volcenginesdkdirectconnect.CreateDirectConnectConnectionRequest(
        bandwidth=1000,
        client_token="123e4567-e89b-12d3-a456-42665544****",
        customer_contact_email="12345test@example.com",
        customer_contact_phone="133****2233",
        customer_name="张*三",
        description="test",
        direct_connect_access_point_id="ap-cn-shanghai-***",
        direct_connect_connection_name="test",
        line_operator="ChinaMobile",
        peer_location="中国上海市静安区XX路XX号XX楼XX机房",
        port_type="1000Base",
    )
    
    try:
        resp = api_instance.create_direct_connect_connection(create_direct_connect_connection_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
