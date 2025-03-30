from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def mock_translate_to_sql(nl_query):
    if "sales" in nl_query.lower():
        return "SELECT * FROM sales_data;", [{"date": "2024-01-01", "sales": 1000}]
    elif "revenue" in nl_query.lower():
        return "SELECT SUM(revenue) FROM sales_data;", [{"total_revenue": 150000}]
    elif "customer" in nl_query.lower():
        return "SELECT * FROM customers;", [{"id": 1, "name": "Alice"}]
    else:
        return "SELECT * FROM dummy_table;", [{"result": "no match"}]



@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def query_view(request):
    query = request.data.get("query")
    if not query:
        return Response({"error": "Query is required"}, status=400)

    sql, mock_data = mock_translate_to_sql(query)
    return Response({"data": mock_data, "sql": sql})



@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def explain_view(request):
    query = request.data.get("query")
    if not query:
        return Response({"error": "Query is required"}, status=400)

    explanation = f"This query is asking about: '{query}'"
    return Response({"explanation": explanation})


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def validate_view(request):
    query = request.data.get("query")
    if not query:
        return Response({"error": "Query is required"}, status=400)

    valid_keywords = ["sales", "revenue", "customer"]
    is_valid = any(word in query.lower() for word in valid_keywords)
    return Response({"valid": is_valid})
