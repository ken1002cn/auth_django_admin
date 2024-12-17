from django.http import JsonResponse

class JsonResponseUtil:
    @staticmethod
    def success(data=None):
        """
        成功响应
        """
        response_data = {
            "code": 200,
            "message": "操作成功",
            "data": data or {}
        }
        return JsonResponse(response_data)

    @staticmethod
    def failure(message="操作失败", code=400):
        """
        失败响应
        """
        response_data = {
            "code": code,
            "message": message,
        }
        return JsonResponse(response_data, status=code)
