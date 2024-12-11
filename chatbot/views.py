from django.shortcuts import render
from django.http import JsonResponse

from palemene_hr import settings
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import FileResponse
from django.shortcuts import reverse
import os


# Define the chatbot home view
def chatbot_home(request):
    return render(request, 'chatbot/chatbot_home.html')  # Adjust template path as needed

# View to handle employee lookup
@csrf_exempt  # This is used to allow the POST request to bypass CSRF for testing purposes
# View to handle employee lookup

def get_employee(request):
    if request.method == 'POST':
        try:
            # Load the POST body (which should be in JSON format)
            data = json.loads(request.body)
            employee_id = data.get('employee_id')

            if not employee_id:
                return JsonResponse({"error": "Employee ID is required"}, status=400)
            
            # Search for the employee by Employee ID
            employee = Employee.objects.get(employee_id=employee_id)

            # Prepare the response data
            response = {
                "greeting": f"Welcome {employee.full_name}, how may I help you today?",
                "options": [
                    "See Leave Balance",
                    "Download Leave Form"
                ]
            }
        except Employee.DoesNotExist:
            # If employee is not found, return an error message
            response = {"error": "Employee ID not found: Enter a Valid EmployeeID please"}
            
        except json.JSONDecodeError:
            # If there's an issue with the JSON body, return an error message
            response = {"error": "Invalid data received"}

        return JsonResponse(response)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
                        
# View to handle leave balance request
def leave_balance(request, employee_id):

    try:
        print(f"Request method: {request.method}")
        # Retrieve employee by their ID
        employee = Employee.objects.get(employee_id=employee_id)

        # Prepare the leave balance data
        leave_balance = {
            "ID": employee.employee_id,
            "Annual Leave": employee.annual_leave,
            "Sick Leave": employee.sick_leave,
            "TOIL": employee.toil,
            "Bereavement Leave": employee.bereavement_leave,
            "Maternity Leave": employee.maternity_leave,
            "Paternity Leave": employee.paternity_leave,
            "Comments": employee.comments,
        }

        return JsonResponse(leave_balance)

    except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found: Enter a Valid EmployeeID please"}, status=404)
    except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
            return JsonResponse({"error": "Invalid request method"}, status=405)



def download_leave_form(request):
    # Full path to the leave form file
    file_path = r"C:\Users\CharlieAhkuoi\OneDrive - Legislative Assembly Office\Documents\Principal IT\Systems\file_management\palemene_hr\chatbot\files\OCLA_WCE_Forms.pdf"

    # Check if the file exists
    if os.path.exists(file_path):
        # Build an absolute URL for the file
        file_url = request.build_absolute_uri('/download_leave_form/file')
        return JsonResponse({
            "message": "Click the link below to download the leave form.",
            "form_url": file_url
        })
    else:
        return JsonResponse({"error": "File not found."}, status=404)

def serve_leave_form_file(request):
    # Full path to the leave form file
    file_path = r"C:\Users\CharlieAhkuoi\OneDrive - Legislative Assembly Office\Documents\Principal IT\Systems\file_management\palemene_hr\chatbot\files\OCLA_WCE_Forms.pdf"

    # Serve the file for download
    if os.path.exists(file_path):
        # Pass the file path directly to FileResponse without manually closing it
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename="OCLA_WCE_Forms.pdf")
    else:
        return JsonResponse({"error": "File not found."}, status=404)


