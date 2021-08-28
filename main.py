from time import sleep

import dxfeed as dx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    endpoint = dx.Endpoint('demo.dxfeed.com:7300')
    print(f'Connected address: {endpoint.address}')
    print(f'Connection status: {endpoint.connection_status}')

    quote_sub = endpoint.create_subscription('Quote')
    quote_handler = dx.DefaultHandler()
    quote_sub = quote_sub.set_event_handler(quote_handler)
    quote_sub = quote_sub.add_symbols(['IBM', 'AAPL'])
    sleep(5)
    print(quote_handler.get_dataframe())
    endpoint.close_connection()
