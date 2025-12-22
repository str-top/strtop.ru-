def prepare_request(**kwargs):
   endpoint = kwargs.get('endpoint', '')
   if not endpoint:
      raise ValueError("endpoint is required")

   control = {key: value for key, value in kwargs.items() if key in ['timeout', 'retries']}

   return {
      "endpoint": endpoint,
      "control": control,
      "payload": {"data": kwargs["data"]}
   }

print(prepare_request(endpoint="/stats", data=[1, 2]))
