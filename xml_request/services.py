from faker import Generator
from zeep import Client
from zeep.transports import Transport
url = "https://rps.digital-remittance.com/api/Send.svc?wsdl"
# Replace "your_soap_service_url" with the actual URL of the SOAP service
soap_service_url =url
wsdl_url=url
# wsdl_url = 'https://rps.digital-remittance.com/api/Send.svc?singleWsdl'
# Replace placeholders with actual values for username, password, and type_data
# username = "testRps"
# password = "testRps"
# type_data = "IncomeSource"

# Replace "your_custom_envelope_xml" with the custom SOAP envelope XML you want to send
# custom_envelope_xml = f"""\
# <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
#     <Body>
#         <GetStaticData xmlns="http://tempuri.org/">
#             <GetStaticDataRequest>
#                 <UserName xmlns="http://schemas.datacontract.org/2004/07/Remit.API">{username}</UserName>
#                 <Password xmlns="http://schemas.datacontract.org/2004/07/Remit.API">{password}</Password>
#                 <Type xmlns="http://schemas.datacontract.org/2004/07/Remit.API">{type_data}</Type>
#             </GetStaticDataRequest>
#         </GetStaticData>
#     </Body>
# </Envelope>
# """

# Create a custom transport with Zeep and set the custom XML envelope
 
# transport.load_custom_xml(custom_envelope_xml)

# Create the Zeep client using the custom transport
# Set the timeout value in seconds
timeout_seconds = 3
# Create a custom transport with the specified timeout
transport = Transport(timeout=timeout_seconds)

try:
    client=Client(wsdl_url, transport=transport)
except Exception as e:
    print(e)
    client=None
    pass
a=None




# def retry_transport():
#     try: 
#         client = Client(wsdl_url, transport=transport)
#         print(a)
#         a=5
#         return (client)
        
#     except:
#         a=99
#         print(a)
        
#         client=None
#         return (client)


# async def initClient():
#     try:
#         return await Client(wsdl_url)

#     except:
#         pass

def get_client() -> Generator:   #new
    try:
        db = Client(wsdl_url)
        yield db
    except:
        pass
    else:
        pass
    finally:
        pass
# initClient()
# input_params = {
#     'username': username,
#     'password': password,
#     'type': type_data,
# }
# # Call the 'GetStaticData' SOAP operation with the necessary parameters in the request body
# response = client.service.GetStaticData(GetStaticDataRequest={
#         'UserName': username,
#         'Password': password,
#         'Type': type_data
#     })

# # Process the response
# print(response)