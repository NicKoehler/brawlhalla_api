class Unauthorized(Exception):
    """Unauthorized -- You Must use HTTPS"""

    def __init__(self, *args: object) -> None:
        super().__init__("Unauthorized -- You Must use HTTPS", *args)


class Forbidden(Exception):
    """Bad API key or missing API key"""

    def __init__(self, *args: object) -> None:
        super().__init__("Bad API key or missing API key", *args)


class NotFound(Exception):
    """The service or endpoint is not found"""

    def __init__(self, *args: object) -> None:
        super().__init__("The service or endpoint is not found", *args)


class BadRequest(Exception):
    """Required Parameters missing, or possibly invalid"""

    def __init__(self, *args: object) -> None:
        super().__init__("Required Parameters missing, or possibly invalid", *args)


class TooManyRequests(Exception):
    """Your API key has hit the rate limit."""

    def __init__(self, *args: object) -> None:
        super().__init__("Your API key has hit the rate limit.", *args)


class ServiceUnavailable(Exception):
    """We're temporarially offline for maintanance. Please try again later."""

    def __init__(self, *args: object) -> None:
        super().__init__(
            "We're temporarially offline for maintanance. Please try again later.",
            *args,
        )


def error_checker(status: int, data: dict):
    match status:
        case 403:
            raise Forbidden()
        case 401:
            raise Unauthorized()
        case 429:
            raise TooManyRequests()
        case 509:
            raise ServiceUnavailable()
        case 404:
            if data["error"]["message"] == "Not Found":
                raise NotFound()
            raise BadRequest()
