from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Books, Members, BorrowRecords
from .serializers import BookSerializer, MemberSerializer, BorrowRecordSerializer

# Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# List all books with filtering options (JSON response)
class BookListView(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        author = request.query_params.get('author')
        category = request.query_params.get('category')
        
        books = Books.objects.all()
        if title:
            books = books.filter(title__icontains=title)
        if author:
            books = books.filter(author__icontains=author)
        if category:
            books = books.filter(category__icontains=category)
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Register a new member
class MemberCreateView(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

# List all members with pagination (JSON response)
class MemberListView(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

# Borrow a book
class BorrowBookView(APIView):
    def post(self, request):
        data = request.data
        try:
            book = Books.objects.get(id=data['book'])
        except Books.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        if book.available_copies <= 0:
            return Response({"error": "No copies available."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BorrowRecordSerializer(data=data)
        if serializer.is_valid():
            book.available_copies -= 1
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Return a book
class ReturnBookView(APIView):
    def post(self, request, pk):
        try:
            record = BorrowRecords.objects.get(id=pk)
        except BorrowRecords.DoesNotExist:
            return Response({"error": "Record not found."}, status=status.HTTP_404_NOT_FOUND)

        if record.return_date:
            return Response({"error": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)

        record.return_date = request.data.get('return_date')
        record.book.available_copies += 1
        record.book.save()
        record.save()
        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)
