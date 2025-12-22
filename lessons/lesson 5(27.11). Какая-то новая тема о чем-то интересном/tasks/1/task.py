def split_control_params(params):
    timeout = params.get("timeout", 5)
    retries = params.get("retries", 3)

    payload = {
        k: v
        for k, v in params.items()
        if k not in {"endpoint", "timeout", "retries"}
    }

    return {"timeout": timeout, "retries": retries}, payload


def prepare_request(**kwargs):
    if "endpoint" not in kwargs:
        raise ValueError("endpoint is required")

    endpoint = kwargs["endpoint"]
    control, payload = split_control_params(kwargs)

    return {
        "endpoint": endpoint,
        "control": control,
        "payload": payload,
    }
