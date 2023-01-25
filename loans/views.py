from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from .models import *
from .serializers import *
from authentication.models import User

# Create your views here.

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Category
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanCategory(request):

    if request.method == 'GET':
        users=LoanCategory.objects.all()    
        serializedData=LoanCategorySerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanCategorySerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanCategoryDetails(request,id):
    speficLoanCategory = LoanCategory.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=LoanCategorySerializer(speficLoanCategory)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanCategorySerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanCategory = LoanCategory.objects.get(pk=id)
        speficLoanCategory.delete()
        return Response('Loan Category Successfully Deleted!')
    
    
#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Request
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanRequest(request):

    if request.method == 'GET':
        users=LoanRequest.objects.all()    
        serializedData=LoanRequestSerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanRequestSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanRequestDetails(request,id):
    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=LoanRequestSerializer(speficLoanRequest)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanRequestSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanRequest = LoanRequest.objects.get(pk=id)
        speficLoanRequest.delete()
        return Response('Loan Request Successfully Deleted!')

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Payment
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanPayment(request):

    if request.method == 'GET':
        users=LoanPayment.objects.all()    
        serializedData=LoanPaymentSerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanPaymentSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanPaymentDetails(request,id):
    speficLoanPayment = LoanPayment.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=LoanPaymentSerializer(speficLoanPayment)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanPaymentSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanPayment = LoanPayment.objects.get(pk=id)
        speficLoanPayment.delete()
        return Response('Loan Payment Successfully Deleted!')

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Process
#-------------------------------------------------------------------------------------------------------------------------------------
def approved_request(request, id):
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    year = loan_obj.year

    approved_customer = loanRequest.objects.get(id=id).customer
    if CustomerLoan.objects.filter(customer=approved_customer).exists():

        # find previous amount of customer
        PreviousAmount = CustomerLoan.objects.get(
            customer=approved_customer).total_loan
        PreviousPayable = CustomerLoan.objects.get(
            customer=approved_customer).payable_loan

        # update balance
        CustomerLoan.objects.filter(
            customer=approved_customer).update(total_loan=int(PreviousAmount)+int(loan_obj.amount))
        CustomerLoan.objects.filter(
            customer=approved_customer).update(payable_loan=int(PreviousPayable)+int(loan_obj.amount)+int(loan_obj.amount)*0.12*int(year))

    else:

        # request customer

        # CustomerLoan object create
        save_loan = CustomerLoan()

        save_loan.customer = approved_customer
        save_loan.total_loan = int(loan_obj.amount)
        save_loan.payable_loan = int(
            loan_obj.amount)+int(loan_obj.amount)*0.12*int(year)
        save_loan.save()

    loanRequest.objects.filter(id=id).update(status='approved')
    loanrequest = loanRequest.objects.filter(status='pending')
    return render(request, 'admin/request_user.html', context={'loanrequest': loanrequest})