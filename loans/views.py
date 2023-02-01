from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from .models import *
from .serializers import *
from authentication.models import User
from django.http import JsonResponse
from datetime import date


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
            loan_request = serializedData.save()
            user = loan_request.user
            
            if CustomerLoan.objects.filter(user=user).exists():
                customer_loan = CustomerLoan.objects.get(user=user)
                customer_loan.initial_loan = loan_request.amount_requested
                customer_loan.save()
            else:
                customer_loan = CustomerLoan(user=user, initial_loan=loan_request.amount_requested)
                customer_loan.save()
    return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanRequestDetails(request,id):
    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    # loan_obj = LoanRequest.objects.get(pk=id)
    speficLoanRequest.status_date = status_date
    speficLoanRequest.save()
    year = speficLoanRequest.payment_period_years
    
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
#Loan approved
#-------------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET','PUT','DELETE'])
def approved_request(request, id):
    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    speficLoanRequest.status_date = status_date
    speficLoanRequest.save()
    year = speficLoanRequest.payment_period_years
    
    approved_user = LoanRequest.objects.get(id=id).user
    if CustomerLoan.objects.filter(user=approved_user).exists():

        # find previous amount of user
        PreviousAmount = CustomerLoan.objects.get(
            user=approved_user).total_loan
        PreviousPayable = CustomerLoan.objects.get(
            user=approved_user).payable_loan

        # update balance
        CustomerLoan.objects.filter(
            user=approved_user).update(total_loan=int(PreviousAmount)+int(speficLoanRequest.amount_requested))
        CustomerLoan.objects.filter(
            user=approved_user).update(payable_loan=int(PreviousPayable)+int(speficLoanRequest.amount_requested)+int(speficLoanRequest.amount_requested)*0.12*int(year))

    else:

        # request user

        # CustomerLoan object create
        save_loan = CustomerLoan()

        save_loan.customer = approved_user
        save_loan.total_loan = int(speficLoanRequest.amount_requested)
        save_loan.payable_loan = int(
            speficLoanRequest.amount_requested)+int(speficLoanRequest.amount_requested)*0.12*int(year)
        save_loan.save()

    LoanRequest.objects.filter(id=id).update(status='approved')
    loanrequest = LoanRequest.objects.filter(status='pending')
    # return render(request, 'admin/request_user.html', context={'loanrequest': loanrequest})
    return JsonResponse(context={'loanrequest': loanrequest})
#-------------------------------------------------------------------------------------------------------------------------------------
#Loan disapproved
#-------------------------------------------------------------------------------------------------------------------------------------

def rejected_request(request, id):

    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    speficLoanRequest.status_date = status_date
    speficLoanRequest.save()
    year = speficLoanRequest.payment_period_years
    
    # rejected_customer = loanRequest.objects.get(id=id).customer
    # print(rejected_customer)
    LoanRequest.objects.filter(id=id).update(status='rejected')
    loanrequest = LoanRequest.objects.filter(status='pending')
    # return render(request, 'admin/request_user.html', context={'loanrequest': loanrequest})
    return JsonResponse(context={'loanrequest': loanrequest})


#-------------------------------------------------------------------------------------------------------------------------------------
#Loan processes
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET'])
def getDashboard(request):
    if request.method == 'GET':
        totalCustomer = User.objects.all().count(),
        # requestLoan = loanRequest.objects.all().filter(status='pending').count(),
        # approved = loanRequest.objects.all().filter(status='approved').count(),
        # rejected = loanRequest.objects.all().filter(status='rejected').count(),
        # totalLoan = CustomerLoan.objects.aggregate(Sum('total_loan'))[
        #     'total_loan__sum'],
        # totalPayable = CustomerLoan.objects.aggregate(
        #     Sum('payable_loan'))['payable_loan__sum'],
        # totalPaid = loanTransaction.objects.aggregate(Sum('payment'))[
        #     'payment__sum'],

        dict = {
            'totalCustomer': totalCustomer[0],
            # 'request': requestLoan[0],
            # 'approved': approved[0],
            # 'rejected': rejected[0],
            # 'totalLoan': totalLoan[0],
            # 'totalPayable': totalPayable[0],
            # 'totalPaid': totalPaid[0],

        }
        print(dict)

    # return render(request, 'admin/dashboard.html', context=dict)
    return JsonResponse(dict)