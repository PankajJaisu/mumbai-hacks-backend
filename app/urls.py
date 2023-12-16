from . import views
from django.urls import path
urlpatterns = [
    path('generate-prescription/',views.generate_prescription),
    path('find-nearby-hospital/',views.find_nearby_hospitals),
    path('generate-otp/',views.generate_otp),
    path('verify-otp/',views.verify_otp),
    path('user-registration/',views.user_registration),
    path('generate-card/',views.generate_card),
    path('upload-prescription/',views.upload_prescription),
    path('get-doc/',views.get_doc),
    path('upload-doc/',views.upload_doc),
    path('table-ocr/',views.table_ocr),
    path('qr-code/',views.qr_code),
    path('show-data-to-patient/',views.show_data_to_patient),
    path('show-data-to-doctor/',views.show_data_to_doctor),
    path('remove-access/',views.remove_access),
    
]