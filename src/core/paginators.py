from rest_framework.pagination import LimitOffsetPagination as DRFLimitOffsetPagination


class LimitOffsetPagination(DRFLimitOffsetPagination):
    max_limit = 100
    limit_query_description = "Количество записей, максимально 100, по умолчанию 100."
    offset_query_description = "Начальный индекс от которого возвращаются записи, по умолчанию 0."
