# This sample demonstrates how to send a parameter in the body of a request.

# For a list of the endpoints that you can use along with the parameters that
# they accept you can view the REST API interactive help page on your
# deployment at https://<hostname>/restapi/doc
# You can also retrieve a list of available endpoints through the API itself
# at the /api/help/capabilities endpoint.

import sys, os
sys.path.append(os.path.realpath('../modules'))
from RestApiClient import RestApiClient
import SampleUtilities


def main():
    
    # Create our client and set up some sample data.
    client = RestApiClient(version='0.1')
    setup_data(client)
    
    # Some endpoints accept body parameters. An example of this is the
    # /referencedata/sets/bulkLoad endpoint.
    # Body parameters may appear with path parameters, as in this case, but will
    # never appear with query parameters.
    
    # You must make sure that you set the content type correctly to a type
    # accepted by the endpoint.
    headers = client.get_headers().copy()
    headers['Content-type'] = 'application/json'
    
    body = b'["abc", "def", "123"]'
    
    # Send the request.
    SampleUtilities.pretty_print_request(client, 'referencedata/sets/bulkLoad/rest_api_samples_testset', 'POST', headers=headers)
    response = client.call_api('referencedata/sets/bulkLoad/rest_api_samples_testset', 'POST', headers=headers, data=body)
    SampleUtilities.pretty_print_response(response)
    
    # The response from the previous command only shows information about the
    # set, not the contents of the set. We can view the contents of the set with
    # this command:
    response = client.call_api('referencedata/sets/rest_api_samples_testset', 'GET')
    SampleUtilities.pretty_print_response(response)
    
    # You can uncomment this line to have this script remove the data it
    # creates after it is done, or you can invoke the Cleanup script directly
    #Cleanup.cleanup_introduction_data(client)


# This helper function sets up data used in this sample.
def setup_data(client):
    SampleUtilities.data_setup(client, 'referencedata/sets?name=rest_api_samples_testset&elementType=ALN&maxElements=20', 'POST')


if __name__ == "__main__":
    main()
