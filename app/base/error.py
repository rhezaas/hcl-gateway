class BaseError(Exception):
    code: int = None
    message: str = None
    detail: str = None

    def __init__(self, code: int, message: str, detail: str):
        super().__init__(message)
        self.code = code
        self.message = message
        self.detail = detail


class HTTPException(BaseError):
    def __init__(self, code: int, message: str, detail: str = ''):
        super().__init__(code, message, detail)


class BadRequestException(BaseError):
    def __init__(self, detail: str = ''):
        super().__init__(400, 'Bad Request', detail)


class NeedAutorizationException(BaseError):
    def __init__(self, detail: str = ''):
        super().__init__(401, 'Need Authorization Token', detail)


class UnauthorizedException(BaseError):
    def __init__(self, detail: str = ''):
        super().__init__(401, 'Unauthorized', detail)


class NotFoundException(BaseError):
    def __init__(self, detail: str = ''):
        super().__init__(404, 'Not Found', detail)
