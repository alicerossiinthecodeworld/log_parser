import data


def format_the_report_dict(log_name):
    requests = data.get_requests(log_name)
    result = {"request number": [len(requests)],
              "top 3 IP": [data.get_most_common_request_ips(requests)],
              "num of requests for each request type": str(data.get_counter_for_each_request_type(requests)),
              "top 3 most endured requests" : data.get_most_endured_request(requests)
              }
    return result

