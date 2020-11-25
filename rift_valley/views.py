import os

from django.shortcuts import render
from .forms import InputForm
import pymongo
from django.contrib.staticfiles.storage import staticfiles_storage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from decimal import Decimal
from django.http import HttpResponse
from django.views.generic import View

from RVF.utils import render_to_pdf

# Create your views here.
def start_page(request):

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_user_1_collection = rvf_db['user_1_table']
    rvf_vector_D_collection = rvf_db['vector_D_table']

    contex = {
                'simulation_years':1,
                'start_day':0,
                'stop_day':0,
                'rng_seed':0,
                'chk_human_zone_1':'Checked',
                'chk_human_zone_2': 'Checked',
                'chk_human_zone_3': 'Checked',
                'chk_animal_zone_1': 'Checked',
                'chk_animal_zone_2': 'Checked',
                'chk_animal_zone_3': 'Checked',
                'chk_vector_A_zone_1':'Checked',
                'chk_vector_A_zone_2': 'Checked',
                'chk_vector_A_zone_3': 'Checked',
                'chk_vector_B_zone_1': 'Checked',
                'chk_vector_B_zone_2': 'Checked',
                'chk_vector_B_zone_3': 'Checked',
                'chk_vector_C_zone_1': 'Checked',
                'chk_vector_C_zone_2': 'Checked',
                'chk_vector_C_zone_3': 'Checked',
                'chk_vector_D_zone_1': 'Checked',
                'chk_vector_D_zone_2': 'Checked',
                'chk_vector_D_zone_3': 'Checked',
            }

    if(request.method == "POST"):
        simulation_years = request.POST['simulation_years']
        start_day = request.POST['start_day']
        stop_day = request.POST['stop_day']
        rng_seed = request.POST['rng_seed']
        if request.POST.get('chk_human_zone_1',False):
            chk_human_zone_1 = 'Checked'
        else :
            chk_human_zone_1 = 'Unchecked'

        if request.POST.get('chk_human_zone_2',False):
            chk_human_zone_2 = 'Checked'
        else :
            chk_human_zone_2 = 'Unchecked'

        if request.POST.get('chk_human_zone_3',False):
            chk_human_zone_3 = 'Checked'
        else :
            chk_human_zone_3 = 'Unchecked'

        if request.POST.get('chk_animal_zone_1',False):
            chk_animal_zone_1 = 'Checked'
        else :
            chk_animal_zone_1 = 'Unchecked'

        if request.POST.get('chk_animal_zone_2',False):
            chk_animal_zone_2 = 'Checked'
        else :
            chk_animal_zone_2 = 'Unchecked'

        if request.POST.get('chk_animal_zone_3',False):
            chk_animal_zone_3 = 'Checked'
        else :
            chk_animal_zone_3 = 'Unchecked'

        if request.POST.get('chk_vector_A_zone_1',False):
            chk_vector_A_zone_1 = 'Checked'
        else :
            chk_vector_A_zone_1 = 'Unchecked'

        if request.POST.get('chk_vector_A_zone_2',False):
            chk_vector_A_zone_2 = 'Checked'
        else :
            chk_vector_A_zone_2 = 'Unchecked'

        if request.POST.get('chk_vector_A_zone_3',False):
            chk_vector_A_zone_3 = 'Checked'
        else :
            chk_vector_A_zone_3 = 'Unchecked'

        if request.POST.get('chk_vector_B_zone_1', False):
            chk_vector_B_zone_1 = 'Checked'
        else:
            chk_vector_B_zone_1 = 'Unchecked'

        if request.POST.get('chk_vector_B_zone_2', False):
            chk_vector_B_zone_2 = 'Checked'
        else:
            chk_vector_B_zone_2 = 'Unchecked'

        if request.POST.get('chk_vector_B_zone_3', False):
            chk_vector_B_zone_3 = 'Checked'
        else:
            chk_vector_B_zone_3 = 'Unchecked'

        if request.POST.get('chk_vector_C_zone_1', False):
            chk_vector_C_zone_1 = 'Checked'
        else:
            chk_vector_C_zone_1 = 'Unchecked'

        if request.POST.get('chk_vector_C_zone_2', False):
            chk_vector_C_zone_2 = 'Checked'
        else:
            chk_vector_C_zone_2 = 'Unchecked'

        if request.POST.get('chk_vector_C_zone_3', False):
            chk_vector_C_zone_3 = 'Checked'
        else:
            chk_vector_C_zone_3 = 'Unchecked'

        if request.POST.get('chk_vector_D_zone_1', False):
            chk_vector_D_zone_1 = 'Checked'
        else:
            chk_vector_D_zone_1 = 'Unchecked'

        if request.POST.get('chk_vector_D_zone_2', False):
            chk_vector_D_zone_2 = 'Checked'
        else:
            chk_vector_D_zone_2 = 'Unchecked'

        if request.POST.get('chk_vector_D_zone_3', False):
            chk_vector_D_zone_3 = 'Checked'
        else:
            chk_vector_D_zone_3 = 'Unchecked'

        x = rvf_user_1_collection.insert_one({
                                                'simulation_years':simulation_years,
                                                'start_day':start_day,
                                                'stop_day':stop_day,
                                                'rng_seed':rng_seed,
                                                'chk_human_zone_1':chk_human_zone_1,
                                                'chk_human_zone_2': chk_human_zone_2,
                                                'chk_human_zone_3': chk_human_zone_3,
                                                'chk_animal_zone_1': chk_animal_zone_1,
                                                'chk_animal_zone_2': chk_animal_zone_2,
                                                'chk_animal_zone_3': chk_animal_zone_3,
                                                'chk_vector_A_zone_1': chk_vector_A_zone_1,
                                                'chk_vector_A_zone_2': chk_vector_A_zone_2,
                                                'chk_vector_A_zone_3': chk_vector_A_zone_3,
                                                'chk_vector_B_zone_1': chk_vector_B_zone_1,
                                                'chk_vector_B_zone_2': chk_vector_B_zone_2,
                                                'chk_vector_B_zone_3': chk_vector_B_zone_3,
                                                'chk_vector_C_zone_1': chk_vector_C_zone_1,
                                                'chk_vector_C_zone_2': chk_vector_C_zone_2,
                                                'chk_vector_C_zone_3': chk_vector_C_zone_3,
                                                'chk_vector_D_zone_1': chk_vector_D_zone_1,
                                                'chk_vector_D_zone_2': chk_vector_D_zone_2,
                                                'chk_vector_D_zone_3': chk_vector_D_zone_3,
                                            })


    for x in rvf_user_1_collection.find({}, {"_id": 0}):
       context = x

    for y in rvf_vector_D_collection.find({}, {"_id": 0}):
        vector_D_context = y

    context2 = {
        'simulation_years':context['simulation_years'],
        'start_day':context['start_day'],
        'stop_day':context['stop_day'],
        'rng_seed': context['rng_seed'],
        'chk_human_zone_1':context['chk_human_zone_1'],
        'chk_human_zone_2': context['chk_human_zone_2'],
        'chk_human_zone_3': context['chk_human_zone_3'],
        'chk_animal_zone_1': context['chk_animal_zone_1'],
        'chk_animal_zone_2': context['chk_animal_zone_2'],
        'chk_animal_zone_3': context['chk_animal_zone_3'],
        'chk_vector_A_zone_1': context['chk_vector_A_zone_1'],
        'chk_vector_A_zone_2': context['chk_vector_A_zone_2'],
        'chk_vector_A_zone_3': context['chk_vector_A_zone_3'],
        'chk_vector_B_zone_1': context['chk_vector_B_zone_1'],
        'chk_vector_B_zone_2': context['chk_vector_B_zone_2'],
        'chk_vector_B_zone_3': context['chk_vector_B_zone_3'],
        'chk_vector_C_zone_1': context['chk_vector_C_zone_1'],
        'chk_vector_C_zone_2': context['chk_vector_C_zone_2'],
        'chk_vector_C_zone_3': context['chk_vector_C_zone_3'],
        'chk_vector_D_zone_1': context['chk_vector_D_zone_1'],
        'chk_vector_D_zone_2': context['chk_vector_D_zone_2'],
        'chk_vector_D_zone_3': context['chk_vector_D_zone_3'],
        'calc':int(context['simulation_years'])*int(context['start_day'])*int(vector_D_context['vector_D_oviposition_rate'])
    }

    #sheets = Sheets.from_files("templates/client_secret.json")
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = os.path.join(__location__, 'templates/shield.json');

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
    creds = Credentials.from_service_account_file(f, scopes = scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("anto1").sheet1

    sheet.update_cell(1,1,"Human Results")
    sheet.update_cell(1,2,"Zone 1")
    sheet.update_cell(1, 3, "Zone 1")
    sheet.update_cell(1, 4, "Zone 1")
    sheet.update_cell(2, 1, "Rate of change in the susceptible human compartment")
    sheet.update_cell(3, 1, "Rate of change in the human exposed (incubating) compartment")
    sheet.update_cell(4, 1, "Rate of change in the infective human compartment")
    sheet.update_cell(5, 1, "Rate of change in the recovered (immune) human compartment")

    sheet.update_cell(2, 2, int(context['simulation_years'])*int(context['start_day'])*int(vector_D_context['vector_D_oviposition_rate']))
    sheet.update_cell(3, 2, "0")
    sheet.update_cell(4, 2, "0")
    sheet.update_cell(5, 2, "0")

    sheet.update_cell(2, 3, "0")
    sheet.update_cell(3, 3, "0")
    sheet.update_cell(4, 3, "0")
    sheet.update_cell(5, 3, "0")

    sheet.update_cell(2, 4, "0")
    sheet.update_cell(3, 4, "0")
    sheet.update_cell(4, 4, "0")
    sheet.update_cell(5, 4, "0")

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_records()
    print(list_of_hashes)

    return render(request,'rvf_start.html',context2)
def page_range_js(req):
    return render(req, 'static/rangeslider.js', {})
def page_range_css(req):
    return render(req, 'static/rangeslider.css', {})
def page_equation_pic(req):
    return render(req, 'static/equations_pic.png', {})

def generate_view(request, *args, **kwargs):
    contex = {
        'HS_Zone1': 0,
        'HS_Zone2': 0,
        'HS_Zone3': 0,
        'HE_Zone1': 0,
        'HE_Zone2': 0,
        'HE_Zone3': 0,
        'HI_Zone1': 0,
        'HI_Zone2': 0,
        'HI_Zone3': 0,
        'HR_Zone1': 0,
        'HR_Zone2': 0,
        'HR_Zone3': 0,
        'MS_Zone1': 0,
        'MS_Zone2': 0,
        'MS_Zone3': 0,
        'ME_Zone1': 0,
        'ME_Zone2': 0,
        'ME_Zone3': 0,
        'MI_Zone1': 0,
        'MI_Zone2': 0,
        'MI_Zone3': 0,
        'MR_Zone1': 0,
        'MR_Zone2': 0,
        'MR_Zone3': 0,

        'AQ_Zone1': 0,
        'AQ_Zone2': 0,
        'AQ_Zone3': 0,
        'AP_Zone1': 0,
        'AP_Zone2': 0,
        'AP_Zone3': 0,
        'AS_Zone1': 0,
        'AS_Zone2': 0,
        'AS_Zone3': 0,
        'AI_Zone1': 0,
        'AI_Zone2': 0,
        'AI_Zone3': 0,
        'BQ_Zone1': 0,
        'BQ_Zone2': 0,
        'BQ_Zone3': 0,
        'BP_Zone1': 0,
        'BP_Zone2': 0,
        'BP_Zone3': 0,
        'BS_Zone1': 0,
        'BS_Zone2': 0,
        'BS_Zone3': 0,

        'BI_Zone1': 0,
        'BI_Zone2': 0,
        'BI_Zone3': 0,
        'CP_Zone1': 0,
        'CP_Zone2': 0,
        'CP_Zone3': 0,
        'CS_Zone1': 0,
        'CS_Zone2': 0,
        'CS_Zone3': 0,
        'CI_Zone1': 0,
        'CI_Zone2': 0,
        'CI_Zone3': 0,
        'DP_Zone1': 0,
        'DP_Zone2': 0,
        'DP_Zone3': 0,
        'DS_Zone1': 0,
        'DS_Zone2': 0,
        'DS_Zone3': 0,
        'DI_Zone1': 0,
        'DI_Zone2': 0,
        'DI_Zone3': 0,
    }
    pdf = render_to_pdf('initial.html', contex)
    return HttpResponse(pdf, content_type='application/pdf')

def initial_state(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['initial_table']

    contex = {
        'HS_Zone1': 0,
        'HS_Zone2': 0,
        'HS_Zone3': 0,
        'HE_Zone1': 0,
        'HE_Zone2': 0,
        'HE_Zone3': 0,
        'HI_Zone1': 0,
        'HI_Zone2': 0,
        'HI_Zone3': 0,
        'HR_Zone1': 0,
        'HR_Zone2': 0,
        'HR_Zone3': 0,
        'MS_Zone1': 0,
        'MS_Zone2': 0,
        'MS_Zone3': 0,
        'ME_Zone1': 0,
        'ME_Zone2': 0,
        'ME_Zone3': 0,
        'MI_Zone1': 0,
        'MI_Zone2': 0,
        'MI_Zone3': 0,
        'MR_Zone1': 0,
        'MR_Zone2': 0,
        'MR_Zone3': 0,

        'AQ_Zone1': 0,
        'AQ_Zone2': 0,
        'AQ_Zone3': 0,
        'AP_Zone1': 0,
        'AP_Zone2': 0,
        'AP_Zone3': 0,
        'AS_Zone1': 0,
        'AS_Zone2': 0,
        'AS_Zone3': 0,
        'AI_Zone1': 0,
        'AI_Zone2': 0,
        'AI_Zone3': 0,
        'BQ_Zone1': 0,
        'BQ_Zone2': 0,
        'BQ_Zone3': 0,
        'BP_Zone1': 0,
        'BP_Zone2': 0,
        'BP_Zone3': 0,
        'BS_Zone1': 0,
        'BS_Zone2': 0,
        'BS_Zone3': 0,

        'BI_Zone1': 0,
        'BI_Zone2': 0,
        'BI_Zone3': 0,
        'CP_Zone1': 0,
        'CP_Zone2': 0,
        'CP_Zone3': 0,
        'CS_Zone1': 0,
        'CS_Zone2': 0,
        'CS_Zone3': 0,
        'CI_Zone1': 0,
        'CI_Zone2': 0,
        'CI_Zone3': 0,
        'DP_Zone1': 0,
        'DP_Zone2': 0,
        'DP_Zone3': 0,
        'DS_Zone1': 0,
        'DS_Zone2': 0,
        'DS_Zone3': 0,
        'DI_Zone1': 0,
        'DI_Zone2': 0,
        'DI_Zone3': 0,
    }

    if (request.method == "POST"):
        HS_Zone1 = request.POST['HS_Zone1']
        HS_Zone2 = request.POST['HS_Zone2']
        HS_Zone3 = request.POST['HS_Zone3']
        HE_Zone1 = request.POST['HE_Zone1']
        HE_Zone2 = request.POST['HE_Zone2']
        HE_Zone3 = request.POST['HE_Zone3']

        HI_Zone1 = request.POST['HI_Zone1']
        HI_Zone2 = request.POST['HI_Zone2']
        HI_Zone3 = request.POST['HI_Zone3']

        HR_Zone1 = request.POST['HR_Zone1']
        HR_Zone2 = request.POST['HR_Zone2']
        HR_Zone3 = request.POST['HR_Zone3']

        MS_Zone1 = request.POST['MS_Zone1']
        MS_Zone2 = request.POST['MS_Zone2']
        MS_Zone3 = request.POST['MS_Zone3']
        ME_Zone1 = request.POST['ME_Zone1']
        ME_Zone2 = request.POST['ME_Zone2']
        ME_Zone3 = request.POST['ME_Zone3']

        MI_Zone1 = request.POST['MI_Zone1']
        MI_Zone2 = request.POST['MI_Zone2']
        MI_Zone3 = request.POST['MI_Zone3']

        MR_Zone1 = request.POST['MR_Zone1']
        MR_Zone2 = request.POST['MR_Zone2']
        MR_Zone3 = request.POST['MR_Zone3']

        AQ_Zone1 = request.POST['AQ_Zone1']
        AQ_Zone2 = request.POST['AQ_Zone2']
        AQ_Zone3 = request.POST['AQ_Zone3']
        AP_Zone1 = request.POST['AP_Zone1']
        AP_Zone2 = request.POST['AP_Zone2']
        AP_Zone3 = request.POST['AP_Zone3']

        AS_Zone1 = request.POST['AS_Zone1']
        AS_Zone2 = request.POST['AS_Zone2']
        AS_Zone3 = request.POST['AS_Zone3']

        AI_Zone1 = request.POST['AI_Zone1']
        AI_Zone2 = request.POST['AI_Zone2']
        AI_Zone3 = request.POST['AI_Zone3']

        BQ_Zone1 = request.POST['BQ_Zone1']
        BQ_Zone2 = request.POST['BQ_Zone2']
        BQ_Zone3 = request.POST['BQ_Zone3']
        BP_Zone1 = request.POST['BP_Zone1']
        BP_Zone2 = request.POST['BP_Zone2']
        BP_Zone3 = request.POST['BP_Zone3']

        BS_Zone1 = request.POST['BS_Zone1']
        BS_Zone2 = request.POST['BS_Zone2']
        BS_Zone3 = request.POST['BS_Zone3']

        BI_Zone1 = request.POST['BI_Zone1']
        BI_Zone2 = request.POST['BI_Zone2']
        BI_Zone3 = request.POST['BI_Zone3']

        CP_Zone1 = request.POST['CP_Zone1']
        CP_Zone2 = request.POST['CP_Zone2']
        CP_Zone3 = request.POST['CP_Zone3']

        CS_Zone1 = request.POST['CS_Zone1']
        CS_Zone2 = request.POST['CS_Zone2']
        CS_Zone3 = request.POST['CS_Zone3']

        CI_Zone1 = request.POST['CI_Zone1']
        CI_Zone2 = request.POST['CI_Zone2']
        CI_Zone3 = request.POST['CI_Zone3']

        DP_Zone1 = request.POST['DP_Zone1']
        DP_Zone2 = request.POST['DP_Zone2']
        DP_Zone3 = request.POST['DP_Zone3']

        DS_Zone1 = request.POST['DS_Zone1']
        DS_Zone2 = request.POST['DS_Zone2']
        DS_Zone3 = request.POST['DS_Zone3']

        DI_Zone1 = request.POST['DI_Zone1']
        DI_Zone2 = request.POST['DI_Zone2']
        DI_Zone3 = request.POST['DI_Zone3']

        x = rvf_initial_collection.insert_one({
            'HS_Zone1': HS_Zone1,
            'HS_Zone2': HS_Zone2,
            'HS_Zone3': HS_Zone3,
            'HE_Zone1': HE_Zone1,
            'HE_Zone2': HE_Zone2,
            'HE_Zone3': HE_Zone3,
            'HI_Zone1': HI_Zone1,
            'HI_Zone2': HI_Zone2,
            'HI_Zone3': HI_Zone3,
            'HR_Zone1': HR_Zone1,
            'HR_Zone2': HR_Zone2,
            'HR_Zone3': HR_Zone3,
            'MS_Zone1': MS_Zone1,
            'MS_Zone2': MS_Zone2,
            'MS_Zone3': MS_Zone3,
            'ME_Zone1': ME_Zone1,
            'ME_Zone2': ME_Zone2,
            'ME_Zone3': ME_Zone3,
            'MI_Zone1': MI_Zone1,
            'MI_Zone2': MI_Zone2,
            'MI_Zone3': MI_Zone3,
            'MR_Zone1': MR_Zone1,
            'MR_Zone2': MR_Zone2,
            'MR_Zone3': MR_Zone3,

            'AQ_Zone1': AQ_Zone1,
            'AQ_Zone2': AQ_Zone2,
            'AQ_Zone3': AQ_Zone3,
            'AP_Zone1': AP_Zone1,
            'AP_Zone2': AP_Zone2,
            'AP_Zone3': AP_Zone3,
            'AS_Zone1': AS_Zone1,
            'AS_Zone2': AS_Zone2,
            'AS_Zone3': AS_Zone3,
            'AI_Zone1': AI_Zone1,
            'AI_Zone2': AI_Zone2,
            'AI_Zone3': AI_Zone3,
            'BQ_Zone1': BQ_Zone1,
            'BQ_Zone2': BQ_Zone2,
            'BQ_Zone3': BQ_Zone3,
            'BP_Zone1': BP_Zone1,
            'BP_Zone2': BP_Zone2,
            'BP_Zone3': BP_Zone3,
            'BS_Zone1': BS_Zone1,
            'BS_Zone2': BS_Zone2,
            'BS_Zone3': BS_Zone3,

            'BI_Zone1': BI_Zone1,
            'BI_Zone2': BI_Zone2,
            'BI_Zone3': BI_Zone3,
            'CP_Zone1': CP_Zone1,
            'CP_Zone2': CP_Zone2,
            'CP_Zone3': CP_Zone3,
            'CS_Zone1': CS_Zone1,
            'CS_Zone2': CS_Zone2,
            'CS_Zone3': CS_Zone3,
            'CI_Zone1': CI_Zone1,
            'CI_Zone2': CI_Zone2,
            'CI_Zone3': CI_Zone3,
            'DP_Zone1': DP_Zone1,
            'DP_Zone2': DP_Zone2,
            'DP_Zone3': DP_Zone3,
            'DS_Zone1': DS_Zone1,
            'DS_Zone2': DS_Zone2,
            'DS_Zone3': DS_Zone3,
            'DI_Zone1': DI_Zone1,
            'DI_Zone2': DI_Zone2,
            'DI_Zone3': DI_Zone3,
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'HS_Zone1': context['HS_Zone1'],
        'HS_Zone2': context['HS_Zone2'],
        'HS_Zone3': context['HS_Zone3'],
        'HE_Zone1': context['HE_Zone1'],
        'HE_Zone2': context['HE_Zone2'],
        'HE_Zone3': context['HE_Zone3'],
        'HI_Zone1': context['HI_Zone1'],
        'HI_Zone2': context['HI_Zone2'],
        'HI_Zone3': context['HI_Zone3'],
        'HR_Zone1': context['HR_Zone1'],
        'HR_Zone2': context['HR_Zone2'],
        'HR_Zone3': context['HR_Zone3'],
        'MS_Zone1': context['MS_Zone1'],
        'MS_Zone2': context['MS_Zone2'],
        'MS_Zone3': context['MS_Zone3'],
        'ME_Zone1': context['ME_Zone1'],
        'ME_Zone2': context['ME_Zone2'],
        'ME_Zone3': context['ME_Zone3'],
        'MI_Zone1': context['MI_Zone1'],
        'MI_Zone2': context['MI_Zone2'],
        'MI_Zone3': context['MI_Zone3'],
        'MR_Zone1': context['MR_Zone1'],
        'MR_Zone2': context['MR_Zone2'],
        'MR_Zone3': context['MR_Zone3'],

        'AQ_Zone1': context['AQ_Zone1'],
        'AQ_Zone2': context['AQ_Zone2'],
        'AQ_Zone3': context['AQ_Zone3'],
        'AP_Zone1': context['AP_Zone1'],
        'AP_Zone2': context['AP_Zone2'],
        'AP_Zone3': context['AP_Zone3'],
        'AS_Zone1': context['AS_Zone1'],
        'AS_Zone2': context['AS_Zone2'],
        'AS_Zone3': context['AS_Zone3'],
        'AI_Zone1': context['AI_Zone1'],
        'AI_Zone2': context['AI_Zone2'],
        'AI_Zone3': context['AI_Zone3'],
        'BQ_Zone1': context['BQ_Zone1'],
        'BQ_Zone2': context['BQ_Zone2'],
        'BQ_Zone3': context['BQ_Zone3'],
        'BP_Zone1': context['BP_Zone1'],
        'BP_Zone2': context['BP_Zone2'],
        'BP_Zone3': context['BP_Zone3'],
        'BS_Zone1': context['BS_Zone1'],
        'BS_Zone2': context['BS_Zone2'],
        'BS_Zone3': context['BS_Zone3'],

        'BI_Zone1': context['BI_Zone1'],
        'BI_Zone2': context['BI_Zone2'],
        'BI_Zone3': context['BI_Zone3'],
        'CP_Zone1': context['CP_Zone1'],
        'CP_Zone2': context['CP_Zone2'],
        'CP_Zone3': context['CP_Zone3'],
        'CS_Zone1': context['CS_Zone1'],
        'CS_Zone2': context['CS_Zone2'],
        'CS_Zone3': context['CS_Zone3'],
        'CI_Zone1': context['CI_Zone1'],
        'CI_Zone2': context['CI_Zone2'],
        'CI_Zone3': context['CI_Zone3'],
        'DP_Zone1': context['DP_Zone1'],
        'DP_Zone2': context['DP_Zone2'],
        'DP_Zone3': context['DP_Zone3'],
        'DS_Zone1': context['DS_Zone1'],
        'DS_Zone2': context['DS_Zone2'],
        'DS_Zone3': context['DS_Zone3'],
        'DI_Zone1': context['DI_Zone1'],
        'DI_Zone2': context['DI_Zone2'],
        'DI_Zone3': context['DI_Zone3'],
    }

    return render(request,'initial.html',context2)
def general_info(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_gm_info_collection = rvf_db['gm_info_table']

    contex = {
        'chk_elnino_flooding': 'Checked',
        'elnino_start_day': 1,
        'elnino_stop_day': 1,
        'chk_annual_flooding': 'Checked',
        'annual_start_day': 1,
        'annual_stop_day': 1,
        'annual_proportion': 1,
        'chk_s_effect_hatching': 'Checked',
        's_effect_hatching_delay': 1,
        's_effect_hatching_peaks': 1,
        'chk_annual_variation_climate': 'Checked',
        'annual_variation_dry_years': 1,
        'annual_variation_total_years': 1,
        'annual_variation_minimum': 1,
        'chk_annual_transhumance': 'Checked',
        'trans_home_to_pasture': 1,
        'trans_pasture_to_home': 1,
        'chk_animal_susceptibility': 'Checked',
        'animal_susceptibility_start': 1,
        'animal_susceptibility_stop': 1,
        'animal_susceptibility_factor': 1,
        'infected_rate_wildlife': 1,
        'alt_host_bite': 1,
    }

    if (request.method == "POST"):
        elnino_start_day = request.POST['elnino_start_day']
        elnino_stop_day = request.POST['elnino_stop_day']
        annual_start_day = request.POST['annual_start_day']
        annual_stop_day = request.POST['annual_stop_day']
        annual_proportion = request.POST['annual_proportion']
        s_effect_hatching_delay = request.POST['s_effect_hatching_delay']
        s_effect_hatching_peaks = request.POST['s_effect_hatching_peaks']
        annual_variation_dry_years = request.POST['annual_variation_dry_years']
        annual_variation_total_years = request.POST['annual_variation_total_years']
        annual_variation_minimum = request.POST['annual_variation_minimum']
        trans_home_to_pasture = request.POST['trans_home_to_pasture']
        trans_pasture_to_home = request.POST['trans_pasture_to_home']
        animal_susceptibility_start = request.POST['animal_susceptibility_start']
        animal_susceptibility_stop = request.POST['animal_susceptibility_stop']
        animal_susceptibility_factor = request.POST['animal_susceptibility_factor']
        infected_rate_wildlife = request.POST['infected_rate_wildlife']
        alt_host_bite = request.POST['alt_host_bite']

        if request.POST.get('chk_elnino_flooding', False):
            chk_elnino_flooding = 'Checked'
        else:
            chk_elnino_flooding = 'Unchecked'

        if request.POST.get('chk_annual_flooding', False):
            chk_annual_flooding = 'Checked'
        else:
            chk_annual_flooding = 'Unchecked'

        if request.POST.get('chk_s_effect_hatching', False):
            chk_s_effect_hatching = 'Checked'
        else:
            chk_s_effect_hatching = 'Unchecked'

        if request.POST.get('chk_annual_variation_climate', False):
            chk_annual_variation_climate = 'Checked'
        else:
            chk_annual_variation_climate = 'Unchecked'

        if request.POST.get('chk_annual_transhumance', False):
            chk_annual_transhumance = 'Checked'
        else:
            chk_annual_transhumance = 'Unchecked'

        if request.POST.get('chk_animal_susceptibility', False):
            chk_animal_susceptibility = 'Checked'
        else:
            chk_animal_susceptibility = 'Unchecked'

        x = rvf_gm_info_collection.insert_one({
            'chk_elnino_flooding': chk_elnino_flooding,
            'elnino_start_day': elnino_start_day,
            'elnino_stop_day': elnino_stop_day,
            'chk_annual_flooding': chk_annual_flooding,
            'annual_start_day': annual_start_day,
            'annual_stop_day': annual_stop_day,
            'annual_proportion': annual_proportion,
            'chk_s_effect_hatching': chk_s_effect_hatching,
            's_effect_hatching_delay': s_effect_hatching_delay,
            's_effect_hatching_peaks': s_effect_hatching_peaks,
            'chk_annual_variation_climate': chk_annual_variation_climate,
            'annual_variation_dry_years': annual_variation_dry_years,
            'annual_variation_total_years': annual_variation_total_years,
            'annual_variation_minimum': annual_variation_minimum,
            'chk_annual_transhumance': chk_annual_transhumance,
            'trans_home_to_pasture': trans_home_to_pasture,
            'trans_pasture_to_home': trans_pasture_to_home,
            'chk_animal_susceptibility': chk_animal_susceptibility,
            'animal_susceptibility_start': animal_susceptibility_start,
            'animal_susceptibility_stop': animal_susceptibility_stop,
            'animal_susceptibility_factor': animal_susceptibility_factor,
            'infected_rate_wildlife': infected_rate_wildlife,
            'alt_host_bite': alt_host_bite,
        })

    for x in rvf_gm_info_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'chk_elnino_flooding': context['chk_elnino_flooding'],
        'elnino_start_day': context['elnino_start_day'],
        'elnino_stop_day': context['elnino_stop_day'],
        'chk_annual_flooding': context['chk_annual_flooding'],
        'annual_start_day': context['annual_start_day'],
        'annual_stop_day': context['annual_stop_day'],
        'annual_proportion': context['annual_proportion'],
        'chk_s_effect_hatching': context['chk_s_effect_hatching'],
        's_effect_hatching_delay': context['s_effect_hatching_delay'],
        's_effect_hatching_peaks': context['s_effect_hatching_peaks'],
        'chk_annual_variation_climate': context['chk_annual_variation_climate'],
        'annual_variation_dry_years': context['annual_variation_dry_years'],
        'annual_variation_total_years': context['annual_variation_total_years'],
        'annual_variation_minimum': context['annual_variation_minimum'],
        'chk_annual_transhumance': context['chk_annual_transhumance'],
        'trans_home_to_pasture': context['trans_home_to_pasture'],
        'trans_pasture_to_home': context['trans_pasture_to_home'],
        'chk_animal_susceptibility': context['chk_animal_susceptibility'],
        'animal_susceptibility_start': context['animal_susceptibility_start'],
        'animal_susceptibility_stop': context['animal_susceptibility_stop'],
        'animal_susceptibility_factor': context['animal_susceptibility_factor'],
        'infected_rate_wildlife': context['infected_rate_wildlife'],
        'alt_host_bite': context['alt_host_bite'],
    }
    return render(request,'gm_info.html',context2)
def people_info(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_human_collection = rvf_db['human_table']

    contex = {
        'human_birth_rate': 0,
        'human_natural_mortality_rate': 0,
        'human_avg_incubation_period': 0,
        'human_avg_infective_period': 0,
        'human_avg_immune_period': 0,
        'human_disease_specific_mort_rate': 0,
        'human_contact_rate_to_animal_zone_1': 0,
        'human_contact_rate_to_animal_zone_2': 0,
        'human_contact_rate_to_animal_zone_3': 0,
        'human_migration_rate_1_to_2': 0,
        'human_migration_rate_1_to_3': 0,
        'human_migration_rate_2_to_1': 0,
        'human_migration_rate_2_to_3': 0,
        'human_migration_rate_3_to_1': 0,
        'human_migration_rate_3_to_2': 0,
        'human_infection_rate_to_vector_A': 0,
        'human_infection_rate_to_vector_B': 0,
        'human_infection_rate_to_vector_C': 0,
        'human_infection_rate_to_vector_D': 0,
        'human_max_biting_rate_zone_1': 0,
        'human_max_biting_rate_zone_2': 0,
        'human_max_biting_rate_zone_3': 0,
    }

    if (request.method == "POST"):
        human_birth_rate = request.POST['human_birth_rate']
        human_natural_mortality_rate = request.POST['human_natural_mortality_rate']
        human_avg_incubation_period = request.POST['human_avg_incubation_period']
        human_avg_infective_period = request.POST['human_avg_infective_period']
        human_avg_immune_period = request.POST['human_avg_immune_period']
        human_disease_specific_mort_rate = request.POST['human_disease_specific_mort_rate']

        human_contact_rate_to_animal_zone_1 = request.POST['human_contact_rate_to_animal_zone_1']
        human_contact_rate_to_animal_zone_2 = request.POST['human_contact_rate_to_animal_zone_2']
        human_contact_rate_to_animal_zone_3 = request.POST['human_contact_rate_to_animal_zone_3']

        human_migration_rate_1_to_2 = request.POST['human_migration_rate_1_to_2']
        human_migration_rate_1_to_3 = request.POST['human_migration_rate_1_to_3']
        human_migration_rate_2_to_1 = request.POST['human_migration_rate_2_to_1']

        human_migration_rate_2_to_3 = request.POST['human_migration_rate_2_to_3']
        human_migration_rate_3_to_1 = request.POST['human_migration_rate_3_to_1']
        human_migration_rate_3_to_2 = request.POST['human_migration_rate_3_to_2']

        human_infection_rate_to_vector_A = request.POST['human_infection_rate_to_vector_A']
        human_infection_rate_to_vector_B = request.POST['human_infection_rate_to_vector_B']
        human_infection_rate_to_vector_C = request.POST['human_infection_rate_to_vector_C']
        human_infection_rate_to_vector_D = request.POST['human_infection_rate_to_vector_D']
        human_max_biting_rate_zone_1 = request.POST['human_max_biting_rate_zone_1']
        human_max_biting_rate_zone_2 = request.POST['human_max_biting_rate_zone_2']
        human_max_biting_rate_zone_3 = request.POST['human_max_biting_rate_zone_3']

        x = rvf_human_collection.insert_one({
            'human_birth_rate': human_birth_rate,
            'human_natural_mortality_rate': human_natural_mortality_rate,
            'human_avg_incubation_period': human_avg_incubation_period,
            'human_avg_infective_period': human_avg_infective_period,
            'human_avg_immune_period': human_avg_immune_period,
            'human_disease_specific_mort_rate': human_disease_specific_mort_rate,
            'human_contact_rate_to_animal_zone_1': human_contact_rate_to_animal_zone_1,
            'human_contact_rate_to_animal_zone_2': human_contact_rate_to_animal_zone_2,
            'human_contact_rate_to_animal_zone_3': human_contact_rate_to_animal_zone_3,
            'human_migration_rate_1_to_2': human_migration_rate_1_to_2,
            'human_migration_rate_1_to_3': human_migration_rate_1_to_3,
            'human_migration_rate_2_to_1': human_migration_rate_2_to_1,
            'human_migration_rate_2_to_3': human_migration_rate_2_to_3,
            'human_migration_rate_3_to_1': human_migration_rate_3_to_1,
            'human_migration_rate_3_to_2': human_migration_rate_3_to_2,
            'human_infection_rate_to_vector_A': human_infection_rate_to_vector_A,
            'human_infection_rate_to_vector_B': human_infection_rate_to_vector_B,
            'human_infection_rate_to_vector_C': human_infection_rate_to_vector_C,
            'human_infection_rate_to_vector_D': human_infection_rate_to_vector_D,
            'human_max_biting_rate_zone_1': human_max_biting_rate_zone_1,
            'human_max_biting_rate_zone_2': human_max_biting_rate_zone_2,
            'human_max_biting_rate_zone_3': human_max_biting_rate_zone_3,
        })

    for x in rvf_human_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
                'human_birth_rate' : context['human_birth_rate'],
                'human_natural_mortality_rate' : context['human_natural_mortality_rate'],
                'human_avg_incubation_period' : context['human_avg_incubation_period'],
                'human_avg_infective_period' : context['human_avg_infective_period'],
                'human_avg_immune_period' : context['human_avg_immune_period'],
                'human_disease_specific_mort_rate' : context['human_disease_specific_mort_rate'],
                'human_contact_rate_to_animal_zone_1' : context['human_contact_rate_to_animal_zone_1'],
                'human_contact_rate_to_animal_zone_2' : context['human_contact_rate_to_animal_zone_2'],
                'human_contact_rate_to_animal_zone_3' : context['human_contact_rate_to_animal_zone_3'],
                'human_migration_rate_1_to_2' : context['human_migration_rate_1_to_2'],
                'human_migration_rate_1_to_3' : context['human_migration_rate_1_to_3'],
                'human_migration_rate_2_to_1' : context['human_migration_rate_2_to_1'],
                'human_migration_rate_2_to_3' : context['human_migration_rate_2_to_3'],
                'human_migration_rate_3_to_1' : context['human_migration_rate_3_to_1'],
                'human_migration_rate_3_to_2' : context['human_migration_rate_3_to_2'],
                'human_infection_rate_to_vector_A' : context['human_infection_rate_to_vector_A'],
                'human_infection_rate_to_vector_B' : context['human_infection_rate_to_vector_B'],
                'human_infection_rate_to_vector_C' : context['human_infection_rate_to_vector_C'],
                'human_infection_rate_to_vector_D' : context['human_infection_rate_to_vector_D'],
                'human_max_biting_rate_zone_1' : context['human_max_biting_rate_zone_1'],
                'human_max_biting_rate_zone_2' : context['human_max_biting_rate_zone_2'],
                'human_max_biting_rate_zone_3' : context['human_max_biting_rate_zone_3'],
    }
    return render(request,'people.html',context2)
def animal_info(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_animal_collection = rvf_db['animal_table']

    contex = {
        'animal_birth_rate_non_infected': 0,
        'animal_RVF_pop_abortion': 0,
        'animal_natural_mortality_rate': 0,
        'animal_avg_incubation_period': 0,
        'animal_avg_infective_period': 0,
        'animal_avg_immune_period': 0,
        'animal_disease_specific_mort_rate': 0,
        'animal_carrying_capacity_zone_1': 0,
        'animal_carrying_capacity_zone_2': 0,
        'animal_carrying_capacity_zone_3': 0,
        'animal_migration_rate_1_to_2': 0,
        'animal_migration_rate_1_to_3': 0,
        'animal_migration_rate_2_to_1': 0,
        'animal_migration_rate_2_to_3': 0,
        'animal_migration_rate_3_to_1': 0,
        'animal_migration_rate_3_to_2': 0,
        'animal_infection_rate_to_human': 0,
        'animal_infection_rate_to_vector_A': 0,
        'animal_infection_rate_to_vector_B': 0,
        'animal_infection_rate_to_vector_C': 0,
        'animal_infection_rate_to_vector_D': 0,
        'animal_max_biting_rate': 0,
    }

    if (request.method == "POST"):
        animal_birth_rate_non_infected = request.POST['animal_birth_rate_non_infected']
        animal_RVF_pop_abortion = request.POST['animal_RVF_pop_abortion']
        animal_natural_mortality_rate = request.POST['animal_natural_mortality_rate']
        animal_avg_incubation_period = request.POST['animal_avg_incubation_period']
        animal_avg_infective_period = request.POST['animal_avg_infective_period']
        animal_avg_immune_period = request.POST['animal_avg_immune_period']
        animal_disease_specific_mort_rate = request.POST['animal_disease_specific_mort_rate']
        animal_carrying_capacity_zone_1 = request.POST['animal_carrying_capacity_zone_1']
        animal_carrying_capacity_zone_2 = request.POST['animal_carrying_capacity_zone_2']
        animal_carrying_capacity_zone_3 = request.POST['animal_carrying_capacity_zone_3']

        animal_migration_rate_1_to_2 = request.POST['animal_migration_rate_1_to_2']
        animal_migration_rate_1_to_3 = request.POST['animal_migration_rate_1_to_3']
        animal_migration_rate_2_to_1 = request.POST['animal_migration_rate_2_to_1']

        animal_migration_rate_2_to_3 = request.POST['animal_migration_rate_2_to_3']
        animal_migration_rate_3_to_1 = request.POST['animal_migration_rate_3_to_1']
        animal_migration_rate_3_to_2 = request.POST['animal_migration_rate_3_to_2']
        animal_infection_rate_to_human = request.POST['animal_infection_rate_to_human']

        animal_infection_rate_to_vector_A = request.POST['animal_infection_rate_to_vector_A']
        animal_infection_rate_to_vector_B = request.POST['animal_infection_rate_to_vector_B']
        animal_infection_rate_to_vector_C = request.POST['animal_infection_rate_to_vector_C']
        animal_infection_rate_to_vector_D = request.POST['animal_infection_rate_to_vector_D']
        animal_max_biting_rate = request.POST['animal_max_biting_rate']

        x = rvf_animal_collection.insert_one({
            'animal_birth_rate_non_infected': animal_birth_rate_non_infected,
            'animal_RVF_pop_abortion': animal_RVF_pop_abortion,
            'animal_natural_mortality_rate': animal_natural_mortality_rate,
            'animal_avg_incubation_period': animal_avg_incubation_period,
            'animal_avg_infective_period': animal_avg_infective_period,
            'animal_avg_immune_period': animal_avg_immune_period,
            'animal_disease_specific_mort_rate': animal_disease_specific_mort_rate,
            'animal_carrying_capacity_zone_1': animal_carrying_capacity_zone_1,
            'animal_carrying_capacity_zone_2': animal_carrying_capacity_zone_2,
            'animal_carrying_capacity_zone_3': animal_carrying_capacity_zone_3,
            'animal_migration_rate_1_to_2': animal_migration_rate_1_to_2,
            'animal_migration_rate_1_to_3': animal_migration_rate_1_to_3,
            'animal_migration_rate_2_to_1': animal_migration_rate_2_to_1,
            'animal_migration_rate_2_to_3': animal_migration_rate_2_to_3,
            'animal_migration_rate_3_to_1': animal_migration_rate_3_to_1,
            'animal_migration_rate_3_to_2': animal_migration_rate_3_to_2,
            'animal_infection_rate_to_human': animal_infection_rate_to_human,
            'animal_infection_rate_to_vector_A': animal_infection_rate_to_vector_A,
            'animal_infection_rate_to_vector_B': animal_infection_rate_to_vector_B,
            'animal_infection_rate_to_vector_C': animal_infection_rate_to_vector_C,
            'animal_infection_rate_to_vector_D': animal_infection_rate_to_vector_D,
            'animal_max_biting_rate': animal_max_biting_rate,
        })


    for x in rvf_animal_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'animal_birth_rate_non_infected': context['animal_birth_rate_non_infected'],
        'animal_RVF_pop_abortion': context['animal_RVF_pop_abortion'],
        'animal_natural_mortality_rate': context['animal_natural_mortality_rate'],
        'animal_avg_incubation_period': context['animal_avg_incubation_period'],
        'animal_avg_infective_period': context['animal_avg_infective_period'],
        'animal_avg_immune_period': context['animal_avg_immune_period'],
        'animal_disease_specific_mort_rate': context['animal_disease_specific_mort_rate'],
        'animal_carrying_capacity_zone_1': context['animal_carrying_capacity_zone_1'],
        'animal_carrying_capacity_zone_2': context['animal_carrying_capacity_zone_2'],
        'animal_carrying_capacity_zone_3': context['animal_carrying_capacity_zone_3'],
        'animal_migration_rate_1_to_2': context['animal_migration_rate_1_to_2'],
        'animal_migration_rate_1_to_3': context['animal_migration_rate_1_to_3'],
        'animal_migration_rate_2_to_1': context['animal_migration_rate_2_to_1'],
        'animal_migration_rate_2_to_3': context['animal_migration_rate_2_to_3'],
        'animal_migration_rate_3_to_1': context['animal_migration_rate_3_to_1'],
        'animal_migration_rate_3_to_2': context['animal_migration_rate_3_to_2'],
        'animal_infection_rate_to_human': context['animal_infection_rate_to_human'],
        'animal_infection_rate_to_vector_A': context['animal_infection_rate_to_vector_A'],
        'animal_infection_rate_to_vector_B': context['animal_infection_rate_to_vector_B'],
        'animal_infection_rate_to_vector_C': context['animal_infection_rate_to_vector_C'],
        'animal_infection_rate_to_vector_D': context['animal_infection_rate_to_vector_D'],
        'animal_max_biting_rate': context['animal_max_biting_rate'],
    }
    return render(request,'animal.html',context2)
def vector_A_info(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_user_1_collection = rvf_db['vector_A_table']

    contex = {
        'vector_A_oviposition_rate': 0,
        'vector_A_prop_vertical_transmission': 0,
        'vector_A_hatching_rate': 0,
        'vector_A_mortality_rate': 0,
        'vector_A_infected_eggs_zone_1_mortality_rate': 0,
        'vector_A_infected_eggs_zone_2_mortality_rate': 0,
        'vector_A_infected_eggs_zone_3_mortality_rate': 0,
        'vector_A_uninfected_eggs_zone_1_mortality_rate': 0,
        'vector_A_uninfected_eggs_zone_2_mortality_rate': 0,
        'vector_A_uninfected_eggs_zone_3_mortality_rate': 0,
        'vector_A_carrying_capacity_zone_1': 0,
        'vector_A_carrying_capacity_zone_2': 0,
        'vector_A_carrying_capacity_zone_3': 0,
        'vector_A_migration_rate_1_to_2': 0,
        'vector_A_migration_rate_1_to_3': 0,
        'vector_A_migration_rate_2_to_1': 0,
        'vector_A_migration_rate_2_to_3': 0,
        'vector_A_migration_rate_3_to_1': 0,
        'vector_A_migration_rate_3_to_2': 0,
        'vector_A_infection_rate_to_human': 0,
        'vector_A_infection_rate_to_animal': 0,
        'vector_A_max_biting_rate': 0,
        'vector_A_human_feeding_prop': 0,
        'vector_A_animal_feeding_prop': 0,
    }

    if (request.method == "POST"):
        vector_A_oviposition_rate = request.POST['vector_A_oviposition_rate']
        vector_A_prop_vertical_transmission = request.POST['vector_A_prop_vertical_transmission']
        vector_A_hatching_rate = request.POST['vector_A_hatching_rate']
        vector_A_mortality_rate = request.POST['vector_A_mortality_rate']
        vector_A_infected_eggs_zone_1_mortality_rate = request.POST['vector_A_infected_eggs_zone_1_mortality_rate']
        vector_A_infected_eggs_zone_2_mortality_rate = request.POST['vector_A_infected_eggs_zone_2_mortality_rate']
        vector_A_infected_eggs_zone_3_mortality_rate = request.POST['vector_A_infected_eggs_zone_3_mortality_rate']
        vector_A_uninfected_eggs_zone_1_mortality_rate = request.POST['vector_A_uninfected_eggs_zone_1_mortality_rate']
        vector_A_uninfected_eggs_zone_2_mortality_rate = request.POST['vector_A_uninfected_eggs_zone_2_mortality_rate']
        vector_A_uninfected_eggs_zone_3_mortality_rate = request.POST['vector_A_uninfected_eggs_zone_3_mortality_rate']

        vector_A_carrying_capacity_zone_1 = request.POST['vector_A_carrying_capacity_zone_1']
        vector_A_carrying_capacity_zone_2 = request.POST['vector_A_carrying_capacity_zone_2']
        vector_A_carrying_capacity_zone_3 = request.POST['vector_A_carrying_capacity_zone_3']
        vector_A_migration_rate_1_to_2 = request.POST['vector_A_migration_rate_1_to_2']
        vector_A_migration_rate_1_to_3 = request.POST['vector_A_migration_rate_1_to_3']
        vector_A_migration_rate_2_to_1 = request.POST['vector_A_migration_rate_2_to_1']

        vector_A_migration_rate_2_to_3 = request.POST['vector_A_migration_rate_2_to_3']
        vector_A_migration_rate_3_to_1 = request.POST['vector_A_migration_rate_3_to_1']
        vector_A_migration_rate_3_to_2 = request.POST['vector_A_migration_rate_3_to_2']
        vector_A_infection_rate_to_human = request.POST['vector_A_infection_rate_to_human']

        vector_A_infection_rate_to_animal = request.POST['vector_A_infection_rate_to_animal']
        vector_A_max_biting_rate = request.POST['vector_A_max_biting_rate']
        vector_A_human_feeding_prop = request.POST['vector_A_human_feeding_prop']
        vector_A_animal_feeding_prop = request.POST['vector_A_animal_feeding_prop']

        x = rvf_user_1_collection.insert_one({
            'vector_A_oviposition_rate': vector_A_oviposition_rate,
            'vector_A_prop_vertical_transmission': vector_A_prop_vertical_transmission,
            'vector_A_hatching_rate': vector_A_hatching_rate,
            'vector_A_mortality_rate': vector_A_mortality_rate,
            'vector_A_infected_eggs_zone_1_mortality_rate': vector_A_infected_eggs_zone_1_mortality_rate,
            'vector_A_infected_eggs_zone_2_mortality_rate': vector_A_infected_eggs_zone_2_mortality_rate,
            'vector_A_infected_eggs_zone_3_mortality_rate': vector_A_infected_eggs_zone_3_mortality_rate,
            'vector_A_uninfected_eggs_zone_1_mortality_rate': vector_A_uninfected_eggs_zone_1_mortality_rate,
            'vector_A_uninfected_eggs_zone_2_mortality_rate': vector_A_uninfected_eggs_zone_2_mortality_rate,
            'vector_A_uninfected_eggs_zone_3_mortality_rate': vector_A_uninfected_eggs_zone_3_mortality_rate,
            'vector_A_carrying_capacity_zone_1': vector_A_carrying_capacity_zone_1,
            'vector_A_carrying_capacity_zone_2': vector_A_carrying_capacity_zone_2,
            'vector_A_carrying_capacity_zone_3': vector_A_carrying_capacity_zone_3,
            'vector_A_migration_rate_1_to_2': vector_A_migration_rate_1_to_2,
            'vector_A_migration_rate_1_to_3': vector_A_migration_rate_1_to_3,
            'vector_A_migration_rate_2_to_1': vector_A_migration_rate_2_to_1,
            'vector_A_migration_rate_2_to_3': vector_A_migration_rate_2_to_3,
            'vector_A_migration_rate_3_to_1': vector_A_migration_rate_3_to_1,
            'vector_A_migration_rate_3_to_2': vector_A_migration_rate_3_to_2,
            'vector_A_infection_rate_to_human': vector_A_infection_rate_to_human,
            'vector_A_infection_rate_to_animal': vector_A_infection_rate_to_animal,
            'vector_A_max_biting_rate': vector_A_max_biting_rate,
            'vector_A_human_feeding_prop': vector_A_human_feeding_prop,
            'vector_A_animal_feeding_prop': vector_A_animal_feeding_prop,
        })


    for x in rvf_user_1_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'vector_A_oviposition_rate': context['vector_A_oviposition_rate'],
        'vector_A_prop_vertical_transmission': context['vector_A_prop_vertical_transmission'],
        'vector_A_hatching_rate': context['vector_A_hatching_rate'],
        'vector_A_mortality_rate': context['vector_A_mortality_rate'],
        'vector_A_infected_eggs_zone_1_mortality_rate': context['vector_A_infected_eggs_zone_1_mortality_rate'],
        'vector_A_infected_eggs_zone_2_mortality_rate': context['vector_A_infected_eggs_zone_2_mortality_rate'],
        'vector_A_infected_eggs_zone_3_mortality_rate': context['vector_A_infected_eggs_zone_3_mortality_rate'],
        'vector_A_uninfected_eggs_zone_1_mortality_rate': context['vector_A_uninfected_eggs_zone_1_mortality_rate'],
        'vector_A_uninfected_eggs_zone_2_mortality_rate': context['vector_A_uninfected_eggs_zone_2_mortality_rate'],
        'vector_A_uninfected_eggs_zone_3_mortality_rate': context['vector_A_uninfected_eggs_zone_3_mortality_rate'],
        'vector_A_carrying_capacity_zone_1': context['vector_A_carrying_capacity_zone_1'],
        'vector_A_carrying_capacity_zone_2': context['vector_A_carrying_capacity_zone_2'],
        'vector_A_carrying_capacity_zone_3': context['vector_A_carrying_capacity_zone_3'],
        'vector_A_migration_rate_1_to_2': context['vector_A_migration_rate_1_to_2'],
        'vector_A_migration_rate_1_to_3': context['vector_A_migration_rate_1_to_3'],
        'vector_A_migration_rate_2_to_1': context['vector_A_migration_rate_2_to_1'],
        'vector_A_migration_rate_2_to_3': context['vector_A_migration_rate_2_to_3'],
        'vector_A_migration_rate_3_to_1': context['vector_A_migration_rate_3_to_1'],
        'vector_A_migration_rate_3_to_2': context['vector_A_migration_rate_3_to_2'],
        'vector_A_infection_rate_to_human': context['vector_A_infection_rate_to_human'],
        'vector_A_infection_rate_to_animal': context['vector_A_infection_rate_to_animal'],
        'vector_A_max_biting_rate': context['vector_A_max_biting_rate'],
        'vector_A_human_feeding_prop': context['vector_A_human_feeding_prop'],
        'vector_A_animal_feeding_prop': context['vector_A_animal_feeding_prop'],
    }
    return render(request,'vector_A.html',context2)
def vector_B_info(request):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        rvf_db = myclient['rvf_db2']

        rvf_user_1_collection = rvf_db['vector_B_table']

        contex = {
            'vector_B_oviposition_rate': 0,
            'vector_B_prop_vertical_transmission': 0,
            'vector_B_hatching_rate': 0,
            'vector_B_mortality_rate': 0,
            'vector_B_infected_eggs_zone_1_mortality_rate': 0,
            'vector_B_infected_eggs_zone_2_mortality_rate': 0,
            'vector_B_infected_eggs_zone_3_mortality_rate': 0,
            'vector_B_uninfected_eggs_zone_1_mortality_rate': 0,
            'vector_B_uninfected_eggs_zone_2_mortality_rate': 0,
            'vector_B_uninfected_eggs_zone_3_mortality_rate': 0,
            'vector_B_carrying_capacity_zone_1': 0,
            'vector_B_carrying_capacity_zone_2': 0,
            'vector_B_carrying_capacity_zone_3': 0,
            'vector_B_migration_rate_1_to_2': 0,
            'vector_B_migration_rate_1_to_3': 0,
            'vector_B_migration_rate_2_to_1': 0,
            'vector_B_migration_rate_2_to_3': 0,
            'vector_B_migration_rate_3_to_1': 0,
            'vector_B_migration_rate_3_to_2': 0,
            'vector_B_infection_rate_to_human': 0,
            'vector_B_infection_rate_to_animal': 0,
            'vector_B_max_biting_rate': 0,
            'vector_B_human_feeding_prop': 0,
            'vector_B_animal_feeding_prop': 0,
        }

        if (request.method == "POST"):
            vector_B_oviposition_rate = request.POST['vector_B_oviposition_rate']
            vector_B_prop_vertical_transmission = request.POST['vector_B_prop_vertical_transmission']
            vector_B_hatching_rate = request.POST['vector_B_hatching_rate']
            vector_B_mortality_rate = request.POST['vector_B_mortality_rate']
            vector_B_infected_eggs_zone_1_mortality_rate = request.POST['vector_B_infected_eggs_zone_1_mortality_rate']
            vector_B_infected_eggs_zone_2_mortality_rate = request.POST['vector_B_infected_eggs_zone_2_mortality_rate']
            vector_B_infected_eggs_zone_3_mortality_rate = request.POST['vector_B_infected_eggs_zone_3_mortality_rate']
            vector_B_uninfected_eggs_zone_1_mortality_rate = request.POST['vector_B_uninfected_eggs_zone_1_mortality_rate']
            vector_B_uninfected_eggs_zone_2_mortality_rate = request.POST['vector_B_uninfected_eggs_zone_2_mortality_rate']
            vector_B_uninfected_eggs_zone_3_mortality_rate = request.POST['vector_B_uninfected_eggs_zone_3_mortality_rate']

            vector_B_carrying_capacity_zone_1 = request.POST['vector_B_carrying_capacity_zone_1']
            vector_B_carrying_capacity_zone_2 = request.POST['vector_B_carrying_capacity_zone_2']
            vector_B_carrying_capacity_zone_3 = request.POST['vector_B_carrying_capacity_zone_3']
            vector_B_migration_rate_1_to_2 = request.POST['vector_B_migration_rate_1_to_2']
            vector_B_migration_rate_1_to_3 = request.POST['vector_B_migration_rate_1_to_3']
            vector_B_migration_rate_2_to_1 = request.POST['vector_B_migration_rate_2_to_1']

            vector_B_migration_rate_2_to_3 = request.POST['vector_B_migration_rate_2_to_3']
            vector_B_migration_rate_3_to_1 = request.POST['vector_B_migration_rate_3_to_1']
            vector_B_migration_rate_3_to_2 = request.POST['vector_B_migration_rate_3_to_2']
            vector_B_infection_rate_to_human = request.POST['vector_B_infection_rate_to_human']

            vector_B_infection_rate_to_animal = request.POST['vector_B_infection_rate_to_animal']
            vector_B_max_biting_rate = request.POST['vector_B_max_biting_rate']
            vector_B_human_feeding_prop = request.POST['vector_B_human_feeding_prop']
            vector_B_animal_feeding_prop = request.POST['vector_B_animal_feeding_prop']

            x = rvf_user_1_collection.insert_one({
                'vector_B_oviposition_rate': vector_B_oviposition_rate,
                'vector_B_prop_vertical_transmission': vector_B_prop_vertical_transmission,
                'vector_B_hatching_rate': vector_B_hatching_rate,
                'vector_B_mortality_rate': vector_B_mortality_rate,
                'vector_B_infected_eggs_zone_1_mortality_rate': vector_B_infected_eggs_zone_1_mortality_rate,
                'vector_B_infected_eggs_zone_2_mortality_rate': vector_B_infected_eggs_zone_2_mortality_rate,
                'vector_B_infected_eggs_zone_3_mortality_rate': vector_B_infected_eggs_zone_3_mortality_rate,
                'vector_B_uninfected_eggs_zone_1_mortality_rate': vector_B_uninfected_eggs_zone_1_mortality_rate,
                'vector_B_uninfected_eggs_zone_2_mortality_rate': vector_B_uninfected_eggs_zone_2_mortality_rate,
                'vector_B_uninfected_eggs_zone_3_mortality_rate': vector_B_uninfected_eggs_zone_3_mortality_rate,
                'vector_B_carrying_capacity_zone_1': vector_B_carrying_capacity_zone_1,
                'vector_B_carrying_capacity_zone_2': vector_B_carrying_capacity_zone_2,
                'vector_B_carrying_capacity_zone_3': vector_B_carrying_capacity_zone_3,
                'vector_B_migration_rate_1_to_2': vector_B_migration_rate_1_to_2,
                'vector_B_migration_rate_1_to_3': vector_B_migration_rate_1_to_3,
                'vector_B_migration_rate_2_to_1': vector_B_migration_rate_2_to_1,
                'vector_B_migration_rate_2_to_3': vector_B_migration_rate_2_to_3,
                'vector_B_migration_rate_3_to_1': vector_B_migration_rate_3_to_1,
                'vector_B_migration_rate_3_to_2': vector_B_migration_rate_3_to_2,
                'vector_B_infection_rate_to_human': vector_B_infection_rate_to_human,
                'vector_B_infection_rate_to_animal': vector_B_infection_rate_to_animal,
                'vector_B_max_biting_rate': vector_B_max_biting_rate,
                'vector_B_human_feeding_prop': vector_B_human_feeding_prop,
                'vector_B_animal_feeding_prop': vector_B_animal_feeding_prop,
            })

        for x in rvf_user_1_collection.find({}, {"_id": 0}):
            context = x

        context2 = {
            'vector_B_oviposition_rate': context['vector_B_oviposition_rate'],
            'vector_B_prop_vertical_transmission': context['vector_B_prop_vertical_transmission'],
            'vector_B_hatching_rate': context['vector_B_hatching_rate'],
            'vector_B_mortality_rate': context['vector_B_mortality_rate'],
            'vector_B_infected_eggs_zone_1_mortality_rate': context['vector_B_infected_eggs_zone_1_mortality_rate'],
            'vector_B_infected_eggs_zone_2_mortality_rate': context['vector_B_infected_eggs_zone_2_mortality_rate'],
            'vector_B_infected_eggs_zone_3_mortality_rate': context['vector_B_infected_eggs_zone_3_mortality_rate'],
            'vector_B_uninfected_eggs_zone_1_mortality_rate': context['vector_B_uninfected_eggs_zone_1_mortality_rate'],
            'vector_B_uninfected_eggs_zone_2_mortality_rate': context['vector_B_uninfected_eggs_zone_2_mortality_rate'],
            'vector_B_uninfected_eggs_zone_3_mortality_rate': context['vector_B_uninfected_eggs_zone_3_mortality_rate'],
            'vector_B_carrying_capacity_zone_1': context['vector_B_carrying_capacity_zone_1'],
            'vector_B_carrying_capacity_zone_2': context['vector_B_carrying_capacity_zone_2'],
            'vector_B_carrying_capacity_zone_3': context['vector_B_carrying_capacity_zone_3'],
            'vector_B_migration_rate_1_to_2': context['vector_B_migration_rate_1_to_2'],
            'vector_B_migration_rate_1_to_3': context['vector_B_migration_rate_1_to_3'],
            'vector_B_migration_rate_2_to_1': context['vector_B_migration_rate_2_to_1'],
            'vector_B_migration_rate_2_to_3': context['vector_B_migration_rate_2_to_3'],
            'vector_B_migration_rate_3_to_1': context['vector_B_migration_rate_3_to_1'],
            'vector_B_migration_rate_3_to_2': context['vector_B_migration_rate_3_to_2'],
            'vector_B_infection_rate_to_human': context['vector_B_infection_rate_to_human'],
            'vector_B_infection_rate_to_animal': context['vector_B_infection_rate_to_animal'],
            'vector_B_max_biting_rate': context['vector_B_max_biting_rate'],
            'vector_B_human_feeding_prop': context['vector_B_human_feeding_prop'],
            'vector_B_animal_feeding_prop': context['vector_B_animal_feeding_prop'],
        }

        return render(request,'vector_B.html',context2)

def vector_C_info(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_user_1_collection = rvf_db['vector_C_table']

    contex = {
        'vector_C_oviposition_rate': 0,
        'vector_C_hatching_rate': 0,
        'vector_C_mortality_rate_adults': 0,
        'vector_C_eggs_zone_1_mortality_rate': 0,
        'vector_C_eggs_zone_2_mortality_rate': 0,
        'vector_C_eggs_zone_3_mortality_rate': 0,
        'vector_C_carrying_capacity_zone_1': 0,
        'vector_C_carrying_capacity_zone_2': 0,
        'vector_C_carrying_capacity_zone_3': 0,
        'vector_C_migration_rate_1_to_2': 0,
        'vector_C_migration_rate_1_to_3': 0,
        'vector_C_migration_rate_2_to_1': 0,
        'vector_C_migration_rate_2_to_3': 0,
        'vector_C_migration_rate_3_to_1': 0,
        'vector_C_migration_rate_3_to_2': 0,
        'vector_C_infection_rate_to_human': 0,
        'vector_C_infection_rate_to_animal': 0,
        'vector_C_max_biting_rate': 0,
        'vector_C_human_feeding_prop': 0,
        'vector_C_animal_feeding_prop': 0,
    }

    if (request.method == "POST"):
        vector_C_oviposition_rate = request.POST['vector_C_oviposition_rate']
        vector_C_hatching_rate = request.POST['vector_C_hatching_rate']
        vector_C_mortality_rate_adults = request.POST['vector_C_mortality_rate_adults']
        vector_C_eggs_zone_1_mortality_rate = request.POST['vector_C_eggs_zone_1_mortality_rate']
        vector_C_eggs_zone_2_mortality_rate = request.POST['vector_C_eggs_zone_2_mortality_rate']
        vector_C_eggs_zone_3_mortality_rate = request.POST['vector_C_eggs_zone_3_mortality_rate']

        vector_C_carrying_capacity_zone_1 = request.POST['vector_C_carrying_capacity_zone_1']
        vector_C_carrying_capacity_zone_2 = request.POST['vector_C_carrying_capacity_zone_2']
        vector_C_carrying_capacity_zone_3 = request.POST['vector_C_carrying_capacity_zone_3']
        vector_C_migration_rate_1_to_2 = request.POST['vector_C_migration_rate_1_to_2']
        vector_C_migration_rate_1_to_3 = request.POST['vector_C_migration_rate_1_to_3']
        vector_C_migration_rate_2_to_1 = request.POST['vector_C_migration_rate_2_to_1']

        vector_C_migration_rate_2_to_3 = request.POST['vector_C_migration_rate_2_to_3']
        vector_C_migration_rate_3_to_1 = request.POST['vector_C_migration_rate_3_to_1']
        vector_C_migration_rate_3_to_2 = request.POST['vector_C_migration_rate_3_to_2']
        vector_C_infection_rate_to_human = request.POST['vector_C_infection_rate_to_human']

        vector_C_infection_rate_to_animal = request.POST['vector_C_infection_rate_to_animal']
        vector_C_max_biting_rate = request.POST['vector_C_max_biting_rate']
        vector_C_human_feeding_prop = request.POST['vector_C_human_feeding_prop']
        vector_C_animal_feeding_prop = request.POST['vector_C_animal_feeding_prop']

        x = rvf_user_1_collection.insert_one({
            'vector_C_oviposition_rate': vector_C_oviposition_rate,
            'vector_C_hatching_rate': vector_C_hatching_rate,
            'vector_C_mortality_rate_adults': vector_C_mortality_rate_adults,
            'vector_C_eggs_zone_1_mortality_rate': vector_C_eggs_zone_1_mortality_rate,
            'vector_C_eggs_zone_2_mortality_rate': vector_C_eggs_zone_2_mortality_rate,
            'vector_C_eggs_zone_3_mortality_rate': vector_C_eggs_zone_3_mortality_rate,
            'vector_C_carrying_capacity_zone_1': vector_C_carrying_capacity_zone_1,
            'vector_C_carrying_capacity_zone_2': vector_C_carrying_capacity_zone_2,
            'vector_C_carrying_capacity_zone_3': vector_C_carrying_capacity_zone_3,
            'vector_C_migration_rate_1_to_2': vector_C_migration_rate_1_to_2,
            'vector_C_migration_rate_1_to_3': vector_C_migration_rate_1_to_3,
            'vector_C_migration_rate_2_to_1': vector_C_migration_rate_2_to_1,
            'vector_C_migration_rate_2_to_3': vector_C_migration_rate_2_to_3,
            'vector_C_migration_rate_3_to_1': vector_C_migration_rate_3_to_1,
            'vector_C_migration_rate_3_to_2': vector_C_migration_rate_3_to_2,
            'vector_C_infection_rate_to_human': vector_C_infection_rate_to_human,
            'vector_C_infection_rate_to_animal': vector_C_infection_rate_to_animal,
            'vector_C_max_biting_rate': vector_C_max_biting_rate,
            'vector_C_human_feeding_prop': vector_C_human_feeding_prop,
            'vector_C_animal_feeding_prop': vector_C_animal_feeding_prop,
        })

    for x in rvf_user_1_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'vector_C_oviposition_rate': context['vector_C_oviposition_rate'],
        'vector_C_hatching_rate': context['vector_C_hatching_rate'],
        'vector_C_mortality_rate_adults': context['vector_C_mortality_rate_adults'],
        'vector_C_eggs_zone_1_mortality_rate': context['vector_C_eggs_zone_1_mortality_rate'],
        'vector_C_eggs_zone_2_mortality_rate': context['vector_C_eggs_zone_2_mortality_rate'],
        'vector_C_eggs_zone_3_mortality_rate': context['vector_C_eggs_zone_3_mortality_rate'],
        'vector_C_carrying_capacity_zone_1': context['vector_C_carrying_capacity_zone_1'],
        'vector_C_carrying_capacity_zone_2': context['vector_C_carrying_capacity_zone_2'],
        'vector_C_carrying_capacity_zone_3': context['vector_C_carrying_capacity_zone_3'],
        'vector_C_migration_rate_1_to_2': context['vector_C_migration_rate_1_to_2'],
        'vector_C_migration_rate_1_to_3': context['vector_C_migration_rate_1_to_3'],
        'vector_C_migration_rate_2_to_1': context['vector_C_migration_rate_2_to_1'],
        'vector_C_migration_rate_2_to_3': context['vector_C_migration_rate_2_to_3'],
        'vector_C_migration_rate_3_to_1': context['vector_C_migration_rate_3_to_1'],
        'vector_C_migration_rate_3_to_2': context['vector_C_migration_rate_3_to_2'],
        'vector_C_infection_rate_to_human': context['vector_C_infection_rate_to_human'],
        'vector_C_infection_rate_to_animal': context['vector_C_infection_rate_to_animal'],
        'vector_C_max_biting_rate': context['vector_C_max_biting_rate'],
        'vector_C_human_feeding_prop': context['vector_C_human_feeding_prop'],
        'vector_C_animal_feeding_prop': context['vector_C_animal_feeding_prop'],
    }
    return render(request,'vector_C.html',context2)

def vector_D_info(request):

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_user_1_collection = rvf_db['vector_D_table']

    contex = {
        'vector_D_oviposition_rate': 0,
        'vector_D_hatching_rate': 0,
        'vector_D_mortality_rate_adults': 0,
        'vector_D_eggs_zone_1_mortality_rate': 0,
        'vector_D_eggs_zone_2_mortality_rate' : 0,
        'vector_D_eggs_zone_3_mortality_rate': 0,
        'vector_D_carrying_capacity_zone_1': 0,
        'vector_D_carrying_capacity_zone_2': 0,
        'vector_D_carrying_capacity_zone_3': 0,
        'vector_D_migration_rate_1_to_2': 0,
        'vector_D_migration_rate_1_to_3' : 0,
        'vector_D_migration_rate_2_to_1': 0,
        'vector_D_migration_rate_2_to_3': 0,
        'vector_D_migration_rate_3_to_1': 0,
        'vector_D_migration_rate_3_to_2': 0,
        'vector_D_infection_rate_to_human': 0,
        'vector_D_infection_rate_to_animal': 0,
        'vector_D_max_biting_rate': 0,
        'vector_D_human_feeding_prop': 0,
        'vector_D_animal_feeding_prop': 0,
    }

    if (request.method == "POST"):
        vector_D_oviposition_rate = request.POST['vector_D_oviposition_rate']
        vector_D_hatching_rate = request.POST['vector_D_hatching_rate']
        vector_D_mortality_rate_adults = request.POST['vector_D_mortality_rate_adults']
        vector_D_eggs_zone_1_mortality_rate = request.POST['vector_D_eggs_zone_1_mortality_rate']
        vector_D_eggs_zone_2_mortality_rate = request.POST['vector_D_eggs_zone_2_mortality_rate']
        vector_D_eggs_zone_3_mortality_rate = request.POST['vector_D_eggs_zone_3_mortality_rate']

        vector_D_carrying_capacity_zone_1 = request.POST['vector_D_carrying_capacity_zone_1']
        vector_D_carrying_capacity_zone_2 = request.POST['vector_D_carrying_capacity_zone_2']
        vector_D_carrying_capacity_zone_3 = request.POST['vector_D_carrying_capacity_zone_3']
        vector_D_migration_rate_1_to_2 = request.POST['vector_D_migration_rate_1_to_2']
        vector_D_migration_rate_1_to_3 = request.POST['vector_D_migration_rate_1_to_3']
        vector_D_migration_rate_2_to_1 = request.POST['vector_D_migration_rate_2_to_1']

        vector_D_migration_rate_2_to_3 = request.POST['vector_D_migration_rate_2_to_3']
        vector_D_migration_rate_3_to_1 = request.POST['vector_D_migration_rate_3_to_1']
        vector_D_migration_rate_3_to_2 = request.POST['vector_D_migration_rate_3_to_2']
        vector_D_infection_rate_to_human = request.POST['vector_D_infection_rate_to_human']

        vector_D_infection_rate_to_animal = request.POST['vector_D_infection_rate_to_animal']
        vector_D_max_biting_rate = request.POST['vector_D_max_biting_rate']
        vector_D_human_feeding_prop = request.POST['vector_D_human_feeding_prop']
        vector_D_animal_feeding_prop = request.POST['vector_D_animal_feeding_prop']

        x = rvf_user_1_collection.insert_one({
            'vector_D_oviposition_rate': vector_D_oviposition_rate,
            'vector_D_hatching_rate': vector_D_hatching_rate,
            'vector_D_mortality_rate_adults': vector_D_mortality_rate_adults,
            'vector_D_eggs_zone_1_mortality_rate': vector_D_eggs_zone_1_mortality_rate,
            'vector_D_eggs_zone_2_mortality_rate': vector_D_eggs_zone_2_mortality_rate ,
            'vector_D_eggs_zone_3_mortality_rate': vector_D_eggs_zone_3_mortality_rate ,
            'vector_D_carrying_capacity_zone_1': vector_D_carrying_capacity_zone_1 ,
            'vector_D_carrying_capacity_zone_2': vector_D_carrying_capacity_zone_2 ,
            'vector_D_carrying_capacity_zone_3': vector_D_carrying_capacity_zone_3 ,
            'vector_D_migration_rate_1_to_2': vector_D_migration_rate_1_to_2,
            'vector_D_migration_rate_1_to_3': vector_D_migration_rate_1_to_3,
            'vector_D_migration_rate_2_to_1': vector_D_migration_rate_2_to_1,
            'vector_D_migration_rate_2_to_3': vector_D_migration_rate_2_to_3,
            'vector_D_migration_rate_3_to_1': vector_D_migration_rate_3_to_1,
            'vector_D_migration_rate_3_to_2': vector_D_migration_rate_3_to_2,
            'vector_D_infection_rate_to_human': vector_D_infection_rate_to_human,
            'vector_D_infection_rate_to_animal': vector_D_infection_rate_to_animal,
            'vector_D_max_biting_rate': vector_D_max_biting_rate,
            'vector_D_human_feeding_prop': vector_D_human_feeding_prop,
            'vector_D_animal_feeding_prop': vector_D_animal_feeding_prop,
        })

    for x in rvf_user_1_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'vector_D_oviposition_rate': context['vector_D_oviposition_rate'],
        'vector_D_hatching_rate': context['vector_D_hatching_rate'],
        'vector_D_mortality_rate_adults': context['vector_D_mortality_rate_adults'],
        'vector_D_eggs_zone_1_mortality_rate': context['vector_D_eggs_zone_1_mortality_rate'],
        'vector_D_eggs_zone_2_mortality_rate':context['vector_D_eggs_zone_2_mortality_rate'],
        'vector_D_eggs_zone_3_mortality_rate':context['vector_D_eggs_zone_3_mortality_rate'],
        'vector_D_carrying_capacity_zone_1':context['vector_D_carrying_capacity_zone_1'],
        'vector_D_carrying_capacity_zone_2':context['vector_D_carrying_capacity_zone_2'],
        'vector_D_carrying_capacity_zone_3':context['vector_D_carrying_capacity_zone_3'],
        'vector_D_migration_rate_1_to_2':context['vector_D_migration_rate_1_to_2'],
        'vector_D_migration_rate_1_to_3':context['vector_D_migration_rate_1_to_3'],
        'vector_D_migration_rate_2_to_1':context['vector_D_migration_rate_2_to_1'],
        'vector_D_migration_rate_2_to_3':context['vector_D_migration_rate_2_to_3'],
        'vector_D_migration_rate_3_to_1':context['vector_D_migration_rate_3_to_1'],
        'vector_D_migration_rate_3_to_2':context['vector_D_migration_rate_3_to_2'],
        'vector_D_infection_rate_to_human':context['vector_D_infection_rate_to_human'],
        'vector_D_infection_rate_to_animal':context['vector_D_infection_rate_to_animal'],
        'vector_D_max_biting_rate':context['vector_D_max_biting_rate'],
        'vector_D_human_feeding_prop':context['vector_D_human_feeding_prop'],
        'vector_D_animal_feeding_prop':context['vector_D_animal_feeding_prop'],
    }

    return render(request,'vector_D.html',context2)
def livestock_population(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['livestock_population']

    context = {
        # 'nairobi_exotic_cattle': 0,
        # 'nairobi_indigenous_cattle': 0,
        # 'nairobi_sheep': 0,
        # 'nairobi_goats': 0,
        # 'nairobi_camels': 0,
        # 'nairobi_donkeys': 0,
        # 'nyandarua_exotic_cattle': 0,
        # 'nyandarua_indigenous_cattle': 0,
        # 'nyandarua_sheep': 0,
        # 'nyandarua_goats': 0,
        # 'nyandarua_camels': 0,
        # 'nyandarua_donkeys': 0,
        # 'nyeri_exotic_cattle': 0,
        # 'nyeri_indigenous_cattle': 0,
        # 'nyeri_sheep': 0,
        # 'nyeri_goats': 0,
        # 'nyeri_camels': 0,
        # 'nyeri_donkeys': 0,
        # 'kirinyaga_exotic_cattle': 0,
        # 'kirinyaga_indigenous_cattle': 0,
        # 'kirinyaga_sheep': 0,
        # 'kirinyaga_goats': 0,
        # 'kirinyaga_camels': 0,
        # 'kirinyaga_donkeys': 0,
        # 'muranga_exotic_cattle': 0,
        # 'muranga_indigenous_cattle': 0,
        # 'muranga_sheep': 0,
        # 'muranga_goats': 0,
        # 'muranga_camels': 0,
        # 'muranga_donkeys': 0,
        # 'kiambu_exotic_cattle': 0,
        # 'kiambu_indigenous_cattle': 0,
        # 'kiambu_sheep': 0,
        # 'kiambu_goats': 0,
        # 'kiambu_camels': 0,
        # 'kiambu_donkeys': 0,
        # 'mombasa_exotic_cattle': 0,
        # 'mombasa_indigenous_cattle': 0,
        # 'mombasa_sheep': 0,
        # 'mombasa_goats': 0,
        # 'mombasa_camels': 0,
        # 'mombasa_donkeys': 0,
        # 'kwale_exotic_cattle': 0,
        # 'kwale_indigenous_cattle': 0,
        # 'kwale_sheep': 0,
        # 'kwale_goats': 0,
        # 'kwale_camels': 0,
        # 'kwale_donkeys': 0,
        # 'kilifi_exotic_cattle': 0,
        # 'kilifi_indigenous_cattle': 0,
        # 'kilifi_sheep': 0,
        # 'kilifi_goats': 0,
        # 'kilifi_camels': 0,
        # 'kilifi_donkeys': 0,
        # 'tanariver_exotic_cattle': 0,
        'tanariver_indigenous_cattle': 0,
        'tanariver_sheep': 0,
        'tanariver_goats': 0,
        'tanariver_camels': 0,
        # 'tanariver_donkeys': 0,
        # 'lamu_exotic_cattle': 0,
        # 'lamu_indigenous_cattle': 0,
        # 'lamu_sheep': 0,
        # 'lamu_goats': 0,
        # 'lamu_camels': 0,
        # 'lamu_donkeys': 0,
        # 'taitataveta_exotic_cattle': 0,
        # 'taitataveta_indigenous_cattle': 0,
        # 'taitataveta_sheep': 0,
        # 'taitataveta_goats': 0,
        # 'taitataveta_camels': 0,
        # 'taitataveta_donkeys': 0,
        # 'marsabit_exotic_cattle': 0,
        'marsabit_indigenous_cattle': 0,
        'marsabit_sheep': 0,
        'marsabit_goats': 0,
        'marsabit_camels': 0,
        # 'marsabit_donkeys': 0,
        # 'isiolo_exotic_cattle': 0,
        # 'isiolo_indigenous_cattle': 0,
        # 'isiolo_sheep': 0,
        # 'isiolo_goats': 0,
        # 'isiolo_camels': 0,
        # 'isiolo_donkeys': 0,
        # 'meru_exotic_cattle': 0,
        # 'meru_indigenous_cattle': 0,
        # 'meru_sheep': 0,
        # 'meru_goats': 0,
        # 'meru_camels': 0,
        # 'meru_donkeys': 0,
        # 'tharaka_exotic_cattle': 0,
        # 'tharaka_indigenous_cattle': 0,
        # 'tharaka_sheep': 0,
        # 'tharaka_goats': 0,
        # 'tharaka_camels': 0,
        # 'tharaka_donkeys': 0,
        # 'embu_exotic_cattle': 0,
        # 'embu_indigenous_cattle': 0,
        # 'embu_sheep': 0,
        # 'embu_goats': 0,
        # 'embu_camels': 0,
        # 'embu_donkeys': 0,
        # 'kitui_exotic_cattle': 0,
        # 'kitui_indigenous_cattle': 0,
        # 'kitui_sheep': 0,
        # 'kitui_goats': 0,
        # 'kitui_camels': 0,
        # 'kitui_donkeys': 0,
        # 'machakos_exotic_cattle': 0,
        # 'machakos_indigenous_cattle': 0,
        # 'machakos_sheep': 0,
        # 'machakos_goats': 0,
        # 'machakos_camels': 0,
        # 'machakos_donkeys': 0,
        # 'makueni_exotic_cattle': 0,
        # 'makueni_indigenous_cattle': 0,
        # 'makueni_sheep': 0,
        # 'makueni_goats': 0,
        # 'makueni_camels': 0,
        # 'makueni_donkeys': 0,
        # 'garissa_exotic_cattle': 0,
        'garissa_indigenous_cattle': 0,
        'garissa_sheep': 0,
        'garissa_goats': 0,
        'garissa_camels': 0,
        # 'garissa_donkeys': 0,
        # 'wajir_exotic_cattle': 0,
        'wajir_indigenous_cattle': 0,
        'wajir_sheep': 0,
        'wajir_goats': 0,
        'wajir_camels': 0,
        # 'wajir_donkeys': 0,
        # 'mandera_exotic_cattle': 0,
        # 'mandera_indigenous_cattle': 0,
        # 'mandera_sheep': 0,
        # 'mandera_goats': 0,
        # 'mandera_camels': 0,
        # 'mandera_donkeys': 0,
        # 'siaya_exotic_cattle': 0,
        # 'siaya_indigenous_cattle': 0,
        # 'siaya_sheep': 0,
        # 'siaya_goats': 0,
        # 'siaya_camels': 0,
        # 'siaya_donkeys': 0,
        # 'kisumu_exotic_cattle': 0,
        # 'kisumu_indigenous_cattle': 0,
        # 'kisumu_sheep': 0,
        # 'kisumu_goats': 0,
        # 'kisumu_camels': 0,
        # 'kisumu_donkeys': 0,
        # 'homabay_exotic_cattle': 0,
        # 'homabay_indigenous_cattle': 0,
        # 'homabay_sheep': 0,
        # 'homabay_goats': 0,
        # 'homabay_camels': 0,
        # 'homabay_donkeys': 0,
        # 'migori_exotic_cattle': 0,
        # 'migori_indigenous_cattle': 0,
        # 'migori_sheep': 0,
        # 'migori_goats': 0,
        # 'migori_camels': 0,
        # 'migori_donkeys': 0,
        # 'kisii_exotic_cattle': 0,
        # 'kisii_indigenous_cattle': 0,
        # 'kisii_sheep': 0,
        # 'kisii_goats': 0,
        # 'kisii_camels': 0,
        # 'kisii_donkeys': 0,
        # 'nyamira_exotic_cattle': 0,
        # 'nyamira_indigenous_cattle': 0,
        # 'nyamira_sheep': 0,
        # 'nyamira_goats': 0,
        # 'nyamira_camels': 0,
        # 'nyamira_donkeys': 0,
        # 'turkana_exotic_cattle': 0,
        # 'turkana_indigenous_cattle': 0,
        # 'turkana_sheep': 0,
        # 'turkana_goats': 0,
        # 'turkana_camels': 0,
        # 'turkana_donkeys': 0,
        # 'westpokot_exotic_cattle': 0,
        # 'westpokot_indigenous_cattle': 0,
        # 'westpokot_sheep': 0,
        # 'westpokot_goats': 0,
        # 'westpokot_camels': 0,
        # 'westpokot_donkeys': 0,
        # 'samburu_exotic_cattle': 0,
        # 'samburu_indigenous_cattle': 0,
        # 'samburu_sheep': 0,
        # 'samburu_goats': 0,
        # 'samburu_camels': 0,
        # 'samburu_donkeys': 0,
        # 'transnzoia_exotic_cattle': 0,
        # 'transnzoia_indigenous_cattle': 0,
        # 'transnzoia_sheep': 0,
        # 'transnzoia_goats': 0,
        # 'transnzoia_camels': 0,
        # 'transnzoia_donkeys': 0,
        # 'baringo_exotic_cattle': 0,
        'baringo_indigenous_cattle': 0,
        'baringo_sheep': 0,
        'baringo_goats': 0,
        'baringo_camels': 0,
        # 'baringo_donkeys': 0,
        # 'uasingishu_exotic_cattle': 0,
        # 'uasingishu_indigenous_cattle': 0,
        # 'uasingishu_sheep': 0,
        # 'uasingishu_goats': 0,
        # 'uasingishu_camels': 0,
        # 'uasingishu_donkeys': 0,
        # 'elgeyomarakwet_exotic_cattle': 0,
        # 'elgeyomarakwet_indigenous_cattle': 0,
        # 'elgeyomarakwet_sheep': 0,
        # 'elgeyomarakwet_goats': 0,
        # 'elgeyomarakwet_camels': 0,
        # 'elgeyomarakwet_donkeys': 0,
        # 'nandi_exotic_cattle': 0,
        # 'nandi_indigenous_cattle': 0,
        # 'nandi_sheep': 0,
        # 'nandi_goats': 0,
        # 'nandi_camels': 0,
        # 'nandi_donkeys': 0,
        # 'laikipia_exotic_cattle': 0,
        # 'laikipia_indigenous_cattle': 0,
        # 'laikipia_sheep': 0,
        # 'laikipia_goats': 0,
        # 'laikipia_camels': 0,
        # 'laikipia_donkeys': 0,
        # 'nakuru_exotic_cattle': 0,
        # 'nakuru_indigenous_cattle': 0,
        # 'nakuru_sheep': 0,
        # 'nakuru_goats': 0,
        # 'nakuru_camels': 0,
        # 'nakuru_donkeys': 0,
        # 'narok_exotic_cattle': 0,
        # 'narok_indigenous_cattle': 0,
        # 'narok_sheep': 0,
        # 'narok_goats': 0,
        # 'narok_camels': 0,
        # 'narok_donkeys': 0,
        # 'kajiado_exotic_cattle': 0,
        # 'kajiado_indigenous_cattle': 0,
        # 'kajiado_sheep': 0,
        # 'kajiado_goats': 0,
        # 'kajiado_camels': 0,
        # 'kajiado_donkeys': 0,
        # 'kericho_exotic_cattle': 0,
        # 'kericho_indigenous_cattle': 0,
        # 'kericho_sheep': 0,
        # 'kericho_goats': 0,
        # 'kericho_camels': 0,
        # 'kericho_donkeys': 0,
        # 'bomet_exotic_cattle': 0,
        # 'bomet_indigenous_cattle': 0,
        # 'bomet_sheep': 0,
        # 'bomet_goats': 0,
        # 'bomet_camels': 0,
        # 'bomet_donkeys': 0,
        # 'kakamega_exotic_cattle': 0,
        # 'kakamega_indigenous_cattle': 0,
        # 'kakamega_sheep': 0,
        # 'kakamega_goats': 0,
        # 'kakamega_camels': 0,
        # 'kakamega_donkeys': 0,
        # 'vihiga_exotic_cattle': 0,
        # 'vihiga_indigenous_cattle': 0,
        # 'vihiga_sheep': 0,
        # 'vihiga_goats': 0,
        # 'vihiga_camels': 0,
        # 'vihiga_donkeys': 0,
        # 'bungoma_exotic_cattle': 0,
        # 'bungoma_indigenous_cattle': 0,
        # 'bungoma_sheep': 0,
        # 'bungoma_goats': 0,
        # 'bungoma_camels': 0,
        # 'bungoma_donkeys': 0,
        # 'busia_exotic_cattle': 0,
        # 'busia_indigenous_cattle': 0,
        # 'busia_sheep': 0,
        # 'busia_goats': 0,
        # 'busia_camels': 0,
        # 'busia_donkeys': 0,
        # 'total_exotic_cattle': 0,
        'total_indigenous_cattle': 0,
        'total_sheep': 0,
        'total_goats': 0,
        'total_camels': 0,
        # 'total_donkeys': 0,
    }

    if (request.method == "POST"):
        # nairobi_exotic_cattle = request.POST['nairobi_exotic_cattle']
        # nairobi_indigenous_cattle = request.POST['nairobi_indigenous_cattle']
        # nairobi_sheep = request.POST['nairobi_sheep']
        # nairobi_goats = request.POST['nairobi_goats']
        # nairobi_camels = request.POST['nairobi_camels']
        # nairobi_donkeys = request.POST['nairobi_donkeys']
        # nyandarua_exotic_cattle = request.POST['nyandarua_exotic_cattle']
        # nyandarua_indigenous_cattle = request.POST['nyandarua_indigenous_cattle']
        # nyandarua_sheep = request.POST['nyandarua_sheep']
        # nyandarua_goats = request.POST['nyandarua_goats']
        # nyandarua_camels = request.POST['nyandarua_camels']
        # nyandarua_donkeys = request.POST['nyandarua_donkeys']
        # nyeri_exotic_cattle = request.POST['nyeri_exotic_cattle']
        # nyeri_indigenous_cattle = request.POST['nyeri_indigenous_cattle']
        # nyeri_sheep = request.POST['nyeri_sheep']
        # nyeri_goats = request.POST['nyeri_goats']
        # nyeri_camels = request.POST['nyeri_camels']
        # nyeri_donkeys = request.POST['nyeri_donkeys']
        # kirinyaga_exotic_cattle = request.POST['kirinyaga_exotic_cattle']
        # kirinyaga_indigenous_cattle = request.POST['kirinyaga_indigenous_cattle']
        # kirinyaga_sheep = request.POST['kirinyaga_sheep']
        # kirinyaga_goats = request.POST['kirinyaga_goats']
        # kirinyaga_camels = request.POST['kirinyaga_camels']
        # kirinyaga_donkeys = request.POST['kirinyaga_donkeys']
        # muranga_exotic_cattle = request.POST['muranga_exotic_cattle']
        # muranga_indigenous_cattle = request.POST['muranga_indigenous_cattle']
        # muranga_sheep = request.POST['muranga_sheep']
        # muranga_goats = request.POST['muranga_goats']
        # muranga_camels = request.POST['muranga_camels']
        # muranga_donkeys = request.POST['muranga_donkeys']
        # kiambu_exotic_cattle = request.POST['kiambu_exotic_cattle']
        # kiambu_indigenous_cattle = request.POST['kiambu_indigenous_cattle']
        # kiambu_sheep = request.POST['kiambu_sheep']
        # kiambu_goats = request.POST['kiambu_goats']
        # kiambu_camels = request.POST['kiambu_camels']
        # kiambu_donkeys = request.POST['kiambu_donkeys']
        # mombasa_exotic_cattle = request.POST['mombasa_exotic_cattle']
        # mombasa_indigenous_cattle = request.POST['mombasa_indigenous_cattle']
        # mombasa_sheep = request.POST['mombasa_sheep']
        # mombasa_goats = request.POST['mombasa_goats']
        # mombasa_camels = request.POST['mombasa_camels']
        # mombasa_donkeys = request.POST['mombasa_donkeys']
        # kwale_exotic_cattle = request.POST['kwale_exotic_cattle']
        # kwale_indigenous_cattle = request.POST['kwale_indigenous_cattle']
        # kwale_sheep = request.POST['kwale_sheep']
        # kwale_goats = request.POST['kwale_goats']
        # kwale_camels = request.POST['kwale_camels']
        # kwale_donkeys = request.POST['kwale_donkeys']
        # kilifi_exotic_cattle = request.POST['kilifi_exotic_cattle']
        # kilifi_indigenous_cattle = request.POST['kilifi_indigenous_cattle']
        # kilifi_sheep = request.POST['kilifi_sheep']
        # kilifi_goats = request.POST['kilifi_goats']
        # kilifi_camels = request.POST['kilifi_camels']
        # kilifi_donkeys = request.POST['kilifi_donkeys']
        # tanariver_exotic_cattle = request.POST['tanariver_exotic_cattle']
        tanariver_indigenous_cattle = request.POST['tanariver_indigenous_cattle']
        tanariver_sheep = request.POST['tanariver_sheep']
        tanariver_goats = request.POST['tanariver_goats']
        tanariver_camels = request.POST['tanariver_camels']
        # tanariver_donkeys = request.POST['tanariver_donkeys']
        # lamu_exotic_cattle = request.POST['lamu_exotic_cattle']
        # lamu_indigenous_cattle = request.POST['lamu_indigenous_cattle']
        # lamu_sheep = request.POST['lamu_sheep']
        # lamu_goats = request.POST['lamu_goats']
        # lamu_camels = request.POST['lamu_camels']
        # lamu_donkeys = request.POST['lamu_donkeys']
        # taitataveta_exotic_cattle = request.POST['taitataveta_exotic_cattle']
        # taitataveta_indigenous_cattle = request.POST['taitataveta_indigenous_cattle']
        # taitataveta_sheep = request.POST['taitataveta_sheep']
        # taitataveta_goats = request.POST['taitataveta_goats']
        # taitataveta_camels = request.POST['taitataveta_camels']
        # taitataveta_donkeys = request.POST['taitataveta_donkeys']
        # marsabit_exotic_cattle = request.POST['marsabit_exotic_cattle']
        marsabit_indigenous_cattle = request.POST['marsabit_indigenous_cattle']
        marsabit_sheep = request.POST['marsabit_sheep']
        marsabit_goats = request.POST['marsabit_goats']
        marsabit_camels = request.POST['marsabit_camels']
        # marsabit_donkeys = request.POST['marsabit_donkeys']
        # isiolo_exotic_cattle = request.POST['isiolo_exotic_cattle']
        # isiolo_indigenous_cattle = request.POST['isiolo_indigenous_cattle']
        # isiolo_sheep = request.POST['isiolo_sheep']
        # isiolo_goats = request.POST['isiolo_goats']
        # isiolo_camels = request.POST['isiolo_camels']
        # isiolo_donkeys = request.POST['isiolo_donkeys']
        # meru_exotic_cattle = request.POST['meru_exotic_cattle']
        # meru_indigenous_cattle = request.POST['meru_indigenous_cattle']
        # meru_sheep = request.POST['meru_sheep']
        # meru_goats = request.POST['meru_goats']
        # meru_camels = request.POST['meru_camels']
        # meru_donkeys = request.POST['meru_donkeys']
        # tharaka_exotic_cattle = request.POST['tharaka_exotic_cattle']
        # tharaka_indigenous_cattle = request.POST['tharaka_indigenous_cattle']
        # tharaka_sheep = request.POST['tharaka_sheep']
        # tharaka_goats = request.POST['tharaka_goats']
        # tharaka_camels = request.POST['tharaka_camels']
        # tharaka_donkeys = request.POST['tharaka_donkeys']
        # embu_exotic_cattle = request.POST['embu_exotic_cattle']
        # embu_indigenous_cattle = request.POST['embu_indigenous_cattle']
        # embu_sheep = request.POST['embu_sheep']
        # embu_goats = request.POST['embu_goats']
        # embu_camels = request.POST['embu_camels']
        # embu_donkeys = request.POST['embu_donkeys']
        # kitui_exotic_cattle = request.POST['kitui_exotic_cattle']
        # kitui_indigenous_cattle = request.POST['kitui_indigenous_cattle']
        # kitui_sheep = request.POST['kitui_sheep']
        # kitui_goats = request.POST['kitui_goats']
        # kitui_camels = request.POST['kitui_camels']
        # kitui_donkeys = request.POST['kitui_donkeys']
        # machakos_exotic_cattle = request.POST['machakos_exotic_cattle']
        # machakos_indigenous_cattle = request.POST['machakos_indigenous_cattle']
        # machakos_sheep = request.POST['machakos_sheep']
        # machakos_goats = request.POST['machakos_goats']
        # machakos_camels = request.POST['machakos_camels']
        # machakos_donkeys = request.POST['machakos_donkeys']
        # makueni_exotic_cattle = request.POST['makueni_exotic_cattle']
        # makueni_indigenous_cattle = request.POST['makueni_indigenous_cattle']
        # makueni_sheep = request.POST['makueni_sheep']
        # makueni_goats = request.POST['makueni_goats']
        # makueni_camels = request.POST['makueni_camels']
        # makueni_donkeys = request.POST['makueni_donkeys']
        # garissa_exotic_cattle = request.POST['garissa_exotic_cattle']
        garissa_indigenous_cattle = request.POST['garissa_indigenous_cattle']
        garissa_sheep = request.POST['garissa_sheep']
        garissa_goats = request.POST['garissa_goats']
        garissa_camels = request.POST['garissa_camels']
        # garissa_donkeys = request.POST['garissa_donkeys']
        # wajir_exotic_cattle = request.POST['wajir_exotic_cattle']
        wajir_indigenous_cattle = request.POST['wajir_indigenous_cattle']
        wajir_sheep = request.POST['wajir_sheep']
        wajir_goats = request.POST['wajir_goats']
        wajir_camels = request.POST['wajir_camels']
        # wajir_donkeys = request.POST['wajir_donkeys']
        # mandera_exotic_cattle = request.POST['mandera_exotic_cattle']
        # mandera_indigenous_cattle = request.POST['mandera_indigenous_cattle']
        # mandera_sheep = request.POST['mandera_sheep']
        # mandera_goats = request.POST['mandera_goats']
        # mandera_camels = request.POST['mandera_camels']
        # mandera_donkeys = request.POST['mandera_donkeys']
        # siaya_exotic_cattle = request.POST['siaya_exotic_cattle']
        # siaya_indigenous_cattle = request.POST['siaya_indigenous_cattle']
        # siaya_sheep = request.POST['siaya_sheep']
        # siaya_goats = request.POST['siaya_goats']
        # siaya_camels = request.POST['siaya_camels']
        # siaya_donkeys = request.POST['siaya_donkeys']
        # kisumu_exotic_cattle = request.POST['kisumu_exotic_cattle']
        # kisumu_indigenous_cattle = request.POST['kisumu_indigenous_cattle']
        # kisumu_sheep = request.POST['kisumu_sheep']
        # kisumu_goats = request.POST['kisumu_goats']
        # kisumu_camels = request.POST['kisumu_camels']
        # kisumu_donkeys = request.POST['kisumu_donkeys']
        # homabay_exotic_cattle = request.POST['homabay_exotic_cattle']
        # homabay_indigenous_cattle = request.POST['homabay_indigenous_cattle']
        # homabay_sheep = request.POST['homabay_sheep']
        # homabay_goats = request.POST['homabay_goats']
        # homabay_camels = request.POST['homabay_camels']
        # homabay_donkeys = request.POST['homabay_donkeys']
        # migori_exotic_cattle = request.POST['migori_exotic_cattle']
        # migori_indigenous_cattle = request.POST['migori_indigenous_cattle']
        # migori_sheep = request.POST['migori_sheep']
        # migori_goats = request.POST['migori_goats']
        # migori_camels = request.POST['migori_camels']
        # migori_donkeys = request.POST['migori_donkeys']
        # kisii_exotic_cattle = request.POST['kisii_exotic_cattle']
        # kisii_indigenous_cattle = request.POST['kisii_indigenous_cattle']
        # kisii_sheep = request.POST['kisii_sheep']
        # kisii_goats = request.POST['kisii_goats']
        # kisii_camels = request.POST['kisii_camels']
        # kisii_donkeys = request.POST['kisii_donkeys']
        # nyamira_exotic_cattle = request.POST['nyamira_exotic_cattle']
        # nyamira_indigenous_cattle = request.POST['nyamira_indigenous_cattle']
        # nyamira_sheep = request.POST['nyamira_sheep']
        # nyamira_goats = request.POST['nyamira_goats']
        # nyamira_camels = request.POST['nyamira_camels']
        # nyamira_donkeys = request.POST['nyamira_donkeys']
        # turkana_exotic_cattle = request.POST['turkana_exotic_cattle']
        # turkana_indigenous_cattle = request.POST['turkana_indigenous_cattle']
        # turkana_sheep = request.POST['turkana_sheep']
        # turkana_goats = request.POST['turkana_goats']
        # turkana_camels = request.POST['turkana_camels']
        # turkana_donkeys = request.POST['turkana_donkeys']
        # westpokot_exotic_cattle = request.POST['westpokot_exotic_cattle']
        # westpokot_indigenous_cattle = request.POST['westpokot_indigenous_cattle']
        # westpokot_sheep = request.POST['westpokot_sheep']
        # westpokot_goats = request.POST['westpokot_goats']
        # westpokot_camels = request.POST['westpokot_camels']
        # westpokot_donkeys = request.POST['westpokot_donkeys']
        # samburu_exotic_cattle = request.POST['samburu_exotic_cattle']
        # samburu_indigenous_cattle = request.POST['samburu_indigenous_cattle']
        # samburu_sheep = request.POST['samburu_sheep']
        # samburu_goats = request.POST['samburu_goats']
        # samburu_camels = request.POST['samburu_camels']
        # samburu_donkeys = request.POST['samburu_donkeys']
        # transnzoia_exotic_cattle = request.POST['transnzoia_exotic_cattle']
        # transnzoia_indigenous_cattle = request.POST['transnzoia_indigenous_cattle']
        # transnzoia_sheep = request.POST['transnzoia_sheep']
        # transnzoia_goats = request.POST['transnzoia_goats']
        # transnzoia_camels = request.POST['transnzoia_camels']
        # transnzoia_donkeys = request.POST['transnzoia_donkeys']
        # baringo_exotic_cattle = request.POST['baringo_exotic_cattle']
        baringo_indigenous_cattle = request.POST['baringo_indigenous_cattle']
        baringo_sheep = request.POST['baringo_sheep']
        baringo_goats = request.POST['baringo_goats']
        baringo_camels = request.POST['baringo_camels']
        # baringo_donkeys = request.POST['baringo_donkeys']
        # uasingishu_exotic_cattle = request.POST['uasingishu_exotic_cattle']
        # uasingishu_indigenous_cattle = request.POST['uasingishu_indigenous_cattle']
        # uasingishu_sheep = request.POST['uasingishu_sheep']
        # uasingishu_goats = request.POST['uasingishu_goats']
        # uasingishu_camels = request.POST['uasingishu_camels']
        # uasingishu_donkeys = request.POST['uasingishu_donkeys']
        # elgeyomarakwet_exotic_cattle = request.POST['elgeyomarakwet_exotic_cattle']
        # elgeyomarakwet_indigenous_cattle = request.POST['elgeyomarakwet_indigenous_cattle']
        # elgeyomarakwet_sheep = request.POST['elgeyomarakwet_sheep']
        # elgeyomarakwet_goats = request.POST['elgeyomarakwet_goats']
        # elgeyomarakwet_camels = request.POST['elgeyomarakwet_camels']
        # elgeyomarakwet_donkeys = request.POST['elgeyomarakwet_donkeys']
        # nandi_exotic_cattle = request.POST['nandi_exotic_cattle']
        # nandi_indigenous_cattle = request.POST['nandi_indigenous_cattle']
        # nandi_sheep = request.POST['nandi_sheep']
        # nandi_goats = request.POST['nandi_goats']
        # nandi_camels = request.POST['nandi_camels']
        # nandi_donkeys = request.POST['nandi_donkeys']
        # laikipia_exotic_cattle = request.POST['laikipia_exotic_cattle']
        # laikipia_indigenous_cattle = request.POST['laikipia_indigenous_cattle']
        # laikipia_sheep = request.POST['laikipia_sheep']
        # laikipia_goats = request.POST['laikipia_goats']
        # laikipia_camels = request.POST['laikipia_camels']
        # laikipia_donkeys = request.POST['laikipia_donkeys']
        # nakuru_exotic_cattle = request.POST['nakuru_exotic_cattle']
        # nakuru_indigenous_cattle = request.POST['nakuru_indigenous_cattle']
        # nakuru_sheep = request.POST['nakuru_sheep']
        # nakuru_goats = request.POST['nakuru_goats']
        # nakuru_camels = request.POST['nakuru_camels']
        # nakuru_donkeys = request.POST['nakuru_donkeys']
        # narok_exotic_cattle = request.POST['narok_exotic_cattle']
        # narok_indigenous_cattle = request.POST['narok_indigenous_cattle']
        # narok_sheep = request.POST['narok_sheep']
        # narok_goats = request.POST['narok_goats']
        # narok_camels = request.POST['narok_camels']
        # narok_donkeys = request.POST['narok_donkeys']
        # kajiado_exotic_cattle = request.POST['kajiado_exotic_cattle']
        # kajiado_indigenous_cattle = request.POST['kajiado_indigenous_cattle']
        # kajiado_sheep = request.POST['kajiado_sheep']
        # kajiado_goats = request.POST['kajiado_goats']
        # kajiado_camels = request.POST['kajiado_camels']
        # kajiado_donkeys = request.POST['kajiado_donkeys']
        # kericho_exotic_cattle = request.POST['kericho_exotic_cattle']
        # kericho_indigenous_cattle = request.POST['kericho_indigenous_cattle']
        # kericho_sheep = request.POST['kericho_sheep']
        # kericho_goats = request.POST['kericho_goats']
        # kericho_camels = request.POST['kericho_camels']
        # kericho_donkeys = request.POST['kericho_donkeys']
        # bomet_exotic_cattle = request.POST['bomet_exotic_cattle']
        # bomet_indigenous_cattle = request.POST['bomet_indigenous_cattle']
        # bomet_sheep = request.POST['bomet_sheep']
        # bomet_goats = request.POST['bomet_goats']
        # bomet_camels = request.POST['bomet_camels']
        # bomet_donkeys = request.POST['bomet_donkeys']
        # kakamega_exotic_cattle = request.POST['kakamega_exotic_cattle']
        # kakamega_indigenous_cattle = request.POST['kakamega_indigenous_cattle']
        # kakamega_sheep = request.POST['kakamega_sheep']
        # kakamega_goats = request.POST['kakamega_goats']
        # kakamega_camels = request.POST['kakamega_camels']
        # kakamega_donkeys = request.POST['kakamega_donkeys']
        # vihiga_exotic_cattle = request.POST['vihiga_exotic_cattle']
        # vihiga_indigenous_cattle = request.POST['vihiga_indigenous_cattle']
        # vihiga_sheep = request.POST['vihiga_sheep']
        # vihiga_goats = request.POST['vihiga_goats']
        # vihiga_camels = request.POST['vihiga_camels']
        # vihiga_donkeys = request.POST['vihiga_donkeys']
        # bungoma_exotic_cattle = request.POST['bungoma_exotic_cattle']
        # bungoma_indigenous_cattle = request.POST['bungoma_indigenous_cattle']
        # bungoma_sheep = request.POST['bungoma_sheep']
        # bungoma_goats = request.POST['bungoma_goats']
        # bungoma_camels = request.POST['bungoma_camels']
        # bungoma_donkeys = request.POST['bungoma_donkeys']
        # busia_exotic_cattle = request.POST['busia_exotic_cattle']
        # busia_indigenous_cattle = request.POST['busia_indigenous_cattle']
        # busia_sheep = request.POST['busia_sheep']
        # busia_goats = request.POST['busia_goats']
        # busia_camels = request.POST['busia_camels']
        # busia_donkeys = request.POST['busia_donkeys']
        #total_exotic_cattle = request.POST['total_exotic_cattle']
        total_indigenous_cattle = request.POST['total_indigenous_cattle']
        total_sheep = request.POST['total_sheep']
        total_goats = request.POST['total_goats']
        total_camels = request.POST['total_camels']
        #total_donkeys = request.POST['total_donkeys']

        x = rvf_initial_collection.insert_one({
            # 'nairobi_exotic_cattle': nairobi_exotic_cattle,
            # 'nairobi_indigenous_cattle': nairobi_indigenous_cattle,
            # 'nairobi_sheep': nairobi_sheep,
            # 'nairobi_goats': nairobi_goats,
            # 'nairobi_camels': nairobi_camels,
            # 'nairobi_donkeys': nairobi_donkeys,
            # 'nyandarua_exotic_cattle': nyandarua_exotic_cattle,
            # 'nyandarua_indigenous_cattle': nyandarua_indigenous_cattle,
            # 'nyandarua_sheep': nyandarua_sheep,
            # 'nyandarua_goats': nyandarua_goats,
            # 'nyandarua_camels': nyandarua_camels,
            # 'nyandarua_donkeys': nyandarua_donkeys,
            # 'nyeri_exotic_cattle': nyeri_exotic_cattle,
            # 'nyeri_indigenous_cattle': nyeri_indigenous_cattle,
            # 'nyeri_sheep': nyeri_sheep,
            # 'nyeri_goats': nyeri_goats,
            # 'nyeri_camels': nyeri_camels,
            # 'nyeri_donkeys': nyeri_donkeys,
            # 'kirinyaga_exotic_cattle': kirinyaga_exotic_cattle,
            # 'kirinyaga_indigenous_cattle': kirinyaga_indigenous_cattle,
            # 'kirinyaga_sheep': kirinyaga_sheep,
            # 'kirinyaga_goats': kirinyaga_goats,
            # 'kirinyaga_camels': kirinyaga_camels,
            # 'kirinyaga_donkeys': kirinyaga_donkeys,
            # 'muranga_exotic_cattle': muranga_exotic_cattle,
            # 'muranga_indigenous_cattle': muranga_indigenous_cattle,
            # 'muranga_sheep': muranga_sheep,
            # 'muranga_goats': muranga_goats,
            # 'muranga_camels': muranga_camels,
            # 'muranga_donkeys': muranga_donkeys,
            # 'kiambu_exotic_cattle': kiambu_exotic_cattle,
            # 'kiambu_indigenous_cattle': kiambu_indigenous_cattle,
            # 'kiambu_sheep': kiambu_sheep,
            # 'kiambu_goats': kiambu_goats,
            # 'kiambu_camels': kiambu_camels,
            # 'kiambu_donkeys': kiambu_donkeys,
            # 'mombasa_exotic_cattle': mombasa_exotic_cattle,
            # 'mombasa_indigenous_cattle': mombasa_indigenous_cattle,
            # 'mombasa_sheep': mombasa_sheep,
            # 'mombasa_goats': mombasa_goats,
            # 'mombasa_camels': mombasa_camels,
            # 'mombasa_donkeys': mombasa_donkeys,
            # 'kwale_exotic_cattle': kwale_exotic_cattle,
            # 'kwale_indigenous_cattle': kwale_indigenous_cattle,
            # 'kwale_sheep': kwale_sheep,
            # 'kwale_goats': kwale_goats,
            # 'kwale_camels': kwale_camels,
            # 'kwale_donkeys': kwale_donkeys,
            # 'kilifi_exotic_cattle': kilifi_exotic_cattle,
            # 'kilifi_indigenous_cattle': kilifi_indigenous_cattle,
            # 'kilifi_sheep': kilifi_sheep,
            # 'kilifi_goats': kilifi_goats,
            # 'kilifi_camels': kilifi_camels,
            # 'kilifi_donkeys': kilifi_donkeys,
            # 'tanariver_exotic_cattle': tanariver_exotic_cattle,
            'tanariver_indigenous_cattle': tanariver_indigenous_cattle,
            'tanariver_sheep': tanariver_sheep,
            'tanariver_goats': tanariver_goats,
            'tanariver_camels': tanariver_camels,
            # 'tanariver_donkeys': tanariver_donkeys,
            # 'lamu_exotic_cattle': lamu_exotic_cattle,
            # 'lamu_indigenous_cattle': lamu_indigenous_cattle,
            # 'lamu_sheep': lamu_sheep,
            # 'lamu_goats': lamu_goats,
            # 'lamu_camels': lamu_camels,
            # 'lamu_donkeys': lamu_donkeys,
            # 'taitataveta_exotic_cattle': taitataveta_exotic_cattle,
            # 'taitataveta_indigenous_cattle': taitataveta_indigenous_cattle,
            # 'taitataveta_sheep': taitataveta_sheep,
            # 'taitataveta_goats': taitataveta_goats,
            # 'taitataveta_camels': taitataveta_camels,
            # 'taitataveta_donkeys': taitataveta_donkeys,
            # 'marsabit_exotic_cattle': marsabit_exotic_cattle,
            'marsabit_indigenous_cattle': marsabit_indigenous_cattle,
            'marsabit_sheep': marsabit_sheep,
            'marsabit_goats': marsabit_goats,
            'marsabit_camels': marsabit_camels,
            # 'marsabit_donkeys': marsabit_donkeys,
            # 'isiolo_exotic_cattle': isiolo_exotic_cattle,
            # 'isiolo_indigenous_cattle': isiolo_indigenous_cattle,
            # 'isiolo_sheep': isiolo_sheep,
            # 'isiolo_goats': isiolo_goats,
            # 'isiolo_camels': isiolo_camels,
            # 'isiolo_donkeys': isiolo_donkeys,
            # 'meru_exotic_cattle': meru_exotic_cattle,
            # 'meru_indigenous_cattle': meru_indigenous_cattle,
            # 'meru_sheep': meru_sheep,
            # 'meru_goats': meru_goats,
            # 'meru_camels': meru_camels,
            # 'meru_donkeys': meru_donkeys,
            # 'tharaka_exotic_cattle': tharaka_exotic_cattle,
            # 'tharaka_indigenous_cattle': tharaka_indigenous_cattle,
            # 'tharaka_sheep': tharaka_sheep,
            # 'tharaka_goats': tharaka_goats,
            # 'tharaka_camels': tharaka_camels,
            # 'tharaka_donkeys': tharaka_donkeys,
            # 'embu_exotic_cattle': embu_exotic_cattle,
            # 'embu_indigenous_cattle': embu_indigenous_cattle,
            # 'embu_sheep': embu_sheep,
            # 'embu_goats': embu_goats,
            # 'embu_camels': embu_camels,
            # 'embu_donkeys': embu_donkeys,
            # 'kitui_exotic_cattle': kitui_exotic_cattle,
            # 'kitui_indigenous_cattle': kitui_indigenous_cattle,
            # 'kitui_sheep': kitui_sheep,
            # 'kitui_goats': kitui_goats,
            # 'kitui_camels': kitui_camels,
            # 'kitui_donkeys': kitui_donkeys,
            # 'machakos_exotic_cattle': machakos_exotic_cattle,
            # 'machakos_indigenous_cattle': machakos_indigenous_cattle,
            # 'machakos_sheep': machakos_sheep,
            # 'machakos_goats': machakos_goats,
            # 'machakos_camels': machakos_camels,
            # 'machakos_donkeys': machakos_donkeys,
            # 'makueni_exotic_cattle': makueni_exotic_cattle,
            # 'makueni_indigenous_cattle': makueni_indigenous_cattle,
            # 'makueni_sheep': makueni_sheep,
            # 'makueni_goats': makueni_goats,
            # 'makueni_camels': makueni_camels,
            # 'makueni_donkeys': makueni_donkeys,
            # 'garissa_exotic_cattle': garissa_exotic_cattle,
             'garissa_indigenous_cattle': garissa_indigenous_cattle,
             'garissa_sheep': garissa_sheep,
             'garissa_goats': garissa_goats,
             'garissa_camels': garissa_camels,
            #  'garissa_donkeys': garissa_donkeys,
            # 'wajir_exotic_cattle': wajir_exotic_cattle,
            'wajir_indigenous_cattle': wajir_indigenous_cattle,
            'wajir_sheep': wajir_sheep,
            'wajir_goats': wajir_goats,
            'wajir_camels': wajir_camels,
            # 'wajir_donkeys': wajir_donkeys,
            # 'mandera_exotic_cattle': mandera_exotic_cattle,
            # 'mandera_indigenous_cattle': mandera_indigenous_cattle,
            # 'mandera_sheep': mandera_sheep,
            # 'mandera_goats': mandera_goats,
            # 'mandera_camels': mandera_camels,
            # 'mandera_donkeys': mandera_donkeys,
            # 'siaya_exotic_cattle': siaya_exotic_cattle,
            # 'siaya_indigenous_cattle': siaya_indigenous_cattle,
            # 'siaya_sheep': siaya_sheep,
            # 'siaya_goats': siaya_goats,
            # 'siaya_camels': siaya_camels,
            # 'siaya_donkeys': siaya_donkeys,
            # 'kisumu_exotic_cattle': kisumu_exotic_cattle,
            # 'kisumu_indigenous_cattle': kisumu_indigenous_cattle,
            # 'kisumu_sheep': kisumu_sheep,
            # 'kisumu_goats': kisumu_goats,
            # 'kisumu_camels': kisumu_camels,
            # 'kisumu_donkeys': kisumu_donkeys,
            # 'homabay_exotic_cattle': homabay_exotic_cattle,
            # 'homabay_indigenous_cattle': homabay_indigenous_cattle,
            # 'homabay_sheep': homabay_sheep,
            # 'homabay_goats': homabay_goats,
            # 'homabay_camels': homabay_camels,
            # 'homabay_donkeys': homabay_donkeys,
            # 'migori_exotic_cattle': migori_exotic_cattle,
            # 'migori_indigenous_cattle': migori_indigenous_cattle,
            # 'migori_sheep': migori_sheep,
            # 'migori_goats': migori_goats,
            # 'migori_camels': migori_camels,
            # 'migori_donkeys': migori_donkeys,
            # 'kisii_exotic_cattle': kisii_exotic_cattle,
            # 'kisii_indigenous_cattle': kisii_indigenous_cattle,
            # 'kisii_sheep': kisii_sheep,
            # 'kisii_goats': kisii_goats,
            # 'kisii_camels': kisii_camels,
            # 'kisii_donkeys': kisii_donkeys,
            # 'nyamira_exotic_cattle': nyamira_exotic_cattle,
            # 'nyamira_indigenous_cattle': nyamira_indigenous_cattle,
            # 'nyamira_sheep': nyamira_sheep,
            # 'nyamira_goats': nyamira_goats,
            # 'nyamira_camels': nyamira_camels,
            # 'nyamira_donkeys': nyamira_donkeys,
            # 'turkana_exotic_cattle': turkana_exotic_cattle,
            # 'turkana_indigenous_cattle': turkana_indigenous_cattle,
            # 'turkana_sheep': turkana_sheep,
            # 'turkana_goats': turkana_goats,
            # 'turkana_camels': turkana_camels,
            # 'turkana_donkeys': turkana_donkeys,
            # 'westpokot_exotic_cattle': westpokot_exotic_cattle,
            # 'westpokot_indigenous_cattle': westpokot_indigenous_cattle,
            # 'westpokot_sheep': westpokot_sheep,
            # 'westpokot_goats': westpokot_goats,
            # 'westpokot_camels': westpokot_camels,
            # 'westpokot_donkeys': westpokot_donkeys,
            # 'samburu_exotic_cattle': samburu_exotic_cattle,
            # 'samburu_indigenous_cattle': samburu_indigenous_cattle,
            # 'samburu_sheep': samburu_sheep,
            # 'samburu_goats': samburu_goats,
            # 'samburu_camels': samburu_camels,
            # 'samburu_donkeys': samburu_donkeys,
            # 'transnzoia_exotic_cattle': transnzoia_exotic_cattle,
            # 'transnzoia_indigenous_cattle': transnzoia_indigenous_cattle,
            # 'transnzoia_sheep': transnzoia_sheep,
            # 'transnzoia_goats': transnzoia_goats,
            # 'transnzoia_camels': transnzoia_camels,
            # 'transnzoia_donkeys': transnzoia_donkeys,
            # 'baringo_exotic_cattle': baringo_exotic_cattle,
            'baringo_indigenous_cattle': baringo_indigenous_cattle,
            'baringo_sheep': baringo_sheep,
            'baringo_goats': baringo_goats,
            'baringo_camels': baringo_camels,
            # 'baringo_donkeys': baringo_donkeys,
            # 'uasingishu_exotic_cattle': uasingishu_exotic_cattle,
            # 'uasingishu_indigenous_cattle': uasingishu_indigenous_cattle,
            # 'uasingishu_sheep': uasingishu_sheep,
            # 'uasingishu_goats': uasingishu_goats,
            # 'uasingishu_camels': uasingishu_camels,
            # 'uasingishu_donkeys': uasingishu_donkeys,
            # 'elgeyomarakwet_exotic_cattle': elgeyomarakwet_exotic_cattle,
            # 'elgeyomarakwet_indigenous_cattle': elgeyomarakwet_indigenous_cattle,
            # 'elgeyomarakwet_sheep': elgeyomarakwet_sheep,
            # 'elgeyomarakwet_goats': elgeyomarakwet_goats,
            # 'elgeyomarakwet_camels': elgeyomarakwet_camels,
            # 'elgeyomarakwet_donkeys': elgeyomarakwet_donkeys,
            # 'nandi_exotic_cattle': nandi_exotic_cattle,
            # 'nandi_indigenous_cattle': nandi_indigenous_cattle,
            # 'nandi_sheep': nandi_sheep,
            # 'nandi_goats': nandi_goats,
            # 'nandi_camels': nandi_camels,
            # 'nandi_donkeys': nandi_donkeys,
            # 'laikipia_exotic_cattle': laikipia_exotic_cattle,
            # 'laikipia_indigenous_cattle': laikipia_indigenous_cattle,
            # 'laikipia_sheep': laikipia_sheep,
            # 'laikipia_goats': laikipia_goats,
            # 'laikipia_camels': laikipia_camels,
            # 'laikipia_donkeys': laikipia_donkeys,
            # 'nakuru_exotic_cattle': nakuru_exotic_cattle,
            # 'nakuru_indigenous_cattle': nakuru_indigenous_cattle,
            # 'nakuru_sheep': nakuru_sheep,
            # 'nakuru_goats': nakuru_goats,
            # 'nakuru_camels': nakuru_camels,
            # 'nakuru_donkeys': nakuru_donkeys,
            # 'narok_exotic_cattle': narok_exotic_cattle,
            # 'narok_indigenous_cattle': narok_indigenous_cattle,
            # 'narok_sheep': narok_sheep,
            # 'narok_goats': narok_goats,
            # 'narok_camels': narok_camels,
            # 'narok_donkeys': narok_donkeys,
            # 'kajiado_exotic_cattle': kajiado_exotic_cattle,
            # 'kajiado_indigenous_cattle': kajiado_indigenous_cattle,
            # 'kajiado_sheep': kajiado_sheep,
            # 'kajiado_goats': kajiado_goats,
            # 'kajiado_camels': kajiado_camels,
            # 'kajiado_donkeys': kajiado_donkeys,
            # 'kericho_exotic_cattle': kericho_exotic_cattle,
            # 'kericho_indigenous_cattle': kericho_indigenous_cattle,
            # 'kericho_sheep': kericho_sheep,
            # 'kericho_goats': kericho_goats,
            # 'kericho_camels': kericho_camels,
            # 'kericho_donkeys': kericho_donkeys,
            # 'bomet_exotic_cattle': bomet_exotic_cattle,
            # 'bomet_indigenous_cattle': bomet_indigenous_cattle,
            # 'bomet_sheep': bomet_sheep,
            # 'bomet_goats': bomet_goats,
            # 'bomet_camels': bomet_camels,
            # 'bomet_donkeys': bomet_donkeys,
            # 'kakamega_exotic_cattle': kakamega_exotic_cattle,
            # 'kakamega_indigenous_cattle': kakamega_indigenous_cattle,
            # 'kakamega_sheep': kakamega_sheep,
            # 'kakamega_goats': kakamega_goats,
            # 'kakamega_camels': kakamega_camels,
            # 'kakamega_donkeys': kakamega_donkeys,
            # 'vihiga_exotic_cattle': vihiga_exotic_cattle,
            # 'vihiga_indigenous_cattle': vihiga_indigenous_cattle,
            # 'vihiga_sheep': vihiga_sheep,
            # 'vihiga_goats': vihiga_goats,
            # 'vihiga_camels': vihiga_camels,
            # 'vihiga_donkeys': vihiga_donkeys,
            # 'bungoma_exotic_cattle': bungoma_exotic_cattle,
            # 'bungoma_indigenous_cattle': bungoma_indigenous_cattle,
            # 'bungoma_sheep': bungoma_sheep,
            # 'bungoma_goats': bungoma_goats,
            # 'bungoma_camels': bungoma_camels,
            # 'bungoma_donkeys': bungoma_donkeys,
            # 'busia_exotic_cattle': busia_exotic_cattle,
            # 'busia_indigenous_cattle': busia_indigenous_cattle,
            # 'busia_sheep': busia_sheep,
            # 'busia_goats': busia_goats,
            # 'busia_camels': busia_camels,
            # 'busia_donkeys': busia_donkeys,
            # 'total_exotic_cattle': int(nairobi_exotic_cattle)+
            #                         int(nyandarua_exotic_cattle)+
            #                         int(nyeri_exotic_cattle)+
            #                         int(kirinyaga_exotic_cattle)+
            #                         int(muranga_exotic_cattle)+
            #                         int(kiambu_exotic_cattle)+
            #                         int(mombasa_exotic_cattle)+
            #                         int(kwale_exotic_cattle)+
            #                         int(kilifi_exotic_cattle)+
            #                         int(tanariver_exotic_cattle)+
            #                         int(lamu_exotic_cattle)+
            #                         int(taitataveta_exotic_cattle)+
            #                         int(marsabit_exotic_cattle)+
            #                         int(isiolo_exotic_cattle)+
            #                         int(meru_exotic_cattle)+
            #                         int(tharaka_exotic_cattle)+
            #                         int(embu_exotic_cattle)+
            #                         int(kitui_exotic_cattle)+
            #                         int(machakos_exotic_cattle)+
            #                         int(makueni_exotic_cattle)+
            #                         int(garissa_exotic_cattle)+
            #                         int(wajir_exotic_cattle)+
            #                         int(mandera_exotic_cattle)+
            #                         int(siaya_exotic_cattle)+
            #                         int(kisumu_exotic_cattle)+
            #                         int(homabay_exotic_cattle)+
            #                         int(migori_exotic_cattle)+
            #                         int(kisii_exotic_cattle)+
            #                         int(nyamira_exotic_cattle)+
            #                         int(turkana_exotic_cattle)+
            #                         int(westpokot_exotic_cattle)+
            #                         int(samburu_exotic_cattle)+
            #                         int(transnzoia_exotic_cattle)+
            #                         int(baringo_exotic_cattle),
            'total_indigenous_cattle':
            #                               int(nairobi_indigenous_cattle)+
            #                             int(nyandarua_indigenous_cattle)+
            #                             int(nyeri_indigenous_cattle)+
            #                             int(kirinyaga_indigenous_cattle)+
            #                             int(muranga_indigenous_cattle)+
            #                             int(kiambu_indigenous_cattle)+
            #                             int(mombasa_indigenous_cattle)+
            #                             int(kwale_indigenous_cattle)+
            #                             int(kilifi_indigenous_cattle)+
                                        int(tanariver_indigenous_cattle)+
                                        # int(lamu_indigenous_cattle)+
                                        # int(taitataveta_indigenous_cattle)+
                                        int(marsabit_indigenous_cattle)+
                                        # int(isiolo_indigenous_cattle)+
                                        # int(meru_indigenous_cattle)+
                                        # int(tharaka_indigenous_cattle)+
                                        # int(embu_indigenous_cattle)+
                                        # int(kitui_indigenous_cattle)+
                                        # int(machakos_indigenous_cattle)+
                                        # int(makueni_indigenous_cattle)+
                                        int(garissa_indigenous_cattle)+
                                        int(wajir_indigenous_cattle)+
                                        # int(mandera_indigenous_cattle)+
                                        # int(siaya_indigenous_cattle)+
                                        # int(kisumu_indigenous_cattle)+
                                        # int(homabay_indigenous_cattle)+
                                        # int(migori_indigenous_cattle)+
                                        # int(kisii_indigenous_cattle)+
                                        # int(nyamira_indigenous_cattle)+
                                        # int(turkana_indigenous_cattle)+
                                        # int(westpokot_indigenous_cattle)+
                                        # int(samburu_indigenous_cattle)+
                                        # int(transnzoia_indigenous_cattle)+
                                         int(baringo_indigenous_cattle),
                                        # int(uasingishu_indigenous_cattle)+
                                        # int(elgeyomarakwet_indigenous_cattle)+
                                        # int(nandi_indigenous_cattle)+
                                        # int(laikipia_indigenous_cattle)+
                                        # int(nakuru_indigenous_cattle)+
                                        # int(narok_indigenous_cattle)+
                                        # int(kajiado_indigenous_cattle)+
                                        # int(kericho_indigenous_cattle)+
                                        # int(bomet_indigenous_cattle)+
                                        # int(kakamega_indigenous_cattle)+
                                        # int(vihiga_indigenous_cattle)+
                                        # int(bungoma_indigenous_cattle)+
                                        # int(busia_indigenous_cattle),
            'total_sheep':
                            # int(nairobi_sheep)+
                            # int(nyandarua_sheep)+
                            # int(nyeri_sheep)+
                            # int(kirinyaga_sheep)+
                            # int(muranga_sheep)+
                            # int(kiambu_sheep)+
                            # int(mombasa_sheep)+
                            # int(kwale_sheep)+
                            # int(kilifi_sheep)+
                            int(tanariver_sheep)+
                            # int(lamu_sheep)+
                            # int(taitataveta_sheep)+
                            int(marsabit_sheep)+
                            # int(isiolo_sheep)+
                            # int(meru_sheep)+
                            # int(tharaka_sheep)+
                            # int(embu_sheep)+
                            # int(kitui_sheep)+
                            # int(machakos_sheep)+
                            # int(makueni_sheep)+
                            int(garissa_sheep)+
                            int(wajir_sheep)+
                            # int(mandera_sheep)+
                            # int(siaya_sheep)+
                            # int(kisumu_sheep)+
                            # int(homabay_sheep)+
                            # int(migori_sheep)+
                            # int(kisii_sheep)+
                            # int(nyamira_sheep)+
                            # int(turkana_sheep)+
                            # int(westpokot_sheep)+
                            # int(samburu_sheep)+
                            # int(transnzoia_sheep)+
                            int(baringo_sheep),
                            # int(uasingishu_sheep)+
                            # int(elgeyomarakwet_sheep)+
                            # int(nandi_sheep)+
                            # int(laikipia_sheep)+
                            # int(nakuru_sheep)+
                            # int(narok_sheep)+
                            # int(kajiado_sheep)+
                            # int(kericho_sheep)+
                            # int(bomet_sheep)+
                            # int(kakamega_sheep)+
                            # int(vihiga_sheep)+
                            # int(bungoma_sheep)+
                            # int(busia_sheep),
            'total_goats':
                            # int(nairobi_goats)+
                            # int(nyandarua_goats)+
                            # int(nyeri_goats)+
                            # int(kirinyaga_goats)+
                            # int(muranga_goats)+
                            # int(kiambu_goats)+
                            # int(mombasa_goats)+
                            # int(kwale_goats)+
                            # int(kilifi_goats)+
                            int(tanariver_goats)+
                            # int(lamu_goats)+
                            # int(taitataveta_goats)+
                            int(marsabit_goats)+
                            # int(isiolo_goats)+
                            # int(meru_goats)+
                            # int(tharaka_goats)+
                            # int(embu_goats)+
                            # int(kitui_goats)+
                            # int(machakos_goats)+
                            # int(makueni_goats)+
                            int(garissa_goats)+
                            int(wajir_goats)+
                            # int(mandera_goats)+
                            # int(siaya_goats)+
                            # int(kisumu_goats)+
                            # int(homabay_goats)+
                            # int(migori_goats)+
                            # int(kisii_goats)+
                            # int(nyamira_goats)+
                            # int(turkana_goats)+
                            # int(westpokot_goats)+
                            # int(samburu_goats)+
                            # int(transnzoia_goats)+
                            int(baringo_goats),
                            # int(uasingishu_goats)+
                            # int(elgeyomarakwet_goats)+
                            # int(nandi_goats)+
                            # int(laikipia_goats)+
                            # int(nakuru_goats)+
                            # int(narok_goats)+
                            # int(kajiado_goats)+
                            # int(kericho_goats)+
                            # int(bomet_goats)+
                            # int(kakamega_goats)+
                            # int(vihiga_goats)+
                            # int(bungoma_goats)+
                            # int(busia_goats),
            'total_camels':
                            # int(nairobi_camels)+
                            # int(nyandarua_camels)+
                            # int(nyeri_camels)+
                            # int(kirinyaga_camels)+
                            # int(muranga_camels)+
                            # int(kiambu_camels)+
                            # int(mombasa_camels)+
                            # int(kwale_camels)+
                            # int(kilifi_camels)+
                            int(tanariver_camels)+
                            # int(lamu_camels)+
                            # int(taitataveta_camels)+
                            int(marsabit_camels)+
                            # int(isiolo_camels)+
                            # int(meru_camels)+
                            # int(tharaka_camels)+
                            # int(embu_camels)+
                            # int(kitui_camels)+
                            # int(machakos_camels)+
                            # int(makueni_camels)+
                            int(garissa_camels)+
                            int(wajir_camels)+
                            # int(mandera_camels)+
                            # int(siaya_camels)+
                            # int(kisumu_camels)+
                            # int(homabay_camels)+
                            # int(migori_camels)+
                            # int(kisii_camels)+
                            # int(nyamira_camels)+
                            # int(turkana_camels)+
                            # int(westpokot_camels)+
                            # int(samburu_camels)+
                            # int(transnzoia_camels)+
                            int(baringo_camels),
                            # int(uasingishu_camels)+
                            # int(elgeyomarakwet_camels)+
                            # int(nandi_camels)+
                            # int(laikipia_camels)+
                            # int(nakuru_camels)+
                            # int(narok_camels)+
                            # int(kajiado_camels)+
                            # int(kericho_camels)+
                            # int(bomet_camels)+
                            # int(kakamega_camels)+
                            # int(vihiga_camels)+
                            # int(bungoma_camels)+
                            # int(busia_camels),
            # 'total_donkeys': int(nairobi_donkeys)+
            #                 int(nyandarua_donkeys)+
            #                 int(nyeri_donkeys)+
            #                 int(kirinyaga_donkeys)+
            #                 int(muranga_donkeys)+
            #                 int(kiambu_donkeys)+
            #                 int(mombasa_donkeys)+
            #                 int(kwale_donkeys)+
            #                 int(kilifi_donkeys)+
            #                 int(tanariver_donkeys)+
            #                 int(lamu_donkeys)+
            #                 int(taitataveta_donkeys)+
            #                 int(marsabit_donkeys)+
            #                 int(isiolo_donkeys)+
            #                 int(meru_donkeys)+
            #                 int(tharaka_donkeys)+
            #                 int(embu_donkeys)+
            #                 int(kitui_donkeys)+
            #                 int(machakos_donkeys)+
            #                 int(makueni_donkeys)+
            #                 int(garissa_donkeys)+
            #                 int(wajir_donkeys)+
            #                 int(mandera_donkeys)+
            #                 int(siaya_donkeys)+
            #                 int(kisumu_donkeys)+
            #                 int(homabay_donkeys)+
            #                 int(migori_donkeys)+
            #                 int(kisii_donkeys)+
            #                 int(nyamira_donkeys)+
            #                 int(turkana_donkeys)+
            #                 int(westpokot_donkeys)+
            #                 int(samburu_donkeys)+
            #                 int(transnzoia_donkeys)+
            #                 int(baringo_donkeys)+
            #                 int(uasingishu_donkeys)+
            #                 int(elgeyomarakwet_donkeys)+
            #                 int(nandi_donkeys)+
            #                 int(laikipia_donkeys)+
            #                 int(nakuru_donkeys)+
            #                 int(narok_donkeys)+
            #                 int(kajiado_donkeys)+
            #                 int(kericho_donkeys)+
            #                 int(bomet_donkeys)+
            #                 int(kakamega_donkeys)+
            #                 int(vihiga_donkeys)+
            #                 int(bungoma_donkeys)+
            #                 int(busia_donkeys),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
         context = x

    context2 = {
        # 'nairobi_exotic_cattle': context['nairobi_exotic_cattle'],
        # 'nairobi_indigenous_cattle': context['nairobi_indigenous_cattle'],
        # 'nairobi_sheep': context['nairobi_sheep'],
        # 'nairobi_goats': context['nairobi_goats'],
        # 'nairobi_camels': context['nairobi_camels'],
        # 'nairobi_donkeys': context['nairobi_donkeys'],
        # 'nyandarua_exotic_cattle': context['nyandarua_exotic_cattle'],
        # 'nyandarua_indigenous_cattle': context['nyandarua_indigenous_cattle'],
        # 'nyandarua_sheep': context['nyandarua_sheep'],
        # 'nyandarua_goats': context['nyandarua_goats'],
        # 'nyandarua_camels': context['nyandarua_camels'],
        # 'nyandarua_donkeys': context['nyandarua_donkeys'],
        # 'nyeri_exotic_cattle': context['nyeri_exotic_cattle'],
        # 'nyeri_indigenous_cattle': context['nyeri_indigenous_cattle'],
        # 'nyeri_sheep': context['nyeri_sheep'],
        # 'nyeri_goats': context['nyeri_goats'],
        # 'nyeri_camels': context['nyeri_camels'],
        # 'nyeri_donkeys': context['nyeri_donkeys'],
        # 'kirinyaga_exotic_cattle': context['kirinyaga_exotic_cattle'],
        # 'kirinyaga_indigenous_cattle': context['kirinyaga_indigenous_cattle'],
        # 'kirinyaga_sheep': context['kirinyaga_sheep'],
        # 'kirinyaga_goats': context['kirinyaga_goats'],
        # 'kirinyaga_camels': context['kirinyaga_camels'],
        # 'kirinyaga_donkeys': context['kirinyaga_donkeys'],
        # 'muranga_exotic_cattle': context['muranga_exotic_cattle'],
        # 'muranga_indigenous_cattle': context['muranga_indigenous_cattle'],
        # 'muranga_sheep': context['muranga_sheep'],
        # 'muranga_goats': context['muranga_goats'],
        # 'muranga_camels': context['muranga_camels'],
        # 'muranga_donkeys': context['muranga_donkeys'],
        # 'kiambu_exotic_cattle': context['kiambu_exotic_cattle'],
        # 'kiambu_indigenous_cattle': context['kiambu_indigenous_cattle'],
        # 'kiambu_sheep': context['kiambu_sheep'],
        # 'kiambu_goats': context['kiambu_goats'],
        # 'kiambu_camels': context['kiambu_camels'],
        # 'kiambu_donkeys': context['kiambu_donkeys'],
        # 'mombasa_exotic_cattle': context['mombasa_exotic_cattle'],
        # 'mombasa_indigenous_cattle': context['mombasa_indigenous_cattle'],
        # 'mombasa_sheep': context['mombasa_sheep'],
        # 'mombasa_goats': context['mombasa_goats'],
        # 'mombasa_camels': context['mombasa_camels'],
        # 'mombasa_donkeys': context['mombasa_donkeys'],
        # 'kwale_exotic_cattle': context['kwale_exotic_cattle'],
        # 'kwale_indigenous_cattle': context['kwale_indigenous_cattle'],
        # 'kwale_sheep': context['kwale_sheep'],
        # 'kwale_goats': context['kwale_goats'],
        # 'kwale_camels': context['kwale_camels'],
        # 'kwale_donkeys': context['kwale_donkeys'],
        # 'kilifi_exotic_cattle': context['kilifi_exotic_cattle'],
        # 'kilifi_indigenous_cattle': context['kilifi_indigenous_cattle'],
        # 'kilifi_sheep': context['kilifi_sheep'],
        # 'kilifi_goats': context['kilifi_goats'],
        # 'kilifi_camels': context['kilifi_camels'],
        # 'kilifi_donkeys': context['kilifi_donkeys'],
        # 'tanariver_exotic_cattle': context['tanariver_exotic_cattle'],
        'tanariver_indigenous_cattle': context['tanariver_indigenous_cattle'],
        'tanariver_sheep': context['tanariver_sheep'],
        'tanariver_goats': context['tanariver_goats'],
        'tanariver_camels': context['tanariver_camels'],
        # 'tanariver_donkeys': context['tanariver_donkeys'],
        # 'lamu_exotic_cattle': context['lamu_exotic_cattle'],
        # 'lamu_indigenous_cattle': context['lamu_indigenous_cattle'],
        # 'lamu_sheep': context['lamu_sheep'],
        # 'lamu_goats': context['lamu_goats'],
        # 'lamu_camels': context['lamu_camels'],
        # 'lamu_donkeys': context['lamu_donkeys'],
        # 'taitataveta_exotic_cattle': context['taitataveta_exotic_cattle'],
        # 'taitataveta_indigenous_cattle': context['taitataveta_indigenous_cattle'],
        # 'taitataveta_sheep': context['taitataveta_sheep'],
        # 'taitataveta_goats': context['taitataveta_goats'],
        # 'taitataveta_camels': context['taitataveta_camels'],
        # 'taitataveta_donkeys': context['taitataveta_donkeys'],
        # 'marsabit_exotic_cattle': context['marsabit_exotic_cattle'],
        'marsabit_indigenous_cattle': context['marsabit_indigenous_cattle'],
        'marsabit_sheep': context['marsabit_sheep'],
        'marsabit_goats': context['marsabit_goats'],
        'marsabit_camels': context['marsabit_camels'],
        # 'marsabit_donkeys': context['marsabit_donkeys'],
        # 'isiolo_exotic_cattle': context['isiolo_exotic_cattle'],
        # 'isiolo_indigenous_cattle': context['isiolo_indigenous_cattle'],
        # 'isiolo_sheep': context['isiolo_sheep'],
        # 'isiolo_goats': context['isiolo_goats'],
        # 'isiolo_camels': context['isiolo_camels'],
        # 'isiolo_donkeys': context['isiolo_donkeys'],
        # 'meru_exotic_cattle': context['meru_exotic_cattle'],
        # 'meru_indigenous_cattle': context['meru_indigenous_cattle'],
        # 'meru_sheep': context['meru_sheep'],
        # 'meru_goats': context['meru_goats'],
        # 'meru_camels': context['meru_camels'],
        # 'meru_donkeys': context['meru_donkeys'],
        # 'tharaka_exotic_cattle': context['tharaka_exotic_cattle'],
        # 'tharaka_indigenous_cattle': context['tharaka_indigenous_cattle'],
        # 'tharaka_sheep': context['tharaka_sheep'],
        # 'tharaka_goats': context['tharaka_goats'],
        # 'tharaka_camels': context['tharaka_camels'],
        # 'tharaka_donkeys': context['tharaka_donkeys'],
        # 'embu_exotic_cattle': context['embu_exotic_cattle'],
        # 'embu_indigenous_cattle': context['embu_indigenous_cattle'],
        # 'embu_sheep': context['embu_sheep'],
        # 'embu_goats': context['embu_goats'],
        # 'embu_camels': context['embu_camels'],
        # 'embu_donkeys': context['embu_donkeys'],
        # 'kitui_exotic_cattle': context['kitui_exotic_cattle'],
        # 'kitui_indigenous_cattle': context['kitui_indigenous_cattle'],
        # 'kitui_sheep': context['kitui_sheep'],
        # 'kitui_goats': context['kitui_goats'],
        # 'kitui_camels': context['kitui_camels'],
        # 'kitui_donkeys': context['kitui_donkeys'],
        # 'machakos_exotic_cattle': context['machakos_exotic_cattle'],
        # 'machakos_indigenous_cattle': context['machakos_indigenous_cattle'],
        # 'machakos_sheep': context['machakos_sheep'],
        # 'machakos_goats': context['machakos_goats'],
        # 'machakos_camels': context['machakos_camels'],
        # 'machakos_donkeys': context['machakos_donkeys'],
        # 'makueni_exotic_cattle': context['makueni_exotic_cattle'],
        # 'makueni_indigenous_cattle': context['makueni_indigenous_cattle'],
        # 'makueni_sheep': context['makueni_sheep'],
        # 'makueni_goats': context['makueni_goats'],
        # 'makueni_camels': context['makueni_camels'],
        # 'makueni_donkeys': context['makueni_donkeys'],
        # 'garissa_exotic_cattle': context['garissa_exotic_cattle'],
         'garissa_indigenous_cattle': context['garissa_indigenous_cattle'],
         'garissa_sheep': context['garissa_sheep'],
         'garissa_goats': context['garissa_goats'],
         'garissa_camels': context['garissa_camels'],
        # 'garissa_donkeys': context['garissa_donkeys'],
        # 'wajir_exotic_cattle': context['wajir_exotic_cattle'],
        'wajir_indigenous_cattle': context['wajir_indigenous_cattle'],
        'wajir_sheep': context['wajir_sheep'],
        'wajir_goats': context['wajir_goats'],
        'wajir_camels': context['wajir_camels'],
        # 'wajir_donkeys': context['wajir_donkeys'],
        # 'mandera_exotic_cattle': context['mandera_exotic_cattle'],
        # 'mandera_indigenous_cattle': context['mandera_indigenous_cattle'],
        # 'mandera_sheep': context['mandera_sheep'],
        # 'mandera_goats': context['mandera_goats'],
        # 'mandera_camels': context['mandera_camels'],
        # 'mandera_donkeys': context['mandera_donkeys'],
        # 'siaya_exotic_cattle': context['siaya_exotic_cattle'],
        # 'siaya_indigenous_cattle': context['siaya_indigenous_cattle'],
        # 'siaya_sheep': context['siaya_sheep'],
        # 'siaya_goats': context['siaya_goats'],
        # 'siaya_camels': context['siaya_camels'],
        # 'siaya_donkeys': context['siaya_donkeys'],
        # 'kisumu_exotic_cattle': context['kisumu_exotic_cattle'],
        # 'kisumu_indigenous_cattle': context['kisumu_indigenous_cattle'],
        # 'kisumu_sheep': context['kisumu_sheep'],
        # 'kisumu_goats': context['kisumu_goats'],
        # 'kisumu_camels': context['kisumu_camels'],
        # 'kisumu_donkeys': context['kisumu_donkeys'],
        # 'homabay_exotic_cattle': context['homabay_exotic_cattle'],
        # 'homabay_indigenous_cattle': context['homabay_indigenous_cattle'],
        # 'homabay_sheep': context['homabay_sheep'],
        # 'homabay_goats': context['homabay_goats'],
        # 'homabay_camels': context['homabay_camels'],
        # 'homabay_donkeys': context['homabay_donkeys'],
        # 'migori_exotic_cattle': context['migori_exotic_cattle'],
        # 'migori_indigenous_cattle': context['migori_indigenous_cattle'],
        # 'migori_sheep': context['migori_sheep'],
        # 'migori_goats': context['migori_goats'],
        # 'migori_camels': context['migori_camels'],
        # 'migori_donkeys': context['migori_donkeys'],
        # 'kisii_exotic_cattle': context['kisii_exotic_cattle'],
        # 'kisii_indigenous_cattle': context['kisii_indigenous_cattle'],
        # 'kisii_sheep': context['kisii_sheep'],
        # 'kisii_goats': context['kisii_goats'],
        # 'kisii_camels': context['kisii_camels'],
        # 'kisii_donkeys': context['kisii_donkeys'],
        # 'nyamira_exotic_cattle': context['nyamira_exotic_cattle'],
        # 'nyamira_indigenous_cattle': context['nyamira_indigenous_cattle'],
        # 'nyamira_sheep': context['nyamira_sheep'],
        # 'nyamira_goats': context['nyamira_goats'],
        # 'nyamira_camels': context['nyamira_camels'],
        # 'nyamira_donkeys': context['nyamira_donkeys'],
        # 'turkana_exotic_cattle': context['turkana_exotic_cattle'],
        # 'turkana_indigenous_cattle': context['turkana_indigenous_cattle'],
        # 'turkana_sheep': context['turkana_sheep'],
        # 'turkana_goats': context['turkana_goats'],
        # 'turkana_camels': context['turkana_camels'],
        # 'turkana_donkeys': context['turkana_donkeys'],
        # 'westpokot_exotic_cattle': context['westpokot_exotic_cattle'],
        # 'westpokot_indigenous_cattle': context['westpokot_indigenous_cattle'],
        # 'westpokot_sheep': context['westpokot_sheep'],
        # 'westpokot_goats': context['westpokot_goats'],
        # 'westpokot_camels': context['westpokot_camels'],
        # 'westpokot_donkeys': context['westpokot_donkeys'],
        # 'samburu_exotic_cattle': context['samburu_exotic_cattle'],
        # 'samburu_indigenous_cattle': context['samburu_indigenous_cattle'],
        # 'samburu_sheep': context['samburu_sheep'],
        # 'samburu_goats': context['samburu_goats'],
        # 'samburu_camels': context['samburu_camels'],
        # 'samburu_donkeys': context['samburu_donkeys'],
        # 'transnzoia_exotic_cattle': context['transnzoia_exotic_cattle'],
        # 'transnzoia_indigenous_cattle': context['transnzoia_indigenous_cattle'],
        # 'transnzoia_sheep': context['transnzoia_sheep'],
        # 'transnzoia_goats': context['transnzoia_goats'],
        # 'transnzoia_camels': context['transnzoia_camels'],
        # 'transnzoia_donkeys': context['transnzoia_donkeys'],
        # 'baringo_exotic_cattle': context['baringo_exotic_cattle'],
        'baringo_indigenous_cattle': context['baringo_indigenous_cattle'],
        'baringo_sheep': context['baringo_sheep'],
        'baringo_goats': context['baringo_goats'],
        'baringo_camels': context['baringo_camels'],
        # 'baringo_donkeys': context['baringo_donkeys'],
        # 'uasingishu_exotic_cattle': context['uasingishu_exotic_cattle'],
        # 'uasingishu_indigenous_cattle': context['uasingishu_indigenous_cattle'],
        # 'uasingishu_sheep': context['uasingishu_sheep'],
        # 'uasingishu_goats': context['uasingishu_goats'],
        # 'uasingishu_camels': context['uasingishu_camels'],
        # 'uasingishu_donkeys': context['uasingishu_donkeys'],
        # 'elgeyomarakwet_exotic_cattle': context['elgeyomarakwet_exotic_cattle'],
        # 'elgeyomarakwet_indigenous_cattle': context['elgeyomarakwet_indigenous_cattle'],
        # 'elgeyomarakwet_sheep': context['elgeyomarakwet_sheep'],
        # 'elgeyomarakwet_goats': context['elgeyomarakwet_goats'],
        # 'elgeyomarakwet_camels': context['elgeyomarakwet_camels'],
        # 'elgeyomarakwet_donkeys': context['elgeyomarakwet_donkeys'],
        # 'nandi_exotic_cattle': context['nandi_exotic_cattle'],
        # 'nandi_indigenous_cattle': context['nandi_indigenous_cattle'],
        # 'nandi_sheep': context['nandi_sheep'],
        # 'nandi_goats': context['nandi_goats'],
        # 'nandi_camels': context['nandi_camels'],
        # 'nandi_donkeys': context['nandi_donkeys'],
        # 'laikipia_exotic_cattle': context['laikipia_exotic_cattle'],
        # 'laikipia_indigenous_cattle': context['laikipia_indigenous_cattle'],
        # 'laikipia_sheep': context['laikipia_sheep'],
        # 'laikipia_goats': context['laikipia_goats'],
        # 'laikipia_camels': context['laikipia_camels'],
        # 'laikipia_donkeys': context['laikipia_donkeys'],
        # 'nakuru_exotic_cattle': context['nakuru_exotic_cattle'],
        # 'nakuru_indigenous_cattle': context['nakuru_indigenous_cattle'],
        # 'nakuru_sheep': context['nakuru_sheep'],
        # 'nakuru_goats': context['nakuru_goats'],
        # 'nakuru_camels': context['nakuru_camels'],
        # 'nakuru_donkeys': context['nakuru_donkeys'],
        # 'narok_exotic_cattle': context['narok_exotic_cattle'],
        # 'narok_indigenous_cattle': context['narok_indigenous_cattle'],
        # 'narok_sheep': context['narok_sheep'],
        # 'narok_goats': context['narok_goats'],
        # 'narok_camels': context['narok_camels'],
        # 'narok_donkeys': context['narok_donkeys'],
        # 'kajiado_exotic_cattle': context['kajiado_exotic_cattle'],
        # 'kajiado_indigenous_cattle': context['kajiado_indigenous_cattle'],
        # 'kajiado_sheep': context['kajiado_sheep'],
        # 'kajiado_goats': context['kajiado_goats'],
        # 'kajiado_camels': context['kajiado_camels'],
        # 'kajiado_donkeys': context['kajiado_donkeys'],
        # 'kericho_exotic_cattle': context['kericho_exotic_cattle'],
        # 'kericho_indigenous_cattle': context['kericho_indigenous_cattle'],
        # 'kericho_sheep': context['kericho_sheep'],
        # 'kericho_goats': context['kericho_goats'],
        # 'kericho_camels': context['kericho_camels'],
        # 'kericho_donkeys': context['kericho_donkeys'],
        # 'bomet_exotic_cattle': context['bomet_exotic_cattle'],
        # 'bomet_indigenous_cattle': context['bomet_indigenous_cattle'],
        # 'bomet_sheep': context['bomet_sheep'],
        # 'bomet_goats': context['bomet_goats'],
        # 'bomet_camels': context['bomet_camels'],
        # 'bomet_donkeys': context['bomet_donkeys'],
        # 'kakamega_exotic_cattle': context['kakamega_exotic_cattle'],
        # 'kakamega_indigenous_cattle': context['kakamega_indigenous_cattle'],
        # 'kakamega_sheep': context['kakamega_sheep'],
        # 'kakamega_goats': context['kakamega_goats'],
        # 'kakamega_camels': context['kakamega_camels'],
        # 'kakamega_donkeys': context['kakamega_donkeys'],
        # 'vihiga_exotic_cattle': context['vihiga_exotic_cattle'],
        # 'vihiga_indigenous_cattle': context['vihiga_indigenous_cattle'],
        # 'vihiga_sheep': context['vihiga_sheep'],
        # 'vihiga_goats': context['vihiga_goats'],
        # 'vihiga_camels': context['vihiga_camels'],
        # 'vihiga_donkeys': context['vihiga_donkeys'],
        # 'bungoma_exotic_cattle': context['bungoma_exotic_cattle'],
        # 'bungoma_indigenous_cattle': context['bungoma_indigenous_cattle'],
        # 'bungoma_sheep': context['bungoma_sheep'],
        # 'bungoma_goats': context['bungoma_goats'],
        # 'bungoma_camels': context['bungoma_camels'],
        # 'bungoma_donkeys': context['bungoma_donkeys'],
        # 'busia_exotic_cattle': context['busia_exotic_cattle'],
        # 'busia_indigenous_cattle': context['busia_indigenous_cattle'],
        # 'busia_sheep': context['busia_sheep'],
        # 'busia_goats': context['busia_goats'],
        # 'busia_camels': context['busia_camels'],
        # 'busia_donkeys': context['busia_donkeys'],
        # 'total_exotic_cattle': int(context['nairobi_exotic_cattle'])+
        #                         int(context['nyandarua_exotic_cattle'])+
        #                         int(context['nyeri_exotic_cattle'])+
        #                         int(context['kirinyaga_exotic_cattle'])+
        #                         int(context['muranga_exotic_cattle'])+
        #                         int(context['kiambu_exotic_cattle'])+
        #                         int(context['mombasa_exotic_cattle'])+
        #                         int(context['kwale_exotic_cattle'])+
        #                         int(context['kilifi_exotic_cattle'])+
        #                         int(context['tanariver_exotic_cattle'])+
        #                         int(context['lamu_exotic_cattle'])+
        #                         int(context['taitataveta_exotic_cattle'])+
        #                         int(context['marsabit_exotic_cattle'])+
        #                         int(context['isiolo_exotic_cattle'])+
        #                         int(context['meru_exotic_cattle'])+
        #                         int(context['tharaka_exotic_cattle'])+
        #                         int(context['embu_exotic_cattle'])+
        #                         int(context['kitui_exotic_cattle'])+
        #                         int(context['machakos_exotic_cattle'])+
        #                         int(context['makueni_exotic_cattle'])+
        #                         int(context['garissa_exotic_cattle'])+
        #                         int(context['wajir_exotic_cattle'])+
        #                         int(context['mandera_exotic_cattle'])+
        #                         int(context['siaya_exotic_cattle'])+
        #                         int(context['kisumu_exotic_cattle'])+
        #                         int(context['homabay_exotic_cattle'])+
        #                         int(context['migori_exotic_cattle'])+
        #                         int(context['kisii_exotic_cattle'])+
        #                         int(context['nyamira_exotic_cattle'])+
        #                         int(context['turkana_exotic_cattle'])+
        #                         int(context['westpokot_exotic_cattle'])+
        #                         int(context['samburu_exotic_cattle'])+
        #                         int(context['transnzoia_exotic_cattle'])+
        #                         int(context['baringo_exotic_cattle'])+
        #                         int(context['uasingishu_exotic_cattle'])+
        #                         int(context['elgeyomarakwet_exotic_cattle'])+
        #                         int(context['nandi_exotic_cattle'])+
        #                         int(context['laikipia_exotic_cattle'])+
        #                         int(context['nakuru_exotic_cattle'])+
        #                         int(context['narok_exotic_cattle'])+
        #                         int(context['kajiado_exotic_cattle'])+
        #                         int(context['kericho_exotic_cattle'])+
        #                         int(context['bomet_exotic_cattle'])+
        #                         int(context['kakamega_exotic_cattle'])+
        #                         int(context['vihiga_exotic_cattle'])+
        #                         int(context['bungoma_exotic_cattle'])+
        #                         int(context['busia_exotic_cattle']),
        'total_indigenous_cattle':
                                    # int(context['nairobi_indigenous_cattle'])+
                                    # int(context['nyandarua_indigenous_cattle'])+
                                    # int(context['nyeri_indigenous_cattle'])+
                                    # int(context['kirinyaga_indigenous_cattle'])+
                                    # int(context['muranga_indigenous_cattle'])+
                                    # int(context['kiambu_indigenous_cattle'])+
                                    # int(context['mombasa_indigenous_cattle'])+
                                    # int(context['kwale_indigenous_cattle'])+
                                    # int(context['kilifi_indigenous_cattle'])+
                                    int(context['tanariver_indigenous_cattle'])+
                                    # int(context['lamu_indigenous_cattle'])+
                                    # int(context['taitataveta_indigenous_cattle'])+
                                    int(context['marsabit_indigenous_cattle'])+
                                    # int(context['isiolo_indigenous_cattle'])+
                                    # int(context['meru_indigenous_cattle'])+
                                    # int(context['tharaka_indigenous_cattle'])+
                                    # int(context['embu_indigenous_cattle'])+
                                    # int(context['kitui_indigenous_cattle'])+
                                    # int(context['machakos_indigenous_cattle'])+
                                    # int(context['makueni_indigenous_cattle'])+
                                    int(context['garissa_indigenous_cattle'])+
                                    int(context['wajir_indigenous_cattle'])+
                                    # int(context['mandera_indigenous_cattle'])+
                                    # int(context['siaya_indigenous_cattle'])+
                                    # int(context['kisumu_indigenous_cattle'])+
                                    # int(context['homabay_indigenous_cattle'])+
                                    # int(context['migori_indigenous_cattle'])+
                                    # int(context['kisii_indigenous_cattle'])+
                                    # int(context['nyamira_indigenous_cattle'])+
                                    # int(context['turkana_indigenous_cattle'])+
                                    # int(context['westpokot_indigenous_cattle'])+
                                    # int(context['samburu_indigenous_cattle'])+
                                    # int(context['transnzoia_indigenous_cattle'])+
                                    int(context['baringo_indigenous_cattle']),
                                    # int(context['uasingishu_indigenous_cattle'])+
                                    # int(context['elgeyomarakwet_indigenous_cattle'])+
                                    # int(context['nandi_indigenous_cattle'])+
                                    # int(context['laikipia_indigenous_cattle'])+
                                    # int(context['nakuru_indigenous_cattle'])+
                                    # int(context['narok_indigenous_cattle'])+
                                    # int(context['kajiado_indigenous_cattle'])+
                                    # int(context['kericho_indigenous_cattle'])+
                                    # int(context['bomet_indigenous_cattle'])+
                                    # int(context['kakamega_indigenous_cattle'])+
                                    # int(context['vihiga_indigenous_cattle'])+
                                    # int(context['bungoma_indigenous_cattle'])+
                                    # int(context['busia_indigenous_cattle']),
        'total_sheep':
                                        # int(context['nairobi_sheep'])+
                                    # int(context['nyandarua_sheep'])+
                                    # int(context['nyeri_sheep'])+
                                    # int(context['kirinyaga_sheep'])+
                                    # int(context['muranga_sheep'])+
                                    # int(context['kiambu_sheep'])+
                                    # int(context['mombasa_sheep'])+
                                    # int(context['kwale_sheep'])+
                                    # int(context['kilifi_sheep'])+
                                    int(context['tanariver_sheep'])+
                                    # int(context['lamu_sheep'])+
                                    # int(context['taitataveta_sheep'])+
                                    int(context['marsabit_sheep'])+
                                    # int(context['isiolo_sheep'])+
                                    # int(context['meru_sheep'])+
                                    # int(context['tharaka_sheep'])+
                                    # int(context['embu_sheep'])+
                                    # int(context['kitui_sheep'])+
                                    # int(context['machakos_sheep'])+
                                    # int(context['makueni_sheep'])+
                                    int(context['garissa_sheep'])+
                                    int(context['wajir_sheep'])+
                                    # int(context['mandera_sheep'])+
                                    # int(context['siaya_sheep'])+
                                    # int(context['kisumu_sheep'])+
                                    # int(context['homabay_sheep'])+
                                    # int(context['migori_sheep'])+
                                    # int(context['kisii_sheep'])+
                                    # int(context['nyamira_sheep'])+
                                    # int(context['turkana_sheep'])+
                                    # int(context['westpokot_sheep'])+
                                    # int(context['samburu_sheep'])+
                                    # int(context['transnzoia_sheep'])+
                                    int(context['baringo_sheep']),
                                    # int(context['uasingishu_sheep'])+
                                    # int(context['elgeyomarakwet_sheep'])+
                                    # int(context['nandi_sheep'])+
                                    # int(context['laikipia_sheep'])+
                                    # int(context['nakuru_sheep'])+
                                    # int(context['narok_sheep'])+
                                    # int(context['kajiado_sheep'])+
                                    # int(context['kericho_sheep'])+
                                    # int(context['bomet_sheep'])+
                                    # int(context['kakamega_sheep'])+
                                    # int(context['vihiga_sheep'])+
                                    # int(context['bungoma_sheep'])+
                                    # int(context['busia_sheep']),
        'total_goats':
                                    # int(context['nairobi_goats'])+
                                    # int(context['nyandarua_goats'])+
                                    # int(context['nyeri_goats'])+
                                    # int(context['kirinyaga_goats'])+
                                    # int(context['muranga_goats'])+
                                    # int(context['kiambu_goats'])+
                                    # int(context['mombasa_goats'])+
                                    # int(context['kwale_goats'])+
                                    # int(context['kilifi_goats'])+
                                    int(context['tanariver_goats'])+
                                    # int(context['lamu_goats'])+
                                    # int(context['taitataveta_goats'])+
                                    int(context['marsabit_goats'])+
                                    # int(context['isiolo_goats'])+
                                    # int(context['meru_goats'])+
                                    # int(context['tharaka_goats'])+
                                    # int(context['embu_goats'])+
                                    # int(context['kitui_goats'])+
                                    # int(context['machakos_goats'])+
                                    # int(context['makueni_goats'])+
                                    int(context['garissa_goats'])+
                                    int(context['wajir_goats'])+
                                    # int(context['mandera_goats'])+
                                    # int(context['siaya_goats'])+
                                    # int(context['kisumu_goats'])+
                                    # int(context['homabay_goats'])+
                                    # int(context['migori_goats'])+
                                    # int(context['kisii_goats'])+
                                    # int(context['nyamira_goats'])+
                                    # int(context['turkana_goats'])+
                                    # int(context['westpokot_goats'])+
                                    # int(context['samburu_goats'])+
                                    # int(context['transnzoia_goats'])+
                                    int(context['baringo_goats']),
                                    # int(context['uasingishu_goats'])+
                                    # int(context['elgeyomarakwet_goats'])+
                                    # int(context['nandi_goats'])+
                                    # int(context['laikipia_goats'])+
                                    # int(context['nakuru_goats'])+
                                    # int(context['narok_goats'])+
                                    # int(context['kajiado_goats'])+
                                    # int(context['kericho_goats'])+
                                    # int(context['bomet_goats'])+
                                    # int(context['kakamega_goats'])+
                                    # int(context['vihiga_goats'])+
                                    # int(context['bungoma_goats'])+
                                    # int(context['busia_goats']),
        'total_camels':
                                    # int(context['nairobi_camels'])+
                                    # int(context['nyandarua_camels'])+
                                    # int(context['nyeri_camels'])+
                                    # int(context['kirinyaga_camels'])+
                                    # int(context['muranga_camels'])+
                                    # int(context['kiambu_camels'])+
                                    # int(context['mombasa_camels'])+
                                    # int(context['kwale_camels'])+
                                    # int(context['kilifi_camels'])+
                                    int(context['tanariver_camels'])+
                                    # int(context['lamu_camels'])+
                                    # int(context['taitataveta_camels'])+
                                    int(context['marsabit_camels'])+
                                    # int(context['isiolo_camels'])+
                                    # int(context['meru_camels'])+
                                    # int(context['tharaka_camels'])+
                                    # int(context['embu_camels'])+
                                    # int(context['kitui_camels'])+
                                    # int(context['machakos_camels'])+
                                    # int(context['makueni_camels'])+
                                    int(context['garissa_camels'])+
                                    int(context['wajir_camels'])+
                                    # int(context['mandera_camels'])+
                                    # int(context['siaya_camels'])+
                                    # int(context['kisumu_camels'])+
                                    # int(context['homabay_camels'])+
                                    # int(context['migori_camels'])+
                                    # int(context['kisii_camels'])+
                                    # int(context['nyamira_camels'])+
                                    # int(context['turkana_camels'])+
                                    # int(context['westpokot_camels'])+
                                    # int(context['samburu_camels'])+
                                    # int(context['transnzoia_camels'])+
                                    int(context['baringo_camels']),
                                    # int(context['uasingishu_camels'])+
                                    # int(context['elgeyomarakwet_camels'])+
                                    # int(context['nandi_camels'])+
                                    # int(context['laikipia_camels'])+
                                    # int(context['nakuru_camels'])+
                                    # int(context['narok_camels'])+
                                    # int(context['kajiado_camels'])+
                                    # int(context['kericho_camels'])+
                                    # int(context['bomet_camels'])+
                                    # int(context['kakamega_camels'])+
                                    # int(context['vihiga_camels'])+
                                    # int(context['bungoma_camels'])+
                                    # int(context['busia_camels']),
        # 'total_donkeys': int(context['nairobi_donkeys'])+
        #                             int(context['nyandarua_donkeys'])+
        #                             int(context['nyeri_donkeys'])+
        #                             int(context['kirinyaga_donkeys'])+
        #                             int(context['muranga_donkeys'])+
        #                             int(context['kiambu_donkeys'])+
        #                             int(context['mombasa_donkeys'])+
        #                             int(context['kwale_donkeys'])+
        #                             int(context['kilifi_donkeys'])+
        #                             int(context['tanariver_donkeys'])+
        #                             int(context['lamu_donkeys'])+
        #                             int(context['taitataveta_donkeys'])+
        #                             int(context['marsabit_donkeys'])+
        #                             int(context['isiolo_donkeys'])+
        #                             int(context['meru_donkeys'])+
        #                             int(context['tharaka_donkeys'])+
        #                             int(context['embu_donkeys'])+
        #                             int(context['kitui_donkeys'])+
        #                             int(context['machakos_donkeys'])+
        #                             int(context['makueni_donkeys'])+
        #                             int(context['garissa_donkeys'])+
        #                             int(context['wajir_donkeys'])+
        #                             int(context['mandera_donkeys'])+
        #                             int(context['siaya_donkeys'])+
        #                             int(context['kisumu_donkeys'])+
        #                             int(context['homabay_donkeys'])+
        #                             int(context['migori_donkeys'])+
        #                             int(context['kisii_donkeys'])+
        #                             int(context['nyamira_donkeys'])+
        #                             int(context['turkana_donkeys'])+
        #                             int(context['westpokot_donkeys'])+
        #                             int(context['samburu_donkeys'])+
        #                             int(context['transnzoia_donkeys'])+
        #                             int(context['baringo_donkeys'])+
        #                             int(context['uasingishu_donkeys'])+
        #                             int(context['elgeyomarakwet_donkeys'])+
        #                             int(context['nandi_donkeys'])+
        #                             int(context['laikipia_donkeys'])+
        #                             int(context['nakuru_donkeys'])+
        #                             int(context['narok_donkeys'])+
        #                             int(context['kajiado_donkeys'])+
        #                             int(context['kericho_donkeys'])+
        #                             int(context['bomet_donkeys'])+
        #                             int(context['kakamega_donkeys'])+
        #                             int(context['vihiga_donkeys'])+
        #                             int(context['bungoma_donkeys'])+
        #                             int(context['busia_donkeys']),
    }


    return render(request,'livestock_population.html',context2)

def human_population(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['human_population']

    context = {
        'nairobi_male_population':0,
        'nairobi_female_population': 0,
        'nairobi_intersex_population': 0,
        'nairobi_total_population': 0,
        'nairobi_outbreak_start_date': 0,
        'nairobi_outbreak_stop_date': 0,
        'nairobi_deaths': 0,
        'nairobi_p_and_c_cases': 0,
        'nairobi_human_reference': 0,
        'nyandarua_male_population':0,
        'nyandarua_female_population': 0,
        'nyandarua_intersex_population': 0,
        'nyandarua_total_population': 0,
        'nyandarua_outbreak_start_date': 0,
        'nyandarua_outbreak_stop_date': 0,
        'nyandarua_deaths': 0,
        'nyandarua_p_and_c_cases': 0,
        'nyandarua_human_reference': 0,
        'nyeri_male_population':0,
        'nyeri_female_population': 0,
        'nyeri_intersex_population': 0,
        'nyeri_total_population': 0,
        'nyeri_outbreak_start_date': 0,
        'nyeri_outbreak_stop_date': 0,
        'nyeri_deaths': 0,
        'nyeri_p_and_c_cases': 0,
        'nyeri_human_reference': 0,
        'kirinyaga_male_population':0,
        'kirinyaga_female_population': 0,
        'kirinyaga_intersex_population': 0,
        'kirinyaga_total_population': 0,
        'kirinyaga_outbreak_start_date': 0,
        'kirinyaga_outbreak_stop_date': 0,
        'kirinyaga_deaths': 0,
        'kirinyaga_p_and_c_cases': 0,
        'kirinyaga_human_reference': 0,
        'muranga_male_population':0,
        'muranga_female_population': 0,
        'muranga_intersex_population': 0,
        'muranga_total_population': 0,
        'muranga_outbreak_start_date': 0,
        'muranga_outbreak_stop_date': 0,
        'muranga_deaths': 0,
        'muranga_p_and_c_cases': 0,
        'muranga_human_reference': 0,
        'kiambu_male_population':0,
        'kiambu_female_population': 0,
        'kiambu_intersex_population': 0,
        'kiambu_total_population': 0,
        'kiambu_outbreak_start_date': 0,
        'kiambu_outbreak_stop_date': 0,
        'kiambu_deaths': 0,
        'kiambu_p_and_c_cases': 0,
        'kiambu_human_reference': 0,
        'mombasa_male_population':0,
        'mombasa_female_population': 0,
        'mombasa_intersex_population': 0,
        'mombasa_total_population': 0,
        'mombasa_outbreak_start_date': 0,
        'mombasa_outbreak_stop_date': 0,
        'mombasa_deaths': 0,
        'mombasa_p_and_c_cases': 0,
        'mombasa_human_reference': 0,
        'kwale_male_population':0,
        'kwale_female_population': 0,
        'kwale_intersex_population': 0,
        'kwale_total_population': 0,
        'kwale_outbreak_start_date': 0,
        'kwale_outbreak_stop_date': 0,
        'kwale_deaths': 0,
        'kwale_p_and_c_cases': 0,
        'kwale_human_reference': 0,
        'kilifi_male_population':0,
        'kilifi_female_population': 0,
        'kilifi_intersex_population': 0,
        'kilifi_total_population': 0,
        'kilifi_outbreak_start_date': 0,
        'kilifi_outbreak_stop_date': 0,
        'kilifi_deaths': 0,
        'kilifi_p_and_c_cases': 0,
        'kilifi_human_reference': 0,
        'tanariver_male_population':0,
        'tanariver_female_population': 0,
        'tanariver_intersex_population': 0,
        'tanariver_total_population': 0,
        'tanariver_outbreak_start_date': 0,
        'tanariver_outbreak_stop_date': 0,
        'tanariver_deaths': 0,
        'tanariver_p_and_c_cases': 0,
        'tanariver_human_reference': 0,
        'lamu_male_population':0,
        'lamu_female_population': 0,
        'lamu_intersex_population': 0,
        'lamu_total_population': 0,
        'lamu_outbreak_start_date': 0,
        'lamu_outbreak_stop_date': 0,
        'lamu_deaths': 0,
        'lamu_p_and_c_cases': 0,
        'lamu_human_reference': 0,
        'taitataveta_male_population':0,
        'taitataveta_female_population': 0,
        'taitataveta_intersex_population': 0,
        'taitataveta_total_population': 0,
        'taitataveta_outbreak_start_date': 0,
        'taitataveta_outbreak_stop_date': 0,
        'taitataveta_deaths': 0,
        'taitataveta_p_and_c_cases': 0,
        'taitataveta_human_reference': 0,
        'marsabit_male_population':0,
        'marsabit_female_population': 0,
        'marsabit_intersex_population': 0,
        'marsabit_total_population': 0,
        'marsabit_outbreak_start_date': 0,
        'marsabit_outbreak_stop_date': 0,
        'marsabit_deaths': 0,
        'marsabit_p_and_c_cases': 0,
        'marsabit_human_reference': 0,
        'isiolo_male_population':0,
        'isiolo_female_population': 0,
        'isiolo_intersex_population': 0,
        'isiolo_total_population': 0,
        'isiolo_outbreak_start_date': 0,
        'isiolo_outbreak_stop_date': 0,
        'isiolo_deaths': 0,
        'isiolo_p_and_c_cases': 0,
        'isiolo_human_reference': 0,
        'meru_male_population':0,
        'meru_female_population': 0,
        'meru_intersex_population': 0,
        'meru_total_population': 0,
        'meru_outbreak_start_date': 0,
        'meru_outbreak_stop_date': 0,
        'meru_deaths': 0,
        'meru_p_and_c_cases': 0,
        'meru_human_reference': 0,
        'tharaka_male_population':0,
        'tharaka_female_population': 0,
        'tharaka_intersex_population': 0,
        'tharaka_total_population': 0,
        'tharaka_outbreak_start_date': 0,
        'tharaka_outbreak_stop_date': 0,
        'tharaka_deaths': 0,
        'tharaka_p_and_c_cases': 0,
        'tharaka_human_reference': 0,
        'embu_male_population':0,
        'embu_female_population': 0,
        'embu_intersex_population': 0,
        'embu_total_population': 0,
        'embu_outbreak_start_date': 0,
        'embu_outbreak_stop_date': 0,
        'embu_deaths': 0,
        'embu_p_and_c_cases': 0,
        'embu_human_reference': 0,
        'kitui_male_population':0,
        'kitui_female_population': 0,
        'kitui_intersex_population': 0,
        'kitui_total_population': 0,
        'kitui_outbreak_start_date': 0,
        'kitui_outbreak_stop_date': 0,
        'kitui_deaths': 0,
        'kitui_p_and_c_cases': 0,
        'kitui_human_reference': 0,
        'machakos_male_population':0,
        'machakos_female_population': 0,
        'machakos_intersex_population': 0,
        'machakos_total_population': 0,
        'machakos_outbreak_start_date': 0,
        'machakos_outbreak_stop_date': 0,
        'machakos_deaths': 0,
        'machakos_p_and_c_cases': 0,
        'machakos_human_reference': 0,
        'makueni_male_population':0,
        'makueni_female_population': 0,
        'makueni_intersex_population': 0,
        'makueni_total_population': 0,
        'makueni_outbreak_start_date': 0,
        'makueni_outbreak_stop_date': 0,
        'makueni_deaths': 0,
        'makueni_p_and_c_cases': 0,
        'makueni_human_reference': 0,
        'garissa_male_population':0,
        'garissa_female_population': 0,
        'garissa_intersex_population': 0,
        'garissa_total_population': 0,
        'garissa_outbreak_start_date': 0,
        'garissa_outbreak_stop_date': 0,
        'garissa_deaths': 0,
        'garissa_p_and_c_cases': 0,
        'garissa_human_reference': 0,
        'wajir_male_population':0,
        'wajir_female_population': 0,
        'wajir_intersex_population': 0,
        'wajir_total_population': 0,
        'wajir_outbreak_start_date': 0,
        'wajir_outbreak_stop_date': 0,
        'wajir_deaths': 0,
        'wajir_p_and_c_cases': 0,
        'wajir_human_reference': 0,
        'mandera_male_population':0,
        'mandera_female_population': 0,
        'mandera_intersex_population': 0,
        'mandera_total_population': 0,
        'mandera_outbreak_start_date': 0,
        'mandera_outbreak_stop_date': 0,
        'mandera_deaths': 0,
        'mandera_p_and_c_cases': 0,
        'mandera_human_reference': 0,
        'siaya_male_population':0,
        'siaya_female_population': 0,
        'siaya_intersex_population': 0,
        'siaya_total_population': 0,
        'siaya_outbreak_start_date': 0,
        'siaya_outbreak_stop_date': 0,
        'siaya_deaths': 0,
        'siaya_p_and_c_cases': 0,
        'siaya_human_reference': 0,
        'kisumu_male_population':0,
        'kisumu_female_population': 0,
        'kisumu_intersex_population': 0,
        'kisumu_total_population': 0,
        'kisumu_outbreak_start_date': 0,
        'kisumu_outbreak_stop_date': 0,
        'kisumu_deaths': 0,
        'kisumu_p_and_c_cases': 0,
        'kisumu_human_reference': 0,
        'homabay_male_population':0,
        'homabay_female_population': 0,
        'homabay_intersex_population': 0,
        'homabay_total_population': 0,
        'homabay_outbreak_start_date': 0,
        'homabay_outbreak_stop_date': 0,
        'homabay_deaths': 0,
        'homabay_p_and_c_cases': 0,
        'homabay_human_reference': 0,
        'migori_male_population':0,
        'migori_female_population': 0,
        'migori_intersex_population': 0,
        'migori_total_population': 0,
        'migori_outbreak_start_date': 0,
        'migori_outbreak_stop_date': 0,
        'migori_deaths': 0,
        'migori_p_and_c_cases': 0,
        'migori_human_reference': 0,
        'kisii_male_population':0,
        'kisii_female_population': 0,
        'kisii_intersex_population': 0,
        'kisii_total_population': 0,
        'kisii_outbreak_start_date': 0,
        'kisii_outbreak_stop_date': 0,
        'kisii_deaths': 0,
        'kisii_p_and_c_cases': 0,
        'kisii_human_reference': 0,
        'nyamira_male_population':0,
        'nyamira_female_population': 0,
        'nyamira_intersex_population': 0,
        'nyamira_total_population': 0,
        'nyamira_outbreak_start_date': 0,
        'nyamira_outbreak_stop_date': 0,
        'nyamira_deaths': 0,
        'nyamira_p_and_c_cases': 0,
        'nyamira_human_reference': 0,
        'turkana_male_population':0,
        'turkana_female_population': 0,
        'turkana_intersex_population': 0,
        'turkana_total_population': 0,
        'turkana_outbreak_start_date': 0,
        'turkana_outbreak_stop_date': 0,
        'turkana_deaths': 0,
        'turkana_p_and_c_cases': 0,
        'turkana_human_reference': 0,
        'westpokot_male_population':0,
        'westpokot_female_population': 0,
        'westpokot_intersex_population': 0,
        'westpokot_total_population': 0,
        'westpokot_outbreak_start_date': 0,
        'westpokot_outbreak_stop_date': 0,
        'westpokot_deaths': 0,
        'westpokot_p_and_c_cases': 0,
        'westpokot_human_reference': 0,
        'samburu_male_population':0,
        'samburu_female_population': 0,
        'samburu_intersex_population': 0,
        'samburu_total_population': 0,
        'samburu_outbreak_start_date': 0,
        'samburu_outbreak_stop_date': 0,
        'samburu_deaths': 0,
        'samburu_p_and_c_cases': 0,
        'samburu_human_reference': 0,
        'transnzoia_male_population':0,
        'transnzoia_female_population': 0,
        'transnzoia_intersex_population': 0,
        'transnzoia_total_population': 0,
        'transnzoia_outbreak_start_date': 0,
        'transnzoia_outbreak_stop_date': 0,
        'transnzoia_deaths': 0,
        'transnzoia_p_and_c_cases': 0,
        'transnzoia_human_reference': 0,
        'baringo_male_population':0,
        'baringo_female_population': 0,
        'baringo_intersex_population': 0,
        'baringo_total_population': 0,
        'baringo_outbreak_start_date': 0,
        'baringo_outbreak_stop_date': 0,
        'baringo_deaths': 0,
        'baringo_p_and_c_cases': 0,
        'baringo_human_reference': 0,
        'uasingishu_male_population':0,
        'uasingishu_female_population': 0,
        'uasingishu_intersex_population': 0,
        'uasingishu_total_population': 0,
        'uasingishu_outbreak_start_date': 0,
        'uasingishu_outbreak_stop_date': 0,
        'uasingishu_deaths': 0,
        'uasingishu_p_and_c_cases': 0,
        'uasingishu_human_reference': 0,
        'elgeyomarakwet_male_population':0,
        'elgeyomarakwet_female_population': 0,
        'elgeyomarakwet_intersex_population': 0,
        'elgeyomarakwet_total_population': 0,
        'elgeyomarakwet_outbreak_start_date': 0,
        'elgeyomarakwet_outbreak_stop_date': 0,
        'elgeyomarakwet_deaths': 0,
        'elgeyomarakwet_p_and_c_cases': 0,
        'elgeyomarakwet_human_reference': 0,
        'nandi_male_population':0,
        'nandi_female_population': 0,
        'nandi_intersex_population': 0,
        'nandi_total_population': 0,
        'nandi_outbreak_start_date': 0,
        'nandi_outbreak_stop_date': 0,
        'nandi_deaths': 0,
        'nandi_p_and_c_cases': 0,
        'nandi_human_reference': 0,
        'laikipia_male_population':0,
        'laikipia_female_population': 0,
        'laikipia_intersex_population': 0,
        'laikipia_total_population': 0,
        'laikipia_outbreak_start_date': 0,
        'laikipia_outbreak_stop_date': 0,
        'laikipia_deaths': 0,
        'laikipia_p_and_c_cases': 0,
        'laikipia_human_reference': 0,
        'nakuru_male_population':0,
        'nakuru_female_population': 0,
        'nakuru_intersex_population': 0,
        'nakuru_total_population': 0,
        'nakuru_outbreak_start_date': 0,
        'nakuru_outbreak_stop_date': 0,
        'nakuru_deaths': 0,
        'nakuru_p_and_c_cases': 0,
        'nakuru_human_reference': 0,
        'narok_male_population':0,
        'narok_female_population': 0,
        'narok_intersex_population': 0,
        'narok_total_population': 0,
        'narok_outbreak_start_date': 0,
        'narok_outbreak_stop_date': 0,
        'narok_deaths': 0,
        'narok_p_and_c_cases': 0,
        'narok_human_reference': 0,
        'kajiado_male_population':0,
        'kajiado_female_population': 0,
        'kajiado_intersex_population': 0,
        'kajiado_total_population': 0,
        'kajiado_outbreak_start_date': 0,
        'kajiado_outbreak_stop_date': 0,
        'kajiado_deaths': 0,
        'kajiado_p_and_c_cases': 0,
        'kajiado_human_reference': 0,
        'kericho_male_population':0,
        'kericho_female_population': 0,
        'kericho_intersex_population': 0,
        'kericho_total_population': 0,
        'kericho_outbreak_start_date': 0,
        'kericho_outbreak_stop_date': 0,
        'kericho_deaths': 0,
        'kericho_p_and_c_cases': 0,
        'kericho_human_reference': 0,
        'bomet_male_population':0,
        'bomet_female_population': 0,
        'bomet_intersex_population': 0,
        'bomet_total_population': 0,
        'bomet_outbreak_start_date': 0,
        'bomet_outbreak_stop_date': 0,
        'bomet_deaths': 0,
        'bomet_p_and_c_cases': 0,
        'bomet_human_reference': 0,
        'kakamega_male_population':0,
        'kakamega_female_population': 0,
        'kakamega_intersex_population': 0,
        'kakamega_total_population': 0,
        'kakamega_outbreak_start_date': 0,
        'kakamega_outbreak_stop_date': 0,
        'kakamega_deaths': 0,
        'kakamega_p_and_c_cases': 0,
        'kakamega_human_reference': 0,
        'vihiga_male_population':0,
        'vihiga_female_population': 0,
        'vihiga_intersex_population': 0,
        'vihiga_total_population': 0,
        'vihiga_outbreak_start_date': 0,
        'vihiga_outbreak_stop_date': 0,
        'vihiga_deaths': 0,
        'vihiga_p_and_c_cases': 0,
        'vihiga_human_reference': 0,
        'bungoma_male_population':0,
        'bungoma_female_population': 0,
        'bungoma_intersex_population': 0,
        'bungoma_total_population': 0,
        'bungoma_outbreak_start_date': 0,
        'bungoma_outbreak_stop_date': 0,
        'bungoma_deaths': 0,
        'bungoma_p_and_c_cases': 0,
        'bungoma_human_reference': 0,
        'busia_male_population':0,
        'busia_female_population': 0,
        'busia_intersex_population': 0,
        'busia_total_population': 0,
        'busia_outbreak_start_date': 0,
        'busia_outbreak_stop_date': 0,
        'busia_deaths': 0,
        'busia_p_and_c_cases': 0,
        'busia_human_reference': 0,
    }

    if (request.method == "POST"):
        # nairobi_male_population = request.POST['nairobi_male_population']
        # nairobi_female_population = request.POST['nairobi_female_population']
        # nairobi_intersex_population = request.POST['nairobi_intersex_population']
        # nairobi_total_population = request.POST['nairobi_total_population']
        # nairobi_outbreak_start_date = request.POST['nairobi_outbreak_start_date']
        # nairobi_outbreak_stop_date = request.POST['nairobi_outbreak_stop_date']
        # nairobi_deaths = request.POST['nairobi_deaths']
        # nairobi_p_and_c_cases = request.POST['nairobi_p_and_c_cases']
        # nairobi_human_reference = request.POST['nairobi_human_reference']
        # nyandarua_male_population = request.POST['nyandarua_male_population']
        # nyandarua_female_population = request.POST['nyandarua_female_population']
        # nyandarua_intersex_population = request.POST['nyandarua_intersex_population']
        # nyandarua_total_population = request.POST['nyandarua_total_population']
        # nyandarua_outbreak_start_date = request.POST['nyandarua_outbreak_start_date']
        # nyandarua_outbreak_stop_date = request.POST['nyandarua_outbreak_stop_date']
        # nyandarua_deaths = request.POST['nyandarua_deaths']
        # nyandarua_p_and_c_cases = request.POST['nyandarua_p_and_c_cases']
        # nyandarua_human_reference = request.POST['nyandarua_human_reference']
        # nyeri_male_population = request.POST['nyeri_male_population']
        # nyeri_female_population = request.POST['nyeri_female_population']
        # nyeri_intersex_population = request.POST['nyeri_intersex_population']
        # nyeri_total_population = request.POST['nyeri_total_population']
        # nyeri_outbreak_start_date = request.POST['nyeri_outbreak_start_date']
        # nyeri_outbreak_stop_date = request.POST['nyeri_outbreak_stop_date']
        # nyeri_deaths = request.POST['nyeri_deaths']
        # nyeri_p_and_c_cases = request.POST['nyeri_p_and_c_cases']
        # nyeri_human_reference = request.POST['nyeri_human_reference']
        # kirinyaga_male_population = request.POST['kirinyaga_male_population']
        # kirinyaga_female_population = request.POST['kirinyaga_female_population']
        # kirinyaga_intersex_population = request.POST['kirinyaga_intersex_population']
        # kirinyaga_total_population = request.POST['kirinyaga_total_population']
        # kirinyaga_outbreak_start_date = request.POST['kirinyaga_outbreak_start_date']
        # kirinyaga_outbreak_stop_date = request.POST['kirinyaga_outbreak_stop_date']
        # kirinyaga_deaths = request.POST['kirinyaga_deaths']
        # kirinyaga_p_and_c_cases = request.POST['kirinyaga_p_and_c_cases']
        # kirinyaga_human_reference = request.POST['kirinyaga_human_reference']
        # muranga_male_population = request.POST['muranga_male_population']
        # muranga_female_population = request.POST['muranga_female_population']
        # muranga_intersex_population = request.POST['muranga_intersex_population']
        # muranga_total_population = request.POST['muranga_total_population']
        # muranga_outbreak_start_date = request.POST['muranga_outbreak_start_date']
        # muranga_outbreak_stop_date = request.POST['muranga_outbreak_stop_date']
        # muranga_deaths = request.POST['muranga_deaths']
        # muranga_p_and_c_cases = request.POST['muranga_p_and_c_cases']
        # muranga_human_reference = request.POST['muranga_human_reference']
        # kiambu_male_population = request.POST['kiambu_male_population']
        # kiambu_female_population = request.POST['kiambu_female_population']
        # kiambu_intersex_population = request.POST['kiambu_intersex_population']
        # kiambu_total_population = request.POST['kiambu_total_population']
        # kiambu_outbreak_start_date = request.POST['kiambu_outbreak_start_date']
        # kiambu_outbreak_stop_date = request.POST['kiambu_outbreak_stop_date']
        # kiambu_deaths = request.POST['kiambu_deaths']
        # kiambu_p_and_c_cases = request.POST['kiambu_p_and_c_cases']
        # kiambu_human_reference = request.POST['kiambu_human_reference']
        # mombasa_male_population = request.POST['mombasa_male_population']
        # mombasa_female_population = request.POST['mombasa_female_population']
        # mombasa_intersex_population = request.POST['mombasa_intersex_population']
        # mombasa_total_population = request.POST['mombasa_total_population']
        # mombasa_outbreak_start_date = request.POST['mombasa_outbreak_start_date']
        # mombasa_outbreak_stop_date = request.POST['mombasa_outbreak_stop_date']
        # mombasa_deaths = request.POST['mombasa_deaths']
        # mombasa_p_and_c_cases = request.POST['mombasa_p_and_c_cases']
        # mombasa_human_reference = request.POST['mombasa_human_reference']
        # kwale_male_population = request.POST['kwale_male_population']
        # kwale_female_population = request.POST['kwale_female_population']
        # kwale_intersex_population = request.POST['kwale_intersex_population']
        # kwale_total_population = request.POST['kwale_total_population']
        # kwale_outbreak_start_date = request.POST['kwale_outbreak_start_date']
        # kwale_outbreak_stop_date = request.POST['kwale_outbreak_stop_date']
        # kwale_deaths = request.POST['kwale_deaths']
        # kwale_p_and_c_cases = request.POST['kwale_p_and_c_cases']
        # kwale_human_reference = request.POST['kwale_human_reference']
        # kilifi_male_population = request.POST['kilifi_male_population']
        # kilifi_female_population = request.POST['kilifi_female_population']
        # kilifi_intersex_population = request.POST['kilifi_intersex_population']
        # kilifi_total_population = request.POST['kilifi_total_population']
        # kilifi_outbreak_start_date = request.POST['kilifi_outbreak_start_date']
        # kilifi_outbreak_stop_date = request.POST['kilifi_outbreak_stop_date']
        # kilifi_deaths = request.POST['kilifi_deaths']
        # kilifi_p_and_c_cases = request.POST['kilifi_p_and_c_cases']
        # kilifi_human_reference = request.POST['kilifi_human_reference']
        tanariver_male_population = request.POST['tanariver_male_population']
        tanariver_female_population = request.POST['tanariver_female_population']
        tanariver_intersex_population = request.POST['tanariver_intersex_population']
        tanariver_total_population = request.POST['tanariver_total_population']
        tanariver_outbreak_start_date = request.POST['tanariver_outbreak_start_date']
        tanariver_outbreak_stop_date = request.POST['tanariver_outbreak_stop_date']
        tanariver_deaths = request.POST['tanariver_deaths']
        tanariver_p_and_c_cases = request.POST['tanariver_p_and_c_cases']
        tanariver_human_reference = request.POST['tanariver_human_reference']
        # lamu_male_population = request.POST['lamu_male_population']
        # lamu_female_population = request.POST['lamu_female_population']
        # lamu_intersex_population = request.POST['lamu_intersex_population']
        # lamu_total_population = request.POST['lamu_total_population']
        # lamu_outbreak_start_date = request.POST['lamu_outbreak_start_date']
        # lamu_outbreak_stop_date = request.POST['lamu_outbreak_stop_date']
        # lamu_deaths = request.POST['lamu_deaths']
        # lamu_p_and_c_cases = request.POST['lamu_p_and_c_cases']
        # lamu_human_reference = request.POST['lamu_human_reference']
        # taitataveta_male_population = request.POST['taitataveta_male_population']
        # taitataveta_female_population = request.POST['taitataveta_female_population']
        # taitataveta_intersex_population = request.POST['taitataveta_intersex_population']
        # taitataveta_total_population = request.POST['taitataveta_total_population']
        # taitataveta_outbreak_start_date = request.POST['taitataveta_outbreak_start_date']
        # taitataveta_outbreak_stop_date = request.POST['taitataveta_outbreak_stop_date']
        # taitataveta_deaths = request.POST['taitataveta_deaths']
        # taitataveta_p_and_c_cases = request.POST['taitataveta_p_and_c_cases']
        # taitataveta_human_reference = request.POST['taitataveta_human_reference']
        marsabit_male_population = request.POST['marsabit_male_population']
        marsabit_female_population = request.POST['marsabit_female_population']
        marsabit_intersex_population = request.POST['marsabit_intersex_population']
        marsabit_total_population = request.POST['marsabit_total_population']
        marsabit_outbreak_start_date = request.POST['marsabit_outbreak_start_date']
        marsabit_outbreak_stop_date = request.POST['marsabit_outbreak_stop_date']
        marsabit_deaths = request.POST['marsabit_deaths']
        marsabit_p_and_c_cases = request.POST['marsabit_p_and_c_cases']
        marsabit_human_reference = request.POST['marsabit_human_reference']
        # isiolo_male_population = request.POST['isiolo_male_population']
        # isiolo_female_population = request.POST['isiolo_female_population']
        # isiolo_intersex_population = request.POST['isiolo_intersex_population']
        # isiolo_total_population = request.POST['isiolo_total_population']
        # isiolo_outbreak_start_date = request.POST['isiolo_outbreak_start_date']
        # isiolo_outbreak_stop_date = request.POST['isiolo_outbreak_stop_date']
        # isiolo_deaths = request.POST['isiolo_deaths']
        # isiolo_p_and_c_cases = request.POST['isiolo_p_and_c_cases']
        # isiolo_human_reference = request.POST['isiolo_human_reference']
        # meru_male_population = request.POST['meru_male_population']
        # meru_female_population = request.POST['meru_female_population']
        # meru_intersex_population = request.POST['meru_intersex_population']
        # meru_total_population = request.POST['meru_total_population']
        # meru_outbreak_start_date = request.POST['meru_outbreak_start_date']
        # meru_outbreak_stop_date = request.POST['meru_outbreak_stop_date']
        # meru_deaths = request.POST['meru_deaths']
        # meru_p_and_c_cases = request.POST['meru_p_and_c_cases']
        # meru_human_reference = request.POST['meru_human_reference']
        # tharaka_male_population = request.POST['tharaka_male_population']
        # tharaka_female_population = request.POST['tharaka_female_population']
        # tharaka_intersex_population = request.POST['tharaka_intersex_population']
        # tharaka_total_population = request.POST['tharaka_total_population']
        # tharaka_outbreak_start_date = request.POST['tharaka_outbreak_start_date']
        # tharaka_outbreak_stop_date = request.POST['tharaka_outbreak_stop_date']
        # tharaka_deaths = request.POST['tharaka_deaths']
        # tharaka_p_and_c_cases = request.POST['tharaka_p_and_c_cases']
        # tharaka_human_reference = request.POST['tharaka_human_reference']
        # embu_male_population = request.POST['embu_male_population']
        # embu_female_population = request.POST['embu_female_population']
        # embu_intersex_population = request.POST['embu_intersex_population']
        # embu_total_population = request.POST['embu_total_population']
        # embu_outbreak_start_date = request.POST['embu_outbreak_start_date']
        # embu_outbreak_stop_date = request.POST['embu_outbreak_stop_date']
        # embu_deaths = request.POST['embu_deaths']
        # embu_p_and_c_cases = request.POST['embu_p_and_c_cases']
        # embu_human_reference = request.POST['embu_human_reference']
        # kitui_male_population = request.POST['kitui_male_population']
        # kitui_female_population = request.POST['kitui_female_population']
        # kitui_intersex_population = request.POST['kitui_intersex_population']
        # kitui_total_population = request.POST['kitui_total_population']
        # kitui_outbreak_start_date = request.POST['kitui_outbreak_start_date']
        # kitui_outbreak_stop_date = request.POST['kitui_outbreak_stop_date']
        # kitui_deaths = request.POST['kitui_deaths']
        # kitui_p_and_c_cases = request.POST['kitui_p_and_c_cases']
        # kitui_human_reference = request.POST['kitui_human_reference']
        # machakos_male_population = request.POST['machakos_male_population']
        # machakos_female_population = request.POST['machakos_female_population']
        # machakos_intersex_population = request.POST['machakos_intersex_population']
        # machakos_total_population = request.POST['machakos_total_population']
        # machakos_outbreak_start_date = request.POST['machakos_outbreak_start_date']
        # machakos_outbreak_stop_date = request.POST['machakos_outbreak_stop_date']
        # machakos_deaths = request.POST['machakos_deaths']
        # machakos_p_and_c_cases = request.POST['machakos_p_and_c_cases']
        # machakos_human_reference = request.POST['machakos_human_reference']
        # makueni_male_population = request.POST['makueni_male_population']
        # makueni_female_population = request.POST['makueni_female_population']
        # makueni_intersex_population = request.POST['makueni_intersex_population']
        # makueni_total_population = request.POST['makueni_total_population']
        # makueni_outbreak_start_date = request.POST['makueni_outbreak_start_date']
        # makueni_outbreak_stop_date = request.POST['makueni_outbreak_stop_date']
        # makueni_deaths = request.POST['makueni_deaths']
        # makueni_p_and_c_cases = request.POST['makueni_p_and_c_cases']
        # makueni_human_reference = request.POST['makueni_human_reference']
        garissa_male_population = request.POST['garissa_male_population']
        garissa_female_population = request.POST['garissa_female_population']
        garissa_intersex_population = request.POST['garissa_intersex_population']
        garissa_total_population = request.POST['garissa_total_population']
        garissa_outbreak_start_date = request.POST['garissa_outbreak_start_date']
        garissa_outbreak_stop_date = request.POST['garissa_outbreak_stop_date']
        garissa_deaths = request.POST['garissa_deaths']
        garissa_p_and_c_cases = request.POST['garissa_p_and_c_cases']
        garissa_human_reference = request.POST['garissa_human_reference']
        wajir_male_population = request.POST['wajir_male_population']
        wajir_female_population = request.POST['wajir_female_population']
        wajir_intersex_population = request.POST['wajir_intersex_population']
        wajir_total_population = request.POST['wajir_total_population']
        wajir_outbreak_start_date = request.POST['wajir_outbreak_start_date']
        wajir_outbreak_stop_date = request.POST['wajir_outbreak_stop_date']
        wajir_deaths = request.POST['wajir_deaths']
        wajir_p_and_c_cases = request.POST['wajir_p_and_c_cases']
        wajir_human_reference = request.POST['wajir_human_reference']
        # mandera_male_population = request.POST['mandera_male_population']
        # mandera_female_population = request.POST['mandera_female_population']
        # mandera_intersex_population = request.POST['mandera_intersex_population']
        # mandera_total_population = request.POST['mandera_total_population']
        # mandera_outbreak_start_date = request.POST['mandera_outbreak_start_date']
        # mandera_outbreak_stop_date = request.POST['mandera_outbreak_stop_date']
        # mandera_deaths = request.POST['mandera_deaths']
        # mandera_p_and_c_cases = request.POST['mandera_p_and_c_cases']
        # mandera_human_reference = request.POST['mandera_human_reference']
        # siaya_male_population = request.POST['siaya_male_population']
        # siaya_female_population = request.POST['siaya_female_population']
        # siaya_intersex_population = request.POST['siaya_intersex_population']
        # siaya_total_population = request.POST['siaya_total_population']
        # siaya_outbreak_start_date = request.POST['siaya_outbreak_start_date']
        # siaya_outbreak_stop_date = request.POST['siaya_outbreak_stop_date']
        # siaya_deaths = request.POST['siaya_deaths']
        # siaya_p_and_c_cases = request.POST['siaya_p_and_c_cases']
        # siaya_human_reference = request.POST['siaya_human_reference']
        # kisumu_male_population = request.POST['kisumu_male_population']
        # kisumu_female_population = request.POST['kisumu_female_population']
        # kisumu_intersex_population = request.POST['kisumu_intersex_population']
        # kisumu_total_population = request.POST['kisumu_total_population']
        # kisumu_outbreak_start_date = request.POST['kisumu_outbreak_start_date']
        # kisumu_outbreak_stop_date = request.POST['kisumu_outbreak_stop_date']
        # kisumu_deaths = request.POST['kisumu_deaths']
        # kisumu_p_and_c_cases = request.POST['kisumu_p_and_c_cases']
        # kisumu_human_reference = request.POST['kisumu_human_reference']
        # homabay_male_population = request.POST['homabay_male_population']
        # homabay_female_population = request.POST['homabay_female_population']
        # homabay_intersex_population = request.POST['homabay_intersex_population']
        # homabay_total_population = request.POST['homabay_total_population']
        # homabay_outbreak_start_date = request.POST['homabay_outbreak_start_date']
        # homabay_outbreak_stop_date = request.POST['homabay_outbreak_stop_date']
        # homabay_deaths = request.POST['homabay_deaths']
        # homabay_p_and_c_cases = request.POST['homabay_p_and_c_cases']
        # homabay_human_reference = request.POST['homabay_human_reference']
        # migori_male_population = request.POST['migori_male_population']
        # migori_female_population = request.POST['migori_female_population']
        # migori_intersex_population = request.POST['migori_intersex_population']
        # migori_total_population = request.POST['migori_total_population']
        # migori_outbreak_start_date = request.POST['migori_outbreak_start_date']
        # migori_outbreak_stop_date = request.POST['migori_outbreak_stop_date']
        # migori_deaths = request.POST['migori_deaths']
        # migori_p_and_c_cases = request.POST['migori_p_and_c_cases']
        # migori_human_reference = request.POST['migori_human_reference']
        # kisii_male_population = request.POST['kisii_male_population']
        # kisii_female_population = request.POST['kisii_female_population']
        # kisii_intersex_population = request.POST['kisii_intersex_population']
        # kisii_total_population = request.POST['kisii_total_population']
        # kisii_outbreak_start_date = request.POST['kisii_outbreak_start_date']
        # kisii_outbreak_stop_date = request.POST['kisii_outbreak_stop_date']
        # kisii_deaths = request.POST['kisii_deaths']
        # kisii_p_and_c_cases = request.POST['kisii_p_and_c_cases']
        # kisii_human_reference = request.POST['kisii_human_reference']
        # nyamira_male_population = request.POST['nyamira_male_population']
        # nyamira_female_population = request.POST['nyamira_female_population']
        # nyamira_intersex_population = request.POST['nyamira_intersex_population']
        # nyamira_total_population = request.POST['nyamira_total_population']
        # nyamira_outbreak_start_date = request.POST['nyamira_outbreak_start_date']
        # nyamira_outbreak_stop_date = request.POST['nyamira_outbreak_stop_date']
        # nyamira_deaths = request.POST['nyamira_deaths']
        # nyamira_p_and_c_cases = request.POST['nyamira_p_and_c_cases']
        # nyamira_human_reference = request.POST['nyamira_human_reference']
        # turkana_male_population = request.POST['turkana_male_population']
        # turkana_female_population = request.POST['turkana_female_population']
        # turkana_intersex_population = request.POST['turkana_intersex_population']
        # turkana_total_population = request.POST['turkana_total_population']
        # turkana_outbreak_start_date = request.POST['turkana_outbreak_start_date']
        # turkana_outbreak_stop_date = request.POST['turkana_outbreak_stop_date']
        # turkana_deaths = request.POST['turkana_deaths']
        # turkana_p_and_c_cases = request.POST['turkana_p_and_c_cases']
        # turkana_human_reference = request.POST['turkana_human_reference']
        # westpokot_male_population = request.POST['westpokot_male_population']
        # westpokot_female_population = request.POST['westpokot_female_population']
        # westpokot_intersex_population = request.POST['westpokot_intersex_population']
        # westpokot_total_population = request.POST['westpokot_total_population']
        # westpokot_outbreak_start_date = request.POST['westpokot_outbreak_start_date']
        # westpokot_outbreak_stop_date = request.POST['westpokot_outbreak_stop_date']
        # westpokot_deaths = request.POST['westpokot_deaths']
        # westpokot_p_and_c_cases = request.POST['westpokot_p_and_c_cases']
        # westpokot_human_reference = request.POST['westpokot_human_reference']
        # samburu_male_population = request.POST['samburu_male_population']
        # samburu_female_population = request.POST['samburu_female_population']
        # samburu_intersex_population = request.POST['samburu_intersex_population']
        # samburu_total_population = request.POST['samburu_total_population']
        # samburu_outbreak_start_date = request.POST['samburu_outbreak_start_date']
        # samburu_outbreak_stop_date = request.POST['samburu_outbreak_stop_date']
        # samburu_deaths = request.POST['samburu_deaths']
        # samburu_p_and_c_cases = request.POST['samburu_p_and_c_cases']
        # samburu_human_reference = request.POST['samburu_human_reference']
        # transnzoia_male_population = request.POST['transnzoia_male_population']
        # transnzoia_female_population = request.POST['transnzoia_female_population']
        # transnzoia_intersex_population = request.POST['transnzoia_intersex_population']
        # transnzoia_total_population = request.POST['transnzoia_total_population']
        # transnzoia_outbreak_start_date = request.POST['transnzoia_outbreak_start_date']
        # transnzoia_outbreak_stop_date = request.POST['transnzoia_outbreak_stop_date']
        # transnzoia_deaths = request.POST['transnzoia_deaths']
        # transnzoia_p_and_c_cases = request.POST['transnzoia_p_and_c_cases']
        # transnzoia_human_reference = request.POST['transnzoia_human_reference']
        baringo_male_population = request.POST['baringo_male_population']
        baringo_female_population = request.POST['baringo_female_population']
        baringo_intersex_population = request.POST['baringo_intersex_population']
        baringo_total_population = request.POST['baringo_total_population']
        baringo_outbreak_start_date = request.POST['baringo_outbreak_start_date']
        baringo_outbreak_stop_date = request.POST['baringo_outbreak_stop_date']
        baringo_deaths = request.POST['baringo_deaths']
        baringo_p_and_c_cases = request.POST['baringo_p_and_c_cases']
        baringo_human_reference = request.POST['baringo_human_reference']
        # uasingishu_male_population = request.POST['uasingishu_male_population']
        # uasingishu_female_population = request.POST['uasingishu_female_population']
        # uasingishu_intersex_population = request.POST['uasingishu_intersex_population']
        # uasingishu_total_population = request.POST['uasingishu_total_population']
        # uasingishu_outbreak_start_date = request.POST['uasingishu_outbreak_start_date']
        # uasingishu_outbreak_stop_date = request.POST['uasingishu_outbreak_stop_date']
        # uasingishu_deaths = request.POST['uasingishu_deaths']
        # uasingishu_p_and_c_cases = request.POST['uasingishu_p_and_c_cases']
        # uasingishu_human_reference = request.POST['uasingishu_human_reference']
        # elgeyomarakwet_male_population = request.POST['elgeyomarakwet_male_population']
        # elgeyomarakwet_female_population = request.POST['elgeyomarakwet_female_population']
        # elgeyomarakwet_intersex_population = request.POST['elgeyomarakwet_intersex_population']
        # elgeyomarakwet_total_population = request.POST['elgeyomarakwet_total_population']
        # elgeyomarakwet_outbreak_start_date = request.POST['elgeyomarakwet_outbreak_start_date']
        # elgeyomarakwet_outbreak_stop_date = request.POST['elgeyomarakwet_outbreak_stop_date']
        # elgeyomarakwet_deaths = request.POST['elgeyomarakwet_deaths']
        # elgeyomarakwet_p_and_c_cases = request.POST['elgeyomarakwet_p_and_c_cases']
        # elgeyomarakwet_human_reference = request.POST['elgeyomarakwet_human_reference']
        # nandi_male_population = request.POST['nandi_male_population']
        # nandi_female_population = request.POST['nandi_female_population']
        # nandi_intersex_population = request.POST['nandi_intersex_population']
        # nandi_total_population = request.POST['nandi_total_population']
        # nandi_outbreak_start_date = request.POST['nandi_outbreak_start_date']
        # nandi_outbreak_stop_date = request.POST['nandi_outbreak_stop_date']
        # nandi_deaths = request.POST['nandi_deaths']
        # nandi_p_and_c_cases = request.POST['nandi_p_and_c_cases']
        # nandi_human_reference = request.POST['nandi_human_reference']
        # laikipia_male_population = request.POST['laikipia_male_population']
        # laikipia_female_population = request.POST['laikipia_female_population']
        # laikipia_intersex_population = request.POST['laikipia_intersex_population']
        # laikipia_total_population = request.POST['laikipia_total_population']
        # laikipia_outbreak_start_date = request.POST['laikipia_outbreak_start_date']
        # laikipia_outbreak_stop_date = request.POST['laikipia_outbreak_stop_date']
        # laikipia_deaths = request.POST['laikipia_deaths']
        # laikipia_p_and_c_cases = request.POST['laikipia_p_and_c_cases']
        # laikipia_human_reference = request.POST['laikipia_human_reference']
        # nakuru_male_population = request.POST['nakuru_male_population']
        # nakuru_female_population = request.POST['nakuru_female_population']
        # nakuru_intersex_population = request.POST['nakuru_intersex_population']
        # nakuru_total_population = request.POST['nakuru_total_population']
        # nakuru_outbreak_start_date = request.POST['nakuru_outbreak_start_date']
        # nakuru_outbreak_stop_date = request.POST['nakuru_outbreak_stop_date']
        # nakuru_deaths = request.POST['nakuru_deaths']
        # nakuru_p_and_c_cases = request.POST['nakuru_p_and_c_cases']
        # nakuru_human_reference = request.POST['nakuru_human_reference']
        # narok_male_population = request.POST['narok_male_population']
        # narok_female_population = request.POST['narok_female_population']
        # narok_intersex_population = request.POST['narok_intersex_population']
        # narok_total_population = request.POST['narok_total_population']
        # narok_outbreak_start_date = request.POST['narok_outbreak_start_date']
        # narok_outbreak_stop_date = request.POST['narok_outbreak_stop_date']
        # narok_deaths = request.POST['narok_deaths']
        # narok_p_and_c_cases = request.POST['narok_p_and_c_cases']
        # narok_human_reference = request.POST['narok_human_reference']
        # kajiado_male_population = request.POST['kajiado_male_population']
        # kajiado_female_population = request.POST['kajiado_female_population']
        # kajiado_intersex_population = request.POST['kajiado_intersex_population']
        # kajiado_total_population = request.POST['kajiado_total_population']
        # kajiado_outbreak_start_date = request.POST['kajiado_outbreak_start_date']
        # kajiado_outbreak_stop_date = request.POST['kajiado_outbreak_stop_date']
        # kajiado_deaths = request.POST['kajiado_deaths']
        # kajiado_p_and_c_cases = request.POST['kajiado_p_and_c_cases']
        # kajiado_human_reference = request.POST['kajiado_human_reference']
        # kericho_male_population = request.POST['kericho_male_population']
        # kericho_female_population = request.POST['kericho_female_population']
        # kericho_intersex_population = request.POST['kericho_intersex_population']
        # kericho_total_population = request.POST['kericho_total_population']
        # kericho_outbreak_start_date = request.POST['kericho_outbreak_start_date']
        # kericho_outbreak_stop_date = request.POST['kericho_outbreak_stop_date']
        # kericho_deaths = request.POST['kericho_deaths']
        # kericho_p_and_c_cases = request.POST['kericho_p_and_c_cases']
        # kericho_human_reference = request.POST['kericho_human_reference']
        # bomet_male_population = request.POST['bomet_male_population']
        # bomet_female_population = request.POST['bomet_female_population']
        # bomet_intersex_population = request.POST['bomet_intersex_population']
        # bomet_total_population = request.POST['bomet_total_population']
        # bomet_outbreak_start_date = request.POST['bomet_outbreak_start_date']
        # bomet_outbreak_stop_date = request.POST['bomet_outbreak_stop_date']
        # bomet_deaths = request.POST['bomet_deaths']
        # bomet_p_and_c_cases = request.POST['bomet_p_and_c_cases']
        # bomet_human_reference = request.POST['bomet_human_reference']
        # kakamega_male_population = request.POST['kakamega_male_population']
        # kakamega_female_population = request.POST['kakamega_female_population']
        # kakamega_intersex_population = request.POST['kakamega_intersex_population']
        # kakamega_total_population = request.POST['kakamega_total_population']
        # kakamega_outbreak_start_date = request.POST['kakamega_outbreak_start_date']
        # kakamega_outbreak_stop_date = request.POST['kakamega_outbreak_stop_date']
        # kakamega_deaths = request.POST['kakamega_deaths']
        # kakamega_p_and_c_cases = request.POST['kakamega_p_and_c_cases']
        # kakamega_human_reference = request.POST['kakamega_human_reference']
        # vihiga_male_population = request.POST['vihiga_male_population']
        # vihiga_female_population = request.POST['vihiga_female_population']
        # vihiga_intersex_population = request.POST['vihiga_intersex_population']
        # vihiga_total_population = request.POST['vihiga_total_population']
        # vihiga_outbreak_start_date = request.POST['vihiga_outbreak_start_date']
        # vihiga_outbreak_stop_date = request.POST['vihiga_outbreak_stop_date']
        # vihiga_deaths = request.POST['vihiga_deaths']
        # vihiga_p_and_c_cases = request.POST['vihiga_p_and_c_cases']
        # vihiga_human_reference = request.POST['vihiga_human_reference']
        # bungoma_male_population = request.POST['bungoma_male_population']
        # bungoma_female_population = request.POST['bungoma_female_population']
        # bungoma_intersex_population = request.POST['bungoma_intersex_population']
        # bungoma_total_population = request.POST['bungoma_total_population']
        # bungoma_outbreak_start_date = request.POST['bungoma_outbreak_start_date']
        # bungoma_outbreak_stop_date = request.POST['bungoma_outbreak_stop_date']
        # bungoma_deaths = request.POST['bungoma_deaths']
        # bungoma_p_and_c_cases = request.POST['bungoma_p_and_c_cases']
        # bungoma_human_reference = request.POST['bungoma_human_reference']
        # busia_male_population = request.POST['busia_male_population']
        # busia_female_population = request.POST['busia_female_population']
        # busia_intersex_population = request.POST['busia_intersex_population']
        # busia_total_population = request.POST['busia_total_population']
        # busia_outbreak_start_date = request.POST['busia_outbreak_start_date']
        # busia_outbreak_stop_date = request.POST['busia_outbreak_stop_date']
        # busia_deaths = request.POST['busia_deaths']
        # busia_p_and_c_cases = request.POST['busia_p_and_c_cases']
        # busia_human_reference = request.POST['busia_human_reference']

        x = rvf_initial_collection.insert_one({
            # 'nairobi_male_population': nairobi_male_population,
            # 'nairobi_female_population': nairobi_female_population,
            # 'nairobi_intersex_population': nairobi_intersex_population,
            # 'nairobi_total_population': int(nairobi_male_population) + int(nairobi_female_population) + int(
            #     nairobi_intersex_population),
            # 'nairobi_outbreak_start_date': nairobi_outbreak_start_date,
            # 'nairobi_outbreak_stop_date': nairobi_outbreak_stop_date,
            # 'nairobi_deaths': nairobi_deaths,
            # 'nairobi_p_and_c_cases': nairobi_p_and_c_cases,
            # 'nairobi_human_reference': nairobi_human_reference,
            # 'nyandarua_male_population': nyandarua_male_population,
            # 'nyandarua_female_population': nyandarua_female_population,
            # 'nyandarua_intersex_population': nyandarua_intersex_population,
            # 'nyandarua_total_population': int(nyandarua_male_population) + int(nyandarua_female_population) + int(
            #     nyandarua_intersex_population),
            # 'nyandarua_outbreak_start_date': nyandarua_outbreak_start_date,
            # 'nyandarua_outbreak_stop_date': nyandarua_outbreak_stop_date,
            # 'nyandarua_deaths': nyandarua_deaths,
            # 'nyandarua_p_and_c_cases': nyandarua_p_and_c_cases,
            # 'nyandarua_human_reference': nyandarua_human_reference,
            # 'nyeri_male_population': nyeri_male_population,
            # 'nyeri_female_population': nyeri_female_population,
            # 'nyeri_intersex_population': nyeri_intersex_population,
            # 'nyeri_total_population': int(nyeri_male_population) + int(nyeri_female_population) + int(
            #     nyeri_intersex_population),
            # 'nyeri_outbreak_start_date': nyeri_outbreak_start_date,
            # 'nyeri_outbreak_stop_date': nyeri_outbreak_stop_date,
            # 'nyeri_deaths': nyeri_deaths,
            # 'nyeri_p_and_c_cases': nyeri_p_and_c_cases,
            # 'nyeri_human_reference': nyeri_human_reference,
            # 'kirinyaga_male_population': kirinyaga_male_population,
            # 'kirinyaga_female_population': kirinyaga_female_population,
            # 'kirinyaga_intersex_population': kirinyaga_intersex_population,
            # 'kirinyaga_total_population': int(kirinyaga_male_population) + int(kirinyaga_female_population) + int(
            #     kirinyaga_intersex_population),
            # 'kirinyaga_outbreak_start_date': kirinyaga_outbreak_start_date,
            # 'kirinyaga_outbreak_stop_date': kirinyaga_outbreak_stop_date,
            # 'kirinyaga_deaths': kirinyaga_deaths,
            # 'kirinyaga_p_and_c_cases': kirinyaga_p_and_c_cases,
            # 'kirinyaga_human_reference': kirinyaga_human_reference,
            # 'muranga_male_population': muranga_male_population,
            # 'muranga_female_population': muranga_female_population,
            # 'muranga_intersex_population': muranga_intersex_population,
            # 'muranga_total_population': int(muranga_male_population) + int(muranga_female_population) + int(
            #     muranga_intersex_population),
            # 'muranga_outbreak_start_date': muranga_outbreak_start_date,
            # 'muranga_outbreak_stop_date': muranga_outbreak_stop_date,
            # 'muranga_deaths': muranga_deaths,
            # 'muranga_p_and_c_cases': muranga_p_and_c_cases,
            # 'muranga_human_reference': muranga_human_reference,
            # 'kiambu_male_population': kiambu_male_population,
            # 'kiambu_female_population': kiambu_female_population,
            # 'kiambu_intersex_population': kiambu_intersex_population,
            # 'kiambu_total_population': int(kiambu_male_population) + int(kiambu_female_population) + int(
            #     kiambu_intersex_population),
            # 'kiambu_outbreak_start_date': kiambu_outbreak_start_date,
            # 'kiambu_outbreak_stop_date': kiambu_outbreak_stop_date,
            # 'kiambu_deaths': kiambu_deaths,
            # 'kiambu_p_and_c_cases': kiambu_p_and_c_cases,
            # 'kiambu_human_reference': kiambu_human_reference,
            # 'mombasa_male_population': mombasa_male_population,
            # 'mombasa_female_population': mombasa_female_population,
            # 'mombasa_intersex_population': mombasa_intersex_population,
            # 'mombasa_total_population': int(mombasa_male_population) + int(mombasa_female_population) + int(
            #     mombasa_intersex_population),
            # 'mombasa_outbreak_start_date': mombasa_outbreak_start_date,
            # 'mombasa_outbreak_stop_date': mombasa_outbreak_stop_date,
            # 'mombasa_deaths': mombasa_deaths,
            # 'mombasa_p_and_c_cases': mombasa_p_and_c_cases,
            # 'mombasa_human_reference': mombasa_human_reference,
            # 'kwale_male_population': kwale_male_population,
            # 'kwale_female_population': kwale_female_population,
            # 'kwale_intersex_population': kwale_intersex_population,
            # 'kwale_total_population': int(kwale_male_population) + int(kwale_female_population) + int(
            #     kwale_intersex_population),
            # 'kwale_outbreak_start_date': kwale_outbreak_start_date,
            # 'kwale_outbreak_stop_date': kwale_outbreak_stop_date,
            # 'kwale_deaths': kwale_deaths,
            # 'kwale_p_and_c_cases': kwale_p_and_c_cases,
            # 'kwale_human_reference': kwale_human_reference,
            # 'kilifi_male_population': kilifi_male_population,
            # 'kilifi_female_population': kilifi_female_population,
            # 'kilifi_intersex_population': kilifi_intersex_population,
            # 'kilifi_total_population': int(kilifi_male_population) + int(kilifi_female_population) + int(
            #     kilifi_intersex_population),
            # 'kilifi_outbreak_start_date': kilifi_outbreak_start_date,
            # 'kilifi_outbreak_stop_date': kilifi_outbreak_stop_date,
            # 'kilifi_deaths': kilifi_deaths,
            # 'kilifi_p_and_c_cases': kilifi_p_and_c_cases,
            # 'kilifi_human_reference': kilifi_human_reference,
            'tanariver_male_population': tanariver_male_population,
            'tanariver_female_population': tanariver_female_population,
            'tanariver_intersex_population': tanariver_intersex_population,
            'tanariver_total_population': int(tanariver_male_population) + int(tanariver_female_population) + int(
                tanariver_intersex_population),
            'tanariver_outbreak_start_date': tanariver_outbreak_start_date,
            'tanariver_outbreak_stop_date': tanariver_outbreak_stop_date,
            'tanariver_deaths': tanariver_deaths,
            'tanariver_p_and_c_cases': tanariver_p_and_c_cases,
            'tanariver_human_reference': tanariver_human_reference,
            # 'lamu_male_population': lamu_male_population,
            # 'lamu_female_population': lamu_female_population,
            # 'lamu_intersex_population': lamu_intersex_population,
            # 'lamu_total_population': int(lamu_male_population) + int(lamu_female_population) + int(
            #     lamu_intersex_population),
            # 'lamu_outbreak_start_date': lamu_outbreak_start_date,
            # 'lamu_outbreak_stop_date': lamu_outbreak_stop_date,
            # 'lamu_deaths': lamu_deaths,
            # 'lamu_p_and_c_cases': lamu_p_and_c_cases,
            # 'lamu_human_reference': lamu_human_reference,
            # 'taitataveta_male_population': taitataveta_male_population,
            # 'taitataveta_female_population': taitataveta_female_population,
            # 'taitataveta_intersex_population': taitataveta_intersex_population,
            # 'taitataveta_total_population': int(taitataveta_male_population) + int(taitataveta_female_population) + int(
            #     taitataveta_intersex_population),
            # 'taitataveta_outbreak_start_date': taitataveta_outbreak_start_date,
            # 'taitataveta_outbreak_stop_date': taitataveta_outbreak_stop_date,
            # 'taitataveta_deaths': taitataveta_deaths,
            # 'taitataveta_p_and_c_cases': taitataveta_p_and_c_cases,
            # 'taitataveta_human_reference': taitataveta_human_reference,
            'marsabit_male_population': marsabit_male_population,
            'marsabit_female_population': marsabit_female_population,
            'marsabit_intersex_population': marsabit_intersex_population,
            'marsabit_total_population': int(marsabit_male_population) + int(marsabit_female_population) + int(
                marsabit_intersex_population),
            'marsabit_outbreak_start_date': marsabit_outbreak_start_date,
            'marsabit_outbreak_stop_date': marsabit_outbreak_stop_date,
            'marsabit_deaths': marsabit_deaths,
            'marsabit_p_and_c_cases': marsabit_p_and_c_cases,
            'marsabit_human_reference': marsabit_human_reference,
            # 'isiolo_male_population': isiolo_male_population,
            # 'isiolo_female_population': isiolo_female_population,
            # 'isiolo_intersex_population': isiolo_intersex_population,
            # 'isiolo_total_population': int(isiolo_male_population) + int(isiolo_female_population) + int(
            #     isiolo_intersex_population),
            # 'isiolo_outbreak_start_date': isiolo_outbreak_start_date,
            # 'isiolo_outbreak_stop_date': isiolo_outbreak_stop_date,
            # 'isiolo_deaths': isiolo_deaths,
            # 'isiolo_p_and_c_cases': isiolo_p_and_c_cases,
            # 'isiolo_human_reference': isiolo_human_reference,
            # 'meru_male_population': meru_male_population,
            # 'meru_female_population': meru_female_population,
            # 'meru_intersex_population': meru_intersex_population,
            # 'meru_total_population': int(meru_male_population) + int(meru_female_population) + int(
            #     meru_intersex_population),
            # 'meru_outbreak_start_date': meru_outbreak_start_date,
            # 'meru_outbreak_stop_date': meru_outbreak_stop_date,
            # 'meru_deaths': meru_deaths,
            # 'meru_p_and_c_cases': meru_p_and_c_cases,
            # 'meru_human_reference': meru_human_reference,
            # 'tharaka_male_population': tharaka_male_population,
            # 'tharaka_female_population': tharaka_female_population,
            # 'tharaka_intersex_population': tharaka_intersex_population,
            # 'tharaka_total_population': int(tharaka_male_population) + int(tharaka_female_population) + int(
            #     tharaka_intersex_population),
            # 'tharaka_outbreak_start_date': tharaka_outbreak_start_date,
            # 'tharaka_outbreak_stop_date': tharaka_outbreak_stop_date,
            # 'tharaka_deaths': tharaka_deaths,
            # 'tharaka_p_and_c_cases': tharaka_p_and_c_cases,
            # 'tharaka_human_reference': tharaka_human_reference,
            # 'embu_male_population': embu_male_population,
            # 'embu_female_population': embu_female_population,
            # 'embu_intersex_population': embu_intersex_population,
            # 'embu_total_population': int(embu_male_population) + int(embu_female_population) + int(
            #     embu_intersex_population),
            # 'embu_outbreak_start_date': embu_outbreak_start_date,
            # 'embu_outbreak_stop_date': embu_outbreak_stop_date,
            # 'embu_deaths': embu_deaths,
            # 'embu_p_and_c_cases': embu_p_and_c_cases,
            # 'embu_human_reference': embu_human_reference,
            # 'kitui_male_population': kitui_male_population,
            # 'kitui_female_population': kitui_female_population,
            # 'kitui_intersex_population': kitui_intersex_population,
            # 'kitui_total_population': int(kitui_male_population) + int(kitui_female_population) + int(
            #     kitui_intersex_population),
            # 'kitui_outbreak_start_date': kitui_outbreak_start_date,
            # 'kitui_outbreak_stop_date': kitui_outbreak_stop_date,
            # 'kitui_deaths': kitui_deaths,
            # 'kitui_p_and_c_cases': kitui_p_and_c_cases,
            # 'kitui_human_reference': kitui_human_reference,
            # 'machakos_male_population': machakos_male_population,
            # 'machakos_female_population': machakos_female_population,
            # 'machakos_intersex_population': machakos_intersex_population,
            # 'machakos_total_population': int(machakos_male_population) + int(machakos_female_population) + int(
            #     machakos_intersex_population),
            # 'machakos_outbreak_start_date': machakos_outbreak_start_date,
            # 'machakos_outbreak_stop_date': machakos_outbreak_stop_date,
            # 'machakos_deaths': machakos_deaths,
            # 'machakos_p_and_c_cases': machakos_p_and_c_cases,
            # 'machakos_human_reference': machakos_human_reference,
            # 'makueni_male_population': makueni_male_population,
            # 'makueni_female_population': makueni_female_population,
            # 'makueni_intersex_population': makueni_intersex_population,
            # 'makueni_total_population': int(makueni_male_population) + int(makueni_female_population) + int(
            #     makueni_intersex_population),
            # 'makueni_outbreak_start_date': makueni_outbreak_start_date,
            # 'makueni_outbreak_stop_date': makueni_outbreak_stop_date,
            # 'makueni_deaths': makueni_deaths,
            # 'makueni_p_and_c_cases': makueni_p_and_c_cases,
            # 'makueni_human_reference': makueni_human_reference,
            'garissa_male_population': garissa_male_population,
            'garissa_female_population': garissa_female_population,
            'garissa_intersex_population': garissa_intersex_population,
            'garissa_total_population': int(garissa_male_population) + int(garissa_female_population) + int(
                garissa_intersex_population),
            'garissa_outbreak_start_date': garissa_outbreak_start_date,
            'garissa_outbreak_stop_date': garissa_outbreak_stop_date,
            'garissa_deaths': garissa_deaths,
            'garissa_p_and_c_cases': garissa_p_and_c_cases,
            'garissa_human_reference': garissa_human_reference,
            'wajir_male_population': wajir_male_population,
            'wajir_female_population': wajir_female_population,
            'wajir_intersex_population': wajir_intersex_population,
            'wajir_total_population': int(wajir_male_population) + int(wajir_female_population) + int(
                wajir_intersex_population),
            'wajir_outbreak_start_date': wajir_outbreak_start_date,
            'wajir_outbreak_stop_date': wajir_outbreak_stop_date,
            'wajir_deaths': wajir_deaths,
            'wajir_p_and_c_cases': wajir_p_and_c_cases,
            'wajir_human_reference': wajir_human_reference,
            # 'mandera_male_population': mandera_male_population,
            # 'mandera_female_population': mandera_female_population,
            # 'mandera_intersex_population': mandera_intersex_population,
            # 'mandera_total_population': int(mandera_male_population) + int(mandera_female_population) + int(
            #     mandera_intersex_population),
            # 'mandera_outbreak_start_date': mandera_outbreak_start_date,
            # 'mandera_outbreak_stop_date': mandera_outbreak_stop_date,
            # 'mandera_deaths': mandera_deaths,
            # 'mandera_p_and_c_cases': mandera_p_and_c_cases,
            # 'mandera_human_reference': mandera_human_reference,
            # 'siaya_male_population': siaya_male_population,
            # 'siaya_female_population': siaya_female_population,
            # 'siaya_intersex_population': siaya_intersex_population,
            # 'siaya_total_population': int(siaya_male_population) + int(siaya_female_population) + int(
            #     siaya_intersex_population),
            # 'siaya_outbreak_start_date': siaya_outbreak_start_date,
            # 'siaya_outbreak_stop_date': siaya_outbreak_stop_date,
            # 'siaya_deaths': siaya_deaths,
            # 'siaya_p_and_c_cases': siaya_p_and_c_cases,
            # 'siaya_human_reference': siaya_human_reference,
            # 'kisumu_male_population': kisumu_male_population,
            # 'kisumu_female_population': kisumu_female_population,
            # 'kisumu_intersex_population': kisumu_intersex_population,
            # 'kisumu_total_population': int(kisumu_male_population) + int(kisumu_female_population) + int(
            #     kisumu_intersex_population),
            # 'kisumu_outbreak_start_date': kisumu_outbreak_start_date,
            # 'kisumu_outbreak_stop_date': kisumu_outbreak_stop_date,
            # 'kisumu_deaths': kisumu_deaths,
            # 'kisumu_p_and_c_cases': kisumu_p_and_c_cases,
            # 'kisumu_human_reference': kisumu_human_reference,
            # 'homabay_male_population': homabay_male_population,
            # 'homabay_female_population': homabay_female_population,
            # 'homabay_intersex_population': homabay_intersex_population,
            # 'homabay_total_population': int(homabay_male_population) + int(homabay_female_population) + int(
            #     homabay_intersex_population),
            # 'homabay_outbreak_start_date': homabay_outbreak_start_date,
            # 'homabay_outbreak_stop_date': homabay_outbreak_stop_date,
            # 'homabay_deaths': homabay_deaths,
            # 'homabay_p_and_c_cases': homabay_p_and_c_cases,
            # 'homabay_human_reference': homabay_human_reference,
            # 'migori_male_population': migori_male_population,
            # 'migori_female_population': migori_female_population,
            # 'migori_intersex_population': migori_intersex_population,
            # 'migori_total_population': int(migori_male_population) + int(migori_female_population) + int(
            #     migori_intersex_population),
            # 'migori_outbreak_start_date': migori_outbreak_start_date,
            # 'migori_outbreak_stop_date': migori_outbreak_stop_date,
            # 'migori_deaths': migori_deaths,
            # 'migori_p_and_c_cases': migori_p_and_c_cases,
            # 'migori_human_reference': migori_human_reference,
            # 'kisii_male_population': kisii_male_population,
            # 'kisii_female_population': kisii_female_population,
            # 'kisii_intersex_population': kisii_intersex_population,
            # 'kisii_total_population': int(kisii_male_population) + int(kisii_female_population) + int(
            #     kisii_intersex_population),
            # 'kisii_outbreak_start_date': kisii_outbreak_start_date,
            # 'kisii_outbreak_stop_date': kisii_outbreak_stop_date,
            # 'kisii_deaths': kisii_deaths,
            # 'kisii_p_and_c_cases': kisii_p_and_c_cases,
            # 'kisii_human_reference': kisii_human_reference,
            # 'nyamira_male_population': nyamira_male_population,
            # 'nyamira_female_population': nyamira_female_population,
            # 'nyamira_intersex_population': nyamira_intersex_population,
            # 'nyamira_total_population': int(nyamira_male_population) + int(nyamira_female_population) + int(
            #     nyamira_intersex_population),
            # 'nyamira_outbreak_start_date': nyamira_outbreak_start_date,
            # 'nyamira_outbreak_stop_date': nyamira_outbreak_stop_date,
            # 'nyamira_deaths': nyamira_deaths,
            # 'nyamira_p_and_c_cases': nyamira_p_and_c_cases,
            # 'nyamira_human_reference': nyamira_human_reference,
            # 'turkana_male_population': turkana_male_population,
            # 'turkana_female_population': turkana_female_population,
            # 'turkana_intersex_population': turkana_intersex_population,
            # 'turkana_total_population': int(turkana_male_population) + int(turkana_female_population) + int(
            #     turkana_intersex_population),
            # 'turkana_outbreak_start_date': turkana_outbreak_start_date,
            # 'turkana_outbreak_stop_date': turkana_outbreak_stop_date,
            # 'turkana_deaths': turkana_deaths,
            # 'turkana_p_and_c_cases': turkana_p_and_c_cases,
            # 'turkana_human_reference': turkana_human_reference,
            # 'westpokot_male_population': westpokot_male_population,
            # 'westpokot_female_population': westpokot_female_population,
            # 'westpokot_intersex_population': westpokot_intersex_population,
            # 'westpokot_total_population': int(westpokot_male_population) + int(westpokot_female_population) + int(
            #     westpokot_intersex_population),
            # 'westpokot_outbreak_start_date': westpokot_outbreak_start_date,
            # 'westpokot_outbreak_stop_date': westpokot_outbreak_stop_date,
            # 'westpokot_deaths': westpokot_deaths,
            # 'westpokot_p_and_c_cases': westpokot_p_and_c_cases,
            # 'westpokot_human_reference': westpokot_human_reference,
            # 'samburu_male_population': samburu_male_population,
            # 'samburu_female_population': samburu_female_population,
            # 'samburu_intersex_population': samburu_intersex_population,
            # 'samburu_total_population': int(samburu_male_population) + int(samburu_female_population) + int(
            #     samburu_intersex_population),
            # 'samburu_outbreak_start_date': samburu_outbreak_start_date,
            # 'samburu_outbreak_stop_date': samburu_outbreak_stop_date,
            # 'samburu_deaths': samburu_deaths,
            # 'samburu_p_and_c_cases': samburu_p_and_c_cases,
            # 'samburu_human_reference': samburu_human_reference,
            # 'transnzoia_male_population': transnzoia_male_population,
            # 'transnzoia_female_population': transnzoia_female_population,
            # 'transnzoia_intersex_population': transnzoia_intersex_population,
            # 'transnzoia_total_population': int(transnzoia_male_population) + int(transnzoia_female_population) + int(
            #     transnzoia_intersex_population),
            # 'transnzoia_outbreak_start_date': transnzoia_outbreak_start_date,
            # 'transnzoia_outbreak_stop_date': transnzoia_outbreak_stop_date,
            # 'transnzoia_deaths': transnzoia_deaths,
            # 'transnzoia_p_and_c_cases': transnzoia_p_and_c_cases,
            # 'transnzoia_human_reference': transnzoia_human_reference,
            'baringo_male_population': baringo_male_population,
            'baringo_female_population': baringo_female_population,
            'baringo_intersex_population': baringo_intersex_population,
            'baringo_total_population': int(baringo_male_population) + int(baringo_female_population) + int(
                baringo_intersex_population),
            'baringo_outbreak_start_date': baringo_outbreak_start_date,
            'baringo_outbreak_stop_date': baringo_outbreak_stop_date,
            'baringo_deaths': baringo_deaths,
            'baringo_p_and_c_cases': baringo_p_and_c_cases,
            'baringo_human_reference': baringo_human_reference,
            # 'uasingishu_male_population': uasingishu_male_population,
            # 'uasingishu_female_population': uasingishu_female_population,
            # 'uasingishu_intersex_population': uasingishu_intersex_population,
            # 'uasingishu_total_population': int(uasingishu_male_population) + int(uasingishu_female_population) + int(
            #     uasingishu_intersex_population),
            # 'uasingishu_outbreak_start_date': uasingishu_outbreak_start_date,
            # 'uasingishu_outbreak_stop_date': uasingishu_outbreak_stop_date,
            # 'uasingishu_deaths': uasingishu_deaths,
            # 'uasingishu_p_and_c_cases': uasingishu_p_and_c_cases,
            # 'uasingishu_human_reference': uasingishu_human_reference,
            # 'elgeyomarakwet_male_population': elgeyomarakwet_male_population,
            # 'elgeyomarakwet_female_population': elgeyomarakwet_female_population,
            # 'elgeyomarakwet_intersex_population': elgeyomarakwet_intersex_population,
            # 'elgeyomarakwet_total_population': int(elgeyomarakwet_male_population) + int(
            #     elgeyomarakwet_female_population) + int(elgeyomarakwet_intersex_population),
            # 'elgeyomarakwet_outbreak_start_date': elgeyomarakwet_outbreak_start_date,
            # 'elgeyomarakwet_outbreak_stop_date': elgeyomarakwet_outbreak_stop_date,
            # 'elgeyomarakwet_deaths': elgeyomarakwet_deaths,
            # 'elgeyomarakwet_p_and_c_cases': elgeyomarakwet_p_and_c_cases,
            # 'elgeyomarakwet_human_reference': elgeyomarakwet_human_reference,
            # 'nandi_male_population': nandi_male_population,
            # 'nandi_female_population': nandi_female_population,
            # 'nandi_intersex_population': nandi_intersex_population,
            # 'nandi_total_population': int(nandi_male_population) + int(nandi_female_population) + int(
            #     nandi_intersex_population),
            # 'nandi_outbreak_start_date': nandi_outbreak_start_date,
            # 'nandi_outbreak_stop_date': nandi_outbreak_stop_date,
            # 'nandi_deaths': nandi_deaths,
            # 'nandi_p_and_c_cases': nandi_p_and_c_cases,
            # 'nandi_human_reference': nandi_human_reference,
            # 'laikipia_male_population': laikipia_male_population,
            # 'laikipia_female_population': laikipia_female_population,
            # 'laikipia_intersex_population': laikipia_intersex_population,
            # 'laikipia_total_population': int(laikipia_male_population) + int(laikipia_female_population) + int(
            #     laikipia_intersex_population),
            # 'laikipia_outbreak_start_date': laikipia_outbreak_start_date,
            # 'laikipia_outbreak_stop_date': laikipia_outbreak_stop_date,
            # 'laikipia_deaths': laikipia_deaths,
            # 'laikipia_p_and_c_cases': laikipia_p_and_c_cases,
            # 'laikipia_human_reference': laikipia_human_reference,
            # 'nakuru_male_population': nakuru_male_population,
            # 'nakuru_female_population': nakuru_female_population,
            # 'nakuru_intersex_population': nakuru_intersex_population,
            # 'nakuru_total_population': int(nakuru_male_population) + int(nakuru_female_population) + int(
            #     nakuru_intersex_population),
            # 'nakuru_outbreak_start_date': nakuru_outbreak_start_date,
            # 'nakuru_outbreak_stop_date': nakuru_outbreak_stop_date,
            # 'nakuru_deaths': nakuru_deaths,
            # 'nakuru_p_and_c_cases': nakuru_p_and_c_cases,
            # 'nakuru_human_reference': nakuru_human_reference,
            # 'narok_male_population': narok_male_population,
            # 'narok_female_population': narok_female_population,
            # 'narok_intersex_population': narok_intersex_population,
            # 'narok_total_population': int(narok_male_population) + int(narok_female_population) + int(
            #     narok_intersex_population),
            # 'narok_outbreak_start_date': narok_outbreak_start_date,
            # 'narok_outbreak_stop_date': narok_outbreak_stop_date,
            # 'narok_deaths': narok_deaths,
            # 'narok_p_and_c_cases': narok_p_and_c_cases,
            # 'narok_human_reference': narok_human_reference,
            # 'kajiado_male_population': kajiado_male_population,
            # 'kajiado_female_population': kajiado_female_population,
            # 'kajiado_intersex_population': kajiado_intersex_population,
            # 'kajiado_total_population': int(kajiado_male_population) + int(kajiado_female_population) + int(
            #     kajiado_intersex_population),
            # 'kajiado_outbreak_start_date': kajiado_outbreak_start_date,
            # 'kajiado_outbreak_stop_date': kajiado_outbreak_stop_date,
            # 'kajiado_deaths': kajiado_deaths,
            # 'kajiado_p_and_c_cases': kajiado_p_and_c_cases,
            # 'kajiado_human_reference': kajiado_human_reference,
            # 'kericho_male_population': kericho_male_population,
            # 'kericho_female_population': kericho_female_population,
            # 'kericho_intersex_population': kericho_intersex_population,
            # 'kericho_total_population': int(kericho_male_population) + int(kericho_female_population) + int(
            #     kericho_intersex_population),
            # 'kericho_outbreak_start_date': kericho_outbreak_start_date,
            # 'kericho_outbreak_stop_date': kericho_outbreak_stop_date,
            # 'kericho_deaths': kericho_deaths,
            # 'kericho_p_and_c_cases': kericho_p_and_c_cases,
            # 'kericho_human_reference': kericho_human_reference,
            # 'bomet_male_population': bomet_male_population,
            # 'bomet_female_population': bomet_female_population,
            # 'bomet_intersex_population': bomet_intersex_population,
            # 'bomet_total_population': int(bomet_male_population) + int(bomet_female_population) + int(
            #     bomet_intersex_population),
            # 'bomet_outbreak_start_date': bomet_outbreak_start_date,
            # 'bomet_outbreak_stop_date': bomet_outbreak_stop_date,
            # 'bomet_deaths': bomet_deaths,
            # 'bomet_p_and_c_cases': bomet_p_and_c_cases,
            # 'bomet_human_reference': bomet_human_reference,
            # 'kakamega_male_population': kakamega_male_population,
            # 'kakamega_female_population': kakamega_female_population,
            # 'kakamega_intersex_population': kakamega_intersex_population,
            # 'kakamega_total_population': int(kakamega_male_population) + int(kakamega_female_population) + int(
            #     kakamega_intersex_population),
            # 'kakamega_outbreak_start_date': kakamega_outbreak_start_date,
            # 'kakamega_outbreak_stop_date': kakamega_outbreak_stop_date,
            # 'kakamega_deaths': kakamega_deaths,
            # 'kakamega_p_and_c_cases': kakamega_p_and_c_cases,
            # 'kakamega_human_reference': kakamega_human_reference,
            # 'vihiga_male_population': vihiga_male_population,
            # 'vihiga_female_population': vihiga_female_population,
            # 'vihiga_intersex_population': vihiga_intersex_population,
            # 'vihiga_total_population': int(vihiga_male_population) + int(vihiga_female_population) + int(
            #     vihiga_intersex_population),
            # 'vihiga_outbreak_start_date': vihiga_outbreak_start_date,
            # 'vihiga_outbreak_stop_date': vihiga_outbreak_stop_date,
            # 'vihiga_deaths': vihiga_deaths,
            # 'vihiga_p_and_c_cases': vihiga_p_and_c_cases,
            # 'vihiga_human_reference': vihiga_human_reference,
            # 'bungoma_male_population': bungoma_male_population,
            # 'bungoma_female_population': bungoma_female_population,
            # 'bungoma_intersex_population': bungoma_intersex_population,
            # 'bungoma_total_population': int(bungoma_male_population) + int(bungoma_female_population) + int(
            #     bungoma_intersex_population),
            # 'bungoma_outbreak_start_date': bungoma_outbreak_start_date,
            # 'bungoma_outbreak_stop_date': bungoma_outbreak_stop_date,
            # 'bungoma_deaths': bungoma_deaths,
            # 'bungoma_p_and_c_cases': bungoma_p_and_c_cases,
            # 'bungoma_human_reference': bungoma_human_reference,
            # 'busia_male_population': busia_male_population,
            # 'busia_female_population': busia_female_population,
            # 'busia_intersex_population': busia_intersex_population,
            # 'busia_total_population': int(busia_male_population) + int(busia_female_population) + int(
            #     busia_intersex_population),
            # 'busia_outbreak_start_date': busia_outbreak_start_date,
            # 'busia_outbreak_stop_date': busia_outbreak_stop_date,
            # 'busia_deaths': busia_deaths,
            # 'busia_p_and_c_cases': busia_p_and_c_cases,
            # 'busia_human_reference': busia_human_reference,
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        # 'nairobi_male_population': context['nairobi_male_population'],
        # 'nairobi_female_population': context['nairobi_female_population'],
        # 'nairobi_intersex_population': context['nairobi_intersex_population'],
        # 'nairobi_total_population': int(context['nairobi_male_population']) + int(context['nairobi_female_population']) + int(context['nairobi_intersex_population']),
        # 'nairobi_outbreak_start_date': context['nairobi_outbreak_start_date'],
        # 'nairobi_outbreak_stop_date': context['nairobi_outbreak_stop_date'],
        # 'nairobi_deaths': context['nairobi_deaths'],
        # 'nairobi_p_and_c_cases': context['nairobi_p_and_c_cases'],
        # 'nairobi_human_reference': context['nairobi_human_reference'],
        # 'nyandarua_male_population': context['nyandarua_male_population'],
        # 'nyandarua_female_population': context['nyandarua_female_population'],
        # 'nyandarua_intersex_population': context['nyandarua_intersex_population'],
        # 'nyandarua_total_population': int(context['nyandarua_male_population']) + int(context['nyandarua_female_population']) + int(context['nyandarua_intersex_population']),
        # 'nyandarua_outbreak_start_date': context['nyandarua_outbreak_start_date'],
        # 'nyandarua_outbreak_stop_date': context['nyandarua_outbreak_stop_date'],
        # 'nyandarua_deaths': context['nyandarua_deaths'],
        # 'nyandarua_p_and_c_cases': context['nyandarua_p_and_c_cases'],
        # 'nyandarua_human_reference': context['nyandarua_human_reference'],
        # 'nyeri_male_population': context['nyeri_male_population'],
        # 'nyeri_female_population': context['nyeri_female_population'],
        # 'nyeri_intersex_population': context['nyeri_intersex_population'],
        # 'nyeri_total_population': int(context['nyeri_male_population']) + int(context['nyeri_female_population']) + int(context['nyeri_intersex_population']),
        # 'nyeri_outbreak_start_date': context['nyeri_outbreak_start_date'],
        # 'nyeri_outbreak_stop_date': context['nyeri_outbreak_stop_date'],
        # 'nyeri_deaths': context['nyeri_deaths'],
        # 'nyeri_p_and_c_cases': context['nyeri_p_and_c_cases'],
        # 'nyeri_human_reference': context['nyeri_human_reference'],
        # 'kirinyaga_male_population': context['kirinyaga_male_population'],
        # 'kirinyaga_female_population': context['kirinyaga_female_population'],
        # 'kirinyaga_intersex_population': context['kirinyaga_intersex_population'],
        # 'kirinyaga_total_population': int(context['kirinyaga_male_population']) + int(context['kirinyaga_female_population']) + int(context['kirinyaga_intersex_population']),
        # 'kirinyaga_outbreak_start_date': context['kirinyaga_outbreak_start_date'],
        # 'kirinyaga_outbreak_stop_date': context['kirinyaga_outbreak_stop_date'],
        # 'kirinyaga_deaths': context['kirinyaga_deaths'],
        # 'kirinyaga_p_and_c_cases': context['kirinyaga_p_and_c_cases'],
        # 'kirinyaga_human_reference': context['kirinyaga_human_reference'],
        # 'muranga_male_population': context['muranga_male_population'],
        # 'muranga_female_population': context['muranga_female_population'],
        # 'muranga_intersex_population': context['muranga_intersex_population'],
        # 'muranga_total_population': int(context['muranga_male_population']) + int(context['muranga_female_population']) + int(context['muranga_intersex_population']),
        # 'muranga_outbreak_start_date': context['muranga_outbreak_start_date'],
        # 'muranga_outbreak_stop_date': context['muranga_outbreak_stop_date'],
        # 'muranga_deaths': context['muranga_deaths'],
        # 'muranga_p_and_c_cases': context['muranga_p_and_c_cases'],
        # 'muranga_human_reference': context['muranga_human_reference'],
        # 'kiambu_male_population': context['kiambu_male_population'],
        # 'kiambu_female_population': context['kiambu_female_population'],
        # 'kiambu_intersex_population': context['kiambu_intersex_population'],
        # 'kiambu_total_population': int(context['kiambu_male_population']) + int(context['kiambu_female_population']) + int(context['kiambu_intersex_population']),
        # 'kiambu_outbreak_start_date': context['kiambu_outbreak_start_date'],
        # 'kiambu_outbreak_stop_date': context['kiambu_outbreak_stop_date'],
        # 'kiambu_deaths': context['kiambu_deaths'],
        # 'kiambu_p_and_c_cases': context['kiambu_p_and_c_cases'],
        # 'kiambu_human_reference': context['kiambu_human_reference'],
        # 'mombasa_male_population': context['mombasa_male_population'],
        # 'mombasa_female_population': context['mombasa_female_population'],
        # 'mombasa_intersex_population': context['mombasa_intersex_population'],
        # 'mombasa_total_population': int(context['mombasa_male_population']) + int(context['mombasa_female_population']) + int(context['mombasa_intersex_population']),
        # 'mombasa_outbreak_start_date': context['mombasa_outbreak_start_date'],
        # 'mombasa_outbreak_stop_date': context['mombasa_outbreak_stop_date'],
        # 'mombasa_deaths': context['mombasa_deaths'],
        # 'mombasa_p_and_c_cases': context['mombasa_p_and_c_cases'],
        # 'mombasa_human_reference': context['mombasa_human_reference'],
        # 'kwale_male_population': context['kwale_male_population'],
        # 'kwale_female_population': context['kwale_female_population'],
        # 'kwale_intersex_population': context['kwale_intersex_population'],
        # 'kwale_total_population': int(context['kwale_male_population']) + int(context['kwale_female_population']) + int(context['kwale_intersex_population']),
        # 'kwale_outbreak_start_date': context['kwale_outbreak_start_date'],
        # 'kwale_outbreak_stop_date': context['kwale_outbreak_stop_date'],
        # 'kwale_deaths': context['kwale_deaths'],
        # 'kwale_p_and_c_cases': context['kwale_p_and_c_cases'],
        # 'kwale_human_reference': context['kwale_human_reference'],
        # 'kilifi_male_population': context['kilifi_male_population'],
        # 'kilifi_female_population': context['kilifi_female_population'],
        # 'kilifi_intersex_population': context['kilifi_intersex_population'],
        # 'kilifi_total_population': int(context['kilifi_male_population']) + int(context['kilifi_female_population']) + int(context['kilifi_intersex_population']),
        # 'kilifi_outbreak_start_date': context['kilifi_outbreak_start_date'],
        # 'kilifi_outbreak_stop_date': context['kilifi_outbreak_stop_date'],
        # 'kilifi_deaths': context['kilifi_deaths'],
        # 'kilifi_p_and_c_cases': context['kilifi_p_and_c_cases'],
        # 'kilifi_human_reference': context['kilifi_human_reference'],
        'tanariver_male_population': context['tanariver_male_population'],
        'tanariver_female_population': context['tanariver_female_population'],
        'tanariver_intersex_population': context['tanariver_intersex_population'],
        'tanariver_total_population': int(context['tanariver_male_population']) + int(context['tanariver_female_population']) + int(context['tanariver_intersex_population']),
        'tanariver_outbreak_start_date': context['tanariver_outbreak_start_date'],
        'tanariver_outbreak_stop_date': context['tanariver_outbreak_stop_date'],
        'tanariver_deaths': context['tanariver_deaths'],
        'tanariver_p_and_c_cases': context['tanariver_p_and_c_cases'],
        'tanariver_human_reference': context['tanariver_human_reference'],
        # 'lamu_male_population': context['lamu_male_population'],
        # 'lamu_female_population': context['lamu_female_population'],
        # 'lamu_intersex_population': context['lamu_intersex_population'],
        # 'lamu_total_population': int(context['lamu_male_population']) + int(context['lamu_female_population']) + int(context['lamu_intersex_population']),
        # 'lamu_outbreak_start_date': context['lamu_outbreak_start_date'],
        # 'lamu_outbreak_stop_date': context['lamu_outbreak_stop_date'],
        # 'lamu_deaths': context['lamu_deaths'],
        # 'lamu_p_and_c_cases': context['lamu_p_and_c_cases'],
        # 'lamu_human_reference': context['lamu_human_reference'],
        # 'taitataveta_male_population': context['taitataveta_male_population'],
        # 'taitataveta_female_population': context['taitataveta_female_population'],
        # 'taitataveta_intersex_population': context['taitataveta_intersex_population'],
        # 'taitataveta_total_population': int(context['taitataveta_male_population']) + int(context['taitataveta_female_population']) + int(context['taitataveta_intersex_population']),
        # 'taitataveta_outbreak_start_date': context['taitataveta_outbreak_start_date'],
        # 'taitataveta_outbreak_stop_date': context['taitataveta_outbreak_stop_date'],
        # 'taitataveta_deaths': context['taitataveta_deaths'],
        # 'taitataveta_p_and_c_cases': context['taitataveta_p_and_c_cases'],
        # 'taitataveta_human_reference': context['taitataveta_human_reference'],
        'marsabit_male_population': context['marsabit_male_population'],
        'marsabit_female_population': context['marsabit_female_population'],
        'marsabit_intersex_population': context['marsabit_intersex_population'],
        'marsabit_total_population': int(context['marsabit_male_population']) + int(context['marsabit_female_population']) + int(context['marsabit_intersex_population']),
        'marsabit_outbreak_start_date': context['marsabit_outbreak_start_date'],
        'marsabit_outbreak_stop_date': context['marsabit_outbreak_stop_date'],
        'marsabit_deaths': context['marsabit_deaths'],
        'marsabit_p_and_c_cases': context['marsabit_p_and_c_cases'],
        'marsabit_human_reference': context['marsabit_human_reference'],
        # 'isiolo_male_population': context['isiolo_male_population'],
        # 'isiolo_female_population': context['isiolo_female_population'],
        # 'isiolo_intersex_population': context['isiolo_intersex_population'],
        # 'isiolo_total_population': int(context['isiolo_male_population']) + int(context['isiolo_female_population']) + int(context['isiolo_intersex_population']),
        # 'isiolo_outbreak_start_date': context['isiolo_outbreak_start_date'],
        # 'isiolo_outbreak_stop_date': context['isiolo_outbreak_stop_date'],
        # 'isiolo_deaths': context['isiolo_deaths'],
        # 'isiolo_p_and_c_cases': context['isiolo_p_and_c_cases'],
        # 'isiolo_human_reference': context['isiolo_human_reference'],
        # 'meru_male_population': context['meru_male_population'],
        # 'meru_female_population': context['meru_female_population'],
        # 'meru_intersex_population': context['meru_intersex_population'],
        # 'meru_total_population': int(context['meru_male_population']) + int(context['meru_female_population']) + int(context['meru_intersex_population']),
        # 'meru_outbreak_start_date': context['meru_outbreak_start_date'],
        # 'meru_outbreak_stop_date': context['meru_outbreak_stop_date'],
        # 'meru_deaths': context['meru_deaths'],
        # 'meru_p_and_c_cases': context['meru_p_and_c_cases'],
        # 'meru_human_reference': context['meru_human_reference'],
        # 'tharaka_male_population': context['tharaka_male_population'],
        # 'tharaka_female_population': context['tharaka_female_population'],
        # 'tharaka_intersex_population': context['tharaka_intersex_population'],
        # 'tharaka_total_population': int(context['tharaka_male_population']) + int(context['tharaka_female_population']) + int(context['tharaka_intersex_population']),
        # 'tharaka_outbreak_start_date': context['tharaka_outbreak_start_date'],
        # 'tharaka_outbreak_stop_date': context['tharaka_outbreak_stop_date'],
        # 'tharaka_deaths': context['tharaka_deaths'],
        # 'tharaka_p_and_c_cases': context['tharaka_p_and_c_cases'],
        # 'tharaka_human_reference': context['tharaka_human_reference'],
        # 'embu_male_population': context['embu_male_population'],
        # 'embu_female_population': context['embu_female_population'],
        # 'embu_intersex_population': context['embu_intersex_population'],
        # 'embu_total_population': int(context['embu_male_population']) + int(context['embu_female_population']) + int(context['embu_intersex_population']),
        # 'embu_outbreak_start_date': context['embu_outbreak_start_date'],
        # 'embu_outbreak_stop_date': context['embu_outbreak_stop_date'],
        # 'embu_deaths': context['embu_deaths'],
        # 'embu_p_and_c_cases': context['embu_p_and_c_cases'],
        # 'embu_human_reference': context['embu_human_reference'],
        # 'kitui_male_population': context['kitui_male_population'],
        # 'kitui_female_population': context['kitui_female_population'],
        # 'kitui_intersex_population': context['kitui_intersex_population'],
        # 'kitui_total_population': int(context['kitui_male_population']) + int(context['kitui_female_population']) + int(context['kitui_intersex_population']),
        # 'kitui_outbreak_start_date': context['kitui_outbreak_start_date'],
        # 'kitui_outbreak_stop_date': context['kitui_outbreak_stop_date'],
        # 'kitui_deaths': context['kitui_deaths'],
        # 'kitui_p_and_c_cases': context['kitui_p_and_c_cases'],
        # 'kitui_human_reference': context['kitui_human_reference'],
        # 'machakos_male_population': context['machakos_male_population'],
        # 'machakos_female_population': context['machakos_female_population'],
        # 'machakos_intersex_population': context['machakos_intersex_population'],
        # 'machakos_total_population': int(context['machakos_male_population']) + int(context['machakos_female_population']) + int(context['machakos_intersex_population']),
        # 'machakos_outbreak_start_date': context['machakos_outbreak_start_date'],
        # 'machakos_outbreak_stop_date': context['machakos_outbreak_stop_date'],
        # 'machakos_deaths': context['machakos_deaths'],
        # 'machakos_p_and_c_cases': context['machakos_p_and_c_cases'],
        # 'machakos_human_reference': context['machakos_human_reference'],
        # 'makueni_male_population': context['makueni_male_population'],
        # 'makueni_female_population': context['makueni_female_population'],
        # 'makueni_intersex_population': context['makueni_intersex_population'],
        # 'makueni_total_population': int(context['makueni_male_population']) + int(context['makueni_female_population']) + int(context['makueni_intersex_population']),
        # 'makueni_outbreak_start_date': context['makueni_outbreak_start_date'],
        # 'makueni_outbreak_stop_date': context['makueni_outbreak_stop_date'],
        # 'makueni_deaths': context['makueni_deaths'],
        # 'makueni_p_and_c_cases': context['makueni_p_and_c_cases'],
        # 'makueni_human_reference': context['makueni_human_reference'],
        'garissa_male_population': context['garissa_male_population'],
        'garissa_female_population': context['garissa_female_population'],
        'garissa_intersex_population': context['garissa_intersex_population'],
        'garissa_total_population': int(context['garissa_male_population']) + int(context['garissa_female_population']) + int(context['garissa_intersex_population']),
        'garissa_outbreak_start_date': context['garissa_outbreak_start_date'],
        'garissa_outbreak_stop_date': context['garissa_outbreak_stop_date'],
        'garissa_deaths': context['garissa_deaths'],
        'garissa_p_and_c_cases': context['garissa_p_and_c_cases'],
        'garissa_human_reference': context['garissa_human_reference'],
        'wajir_male_population': context['wajir_male_population'],
        'wajir_female_population': context['wajir_female_population'],
        'wajir_intersex_population': context['wajir_intersex_population'],
        'wajir_total_population': int(context['wajir_male_population']) + int(context['wajir_female_population']) + int(context['wajir_intersex_population']),
        'wajir_outbreak_start_date': context['wajir_outbreak_start_date'],
        'wajir_outbreak_stop_date': context['wajir_outbreak_stop_date'],
        'wajir_deaths': context['wajir_deaths'],
        'wajir_p_and_c_cases': context['wajir_p_and_c_cases'],
        'wajir_human_reference': context['wajir_human_reference'],
        # 'mandera_male_population': context['mandera_male_population'],
        # 'mandera_female_population': context['mandera_female_population'],
        # 'mandera_intersex_population': context['mandera_intersex_population'],
        # 'mandera_total_population': int(context['mandera_male_population']) + int(context['mandera_female_population']) + int(context['mandera_intersex_population']),
        # 'mandera_outbreak_start_date': context['mandera_outbreak_start_date'],
        # 'mandera_outbreak_stop_date': context['mandera_outbreak_stop_date'],
        # 'mandera_deaths': context['mandera_deaths'],
        # 'mandera_p_and_c_cases': context['mandera_p_and_c_cases'],
        # 'mandera_human_reference': context['mandera_human_reference'],
        # 'siaya_male_population': context['siaya_male_population'],
        # 'siaya_female_population': context['siaya_female_population'],
        # 'siaya_intersex_population': context['siaya_intersex_population'],
        # 'siaya_total_population': int(context['siaya_male_population']) + int(context['siaya_female_population']) + int(context['siaya_intersex_population']),
        # 'siaya_outbreak_start_date': context['siaya_outbreak_start_date'],
        # 'siaya_outbreak_stop_date': context['siaya_outbreak_stop_date'],
        # 'siaya_deaths': context['siaya_deaths'],
        # 'siaya_p_and_c_cases': context['siaya_p_and_c_cases'],
        # 'siaya_human_reference': context['siaya_human_reference'],
        # 'kisumu_male_population': context['kisumu_male_population'],
        # 'kisumu_female_population': context['kisumu_female_population'],
        # 'kisumu_intersex_population': context['kisumu_intersex_population'],
        # 'kisumu_total_population': int(context['kisumu_male_population']) + int(context['kisumu_female_population']) + int(context['kisumu_intersex_population']),
        # 'kisumu_outbreak_start_date': context['kisumu_outbreak_start_date'],
        # 'kisumu_outbreak_stop_date': context['kisumu_outbreak_stop_date'],
        # 'kisumu_deaths': context['kisumu_deaths'],
        # 'kisumu_p_and_c_cases': context['kisumu_p_and_c_cases'],
        # 'kisumu_human_reference': context['kisumu_human_reference'],
        # 'homabay_male_population': context['homabay_male_population'],
        # 'homabay_female_population': context['homabay_female_population'],
        # 'homabay_intersex_population': context['homabay_intersex_population'],
        # 'homabay_total_population': int(context['homabay_male_population']) + int(context['homabay_female_population']) + int(context['homabay_intersex_population']),
        # 'homabay_outbreak_start_date': context['homabay_outbreak_start_date'],
        # 'homabay_outbreak_stop_date': context['homabay_outbreak_stop_date'],
        # 'homabay_deaths': context['homabay_deaths'],
        # 'homabay_p_and_c_cases': context['homabay_p_and_c_cases'],
        # 'homabay_human_reference': context['homabay_human_reference'],
        # 'migori_male_population': context['migori_male_population'],
        # 'migori_female_population': context['migori_female_population'],
        # 'migori_intersex_population': context['migori_intersex_population'],
        # 'migori_total_population': int(context['migori_male_population']) + int(context['migori_female_population']) + int(context['migori_intersex_population']),
        # 'migori_outbreak_start_date': context['migori_outbreak_start_date'],
        # 'migori_outbreak_stop_date': context['migori_outbreak_stop_date'],
        # 'migori_deaths': context['migori_deaths'],
        # 'migori_p_and_c_cases': context['migori_p_and_c_cases'],
        # 'migori_human_reference': context['migori_human_reference'],
        # 'kisii_male_population': context['kisii_male_population'],
        # 'kisii_female_population': context['kisii_female_population'],
        # 'kisii_intersex_population': context['kisii_intersex_population'],
        # 'kisii_total_population': int(context['kisii_male_population']) + int(context['kisii_female_population']) + int(context['kisii_intersex_population']),
        # 'kisii_outbreak_start_date': context['kisii_outbreak_start_date'],
        # 'kisii_outbreak_stop_date': context['kisii_outbreak_stop_date'],
        # 'kisii_deaths': context['kisii_deaths'],
        # 'kisii_p_and_c_cases': context['kisii_p_and_c_cases'],
        # 'kisii_human_reference': context['kisii_human_reference'],
        # 'nyamira_male_population': context['nyamira_male_population'],
        # 'nyamira_female_population': context['nyamira_female_population'],
        # 'nyamira_intersex_population': context['nyamira_intersex_population'],
        # 'nyamira_total_population': int(context['nyamira_male_population']) + int(context['nyamira_female_population']) + int(context['nyamira_intersex_population']),
        # 'nyamira_outbreak_start_date': context['nyamira_outbreak_start_date'],
        # 'nyamira_outbreak_stop_date': context['nyamira_outbreak_stop_date'],
        # 'nyamira_deaths': context['nyamira_deaths'],
        # 'nyamira_p_and_c_cases': context['nyamira_p_and_c_cases'],
        # 'nyamira_human_reference': context['nyamira_human_reference'],
        # 'turkana_male_population': context['turkana_male_population'],
        # 'turkana_female_population': context['turkana_female_population'],
        # 'turkana_intersex_population': context['turkana_intersex_population'],
        # 'turkana_total_population': int(context['turkana_male_population']) + int(context['turkana_female_population']) + int(context['turkana_intersex_population']),
        # 'turkana_outbreak_start_date': context['turkana_outbreak_start_date'],
        # 'turkana_outbreak_stop_date': context['turkana_outbreak_stop_date'],
        # 'turkana_deaths': context['turkana_deaths'],
        # 'turkana_p_and_c_cases': context['turkana_p_and_c_cases'],
        # 'turkana_human_reference': context['turkana_human_reference'],
        # 'westpokot_male_population': context['westpokot_male_population'],
        # 'westpokot_female_population': context['westpokot_female_population'],
        # 'westpokot_intersex_population': context['westpokot_intersex_population'],
        # 'westpokot_total_population': int(context['westpokot_male_population']) + int(context['westpokot_female_population']) + int(context['westpokot_intersex_population']),
        # 'westpokot_outbreak_start_date': context['westpokot_outbreak_start_date'],
        # 'westpokot_outbreak_stop_date': context['westpokot_outbreak_stop_date'],
        # 'westpokot_deaths': context['westpokot_deaths'],
        # 'westpokot_p_and_c_cases': context['westpokot_p_and_c_cases'],
        # 'westpokot_human_reference': context['westpokot_human_reference'],
        # 'samburu_male_population': context['samburu_male_population'],
        # 'samburu_female_population': context['samburu_female_population'],
        # 'samburu_intersex_population': context['samburu_intersex_population'],
        # 'samburu_total_population': int(context['samburu_male_population']) + int(context['samburu_female_population']) + int(context['samburu_intersex_population']),
        # 'samburu_outbreak_start_date': context['samburu_outbreak_start_date'],
        # 'samburu_outbreak_stop_date': context['samburu_outbreak_stop_date'],
        # 'samburu_deaths': context['samburu_deaths'],
        # 'samburu_p_and_c_cases': context['samburu_p_and_c_cases'],
        # 'samburu_human_reference': context['samburu_human_reference'],
        # 'transnzoia_male_population': context['transnzoia_male_population'],
        # 'transnzoia_female_population': context['transnzoia_female_population'],
        # 'transnzoia_intersex_population': context['transnzoia_intersex_population'],
        # 'transnzoia_total_population': int(context['transnzoia_male_population']) + int(context['transnzoia_female_population']) + int(context['transnzoia_intersex_population']),
        # 'transnzoia_outbreak_start_date': context['transnzoia_outbreak_start_date'],
        # 'transnzoia_outbreak_stop_date': context['transnzoia_outbreak_stop_date'],
        # 'transnzoia_deaths': context['transnzoia_deaths'],
        # 'transnzoia_p_and_c_cases': context['transnzoia_p_and_c_cases'],
        # 'transnzoia_human_reference': context['transnzoia_human_reference'],
        'baringo_male_population': context['baringo_male_population'],
        'baringo_female_population': context['baringo_female_population'],
        'baringo_intersex_population': context['baringo_intersex_population'],
        'baringo_total_population': int(context['baringo_male_population']) + int(context['baringo_female_population']) + int(context['baringo_intersex_population']),
        'baringo_outbreak_start_date': context['baringo_outbreak_start_date'],
        'baringo_outbreak_stop_date': context['baringo_outbreak_stop_date'],
        'baringo_deaths': context['baringo_deaths'],
        'baringo_p_and_c_cases': context['baringo_p_and_c_cases'],
        'baringo_human_reference': context['baringo_human_reference'],
        # 'uasingishu_male_population': context['uasingishu_male_population'],
        # 'uasingishu_female_population': context['uasingishu_female_population'],
        # 'uasingishu_intersex_population': context['uasingishu_intersex_population'],
        # 'uasingishu_total_population': int(context['uasingishu_male_population']) + int(context['uasingishu_female_population']) + int(context['uasingishu_intersex_population']),
        # 'uasingishu_outbreak_start_date': context['uasingishu_outbreak_start_date'],
        # 'uasingishu_outbreak_stop_date': context['uasingishu_outbreak_stop_date'],
        # 'uasingishu_deaths': context['uasingishu_deaths'],
        # 'uasingishu_p_and_c_cases': context['uasingishu_p_and_c_cases'],
        # 'uasingishu_human_reference': context['uasingishu_human_reference'],
        # 'elgeyomarakwet_male_population': context['elgeyomarakwet_male_population'],
        # 'elgeyomarakwet_female_population': context['elgeyomarakwet_female_population'],
        # 'elgeyomarakwet_intersex_population': context['elgeyomarakwet_intersex_population'],
        # 'elgeyomarakwet_total_population': int(context['elgeyomarakwet_male_population']) + int(context['elgeyomarakwet_female_population']) + int(context['elgeyomarakwet_intersex_population']),
        # 'elgeyomarakwet_outbreak_start_date': context['elgeyomarakwet_outbreak_start_date'],
        # 'elgeyomarakwet_outbreak_stop_date': context['elgeyomarakwet_outbreak_stop_date'],
        # 'elgeyomarakwet_deaths': context['elgeyomarakwet_deaths'],
        # 'elgeyomarakwet_p_and_c_cases': context['elgeyomarakwet_p_and_c_cases'],
        # 'elgeyomarakwet_human_reference': context['elgeyomarakwet_human_reference'],
        # 'nandi_male_population': context['nandi_male_population'],
        # 'nandi_female_population': context['nandi_female_population'],
        # 'nandi_intersex_population': context['nandi_intersex_population'],
        # 'nandi_total_population': int(context['nandi_male_population']) + int(context['nandi_female_population']) + int(context['nandi_intersex_population']),
        # 'nandi_outbreak_start_date': context['nandi_outbreak_start_date'],
        # 'nandi_outbreak_stop_date': context['nandi_outbreak_stop_date'],
        # 'nandi_deaths': context['nandi_deaths'],
        # 'nandi_p_and_c_cases': context['nandi_p_and_c_cases'],
        # 'nandi_human_reference': context['nandi_human_reference'],
        # 'laikipia_male_population': context['laikipia_male_population'],
        # 'laikipia_female_population': context['laikipia_female_population'],
        # 'laikipia_intersex_population': context['laikipia_intersex_population'],
        # 'laikipia_total_population': int(context['laikipia_male_population']) + int(context['laikipia_female_population']) + int(context['laikipia_intersex_population']),
        # 'laikipia_outbreak_start_date': context['laikipia_outbreak_start_date'],
        # 'laikipia_outbreak_stop_date': context['laikipia_outbreak_stop_date'],
        # 'laikipia_deaths': context['laikipia_deaths'],
        # 'laikipia_p_and_c_cases': context['laikipia_p_and_c_cases'],
        # 'laikipia_human_reference': context['laikipia_human_reference'],
        # 'nakuru_male_population': context['nakuru_male_population'],
        # 'nakuru_female_population': context['nakuru_female_population'],
        # 'nakuru_intersex_population': context['nakuru_intersex_population'],
        # 'nakuru_total_population': int(context['nakuru_male_population']) + int(context['nakuru_female_population']) + int(context['nakuru_intersex_population']),
        # 'nakuru_outbreak_start_date': context['nakuru_outbreak_start_date'],
        # 'nakuru_outbreak_stop_date': context['nakuru_outbreak_stop_date'],
        # 'nakuru_deaths': context['nakuru_deaths'],
        # 'nakuru_p_and_c_cases': context['nakuru_p_and_c_cases'],
        # 'nakuru_human_reference': context['nakuru_human_reference'],
        # 'narok_male_population': context['narok_male_population'],
        # 'narok_female_population': context['narok_female_population'],
        # 'narok_intersex_population': context['narok_intersex_population'],
        # 'narok_total_population': int(context['narok_male_population']) + int(context['narok_female_population']) + int(context['narok_intersex_population']),
        # 'narok_outbreak_start_date': context['narok_outbreak_start_date'],
        # 'narok_outbreak_stop_date': context['narok_outbreak_stop_date'],
        # 'narok_deaths': context['narok_deaths'],
        # 'narok_p_and_c_cases': context['narok_p_and_c_cases'],
        # 'narok_human_reference': context['narok_human_reference'],
        # 'kajiado_male_population': context['kajiado_male_population'],
        # 'kajiado_female_population': context['kajiado_female_population'],
        # 'kajiado_intersex_population': context['kajiado_intersex_population'],
        # 'kajiado_total_population': int(context['kajiado_male_population']) + int(context['kajiado_female_population']) + int(context['kajiado_intersex_population']),
        # 'kajiado_outbreak_start_date': context['kajiado_outbreak_start_date'],
        # 'kajiado_outbreak_stop_date': context['kajiado_outbreak_stop_date'],
        # 'kajiado_deaths': context['kajiado_deaths'],
        # 'kajiado_p_and_c_cases': context['kajiado_p_and_c_cases'],
        # 'kajiado_human_reference': context['kajiado_human_reference'],
        # 'kericho_male_population': context['kericho_male_population'],
        # 'kericho_female_population': context['kericho_female_population'],
        # 'kericho_intersex_population': context['kericho_intersex_population'],
        # 'kericho_total_population': int(context['kericho_male_population']) + int(context['kericho_female_population']) + int(context['kericho_intersex_population']),
        # 'kericho_outbreak_start_date': context['kericho_outbreak_start_date'],
        # 'kericho_outbreak_stop_date': context['kericho_outbreak_stop_date'],
        # 'kericho_deaths': context['kericho_deaths'],
        # 'kericho_p_and_c_cases': context['kericho_p_and_c_cases'],
        # 'kericho_human_reference': context['kericho_human_reference'],
        # 'bomet_male_population': context['bomet_male_population'],
        # 'bomet_female_population': context['bomet_female_population'],
        # 'bomet_intersex_population': context['bomet_intersex_population'],
        # 'bomet_total_population': int(context['bomet_male_population']) + int(context['bomet_female_population']) + int(context['bomet_intersex_population']),
        # 'bomet_outbreak_start_date': context['bomet_outbreak_start_date'],
        # 'bomet_outbreak_stop_date': context['bomet_outbreak_stop_date'],
        # 'bomet_deaths': context['bomet_deaths'],
        # 'bomet_p_and_c_cases': context['bomet_p_and_c_cases'],
        # 'bomet_human_reference': context['bomet_human_reference'],
        # 'kakamega_male_population': context['kakamega_male_population'],
        # 'kakamega_female_population': context['kakamega_female_population'],
        # 'kakamega_intersex_population': context['kakamega_intersex_population'],
        # 'kakamega_total_population': int(context['kakamega_male_population']) + int(context['kakamega_female_population']) + int(context['kakamega_intersex_population']),
        # 'kakamega_outbreak_start_date': context['kakamega_outbreak_start_date'],
        # 'kakamega_outbreak_stop_date': context['kakamega_outbreak_stop_date'],
        # 'kakamega_deaths': context['kakamega_deaths'],
        # 'kakamega_p_and_c_cases': context['kakamega_p_and_c_cases'],
        # 'kakamega_human_reference': context['kakamega_human_reference'],
        # 'vihiga_male_population': context['vihiga_male_population'],
        # 'vihiga_female_population': context['vihiga_female_population'],
        # 'vihiga_intersex_population': context['vihiga_intersex_population'],
        # 'vihiga_total_population': int(context['vihiga_male_population']) + int(context['vihiga_female_population']) + int(context['vihiga_intersex_population']),
        # 'vihiga_outbreak_start_date': context['vihiga_outbreak_start_date'],
        # 'vihiga_outbreak_stop_date': context['vihiga_outbreak_stop_date'],
        # 'vihiga_deaths': context['vihiga_deaths'],
        # 'vihiga_p_and_c_cases': context['vihiga_p_and_c_cases'],
        # 'vihiga_human_reference': context['vihiga_human_reference'],
        # 'bungoma_male_population': context['bungoma_male_population'],
        # 'bungoma_female_population': context['bungoma_female_population'],
        # 'bungoma_intersex_population': context['bungoma_intersex_population'],
        # 'bungoma_total_population': int(context['bungoma_male_population']) + int(context['bungoma_female_population']) + int(context['bungoma_intersex_population']),
        # 'bungoma_outbreak_start_date': context['bungoma_outbreak_start_date'],
        # 'bungoma_outbreak_stop_date': context['bungoma_outbreak_stop_date'],
        # 'bungoma_deaths': context['bungoma_deaths'],
        # 'bungoma_p_and_c_cases': context['bungoma_p_and_c_cases'],
        # 'bungoma_human_reference': context['bungoma_human_reference'],
        # 'busia_male_population': context['busia_male_population'],
        # 'busia_female_population': context['busia_female_population'],
        # 'busia_intersex_population': context['busia_intersex_population'],
        # 'busia_total_population': int(context['busia_male_population']) + int(context['busia_female_population']) + int(context['busia_intersex_population']),
        # 'busia_outbreak_start_date': context['busia_outbreak_start_date'],
        # 'busia_outbreak_stop_date': context['busia_outbreak_stop_date'],
        # 'busia_deaths': context['busia_deaths'],
        # 'busia_p_and_c_cases': context['busia_p_and_c_cases'],
        # 'busia_human_reference': context['busia_human_reference'],
    }

    return render(request,'human_population.html',context2)

def human_dalys(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['human_dalys']

    context = {
        'nairobi_male_population': 0,
        'nairobi_female_population': 0,
        'nairobi_intersex_population': 0,
        'nairobi_total_population': 0,
        'nyandarua_male_population': 0,
        'nyandarua_female_population': 0,
        'nyandarua_intersex_population': 0,
        'nyandarua_total_population': 0,
        'nyeri_male_population': 0,
        'nyeri_female_population': 0,
        'nyeri_intersex_population': 0,
        'nyeri_total_population': 0,
        'kirinyaga_male_population': 0,
        'kirinyaga_female_population': 0,
        'kirinyaga_intersex_population': 0,
        'kirinyaga_total_population': 0,
        'muranga_male_population': 0,
        'muranga_female_population': 0,
        'muranga_intersex_population': 0,
        'muranga_total_population': 0,
        'kiambu_male_population': 0,
        'kiambu_female_population': 0,
        'kiambu_intersex_population': 0,
        'kiambu_total_population': 0,
        'mombasa_male_population': 0,
        'mombasa_female_population': 0,
        'mombasa_intersex_population': 0,
        'mombasa_total_population': 0,
        'kwale_male_population': 0,
        'kwale_female_population': 0,
        'kwale_intersex_population': 0,
        'kwale_total_population': 0,
        'kilifi_male_population': 0,
        'kilifi_female_population': 0,
        'kilifi_intersex_population': 0,
        'kilifi_total_population': 0,
        'tanariver_male_population': 0,
        'tanariver_female_population': 0,
        'tanariver_intersex_population': 0,
        'tanariver_total_population': 0,
        'lamu_male_population': 0,
        'lamu_female_population': 0,
        'lamu_intersex_population': 0,
        'lamu_total_population': 0,
        'taitataveta_male_population': 0,
        'taitataveta_female_population': 0,
        'taitataveta_intersex_population': 0,
        'taitataveta_total_population': 0,
        'marsabit_male_population': 0,
        'marsabit_female_population': 0,
        'marsabit_intersex_population': 0,
        'marsabit_total_population': 0,
        'isiolo_male_population': 0,
        'isiolo_female_population': 0,
        'isiolo_intersex_population': 0,
        'isiolo_total_population': 0,
        'meru_male_population': 0,
        'meru_female_population': 0,
        'meru_intersex_population': 0,
        'meru_total_population': 0,
        'tharaka_male_population': 0,
        'tharaka_female_population': 0,
        'tharaka_intersex_population': 0,
        'tharaka_total_population': 0,
        'embu_male_population': 0,
        'embu_female_population': 0,
        'embu_intersex_population': 0,
        'embu_total_population': 0,
        'kitui_male_population': 0,
        'kitui_female_population': 0,
        'kitui_intersex_population': 0,
        'kitui_total_population': 0,
        'machakos_male_population': 0,
        'machakos_female_population': 0,
        'machakos_intersex_population': 0,
        'machakos_total_population': 0,
        'makueni_male_population': 0,
        'makueni_female_population': 0,
        'makueni_intersex_population': 0,
        'makueni_total_population': 0,
        'garissa_male_population': 0,
        'garissa_female_population': 0,
        'garissa_intersex_population': 0,
        'garissa_total_population': 0,
        'wajir_male_population': 0,
        'wajir_female_population': 0,
        'wajir_intersex_population': 0,
        'wajir_total_population': 0,
        'mandera_male_population': 0,
        'mandera_female_population': 0,
        'mandera_intersex_population': 0,
        'mandera_total_population': 0,
        'siaya_male_population': 0,
        'siaya_female_population': 0,
        'siaya_intersex_population': 0,
        'siaya_total_population': 0,
        'kisumu_male_population': 0,
        'kisumu_female_population': 0,
        'kisumu_intersex_population': 0,
        'kisumu_total_population': 0,
        'homabay_male_population': 0,
        'homabay_female_population': 0,
        'homabay_intersex_population': 0,
        'homabay_total_population': 0,
        'migori_male_population': 0,
        'migori_female_population': 0,
        'migori_intersex_population': 0,
        'migori_total_population': 0,
        'kisii_male_population': 0,
        'kisii_female_population': 0,
        'kisii_intersex_population': 0,
        'kisii_total_population': 0,
        'nyamira_male_population': 0,
        'nyamira_female_population': 0,
        'nyamira_intersex_population': 0,
        'nyamira_total_population': 0,
        'turkana_male_population': 0,
        'turkana_female_population': 0,
        'turkana_intersex_population': 0,
        'turkana_total_population': 0,
        'westpokot_male_population': 0,
        'westpokot_female_population': 0,
        'westpokot_intersex_population': 0,
        'westpokot_total_population': 0,
        'samburu_male_population': 0,
        'samburu_female_population': 0,
        'samburu_intersex_population': 0,
        'samburu_total_population': 0,
        'transnzoia_male_population': 0,
        'transnzoia_female_population': 0,
        'transnzoia_intersex_population': 0,
        'transnzoia_total_population': 0,
        'baringo_male_population': 0,
        'baringo_female_population': 0,
        'baringo_intersex_population': 0,
        'baringo_total_population': 0,
        'uasingishu_male_population': 0,
        'uasingishu_female_population': 0,
        'uasingishu_intersex_population': 0,
        'uasingishu_total_population': 0,
        'elgeyomarakwet_male_population': 0,
        'elgeyomarakwet_female_population': 0,
        'elgeyomarakwet_intersex_population': 0,
        'elgeyomarakwet_total_population': 0,
        'nandi_male_population': 0,
        'nandi_female_population': 0,
        'nandi_intersex_population': 0,
        'nandi_total_population': 0,
        'laikipia_male_population': 0,
        'laikipia_female_population': 0,
        'laikipia_intersex_population': 0,
        'laikipia_total_population': 0,
        'nakuru_male_population': 0,
        'nakuru_female_population': 0,
        'nakuru_intersex_population': 0,
        'nakuru_total_population': 0,
        'narok_male_population': 0,
        'narok_female_population': 0,
        'narok_intersex_population': 0,
        'narok_total_population': 0,
        'kajiado_male_population': 0,
        'kajiado_female_population': 0,
        'kajiado_intersex_population': 0,
        'kajiado_total_population': 0,
        'kericho_male_population': 0,
        'kericho_female_population': 0,
        'kericho_intersex_population': 0,
        'kericho_total_population': 0,
        'bomet_male_population': 0,
        'bomet_female_population': 0,
        'bomet_intersex_population': 0,
        'bomet_total_population': 0,
        'kakamega_male_population': 0,
        'kakamega_female_population': 0,
        'kakamega_intersex_population': 0,
        'kakamega_total_population': 0,
        'vihiga_male_population': 0,
        'vihiga_female_population': 0,
        'vihiga_intersex_population': 0,
        'vihiga_total_population': 0,
        'bungoma_male_population': 0,
        'bungoma_female_population': 0,
        'bungoma_intersex_population': 0,
        'bungoma_total_population': 0,
        'busia_male_population': 0,
        'busia_female_population': 0,
        'busia_intersex_population': 0,
        'busia_total_population': 0,
    }

    if (request.method == "POST"):
        # nairobi_male_population = request.POST['nairobi_male_population']
        # nairobi_female_population = request.POST['nairobi_female_population']
        # nairobi_intersex_population = request.POST['nairobi_intersex_population']
        # nairobi_total_population = request.POST['nairobi_total_population']
        # nyandarua_male_population = request.POST['nyandarua_male_population']
        # nyandarua_female_population = request.POST['nyandarua_female_population']
        # nyandarua_intersex_population = request.POST['nyandarua_intersex_population']
        # nyandarua_total_population = request.POST['nyandarua_total_population']
        # nyeri_male_population = request.POST['nyeri_male_population']
        # nyeri_female_population = request.POST['nyeri_female_population']
        # nyeri_intersex_population = request.POST['nyeri_intersex_population']
        # nyeri_total_population = request.POST['nyeri_total_population']
        # kirinyaga_male_population = request.POST['kirinyaga_male_population']
        # kirinyaga_female_population = request.POST['kirinyaga_female_population']
        # kirinyaga_intersex_population = request.POST['kirinyaga_intersex_population']
        # kirinyaga_total_population = request.POST['kirinyaga_total_population']
        # muranga_male_population = request.POST['muranga_male_population']
        # muranga_female_population = request.POST['muranga_female_population']
        # muranga_intersex_population = request.POST['muranga_intersex_population']
        # muranga_total_population = request.POST['muranga_total_population']
        # kiambu_male_population = request.POST['kiambu_male_population']
        # kiambu_female_population = request.POST['kiambu_female_population']
        # kiambu_intersex_population = request.POST['kiambu_intersex_population']
        # kiambu_total_population = request.POST['kiambu_total_population']
        # mombasa_male_population = request.POST['mombasa_male_population']
        # mombasa_female_population = request.POST['mombasa_female_population']
        # mombasa_intersex_population = request.POST['mombasa_intersex_population']
        # mombasa_total_population = request.POST['mombasa_total_population']
        # kwale_male_population = request.POST['kwale_male_population']
        # kwale_female_population = request.POST['kwale_female_population']
        # kwale_intersex_population = request.POST['kwale_intersex_population']
        # kwale_total_population = request.POST['kwale_total_population']
        # kilifi_male_population = request.POST['kilifi_male_population']
        # kilifi_female_population = request.POST['kilifi_female_population']
        # kilifi_intersex_population = request.POST['kilifi_intersex_population']
        # kilifi_total_population = request.POST['kilifi_total_population']
        tanariver_male_population = request.POST['tanariver_male_population']
        tanariver_female_population = request.POST['tanariver_female_population']
        tanariver_intersex_population = request.POST['tanariver_intersex_population']
        tanariver_total_population = request.POST['tanariver_total_population']
        # lamu_male_population = request.POST['lamu_male_population']
        # lamu_female_population = request.POST['lamu_female_population']
        # lamu_intersex_population = request.POST['lamu_intersex_population']
        # lamu_total_population = request.POST['lamu_total_population']
        # taitataveta_male_population = request.POST['taitataveta_male_population']
        # taitataveta_female_population = request.POST['taitataveta_female_population']
        # taitataveta_intersex_population = request.POST['taitataveta_intersex_population']
        # taitataveta_total_population = request.POST['taitataveta_total_population']
        marsabit_male_population = request.POST['marsabit_male_population']
        marsabit_female_population = request.POST['marsabit_female_population']
        marsabit_intersex_population = request.POST['marsabit_intersex_population']
        marsabit_total_population = request.POST['marsabit_total_population']
        # isiolo_male_population = request.POST['isiolo_male_population']
        # isiolo_female_population = request.POST['isiolo_female_population']
        # isiolo_intersex_population = request.POST['isiolo_intersex_population']
        # isiolo_total_population = request.POST['isiolo_total_population']
        # meru_male_population = request.POST['meru_male_population']
        # meru_female_population = request.POST['meru_female_population']
        # meru_intersex_population = request.POST['meru_intersex_population']
        # meru_total_population = request.POST['meru_total_population']
        # tharaka_male_population = request.POST['tharaka_male_population']
        # tharaka_female_population = request.POST['tharaka_female_population']
        # tharaka_intersex_population = request.POST['tharaka_intersex_population']
        # tharaka_total_population = request.POST['tharaka_total_population']
        # embu_male_population = request.POST['embu_male_population']
        # embu_female_population = request.POST['embu_female_population']
        # embu_intersex_population = request.POST['embu_intersex_population']
        # embu_total_population = request.POST['embu_total_population']
        # kitui_male_population = request.POST['kitui_male_population']
        # kitui_female_population = request.POST['kitui_female_population']
        # kitui_intersex_population = request.POST['kitui_intersex_population']
        # kitui_total_population = request.POST['kitui_total_population']
        # machakos_male_population = request.POST['machakos_male_population']
        # machakos_female_population = request.POST['machakos_female_population']
        # machakos_intersex_population = request.POST['machakos_intersex_population']
        # machakos_total_population = request.POST['machakos_total_population']
        # makueni_male_population = request.POST['makueni_male_population']
        # makueni_female_population = request.POST['makueni_female_population']
        # makueni_intersex_population = request.POST['makueni_intersex_population']
        # makueni_total_population = request.POST['makueni_total_population']
        garissa_male_population = request.POST['garissa_male_population']
        garissa_female_population = request.POST['garissa_female_population']
        garissa_intersex_population = request.POST['garissa_intersex_population']
        garissa_total_population = request.POST['garissa_total_population']
        wajir_male_population = request.POST['wajir_male_population']
        wajir_female_population = request.POST['wajir_female_population']
        wajir_intersex_population = request.POST['wajir_intersex_population']
        wajir_total_population = request.POST['wajir_total_population']
        # mandera_male_population = request.POST['mandera_male_population']
        # mandera_female_population = request.POST['mandera_female_population']
        # mandera_intersex_population = request.POST['mandera_intersex_population']
        # mandera_total_population = request.POST['mandera_total_population']
        # siaya_male_population = request.POST['siaya_male_population']
        # siaya_female_population = request.POST['siaya_female_population']
        # siaya_intersex_population = request.POST['siaya_intersex_population']
        # siaya_total_population = request.POST['siaya_total_population']
        # kisumu_male_population = request.POST['kisumu_male_population']
        # kisumu_female_population = request.POST['kisumu_female_population']
        # kisumu_intersex_population = request.POST['kisumu_intersex_population']
        # kisumu_total_population = request.POST['kisumu_total_population']
        # homabay_male_population = request.POST['homabay_male_population']
        # homabay_female_population = request.POST['homabay_female_population']
        # homabay_intersex_population = request.POST['homabay_intersex_population']
        # homabay_total_population = request.POST['homabay_total_population']
        # migori_male_population = request.POST['migori_male_population']
        # migori_female_population = request.POST['migori_female_population']
        # migori_intersex_population = request.POST['migori_intersex_population']
        # migori_total_population = request.POST['migori_total_population']
        # kisii_male_population = request.POST['kisii_male_population']
        # kisii_female_population = request.POST['kisii_female_population']
        # kisii_intersex_population = request.POST['kisii_intersex_population']
        # kisii_total_population = request.POST['kisii_total_population']
        # nyamira_male_population = request.POST['nyamira_male_population']
        # nyamira_female_population = request.POST['nyamira_female_population']
        # nyamira_intersex_population = request.POST['nyamira_intersex_population']
        # nyamira_total_population = request.POST['nyamira_total_population']
        # turkana_male_population = request.POST['turkana_male_population']
        # turkana_female_population = request.POST['turkana_female_population']
        # turkana_intersex_population = request.POST['turkana_intersex_population']
        # turkana_total_population = request.POST['turkana_total_population']
        # westpokot_male_population = request.POST['westpokot_male_population']
        # westpokot_female_population = request.POST['westpokot_female_population']
        # westpokot_intersex_population = request.POST['westpokot_intersex_population']
        # westpokot_total_population = request.POST['westpokot_total_population']
        # samburu_male_population = request.POST['samburu_male_population']
        # samburu_female_population = request.POST['samburu_female_population']
        # samburu_intersex_population = request.POST['samburu_intersex_population']
        # samburu_total_population = request.POST['samburu_total_population']
        # transnzoia_male_population = request.POST['transnzoia_male_population']
        # transnzoia_female_population = request.POST['transnzoia_female_population']
        # transnzoia_intersex_population = request.POST['transnzoia_intersex_population']
        # transnzoia_total_population = request.POST['transnzoia_total_population']
        baringo_male_population = request.POST['baringo_male_population']
        baringo_female_population = request.POST['baringo_female_population']
        baringo_intersex_population = request.POST['baringo_intersex_population']
        baringo_total_population = request.POST['baringo_total_population']
        # uasingishu_male_population = request.POST['uasingishu_male_population']
        # uasingishu_female_population = request.POST['uasingishu_female_population']
        # uasingishu_intersex_population = request.POST['uasingishu_intersex_population']
        # uasingishu_total_population = request.POST['uasingishu_total_population']
        # elgeyomarakwet_male_population = request.POST['elgeyomarakwet_male_population']
        # elgeyomarakwet_female_population = request.POST['elgeyomarakwet_female_population']
        # elgeyomarakwet_intersex_population = request.POST['elgeyomarakwet_intersex_population']
        # elgeyomarakwet_total_population = request.POST['elgeyomarakwet_total_population']
        # nandi_male_population = request.POST['nandi_male_population']
        # nandi_female_population = request.POST['nandi_female_population']
        # nandi_intersex_population = request.POST['nandi_intersex_population']
        # nandi_total_population = request.POST['nandi_total_population']
        # laikipia_male_population = request.POST['laikipia_male_population']
        # laikipia_female_population = request.POST['laikipia_female_population']
        # laikipia_intersex_population = request.POST['laikipia_intersex_population']
        # laikipia_total_population = request.POST['laikipia_total_population']
        # nakuru_male_population = request.POST['nakuru_male_population']
        # nakuru_female_population = request.POST['nakuru_female_population']
        # nakuru_intersex_population = request.POST['nakuru_intersex_population']
        # nakuru_total_population = request.POST['nakuru_total_population']
        # narok_male_population = request.POST['narok_male_population']
        # narok_female_population = request.POST['narok_female_population']
        # narok_intersex_population = request.POST['narok_intersex_population']
        # narok_total_population = request.POST['narok_total_population']
        # kajiado_male_population = request.POST['kajiado_male_population']
        # kajiado_female_population = request.POST['kajiado_female_population']
        # kajiado_intersex_population = request.POST['kajiado_intersex_population']
        # kajiado_total_population = request.POST['kajiado_total_population']
        # kericho_male_population = request.POST['kericho_male_population']
        # kericho_female_population = request.POST['kericho_female_population']
        # kericho_intersex_population = request.POST['kericho_intersex_population']
        # kericho_total_population = request.POST['kericho_total_population']
        # bomet_male_population = request.POST['bomet_male_population']
        # bomet_female_population = request.POST['bomet_female_population']
        # bomet_intersex_population = request.POST['bomet_intersex_population']
        # bomet_total_population = request.POST['bomet_total_population']
        # kakamega_male_population = request.POST['kakamega_male_population']
        # kakamega_female_population = request.POST['kakamega_female_population']
        # kakamega_intersex_population = request.POST['kakamega_intersex_population']
        # kakamega_total_population = request.POST['kakamega_total_population']
        # vihiga_male_population = request.POST['vihiga_male_population']
        # vihiga_female_population = request.POST['vihiga_female_population']
        # vihiga_intersex_population = request.POST['vihiga_intersex_population']
        # vihiga_total_population = request.POST['vihiga_total_population']
        # bungoma_male_population = request.POST['bungoma_male_population']
        # bungoma_female_population = request.POST['bungoma_female_population']
        # bungoma_intersex_population = request.POST['bungoma_intersex_population']
        # bungoma_total_population = request.POST['bungoma_total_population']
        # busia_male_population = request.POST['busia_male_population']
        # busia_female_population = request.POST['busia_female_population']
        # busia_intersex_population = request.POST['busia_intersex_population']
        # busia_total_population = request.POST['busia_total_population']

        x = rvf_initial_collection.insert_one({
            # 'nairobi_male_population': nairobi_male_population,
            # 'nairobi_female_population': nairobi_female_population,
            # 'nairobi_intersex_population': nairobi_intersex_population,
            # 'nairobi_total_population': nairobi_total_population,
            # 'nyandarua_male_population': nyandarua_male_population,
            # 'nyandarua_female_population': nyandarua_female_population,
            # 'nyandarua_intersex_population': nyandarua_intersex_population,
            # 'nyandarua_total_population': nyandarua_total_population,
            # 'nyeri_male_population': nyeri_male_population,
            # 'nyeri_female_population': nyeri_female_population,
            # 'nyeri_intersex_population': nyeri_intersex_population,
            # 'nyeri_total_population': nyeri_total_population,
            # 'kirinyaga_male_population': kirinyaga_male_population,
            # 'kirinyaga_female_population': kirinyaga_female_population,
            # 'kirinyaga_intersex_population': kirinyaga_intersex_population,
            # 'kirinyaga_total_population': kirinyaga_total_population,
            # 'muranga_male_population': muranga_male_population,
            # 'muranga_female_population': muranga_female_population,
            # 'muranga_intersex_population': muranga_intersex_population,
            # 'muranga_total_population': muranga_total_population,
            # 'kiambu_male_population': kiambu_male_population,
            # 'kiambu_female_population': kiambu_female_population,
            # 'kiambu_intersex_population': kiambu_intersex_population,
            # 'kiambu_total_population': kiambu_total_population,
            # 'mombasa_male_population': mombasa_male_population,
            # 'mombasa_female_population': mombasa_female_population,
            # 'mombasa_intersex_population': mombasa_intersex_population,
            # 'mombasa_total_population': mombasa_total_population,
            # 'kwale_male_population': kwale_male_population,
            # 'kwale_female_population': kwale_female_population,
            # 'kwale_intersex_population': kwale_intersex_population,
            # 'kwale_total_population': kwale_total_population,
            # 'kilifi_male_population': kilifi_male_population,
            # 'kilifi_female_population': kilifi_female_population,
            # 'kilifi_intersex_population': kilifi_intersex_population,
            # 'kilifi_total_population': kilifi_total_population,
            'tanariver_male_population': tanariver_male_population,
            'tanariver_female_population': tanariver_female_population,
            'tanariver_intersex_population': tanariver_intersex_population,
            'tanariver_total_population': tanariver_total_population,
            # 'lamu_male_population': lamu_male_population,
            # 'lamu_female_population': lamu_female_population,
            # 'lamu_intersex_population': lamu_intersex_population,
            # 'lamu_total_population': lamu_total_population,
            # 'taitataveta_male_population': taitataveta_male_population,
            # 'taitataveta_female_population': taitataveta_female_population,
            # 'taitataveta_intersex_population': taitataveta_intersex_population,
            # 'taitataveta_total_population': taitataveta_total_population,
            'marsabit_male_population': marsabit_male_population,
            'marsabit_female_population': marsabit_female_population,
            'marsabit_intersex_population': marsabit_intersex_population,
            'marsabit_total_population': marsabit_total_population,
            # 'isiolo_male_population': isiolo_male_population,
            # 'isiolo_female_population': isiolo_female_population,
            # 'isiolo_intersex_population': isiolo_intersex_population,
            # 'isiolo_total_population': isiolo_total_population,
            # 'meru_male_population': meru_male_population,
            # 'meru_female_population': meru_female_population,
            # 'meru_intersex_population': meru_intersex_population,
            # 'meru_total_population': meru_total_population,
            # 'tharaka_male_population': tharaka_male_population,
            # 'tharaka_female_population': tharaka_female_population,
            # 'tharaka_intersex_population': tharaka_intersex_population,
            # 'tharaka_total_population': tharaka_total_population,
            # 'embu_male_population': embu_male_population,
            # 'embu_female_population': embu_female_population,
            # 'embu_intersex_population': embu_intersex_population,
            # 'embu_total_population': embu_total_population,
            # 'kitui_male_population': kitui_male_population,
            # 'kitui_female_population': kitui_female_population,
            # 'kitui_intersex_population': kitui_intersex_population,
            # 'kitui_total_population': kitui_total_population,
            # 'machakos_male_population': machakos_male_population,
            # 'machakos_female_population': machakos_female_population,
            # 'machakos_intersex_population': machakos_intersex_population,
            # 'machakos_total_population': machakos_total_population,
            # 'makueni_male_population': makueni_male_population,
            # 'makueni_female_population': makueni_female_population,
            # 'makueni_intersex_population': makueni_intersex_population,
            # 'makueni_total_population': makueni_total_population,
            'garissa_male_population': garissa_male_population,
            'garissa_female_population': garissa_female_population,
            'garissa_intersex_population': garissa_intersex_population,
            'garissa_total_population': garissa_total_population,
            'wajir_male_population': wajir_male_population,
            'wajir_female_population': wajir_female_population,
            'wajir_intersex_population': wajir_intersex_population,
            'wajir_total_population': wajir_total_population,
            # 'mandera_male_population': mandera_male_population,
            # 'mandera_female_population': mandera_female_population,
            # 'mandera_intersex_population': mandera_intersex_population,
            # 'mandera_total_population': mandera_total_population,
            # 'siaya_male_population': siaya_male_population,
            # 'siaya_female_population': siaya_female_population,
            # 'siaya_intersex_population': siaya_intersex_population,
            # 'siaya_total_population': siaya_total_population,
            # 'kisumu_male_population': kisumu_male_population,
            # 'kisumu_female_population': kisumu_female_population,
            # 'kisumu_intersex_population': kisumu_intersex_population,
            # 'kisumu_total_population': kisumu_total_population,
            # 'homabay_male_population': homabay_male_population,
            # 'homabay_female_population': homabay_female_population,
            # 'homabay_intersex_population': homabay_intersex_population,
            # 'homabay_total_population': homabay_total_population,
            # 'migori_male_population': migori_male_population,
            # 'migori_female_population': migori_female_population,
            # 'migori_intersex_population': migori_intersex_population,
            # 'migori_total_population': migori_total_population,
            # 'kisii_male_population': kisii_male_population,
            # 'kisii_female_population': kisii_female_population,
            # 'kisii_intersex_population': kisii_intersex_population,
            # 'kisii_total_population': kisii_total_population,
            # 'nyamira_male_population': nyamira_male_population,
            # 'nyamira_female_population': nyamira_female_population,
            # 'nyamira_intersex_population': nyamira_intersex_population,
            # 'nyamira_total_population': nyamira_total_population,
            # 'turkana_male_population': turkana_male_population,
            # 'turkana_female_population': turkana_female_population,
            # 'turkana_intersex_population': turkana_intersex_population,
            # 'turkana_total_population': turkana_total_population,
            # 'westpokot_male_population': westpokot_male_population,
            # 'westpokot_female_population': westpokot_female_population,
            # 'westpokot_intersex_population': westpokot_intersex_population,
            # 'westpokot_total_population': westpokot_total_population,
            # 'samburu_male_population': samburu_male_population,
            # 'samburu_female_population': samburu_female_population,
            # 'samburu_intersex_population': samburu_intersex_population,
            # 'samburu_total_population': samburu_total_population,
            # 'transnzoia_male_population': transnzoia_male_population,
            # 'transnzoia_female_population': transnzoia_female_population,
            # 'transnzoia_intersex_population': transnzoia_intersex_population,
            # 'transnzoia_total_population': transnzoia_total_population,
            'baringo_male_population': baringo_male_population,
            'baringo_female_population': baringo_female_population,
            'baringo_intersex_population': baringo_intersex_population,
            'baringo_total_population': baringo_total_population,
            # 'uasingishu_male_population': uasingishu_male_population,
            # 'uasingishu_female_population': uasingishu_female_population,
            # 'uasingishu_intersex_population': uasingishu_intersex_population,
            # 'uasingishu_total_population': uasingishu_total_population,
            # 'elgeyomarakwet_male_population': elgeyomarakwet_male_population,
            # 'elgeyomarakwet_female_population': elgeyomarakwet_female_population,
            # 'elgeyomarakwet_intersex_population': elgeyomarakwet_intersex_population,
            # 'elgeyomarakwet_total_population': elgeyomarakwet_total_population,
            # 'nandi_male_population': nandi_male_population,
            # 'nandi_female_population': nandi_female_population,
            # 'nandi_intersex_population': nandi_intersex_population,
            # 'nandi_total_population': nandi_total_population,
            # 'laikipia_male_population': laikipia_male_population,
            # 'laikipia_female_population': laikipia_female_population,
            # 'laikipia_intersex_population': laikipia_intersex_population,
            # 'laikipia_total_population': laikipia_total_population,
            # 'nakuru_male_population': nakuru_male_population,
            # 'nakuru_female_population': nakuru_female_population,
            # 'nakuru_intersex_population': nakuru_intersex_population,
            # 'nakuru_total_population': nakuru_total_population,
            # 'narok_male_population': narok_male_population,
            # 'narok_female_population': narok_female_population,
            # 'narok_intersex_population': narok_intersex_population,
            # 'narok_total_population': narok_total_population,
            # 'kajiado_male_population': kajiado_male_population,
            # 'kajiado_female_population': kajiado_female_population,
            # 'kajiado_intersex_population': kajiado_intersex_population,
            # 'kajiado_total_population': kajiado_total_population,
            # 'kericho_male_population': kericho_male_population,
            # 'kericho_female_population': kericho_female_population,
            # 'kericho_intersex_population': kericho_intersex_population,
            # 'kericho_total_population': kericho_total_population,
            # 'bomet_male_population': bomet_male_population,
            # 'bomet_female_population': bomet_female_population,
            # 'bomet_intersex_population': bomet_intersex_population,
            # 'bomet_total_population': bomet_total_population,
            # 'kakamega_male_population': kakamega_male_population,
            # 'kakamega_female_population': kakamega_female_population,
            # 'kakamega_intersex_population': kakamega_intersex_population,
            # 'kakamega_total_population': kakamega_total_population,
            # 'vihiga_male_population': vihiga_male_population,
            # 'vihiga_female_population': vihiga_female_population,
            # 'vihiga_intersex_population': vihiga_intersex_population,
            # 'vihiga_total_population': vihiga_total_population,
            # 'bungoma_male_population': bungoma_male_population,
            # 'bungoma_female_population': bungoma_female_population,
            # 'bungoma_intersex_population': bungoma_intersex_population,
            # 'bungoma_total_population': bungoma_total_population,
            # 'busia_male_population': busia_male_population,
            # 'busia_female_population': busia_female_population,
            # 'busia_intersex_population': busia_intersex_population,
            # 'busia_total_population': busia_total_population,
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        # 'nairobi_male_population': context['nairobi_male_population'],
        # 'nairobi_female_population': context['nairobi_female_population'],
        # 'nairobi_intersex_population': context['nairobi_intersex_population'],
        # 'nairobi_total_population': int(context['nairobi_male_population']) + int(
        #     context['nairobi_female_population']) + int(context['nairobi_intersex_population']),
        # 'nyandarua_male_population': context['nyandarua_male_population'],
        # 'nyandarua_female_population': context['nyandarua_female_population'],
        # 'nyandarua_intersex_population': context['nyandarua_intersex_population'],
        # 'nyandarua_total_population': int(context['nyandarua_male_population']) + int(
        #     context['nyandarua_female_population']) + int(context['nyandarua_intersex_population']),
        # 'nyeri_male_population': context['nyeri_male_population'],
        # 'nyeri_female_population': context['nyeri_female_population'],
        # 'nyeri_intersex_population': context['nyeri_intersex_population'],
        # 'nyeri_total_population': int(context['nyeri_male_population']) + int(context['nyeri_female_population']) + int(
        #     context['nyeri_intersex_population']),
        # 'kirinyaga_male_population': context['kirinyaga_male_population'],
        # 'kirinyaga_female_population': context['kirinyaga_female_population'],
        # 'kirinyaga_intersex_population': context['kirinyaga_intersex_population'],
        # 'kirinyaga_total_population': int(context['kirinyaga_male_population']) + int(
        #     context['kirinyaga_female_population']) + int(context['kirinyaga_intersex_population']),
        # 'muranga_male_population': context['muranga_male_population'],
        # 'muranga_female_population': context['muranga_female_population'],
        # 'muranga_intersex_population': context['muranga_intersex_population'],
        # 'muranga_total_population': int(context['muranga_male_population']) + int(
        #     context['muranga_female_population']) + int(context['muranga_intersex_population']),
        # 'kiambu_male_population': context['kiambu_male_population'],
        # 'kiambu_female_population': context['kiambu_female_population'],
        # 'kiambu_intersex_population': context['kiambu_intersex_population'],
        # 'kiambu_total_population': int(context['kiambu_male_population']) + int(
        #     context['kiambu_female_population']) + int(context['kiambu_intersex_population']),
        # 'mombasa_male_population': context['mombasa_male_population'],
        # 'mombasa_female_population': context['mombasa_female_population'],
        # 'mombasa_intersex_population': context['mombasa_intersex_population'],
        # 'mombasa_total_population': int(context['mombasa_male_population']) + int(
        #     context['mombasa_female_population']) + int(context['mombasa_intersex_population']),
        # 'kwale_male_population': context['kwale_male_population'],
        # 'kwale_female_population': context['kwale_female_population'],
        # 'kwale_intersex_population': context['kwale_intersex_population'],
        # 'kwale_total_population': int(context['kwale_male_population']) + int(context['kwale_female_population']) + int(
        #     context['kwale_intersex_population']),
        # 'kilifi_male_population': context['kilifi_male_population'],
        # 'kilifi_female_population': context['kilifi_female_population'],
        # 'kilifi_intersex_population': context['kilifi_intersex_population'],
        # 'kilifi_total_population': int(context['kilifi_male_population']) + int(
        #     context['kilifi_female_population']) + int(context['kilifi_intersex_population']),
        'tanariver_male_population': context['tanariver_male_population'],
        'tanariver_female_population': context['tanariver_female_population'],
        'tanariver_intersex_population': context['tanariver_intersex_population'],
        'tanariver_total_population': int(context['tanariver_male_population']) + int(
            context['tanariver_female_population']) + int(context['tanariver_intersex_population']),
        # 'lamu_male_population': context['lamu_male_population'],
        # 'lamu_female_population': context['lamu_female_population'],
        # 'lamu_intersex_population': context['lamu_intersex_population'],
        # 'lamu_total_population': int(context['lamu_male_population']) + int(context['lamu_female_population']) + int(
        #     context['lamu_intersex_population']),
        # 'taitataveta_male_population': context['taitataveta_male_population'],
        # 'taitataveta_female_population': context['taitataveta_female_population'],
        # 'taitataveta_intersex_population': context['taitataveta_intersex_population'],
        # 'taitataveta_total_population': int(context['taitataveta_male_population']) + int(
        #     context['taitataveta_female_population']) + int(context['taitataveta_intersex_population']),
        'marsabit_male_population': context['marsabit_male_population'],
        'marsabit_female_population': context['marsabit_female_population'],
        'marsabit_intersex_population': context['marsabit_intersex_population'],
        'marsabit_total_population': int(context['marsabit_male_population']) + int(
            context['marsabit_female_population']) + int(context['marsabit_intersex_population']),
        # 'isiolo_male_population': context['isiolo_male_population'],
        # 'isiolo_female_population': context['isiolo_female_population'],
        # 'isiolo_intersex_population': context['isiolo_intersex_population'],
        # 'isiolo_total_population': int(context['isiolo_male_population']) + int(
        #     context['isiolo_female_population']) + int(context['isiolo_intersex_population']),
        # 'meru_male_population': context['meru_male_population'],
        # 'meru_female_population': context['meru_female_population'],
        # 'meru_intersex_population': context['meru_intersex_population'],
        # 'meru_total_population': int(context['meru_male_population']) + int(context['meru_female_population']) + int(
        #     context['meru_intersex_population']),
        # 'tharaka_male_population': context['tharaka_male_population'],
        # 'tharaka_female_population': context['tharaka_female_population'],
        # 'tharaka_intersex_population': context['tharaka_intersex_population'],
        # 'tharaka_total_population': int(context['tharaka_male_population']) + int(
        #     context['tharaka_female_population']) + int(context['tharaka_intersex_population']),
        # 'embu_male_population': context['embu_male_population'],
        # 'embu_female_population': context['embu_female_population'],
        # 'embu_intersex_population': context['embu_intersex_population'],
        # 'embu_total_population': int(context['embu_male_population']) + int(context['embu_female_population']) + int(
        #     context['embu_intersex_population']),
        # 'kitui_male_population': context['kitui_male_population'],
        # 'kitui_female_population': context['kitui_female_population'],
        # 'kitui_intersex_population': context['kitui_intersex_population'],
        # 'kitui_total_population': int(context['kitui_male_population']) + int(context['kitui_female_population']) + int(
        #     context['kitui_intersex_population']),
        # 'machakos_male_population': context['machakos_male_population'],
        # 'machakos_female_population': context['machakos_female_population'],
        # 'machakos_intersex_population': context['machakos_intersex_population'],
        # 'machakos_total_population': int(context['machakos_male_population']) + int(
        #     context['machakos_female_population']) + int(context['machakos_intersex_population']),
        # 'makueni_male_population': context['makueni_male_population'],
        # 'makueni_female_population': context['makueni_female_population'],
        # 'makueni_intersex_population': context['makueni_intersex_population'],
        # 'makueni_total_population': int(context['makueni_male_population']) + int(
        #     context['makueni_female_population']) + int(context['makueni_intersex_population']),
        'garissa_male_population': context['garissa_male_population'],
        'garissa_female_population': context['garissa_female_population'],
        'garissa_intersex_population': context['garissa_intersex_population'],
        'garissa_total_population': int(context['garissa_male_population']) + int(
            context['garissa_female_population']) + int(context['garissa_intersex_population']),
        'wajir_male_population': context['wajir_male_population'],
        'wajir_female_population': context['wajir_female_population'],
        'wajir_intersex_population': context['wajir_intersex_population'],
        'wajir_total_population': int(context['wajir_male_population']) + int(context['wajir_female_population']) + int(
            context['wajir_intersex_population']),
        # 'mandera_male_population': context['mandera_male_population'],
        # 'mandera_female_population': context['mandera_female_population'],
        # 'mandera_intersex_population': context['mandera_intersex_population'],
        # 'mandera_total_population': int(context['mandera_male_population']) + int(
        #     context['mandera_female_population']) + int(context['mandera_intersex_population']),
        # 'siaya_male_population': context['siaya_male_population'],
        # 'siaya_female_population': context['siaya_female_population'],
        # 'siaya_intersex_population': context['siaya_intersex_population'],
        # 'siaya_total_population': int(context['siaya_male_population']) + int(context['siaya_female_population']) + int(
        #     context['siaya_intersex_population']),
        # 'kisumu_male_population': context['kisumu_male_population'],
        # 'kisumu_female_population': context['kisumu_female_population'],
        # 'kisumu_intersex_population': context['kisumu_intersex_population'],
        # 'kisumu_total_population': int(context['kisumu_male_population']) + int(
        #     context['kisumu_female_population']) + int(context['kisumu_intersex_population']),
        # 'homabay_male_population': context['homabay_male_population'],
        # 'homabay_female_population': context['homabay_female_population'],
        # 'homabay_intersex_population': context['homabay_intersex_population'],
        # 'homabay_total_population': int(context['homabay_male_population']) + int(
        #     context['homabay_female_population']) + int(context['homabay_intersex_population']),
        # 'migori_male_population': context['migori_male_population'],
        # 'migori_female_population': context['migori_female_population'],
        # 'migori_intersex_population': context['migori_intersex_population'],
        # 'migori_total_population': int(context['migori_male_population']) + int(
        #     context['migori_female_population']) + int(context['migori_intersex_population']),
        # 'kisii_male_population': context['kisii_male_population'],
        # 'kisii_female_population': context['kisii_female_population'],
        # 'kisii_intersex_population': context['kisii_intersex_population'],
        # 'kisii_total_population': int(context['kisii_male_population']) + int(context['kisii_female_population']) + int(
        #     context['kisii_intersex_population']),
        # 'nyamira_male_population': context['nyamira_male_population'],
        # 'nyamira_female_population': context['nyamira_female_population'],
        # 'nyamira_intersex_population': context['nyamira_intersex_population'],
        # 'nyamira_total_population': int(context['nyamira_male_population']) + int(
        #     context['nyamira_female_population']) + int(context['nyamira_intersex_population']),
        # 'turkana_male_population': context['turkana_male_population'],
        # 'turkana_female_population': context['turkana_female_population'],
        # 'turkana_intersex_population': context['turkana_intersex_population'],
        # 'turkana_total_population': int(context['turkana_male_population']) + int(
        #     context['turkana_female_population']) + int(context['turkana_intersex_population']),
        # 'westpokot_male_population': context['westpokot_male_population'],
        # 'westpokot_female_population': context['westpokot_female_population'],
        # 'westpokot_intersex_population': context['westpokot_intersex_population'],
        # 'westpokot_total_population': int(context['westpokot_male_population']) + int(
        #     context['westpokot_female_population']) + int(context['westpokot_intersex_population']),
        # 'samburu_male_population': context['samburu_male_population'],
        # 'samburu_female_population': context['samburu_female_population'],
        # 'samburu_intersex_population': context['samburu_intersex_population'],
        # 'samburu_total_population': int(context['samburu_male_population']) + int(
        #     context['samburu_female_population']) + int(context['samburu_intersex_population']),
        # 'transnzoia_male_population': context['transnzoia_male_population'],
        # 'transnzoia_female_population': context['transnzoia_female_population'],
        # 'transnzoia_intersex_population': context['transnzoia_intersex_population'],
        # 'transnzoia_total_population': int(context['transnzoia_male_population']) + int(
        #     context['transnzoia_female_population']) + int(context['transnzoia_intersex_population']),
        'baringo_male_population': context['baringo_male_population'],
        'baringo_female_population': context['baringo_female_population'],
        'baringo_intersex_population': context['baringo_intersex_population'],
        'baringo_total_population': int(context['baringo_male_population']) + int(
            context['baringo_female_population']) + int(context['baringo_intersex_population']),
        # 'uasingishu_male_population': context['uasingishu_male_population'],
        # 'uasingishu_female_population': context['uasingishu_female_population'],
        # 'uasingishu_intersex_population': context['uasingishu_intersex_population'],
        # 'uasingishu_total_population': int(context['uasingishu_male_population']) + int(
        #     context['uasingishu_female_population']) + int(context['uasingishu_intersex_population']),
        # 'elgeyomarakwet_male_population': context['elgeyomarakwet_male_population'],
        # 'elgeyomarakwet_female_population': context['elgeyomarakwet_female_population'],
        # 'elgeyomarakwet_intersex_population': context['elgeyomarakwet_intersex_population'],
        # 'elgeyomarakwet_total_population': int(context['elgeyomarakwet_male_population']) + int(
        #     context['elgeyomarakwet_female_population']) + int(context['elgeyomarakwet_intersex_population']),
        # 'nandi_male_population': context['nandi_male_population'],
        # 'nandi_female_population': context['nandi_female_population'],
        # 'nandi_intersex_population': context['nandi_intersex_population'],
        # 'nandi_total_population': int(context['nandi_male_population']) + int(context['nandi_female_population']) + int(
        #     context['nandi_intersex_population']),
        # 'laikipia_male_population': context['laikipia_male_population'],
        # 'laikipia_female_population': context['laikipia_female_population'],
        # 'laikipia_intersex_population': context['laikipia_intersex_population'],
        # 'laikipia_total_population': int(context['laikipia_male_population']) + int(
        #     context['laikipia_female_population']) + int(context['laikipia_intersex_population']),
        # 'nakuru_male_population': context['nakuru_male_population'],
        # 'nakuru_female_population': context['nakuru_female_population'],
        # 'nakuru_intersex_population': context['nakuru_intersex_population'],
        # 'nakuru_total_population': int(context['nakuru_male_population']) + int(
        #     context['nakuru_female_population']) + int(context['nakuru_intersex_population']),
        # 'narok_male_population': context['narok_male_population'],
        # 'narok_female_population': context['narok_female_population'],
        # 'narok_intersex_population': context['narok_intersex_population'],
        # 'narok_total_population': int(context['narok_male_population']) + int(context['narok_female_population']) + int(
        #     context['narok_intersex_population']),
        # 'kajiado_male_population': context['kajiado_male_population'],
        # 'kajiado_female_population': context['kajiado_female_population'],
        # 'kajiado_intersex_population': context['kajiado_intersex_population'],
        # 'kajiado_total_population': int(context['kajiado_male_population']) + int(
        #     context['kajiado_female_population']) + int(context['kajiado_intersex_population']),
        # 'kericho_male_population': context['kericho_male_population'],
        # 'kericho_female_population': context['kericho_female_population'],
        # 'kericho_intersex_population': context['kericho_intersex_population'],
        # 'kericho_total_population': int(context['kericho_male_population']) + int(
        #     context['kericho_female_population']) + int(context['kericho_intersex_population']),
        # 'bomet_male_population': context['bomet_male_population'],
        # 'bomet_female_population': context['bomet_female_population'],
        # 'bomet_intersex_population': context['bomet_intersex_population'],
        # 'bomet_total_population': int(context['bomet_male_population']) + int(context['bomet_female_population']) + int(
        #     context['bomet_intersex_population']),
        # 'kakamega_male_population': context['kakamega_male_population'],
        # 'kakamega_female_population': context['kakamega_female_population'],
        # 'kakamega_intersex_population': context['kakamega_intersex_population'],
        # 'kakamega_total_population': int(context['kakamega_male_population']) + int(
        #     context['kakamega_female_population']) + int(context['kakamega_intersex_population']),
        # 'vihiga_male_population': context['vihiga_male_population'],
        # 'vihiga_female_population': context['vihiga_female_population'],
        # 'vihiga_intersex_population': context['vihiga_intersex_population'],
        # 'vihiga_total_population': int(context['vihiga_male_population']) + int(
        #     context['vihiga_female_population']) + int(context['vihiga_intersex_population']),
        # 'bungoma_male_population': context['bungoma_male_population'],
        # 'bungoma_female_population': context['bungoma_female_population'],
        # 'bungoma_intersex_population': context['bungoma_intersex_population'],
        # 'bungoma_total_population': int(context['bungoma_male_population']) + int(
        #     context['bungoma_female_population']) + int(context['bungoma_intersex_population']),
        # 'busia_male_population': context['busia_male_population'],
        # 'busia_female_population': context['busia_female_population'],
        # 'busia_intersex_population': context['busia_intersex_population'],
        # 'busia_total_population': int(context['busia_male_population']) + int(context['busia_female_population']) + int(
        #     context['busia_intersex_population']),
    }

    return render(request,'human_dalys.html',context2)

def early_detection(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['early_detection']

    context = {
        '47lang_training_material_design_per_county_quantity': 0,
        '47lang_training_material_design_total_quantity': 0,
        '47lang_training_material_design_unit_cost': 0,
        '47lang_training_material_design_total_cost': 0,
        'print_materials_per_county_quantity': 0,
        'print_materials_total_quantity': 0,
        'print_materials_unit_cost': 0,
        'print_materials_total_cost': 0,
        '15lang_radiospots_per_county_quantity': 0,
        '15lang_radiospots_total_quantity': 0,
        '15lang_radiospots_unit_cost': 0,
        '15lang_radiospots_total_cost': 0,
        'en_swa_radiospots_per_county_quantity': 0,
        'en_swa_radiospots_total_quantity': 0,
        'en_swa_radiospots_unit_cost': 0,
        'en_swa_radiospots_total_cost': 0,
        'tv_commercials_per_county_quantity': 0,
        'tv_commercials_total_quantity': 0,
        'tv_commercials_unit_cost': 0,
        'tv_commercials_total_cost': 0,
        'trainers_training_per_county_quantity': 0,
        'trainers_training_total_quantity': 0,
        'trainers_training_unit_cost': 0,
        'trainers_training_total_cost': 0,
        'farmer_training_per_county_quantity': 0,
        'farmer_training_total_quantity': 0,
        'farmer_training_unit_cost': 0,
        'farmer_training_total_cost': 0,
        'AHA_training_per_county_quantity': 0,
        'AHA_training_total_quantity': 0,
        'AHA_training_unit_cost': 0,
        'AHA_training_total_cost': 0,
        'vet_training_per_county_quantity': 0,
        'vet_training_total_quantity': 0,
        'vet_training_unit_cost': 0,
        'vet_training_total_cost': 0,
        'clinician_training_per_county_quantity': 0,
        'clinician_training_total_quantity': 0,
        'clinician_training_unit_cost': 0,
        'clinician_training_total_cost': 0,
        'transport_per_county_quantity': 0,
        'transport_total_quantity': 0,
        'transport_unit_cost': 0,
        'transport_total_cost': 0,
        'translator_allowance_per_county_quantity': 0,
        'translator_allowance_total_quantity': 0,
        'translator_allowance_unit_cost': 0,
        'translator_allowance_total_cost': 0,
        'vet_epidemiologist_per_county_quantity': 0,
        'vet_epidemiologist_total_quantity': 0,
        'vet_epidemiologist_unit_cost': 0,
        'vet_epidemiologist_total_cost': 0,
        'medical_epidemiologist_per_county_quantity': 0,
        'medical_epidemiologist_total_quantity': 0,
        'medical_epidemiologist_unit_cost': 0,
        'medical_epidemiologist_total_cost': 0,
        'socio_economist_per_county_quantity': 0,
        'socio_economist_total_quantity': 0,
        'socio_economist_unit_cost': 0,
        'socio_economist_total_cost': 0,
        'technician_per_county_quantity': 0,
        'technician_total_quantity': 0,
        'technician_unit_cost': 0,
        'technician_total_cost': 0,
        'driver_per_county_quantity': 0,
        'driver_total_quantity': 0,
        'driver_unit_cost': 0,
        'driver_total_cost': 0,
        'early_detection_total_cost': 0,
    }

    if (request.method == "POST"):
        _47lang_training_material_design_per_county_quantity = request.POST['47lang_training_material_design_per_county_quantity']
        _47lang_training_material_design_total_quantity = request.POST['47lang_training_material_design_total_quantity']
        _47lang_training_material_design_unit_cost = request.POST['47lang_training_material_design_unit_cost']
        _47lang_training_material_design_total_cost = request.POST['47lang_training_material_design_total_cost']
        print_materials_per_county_quantity = request.POST['print_materials_per_county_quantity']
        print_materials_total_quantity = request.POST['print_materials_total_quantity']
        print_materials_unit_cost = request.POST['print_materials_unit_cost']
        print_materials_total_cost = request.POST['print_materials_total_cost']
        _15lang_radiospots_per_county_quantity = request.POST['15lang_radiospots_per_county_quantity']
        _15lang_radiospots_total_quantity = request.POST['15lang_radiospots_total_quantity']
        _15lang_radiospots_unit_cost = request.POST['15lang_radiospots_unit_cost']
        _15lang_radiospots_total_cost = request.POST['15lang_radiospots_total_cost']
        en_swa_radiospots_per_county_quantity = request.POST['en_swa_radiospots_per_county_quantity']
        en_swa_radiospots_total_quantity = request.POST['en_swa_radiospots_total_quantity']
        en_swa_radiospots_unit_cost = request.POST['en_swa_radiospots_unit_cost']
        en_swa_radiospots_total_cost = request.POST['en_swa_radiospots_total_cost']
        tv_commercials_per_county_quantity = request.POST['tv_commercials_per_county_quantity']
        tv_commercials_total_quantity = request.POST['tv_commercials_total_quantity']
        tv_commercials_unit_cost = request.POST['tv_commercials_unit_cost']
        tv_commercials_total_cost = request.POST['tv_commercials_total_cost']
        trainers_training_per_county_quantity = request.POST['trainers_training_per_county_quantity']
        trainers_training_total_quantity = request.POST['trainers_training_total_quantity']
        trainers_training_unit_cost = request.POST['trainers_training_unit_cost']
        trainers_training_total_cost = request.POST['trainers_training_total_cost']
        farmer_training_per_county_quantity = request.POST['farmer_training_per_county_quantity']
        farmer_training_total_quantity = request.POST['farmer_training_total_quantity']
        farmer_training_unit_cost = request.POST['farmer_training_unit_cost']
        farmer_training_total_cost = request.POST['farmer_training_total_cost']
        AHA_training_per_county_quantity = request.POST['AHA_training_per_county_quantity']
        AHA_training_total_quantity = request.POST['AHA_training_total_quantity']
        AHA_training_unit_cost = request.POST['AHA_training_unit_cost']
        AHA_training_total_cost = request.POST['AHA_training_total_cost']
        vet_training_per_county_quantity = request.POST['vet_training_per_county_quantity']
        vet_training_total_quantity = request.POST['vet_training_total_quantity']
        vet_training_unit_cost = request.POST['vet_training_unit_cost']
        vet_training_total_cost = request.POST['vet_training_total_cost']
        clinician_training_per_county_quantity = request.POST['clinician_training_per_county_quantity']
        clinician_training_total_quantity = request.POST['clinician_training_total_quantity']
        clinician_training_unit_cost = request.POST['clinician_training_unit_cost']
        clinician_training_total_cost = request.POST['clinician_training_total_cost']
        transport_per_county_quantity = request.POST['transport_per_county_quantity']
        transport_total_quantity = request.POST['transport_total_quantity']
        transport_unit_cost = request.POST['transport_unit_cost']
        transport_total_cost = request.POST['transport_total_cost']
        translator_allowance_per_county_quantity = request.POST['translator_allowance_per_county_quantity']
        translator_allowance_total_quantity = request.POST['translator_allowance_total_quantity']
        translator_allowance_unit_cost = request.POST['translator_allowance_unit_cost']
        translator_allowance_total_cost = request.POST['translator_allowance_total_cost']
        vet_epidemiologist_per_county_quantity = request.POST['vet_epidemiologist_per_county_quantity']
        vet_epidemiologist_total_quantity = request.POST['vet_epidemiologist_total_quantity']
        vet_epidemiologist_unit_cost = request.POST['vet_epidemiologist_unit_cost']
        vet_epidemiologist_total_cost = request.POST['vet_epidemiologist_total_cost']
        medical_epidemiologist_per_county_quantity = request.POST['medical_epidemiologist_per_county_quantity']
        medical_epidemiologist_total_quantity = request.POST['medical_epidemiologist_total_quantity']
        medical_epidemiologist_unit_cost = request.POST['medical_epidemiologist_unit_cost']
        medical_epidemiologist_total_cost = request.POST['medical_epidemiologist_total_cost']
        socio_economist_per_county_quantity = request.POST['socio_economist_per_county_quantity']
        socio_economist_total_quantity = request.POST['socio_economist_total_quantity']
        socio_economist_unit_cost = request.POST['socio_economist_unit_cost']
        socio_economist_total_cost = request.POST['socio_economist_total_cost']
        technician_per_county_quantity = request.POST['technician_per_county_quantity']
        technician_total_quantity = request.POST['technician_total_quantity']
        technician_unit_cost = request.POST['technician_unit_cost']
        technician_total_cost = request.POST['technician_total_cost']
        driver_per_county_quantity = request.POST['driver_per_county_quantity']
        driver_total_quantity = request.POST['driver_total_quantity']
        driver_unit_cost = request.POST['driver_unit_cost']
        driver_total_cost = request.POST['driver_total_cost']
        early_detection_total_cost = request.POST['early_detection_total_cost']

        x = rvf_initial_collection.insert_one({
            '47lang_training_material_design_per_county_quantity': _47lang_training_material_design_per_county_quantity,
            '47lang_training_material_design_total_quantity': _47lang_training_material_design_total_quantity,
            '47lang_training_material_design_unit_cost': _47lang_training_material_design_unit_cost,
            '47lang_training_material_design_total_cost': _47lang_training_material_design_total_cost,
            'print_materials_per_county_quantity': print_materials_per_county_quantity,
            'print_materials_total_quantity': print_materials_total_quantity,
            'print_materials_unit_cost': print_materials_unit_cost,
            'print_materials_total_cost': print_materials_total_cost,
            '15lang_radiospots_per_county_quantity': _15lang_radiospots_per_county_quantity,
            '15lang_radiospots_total_quantity': _15lang_radiospots_total_quantity,
            '15lang_radiospots_unit_cost': _15lang_radiospots_unit_cost,
            '15_lang_radiospots_total_cost': _15lang_radiospots_total_cost,
            'en_swa_radiospots_per_county_quantity': en_swa_radiospots_per_county_quantity,
            'en_swa_radiospots_total_quantity': en_swa_radiospots_total_quantity,
            'en_swa_radiospots_unit_cost': en_swa_radiospots_unit_cost,
            'en_swa_radiospots_total_cost': en_swa_radiospots_total_cost,
            'tv_commercials_per_county_quantity': tv_commercials_per_county_quantity,
            'tv_commercials_total_quantity': tv_commercials_total_quantity,
            'tv_commercials_unit_cost': tv_commercials_unit_cost,
            'tv_commercials_total_cost': tv_commercials_total_cost,
            'trainers_training_per_county_quantity': trainers_training_per_county_quantity,
            'trainers_training_total_quantity': trainers_training_total_quantity,
            'trainers_training_unit_cost': trainers_training_unit_cost,
            'trainers_training_total_cost': trainers_training_total_cost,
            'farmer_training_per_county_quantity': farmer_training_per_county_quantity,
            'farmer_training_total_quantity': farmer_training_total_quantity,
            'farmer_training_unit_cost': farmer_training_unit_cost,
            'farmer_training_total_cost': farmer_training_total_cost,
            'AHA_training_per_county_quantity': AHA_training_per_county_quantity,
            'AHA_training_total_quantity': AHA_training_total_quantity,
            'AHA_training_unit_cost': AHA_training_unit_cost,
            'AHA_training_total_cost': AHA_training_total_cost,
            'vet_training_per_county_quantity': vet_training_per_county_quantity,
            'vet_training_total_quantity': vet_training_total_quantity,
            'vet_training_unit_cost': vet_training_unit_cost,
            'vet_training_total_cost': vet_training_total_cost,
            'clinician_training_per_county_quantity': clinician_training_per_county_quantity,
            'clinician_training_total_quantity': clinician_training_total_quantity,
            'clinician_training_unit_cost': clinician_training_unit_cost,
            'clinician_training_total_cost': clinician_training_total_cost,
            'transport_per_county_quantity': transport_per_county_quantity,
            'transport_total_quantity': transport_total_quantity,
            'transport_unit_cost': transport_unit_cost,
            'transport_total_cost': transport_total_cost,
            'translator_allowance_per_county_quantity': translator_allowance_per_county_quantity,
            'translator_allowance_total_quantity': translator_allowance_total_quantity,
            'translator_allowance_unit_cost': translator_allowance_unit_cost,
            'translator_allowance_total_cost': translator_allowance_total_cost,
            'vet_epidemiologist_per_county_quantity': vet_epidemiologist_per_county_quantity,
            'vet_epidemiologist_total_quantity': vet_epidemiologist_total_quantity,
            'vet_epidemiologist_unit_cost': vet_epidemiologist_unit_cost,
            'vet_epidemiologist_total_cost': vet_epidemiologist_total_cost,
            'medical_epidemiologist_per_county_quantity': medical_epidemiologist_per_county_quantity,
            'medical_epidemiologist_total_quantity': medical_epidemiologist_total_quantity,
            'medical_epidemiologist_unit_cost': medical_epidemiologist_unit_cost,
            'medical_epidemiologist_total_cost': medical_epidemiologist_total_cost,
            'socio_economist_per_county_quantity': socio_economist_per_county_quantity,
            'socio_economist_total_quantity': socio_economist_total_quantity,
            'socio_economist_unit_cost': socio_economist_unit_cost,
            'socio_economist_total_cost': socio_economist_total_cost,
            'technician_per_county_quantity': technician_per_county_quantity,
            'technician_total_quantity': technician_total_quantity,
            'technician_unit_cost': technician_unit_cost,
            'technician_total_cost': technician_total_cost,
            'driver_per_county_quantity': driver_per_county_quantity,
            'driver_total_quantity': driver_total_quantity,
            'driver_unit_cost': driver_unit_cost,
            'driver_total_cost': driver_total_cost,
            'early_detection_total_cost': int(_47lang_training_material_design_total_cost)+
                                            int(print_materials_total_cost),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        '47lang_training_material_design_per_county_quantity': context[
            '47lang_training_material_design_per_county_quantity'],
        '47lang_training_material_design_total_quantity': int(
            context['47lang_training_material_design_per_county_quantity']) * 47,
        '47lang_training_material_design_unit_cost': context['47lang_training_material_design_unit_cost'],
        '47lang_training_material_design_total_cost': int(
            context['47lang_training_material_design_total_quantity']) * int(
            context['47lang_training_material_design_unit_cost']),
        'print_materials_per_county_quantity': context['print_materials_per_county_quantity'],
        'print_materials_total_quantity': int(context['print_materials_per_county_quantity']) * 47,
        'print_materials_unit_cost': context['print_materials_unit_cost'],
        'print_materials_total_cost': int(context['print_materials_total_quantity']) * int(
            context['print_materials_unit_cost']),'15lang_radiospots_per_county_quantity': context[
            '15lang_radiospots_per_county_quantity'],
        '15lang_radiospots_total_quantity': int(context['15lang_radiospots_per_county_quantity']) * 15,
        '15lang_radiospots_unit_cost': context['15lang_radiospots_unit_cost'],
        '15lang_radiospots_total_cost': int(context['15lang_radiospots_total_quantity']) * int(
            context['15lang_radiospots_unit_cost']),
        'en_swa_radiospots_per_county_quantity': context['en_swa_radiospots_per_county_quantity'],
        'en_swa_radiospots_total_quantity': 2,
        'en_swa_radiospots_unit_cost': context['en_swa_radiospots_unit_cost'],
        'en_swa_radiospots_total_cost': int(context['en_swa_radiospots_total_quantity']) * int(
            context['en_swa_radiospots_unit_cost']),
        'tv_commercials_per_county_quantity': context['tv_commercials_per_county_quantity'],
        'tv_commercials_total_quantity': int(context['tv_commercials_per_county_quantity']) * 20,
        'tv_commercials_unit_cost': context['tv_commercials_unit_cost'],
        'tv_commercials_total_cost': int(context['tv_commercials_total_quantity']) * int(context['tv_commercials_unit_cost']), 'trainers_training_per_county_quantity': context[
            'trainers_training_per_county_quantity'],
        'trainers_training_total_quantity': int(context['trainers_training_per_county_quantity']) * 47,
        'trainers_training_unit_cost': context['trainers_training_unit_cost'],
        'trainers_training_total_cost': int(context['trainers_training_total_quantity']) * int(
            context['trainers_training_unit_cost']),
        'farmer_training_per_county_quantity': context['farmer_training_per_county_quantity'],
        'farmer_training_total_quantity': int(context['farmer_training_per_county_quantity']) * 47,
        'farmer_training_unit_cost': context['farmer_training_unit_cost'],
        'farmer_training_total_cost': int(context['farmer_training_total_quantity']) * int(
            context['farmer_training_unit_cost']),
        'AHA_training_per_county_quantity': context['AHA_training_per_county_quantity'],
        'AHA_training_total_quantity': int(context['AHA_training_per_county_quantity']) * 47,
        'AHA_training_unit_cost': context['AHA_training_unit_cost'],
        'AHA_training_total_cost': int(context['AHA_training_total_quantity']) * int(context['AHA_training_unit_cost']),
        'vet_training_per_county_quantity': context['vet_training_per_county_quantity'],
        'vet_training_total_quantity': int(context['vet_training_per_county_quantity']) * 47,
        'vet_training_unit_cost': context['vet_training_unit_cost'],
        'vet_training_total_cost': int(context['vet_training_total_quantity']) * int(context['vet_training_unit_cost']),
        'clinician_training_per_county_quantity': context['clinician_training_per_county_quantity'],
        'clinician_training_total_quantity': int(context['clinician_training_per_county_quantity']) * 47,
        'clinician_training_unit_cost': context['clinician_training_unit_cost'],
        'clinician_training_total_cost': int(context['clinician_training_total_quantity']) * int(
            context['clinician_training_unit_cost']),
        'transport_per_county_quantity': context['transport_per_county_quantity'],
        'transport_total_quantity': int(context['transport_per_county_quantity']) * 3,
        'transport_unit_cost': context['transport_unit_cost'],
        'transport_total_cost': int(context['transport_total_quantity']) * int(context['transport_unit_cost']),
        'translator_allowance_per_county_quantity': context['translator_allowance_per_county_quantity'],
        'translator_allowance_total_quantity': int(context['translator_allowance_per_county_quantity']) * 2,
        'translator_allowance_unit_cost': context['translator_allowance_unit_cost'],
        'translator_allowance_total_cost': int(context['translator_allowance_total_quantity']) * int(
            context['translator_allowance_unit_cost']),
        'vet_epidemiologist_per_county_quantity': context['vet_epidemiologist_per_county_quantity'],
        'vet_epidemiologist_total_quantity': int(context['vet_epidemiologist_per_county_quantity']) * 3,
        'vet_epidemiologist_unit_cost': context['vet_epidemiologist_unit_cost'],
        'vet_epidemiologist_total_cost': int(context['vet_epidemiologist_total_quantity']) * int(
            context['vet_epidemiologist_unit_cost']),
        'medical_epidemiologist_per_county_quantity': context['medical_epidemiologist_per_county_quantity'],
        'medical_epidemiologist_total_quantity': int(context['medical_epidemiologist_per_county_quantity']) * 3,
        'medical_epidemiologist_unit_cost': context['medical_epidemiologist_unit_cost'],
        'medical_epidemiologist_total_cost': int(context['medical_epidemiologist_total_quantity']) * int(
            context['medical_epidemiologist_unit_cost']),
        'socio_economist_per_county_quantity': context['socio_economist_per_county_quantity'],
        'socio_economist_total_quantity': int(context['socio_economist_per_county_quantity']) * 3,
        'socio_economist_unit_cost': context['socio_economist_unit_cost'],
        'socio_economist_total_cost': int(context['socio_economist_total_quantity']) * int(
            context['socio_economist_unit_cost']),
        'technician_per_county_quantity': context['technician_per_county_quantity'],
        'technician_total_quantity': int(context['technician_per_county_quantity']) * 3,
        'technician_unit_cost': context['technician_unit_cost'],
        'technician_total_cost': int(context['technician_total_quantity']) * int(context['technician_unit_cost']),
        'driver_per_county_quantity': context['driver_per_county_quantity'],
        'driver_total_quantity': int(context['driver_per_county_quantity']) * 3,
        'driver_unit_cost': context['driver_unit_cost'],
        'driver_total_cost': int(context['driver_total_quantity']) * int(context['driver_unit_cost']),
        'early_detection_total_cost': context['early_detection_total_cost'],

    }

    return render(request,'early_detection.html',context2)

def passive_surveillance(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['passive_surveillance']

    context = {
        'headman_total_quantity': 705,
        'headman_unit_cost': 0,
        'headman_total_cost': 0,
        'headman_annual_depreciation': 0,
        'headman_annual_cost': 0,
        'headman_remarks': 0,
        'veterinarians_total_quantity': 470,
        'veterinarians_unit_cost': 0,
        'veterinarians_total_cost': 0,
        'veterinarians_annual_depreciation': 0,
        'veterinarians_annual_cost': 0,
        'veterinarians_remarks': 0,
        'livestock_production_officers_total_quantity': 470,
        'livestock_production_officers_unit_cost': 0,
        'livestock_production_officers_total_cost': 0,
        'livestock_production_officers_annual_depreciation': 0,
        'livestock_production_officers_annual_cost': 0,
        'livestock_production_officers_remarks': 0,
        'CHWs_total_quantity': 705,
        'CHWs_unit_cost': 0,
        'CHWs_total_cost': 0,
        'CHWs_annual_depreciation': 0,
        'CHWs_annual_cost': 0,
        'CHWs_remarks': 0,
        'clinicians_total_quantity': 470,
        'clinicians_unit_cost': 0,
        'clinicians_total_cost': 0,
        'clinicians_annual_depreciation': 0,
        'clinicians_annual_cost': 0,
        'clinicians_remarks': 0,
        'nurses_total_quantity': 470,
        'nurses_unit_cost': 0,
        'nurses_total_cost': 0,
        'nurses_annual_depreciation': 0,
        'nurses_annual_cost': 0,
        'nurses_remarks': 0,
        'doctors_total_quantity': 235,
        'doctors_unit_cost': 0,
        'doctors_total_cost': 0,
        'doctors_annual_depreciation': 0,
        'doctors_annual_cost': 0,
        'doctors_remarks': 0,
        'CHO_total_quantity': 47,
        'CHO_unit_cost': 0,
        'CHO_total_cost': 0,
        'CHO_annual_depreciation': 0,
        'CHO_annual_cost': 0,
        'CHO_remarks': 0,
        'ground_truthing_fuel_total_quantity': 47,
        'ground_truthing_fuel_unit_cost': 0,
        'ground_truthing_fuel_total_cost': 0,
        'ground_truthing_fuel_annual_depreciation': 0,
        'ground_truthing_fuel_annual_cost': 0,
        'ground_truthing_fuel_remarks': 0,
        'satellite_phones_total_quantity': 22,
        'satellite_phones_unit_cost': 0,
        'satellite_phones_total_cost': 0,
        'satellite_phones_annual_depreciation': 0,
        'satellite_phones_annual_cost': 0,
        'satellite_phones_remarks': 0,
        'laptop_total_quantity': 235,
        'laptop_unit_cost': 0,
        'laptop_total_cost': 0,
        'laptop_annual_depreciation': 0,
        'laptop_annual_cost': 0,
        'laptop_remarks': 0,
        'digital_pens_total_quantity': 940,
        'digital_pens_unit_cost': 0,
        'digital_pens_total_cost': 0,
        'digital_pens_annual_depreciation': 0,
        'digital_pens_annual_cost': 0,
        'digital_pens_remarks': 0,
        'GIS_compartible_phones_total_quantity': 940,
        'GIS_compartible_phones_unit_cost': 0,
        'GIS_compartible_phones_total_cost': 0,
        'GIS_compartible_phones_annual_depreciation': 0,
        'GIS_compartible_phones_annual_cost': 0,
        'GIS_compartible_phones_remarks': 0,
        'GIS_compartible_forms_total_quantity': 94000,
        'GIS_compartible_forms_unit_cost': 0,
        'GIS_compartible_forms_total_cost': 0,
        'GIS_compartible_forms_annual_depreciation': 0,
        'GIS_compartible_forms_annual_cost': 0,
        'GIS_compartible_forms_remarks': 0,
        'server_fees_total_quantity': 1,
        'server_fees_unit_cost': 0,
        'server_fees_total_cost': 0,
        'server_fees_annual_depreciation': 0,
        'server_fees_annual_cost': 0,
        'server_fees_remarks': 0,
        'digital_pen_licenses_total_quantity': 940,
        'digital_pen_licenses_unit_cost': 0,
        'digital_pen_licenses_total_cost': 0,
        'digital_pen_licenses_annual_depreciation': 0,
        'digital_pen_licenses_annual_cost': 0,
        'digital_pen_licenses_remarks': 0,
        'passive_surveillance_total_annual_cost': 0,
    }

    if (request.method == "POST"):
        headman_total_quantity = request.POST['headman_total_quantity']
        headman_unit_cost = request.POST['headman_unit_cost']
        headman_total_cost = request.POST['headman_total_cost']
        headman_annual_depreciation = request.POST['headman_annual_depreciation']
        headman_annual_cost = request.POST['headman_total_cost']
        headman_remarks = request.POST['headman_remarks']
        veterinarians_total_quantity = request.POST['veterinarians_total_quantity']
        veterinarians_unit_cost = request.POST['veterinarians_unit_cost']
        veterinarians_total_cost = request.POST['veterinarians_total_cost']
        veterinarians_annual_depreciation = request.POST['veterinarians_annual_depreciation']
        veterinarians_annual_cost = request.POST['veterinarians_total_cost']
        veterinarians_remarks = request.POST['veterinarians_remarks']
        livestock_production_officers_total_quantity = request.POST['livestock_production_officers_total_quantity']
        livestock_production_officers_unit_cost = request.POST['livestock_production_officers_unit_cost']
        livestock_production_officers_total_cost = request.POST['livestock_production_officers_total_cost']
        livestock_production_officers_annual_depreciation = request.POST['livestock_production_officers_annual_depreciation']
        livestock_production_officers_annual_cost = request.POST['livestock_production_officers_total_cost']
        livestock_production_officers_remarks = request.POST['livestock_production_officers_remarks']
        CHWs_total_quantity = request.POST['CHWs_total_quantity']
        CHWs_unit_cost = request.POST['CHWs_unit_cost']
        CHWs_total_cost = request.POST['CHWs_total_cost']
        CHWs_annual_depreciation = request.POST['CHWs_annual_depreciation']
        CHWs_annual_cost = request.POST['CHWs_total_cost']
        CHWs_remarks = request.POST['CHWs_remarks']
        clinicians_total_quantity = request.POST['clinicians_total_quantity']
        clinicians_unit_cost = request.POST['clinicians_unit_cost']
        clinicians_total_cost = request.POST['clinicians_total_cost']
        clinicians_annual_depreciation = request.POST['clinicians_annual_depreciation']
        clinicians_annual_cost = request.POST['clinicians_total_cost']
        clinicians_remarks = request.POST['clinicians_remarks']
        nurses_total_quantity = request.POST['nurses_total_quantity']
        nurses_unit_cost = request.POST['nurses_unit_cost']
        nurses_total_cost = request.POST['nurses_total_cost']
        nurses_annual_depreciation = request.POST['nurses_annual_depreciation']
        nurses_annual_cost = request.POST['nurses_total_cost']
        nurses_remarks = request.POST['nurses_remarks']
        doctors_total_quantity = request.POST['doctors_total_quantity']
        doctors_unit_cost = request.POST['doctors_unit_cost']
        doctors_total_cost = request.POST['doctors_total_cost']
        doctors_annual_depreciation = request.POST['doctors_annual_depreciation']
        doctors_annual_cost = request.POST['doctors_total_cost']
        doctors_remarks = request.POST['doctors_remarks']
        CHO_total_quantity = request.POST['CHO_total_quantity']
        CHO_unit_cost = request.POST['CHO_unit_cost']
        CHO_total_cost = request.POST['CHO_total_cost']
        CHO_annual_depreciation = request.POST['CHO_annual_depreciation']
        CHO_annual_cost = request.POST['CHO_total_cost']
        CHO_remarks = request.POST['CHO_remarks']
        ground_truthing_fuel_total_quantity = request.POST['ground_truthing_fuel_total_quantity']
        ground_truthing_fuel_unit_cost = request.POST['ground_truthing_fuel_unit_cost']
        ground_truthing_fuel_total_cost = request.POST['ground_truthing_fuel_total_cost']
        ground_truthing_fuel_annual_depreciation = request.POST['ground_truthing_fuel_annual_depreciation']
        ground_truthing_fuel_annual_cost = request.POST['ground_truthing_fuel_total_cost']
        ground_truthing_fuel_remarks = request.POST['ground_truthing_fuel_remarks']
        satellite_phones_total_quantity = request.POST['satellite_phones_total_quantity']
        satellite_phones_unit_cost = request.POST['satellite_phones_unit_cost']
        satellite_phones_total_cost = request.POST['satellite_phones_total_cost']
        satellite_phones_annual_depreciation = request.POST['satellite_phones_annual_depreciation']
        satellite_phones_annual_cost = request.POST['satellite_phones_total_cost']
        satellite_phones_remarks = request.POST['satellite_phones_remarks']
        laptop_total_quantity = request.POST['laptop_total_quantity']
        laptop_unit_cost = request.POST['laptop_unit_cost']
        laptop_total_cost = request.POST['laptop_total_cost']
        laptop_annual_depreciation = request.POST['laptop_annual_depreciation']
        laptop_annual_cost = request.POST['laptop_total_cost']
        laptop_remarks = request.POST['laptop_remarks']
        digital_pens_total_quantity = request.POST['digital_pens_total_quantity']
        digital_pens_unit_cost = request.POST['digital_pens_unit_cost']
        digital_pens_total_cost = request.POST['digital_pens_total_cost']
        digital_pens_annual_depreciation = request.POST['digital_pens_annual_depreciation']
        digital_pens_annual_cost = request.POST['digital_pens_total_cost']
        digital_pens_remarks = request.POST['digital_pens_remarks']
        GIS_compartible_phones_total_quantity = request.POST['GIS_compartible_phones_total_quantity']
        GIS_compartible_phones_unit_cost = request.POST['GIS_compartible_phones_unit_cost']
        GIS_compartible_phones_total_cost = request.POST['GIS_compartible_phones_total_cost']
        GIS_compartible_phones_annual_depreciation = request.POST['GIS_compartible_phones_annual_depreciation']
        GIS_compartible_phones_annual_cost = request.POST['GIS_compartible_phones_total_cost']
        GIS_compartible_phones_remarks = request.POST['GIS_compartible_phones_remarks']
        GIS_compartible_forms_total_quantity = request.POST['GIS_compartible_forms_total_quantity']
        GIS_compartible_forms_unit_cost = request.POST['GIS_compartible_forms_unit_cost']
        GIS_compartible_forms_total_cost = request.POST['GIS_compartible_forms_total_cost']
        GIS_compartible_forms_annual_depreciation = request.POST['GIS_compartible_forms_annual_depreciation']
        GIS_compartible_forms_annual_cost = request.POST['GIS_compartible_forms_total_cost']
        GIS_compartible_forms_remarks = request.POST['GIS_compartible_forms_remarks']
        server_fees_total_quantity = request.POST['server_fees_total_quantity']
        server_fees_unit_cost = request.POST['server_fees_unit_cost']
        server_fees_total_cost = request.POST['server_fees_total_cost']
        server_fees_annual_depreciation = request.POST['server_fees_annual_depreciation']
        server_fees_annual_cost = request.POST['server_fees_total_cost']
        server_fees_remarks = request.POST['server_fees_remarks']
        digital_pen_licenses_total_quantity = request.POST['digital_pen_licenses_total_quantity']
        digital_pen_licenses_unit_cost = request.POST['digital_pen_licenses_unit_cost']
        digital_pen_licenses_total_cost = request.POST['digital_pen_licenses_total_cost']
        digital_pen_licenses_annual_depreciation = request.POST['digital_pen_licenses_annual_depreciation']
        digital_pen_licenses_annual_cost = request.POST['digital_pen_licenses_total_cost']
        digital_pen_licenses_remarks = request.POST['digital_pen_licenses_remarks']
        headman_total_quantity = request.POST['headman_total_quantity']
        headman_unit_cost = request.POST['headman_unit_cost']
        headman_total_cost = request.POST['headman_total_cost']
        headman_annual_depreciation = request.POST['headman_annual_depreciation']
        headman_annual_cost = request.POST['headman_total_cost']
        headman_remarks = request.POST['headman_remarks']
        passive_surveillance_total_annual_cost = request.POST['passive_surveillance_total_annual_cost']

        x = rvf_initial_collection.insert_one({
            'headman_total_quantity': headman_total_quantity,
            'headman_unit_cost': headman_unit_cost,
            'headman_total_cost': int(headman_total_quantity) * int(headman_unit_cost),
            'headman_annual_depreciation': headman_annual_depreciation,
            'headman_annual_cost': int(headman_total_cost) * 12,
            'headman_remarks': headman_remarks,
            'veterinarians_total_quantity': veterinarians_total_quantity,
            'veterinarians_unit_cost': veterinarians_unit_cost,
            'veterinarians_total_cost': int(veterinarians_total_quantity) * int(veterinarians_unit_cost),
            'veterinarians_annual_depreciation': veterinarians_annual_depreciation,
            'veterinarians_annual_cost': int(veterinarians_total_cost) * 12,
            'veterinarians_remarks': veterinarians_remarks,
            'livestock_production_officers_total_quantity': livestock_production_officers_total_quantity,
            'livestock_production_officers_unit_cost': livestock_production_officers_unit_cost,
            'livestock_production_officers_total_cost': int(livestock_production_officers_total_quantity) * int(
                livestock_production_officers_unit_cost),
            'livestock_production_officers_annual_depreciation': livestock_production_officers_annual_depreciation,
            'livestock_production_officers_annual_cost': int(livestock_production_officers_total_cost) * 12,
            'livestock_production_officers_remarks': livestock_production_officers_remarks,
            'CHWs_total_quantity': CHWs_total_quantity,
            'CHWs_unit_cost': CHWs_unit_cost,
            'CHWs_total_cost': int(CHWs_total_quantity) * int(CHWs_unit_cost),
            'CHWs_annual_depreciation': CHWs_annual_depreciation,
            'CHWs_annual_cost': int(CHWs_total_cost) * 12,
            'CHWs_remarks': CHWs_remarks,
            'clinicians_total_quantity': clinicians_total_quantity,
            'clinicians_unit_cost': clinicians_unit_cost,
            'clinicians_total_cost': int(clinicians_total_quantity) * int(clinicians_unit_cost),
            'clinicians_annual_depreciation': clinicians_annual_depreciation,
            'clinicians_annual_cost': int(clinicians_total_cost) * 12,
            'clinicians_remarks': clinicians_remarks,
            'nurses_total_quantity': nurses_total_quantity,
            'nurses_unit_cost': nurses_unit_cost,
            'nurses_total_cost': int(nurses_total_quantity) * int(nurses_unit_cost),
            'nurses_annual_depreciation': nurses_annual_depreciation,
            'nurses_annual_cost': int(nurses_total_cost) * 12,
            'nurses_remarks': nurses_remarks,
            'doctors_total_quantity': doctors_total_quantity,
            'doctors_unit_cost': doctors_unit_cost,
            'doctors_total_cost': int(doctors_total_quantity) * int(doctors_unit_cost),
            'doctors_annual_depreciation': doctors_annual_depreciation,
            'doctors_annual_cost': int(doctors_total_cost) * 12,
            'doctors_remarks': doctors_remarks,
            'CHO_total_quantity': CHO_total_quantity,
            'CHO_unit_cost': CHO_unit_cost,
            'CHO_total_cost': int(CHO_total_quantity) * int(CHO_unit_cost),
            'CHO_annual_depreciation': CHO_annual_depreciation,
            'CHO_annual_cost': int(CHO_total_cost) * 12,
            'CHO_remarks': CHO_remarks,
            'ground_truthing_fuel_total_quantity': ground_truthing_fuel_total_quantity,
            'ground_truthing_fuel_unit_cost': ground_truthing_fuel_unit_cost,
            'ground_truthing_fuel_total_cost': int(ground_truthing_fuel_total_quantity) * int(
                ground_truthing_fuel_unit_cost),
            'ground_truthing_fuel_annual_depreciation': ground_truthing_fuel_annual_depreciation,
            'ground_truthing_fuel_annual_cost': int(ground_truthing_fuel_total_cost) * 12,
            'ground_truthing_fuel_remarks': ground_truthing_fuel_remarks,
            'satellite_phones_total_quantity': satellite_phones_total_quantity,
            'satellite_phones_unit_cost': satellite_phones_unit_cost,
            'satellite_phones_total_cost': int(satellite_phones_total_quantity) * int(satellite_phones_unit_cost),
            'satellite_phones_annual_depreciation': int(satellite_phones_total_cost) / 5,
            'satellite_phones_annual_cost': int(satellite_phones_total_cost) / 5,
            'satellite_phones_remarks': satellite_phones_remarks,
            'laptop_total_quantity': laptop_total_quantity,
            'laptop_unit_cost': laptop_unit_cost,
            'laptop_total_cost': int(laptop_total_quantity) * int(laptop_unit_cost),
            'laptop_annual_depreciation': int(laptop_total_cost) / 5,
            'laptop_annual_cost': int(laptop_total_cost) / 5,
            'laptop_remarks': laptop_remarks,
            'digital_pens_total_quantity': digital_pens_total_quantity,
            'digital_pens_unit_cost': digital_pens_unit_cost,
            'digital_pens_total_cost': int(digital_pens_total_quantity) * int(digital_pens_unit_cost),
            'digital_pens_annual_depreciation': int(digital_pens_total_cost) / 5,
            'digital_pens_annual_cost': int(digital_pens_total_cost) / 5,
            'digital_pens_remarks': digital_pens_remarks,
            'GIS_compartible_phones_total_quantity': GIS_compartible_phones_total_quantity,
            'GIS_compartible_phones_unit_cost': GIS_compartible_phones_unit_cost,
            'GIS_compartible_phones_total_cost': int(GIS_compartible_phones_total_quantity) * int(
                GIS_compartible_phones_unit_cost),
            'GIS_compartible_phones_annual_depreciation': int(GIS_compartible_phones_total_cost) / 5,
            'GIS_compartible_phones_annual_cost': int(GIS_compartible_phones_total_cost) / 5,
            'GIS_compartible_phones_remarks': GIS_compartible_phones_remarks,
            'GIS_compartible_forms_total_quantity': GIS_compartible_forms_total_quantity,
            'GIS_compartible_forms_unit_cost': GIS_compartible_forms_unit_cost,
            'GIS_compartible_forms_total_cost': int(GIS_compartible_forms_total_quantity) * int(
                GIS_compartible_forms_unit_cost),
            'GIS_compartible_forms_annual_depreciation': GIS_compartible_forms_annual_depreciation,
            'GIS_compartible_forms_annual_cost': int(GIS_compartible_forms_total_cost),
            'GIS_compartible_forms_remarks': GIS_compartible_forms_remarks,
            'server_fees_total_quantity': server_fees_total_quantity,
            'server_fees_unit_cost': server_fees_unit_cost,
            'server_fees_total_cost': int(server_fees_total_quantity) * int(server_fees_unit_cost),
            'server_fees_annual_depreciation': int(server_fees_total_cost) / 5,
            'server_fees_annual_cost': int(server_fees_total_cost) / 5,
            'server_fees_remarks': server_fees_remarks,
            'digital_pen_licenses_total_quantity': digital_pen_licenses_total_quantity,
            'digital_pen_licenses_unit_cost': digital_pen_licenses_unit_cost,
            'digital_pen_licenses_total_cost': int(digital_pen_licenses_total_quantity) * int(
                digital_pen_licenses_unit_cost),
            'digital_pen_licenses_annual_depreciation': digital_pen_licenses_annual_depreciation,
            'digital_pen_licenses_annual_cost': int(digital_pen_licenses_total_cost) / 12,
            'digital_pen_licenses_remarks': digital_pen_licenses_remarks,
            'passive_surveillance_total_annual_cost': (int(headman_annual_cost) * 12) + (
                        int(veterinarians_total_cost) * 12) +
                                                      (int(livestock_production_officers_total_cost) * 12) + (
                                                                  int(CHWs_total_cost) * 12) +
                                                      (int(clinicians_total_cost) * 12) + (
                                                                  int(nurses_total_cost) * 12) +
                                                      (int(doctors_total_cost) * 12) + (int(CHO_total_cost) * 12) +
                                                      (int(ground_truthing_fuel_total_cost) * 12) + (
                                                                  int(satellite_phones_total_cost) / 5) +
                                                      (int(laptop_total_cost) / 5) + (
                                                                  int(digital_pens_total_cost) / 5) +
                                                      (int(GIS_compartible_phones_total_cost) / 5) + (
                                                          int(GIS_compartible_forms_total_cost)) +
                                                      (int(server_fees_total_cost) / 5) + (
                                                                  int(digital_pen_licenses_total_cost) / 12),

        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'headman_total_quantity': context['headman_total_quantity'],
        'headman_unit_cost': context['headman_unit_cost'],
        'headman_total_cost': context['headman_total_cost'],
        'headman_annual_depreciation': context['headman_annual_depreciation'],
        'headman_annual_cost': context['headman_annual_cost'],
        'headman_remarks': context['headman_remarks'],
        'veterinarians_total_quantity': context['veterinarians_total_quantity'],
        'veterinarians_unit_cost': context['veterinarians_unit_cost'],
        'veterinarians_total_cost': context['veterinarians_total_cost'],
        'veterinarians_annual_depreciation': context['veterinarians_annual_depreciation'],
        'veterinarians_annual_cost': context['veterinarians_annual_cost'],
        'veterinarians_remarks': context['veterinarians_remarks'],
        'livestock_production_officers_total_quantity': context['livestock_production_officers_total_quantity'],
        'livestock_production_officers_unit_cost': context['livestock_production_officers_unit_cost'],
        'livestock_production_officers_total_cost': context['livestock_production_officers_total_cost'],
        'livestock_production_officers_annual_depreciation': context[
            'livestock_production_officers_annual_depreciation'],
        'livestock_production_officers_annual_cost': context['livestock_production_officers_annual_cost'],
        'livestock_production_officers_remarks': context['livestock_production_officers_remarks'],
        'CHWs_total_quantity': context['CHWs_total_quantity'],
        'CHWs_unit_cost': context['CHWs_unit_cost'],
        'CHWs_total_cost': context['CHWs_total_cost'],
        'CHWs_annual_depreciation': context['CHWs_annual_depreciation'],
        'CHWs_annual_cost': context['CHWs_annual_cost'],
        'CHWs_remarks': context['CHWs_remarks'],
        'clinicians_total_quantity': context['clinicians_total_quantity'],
        'clinicians_unit_cost': context['clinicians_unit_cost'],
        'clinicians_total_cost': context['clinicians_total_cost'],
        'clinicians_annual_depreciation': context['clinicians_annual_depreciation'],
        'clinicians_annual_cost': context['clinicians_annual_cost'],
        'clinicians_remarks': context['clinicians_remarks'],
        'nurses_total_quantity': context['nurses_total_quantity'],
        'nurses_unit_cost': context['nurses_unit_cost'],
        'nurses_total_cost': context['nurses_total_cost'],
        'nurses_annual_depreciation': context['nurses_annual_depreciation'],
        'nurses_annual_cost': context['nurses_annual_cost'],
        'nurses_remarks': context['nurses_remarks'],
        'doctors_total_quantity': context['doctors_total_quantity'],
        'doctors_unit_cost': context['doctors_unit_cost'],
        'doctors_total_cost': context['doctors_total_cost'],
        'doctors_annual_depreciation': context['doctors_annual_depreciation'],
        'doctors_annual_cost': context['doctors_annual_cost'],
        'doctors_remarks': context['doctors_remarks'],
        'CHO_total_quantity': context['CHO_total_quantity'],
        'CHO_unit_cost': context['CHO_unit_cost'],
        'CHO_total_cost': context['CHO_total_cost'],
        'CHO_annual_depreciation': context['CHO_annual_depreciation'],
        'CHO_annual_cost': context['CHO_annual_cost'],
        'CHO_remarks': context['CHO_remarks'],
        'ground_truthing_fuel_total_quantity': context['ground_truthing_fuel_total_quantity'],
        'ground_truthing_fuel_unit_cost': context['ground_truthing_fuel_unit_cost'],
        'ground_truthing_fuel_total_cost': context['ground_truthing_fuel_total_cost'],
        'ground_truthing_fuel_annual_depreciation': context['ground_truthing_fuel_annual_depreciation'],
        'ground_truthing_fuel_annual_cost': context['ground_truthing_fuel_annual_cost'],
        'ground_truthing_fuel_remarks': context['ground_truthing_fuel_remarks'],
        'satellite_phones_total_quantity': context['satellite_phones_total_quantity'],
        'satellite_phones_unit_cost': context['satellite_phones_unit_cost'],
        'satellite_phones_total_cost': context['satellite_phones_total_cost'],
        'satellite_phones_annual_depreciation': context['satellite_phones_annual_depreciation'],
        'satellite_phones_annual_cost': context['satellite_phones_annual_cost'],
        'satellite_phones_remarks': context['satellite_phones_remarks'],
        'laptop_total_quantity': context['laptop_total_quantity'],
        'laptop_unit_cost': context['laptop_unit_cost'],
        'laptop_total_cost': context['laptop_total_cost'],
        'laptop_annual_depreciation': context['laptop_annual_depreciation'],
        'laptop_annual_cost': context['laptop_annual_cost'],
        'laptop_remarks': context['laptop_remarks'],
        'digital_pens_total_quantity': context['digital_pens_total_quantity'],
        'digital_pens_unit_cost': context['digital_pens_unit_cost'],
        'digital_pens_total_cost': context['digital_pens_total_cost'],
        'digital_pens_annual_depreciation': context['digital_pens_annual_depreciation'],
        'digital_pens_annual_cost': context['digital_pens_annual_cost'],
        'digital_pens_remarks': context['digital_pens_remarks'],
        'GIS_compartible_phones_total_quantity': context['GIS_compartible_phones_total_quantity'],
        'GIS_compartible_phones_unit_cost': context['GIS_compartible_phones_unit_cost'],
        'GIS_compartible_phones_total_cost': context['GIS_compartible_phones_total_cost'],
        'GIS_compartible_phones_annual_depreciation': context['GIS_compartible_phones_annual_depreciation'],
        'GIS_compartible_phones_annual_cost': context['GIS_compartible_phones_annual_cost'],
        'GIS_compartible_phones_remarks': context['GIS_compartible_phones_remarks'],
        'GIS_compartible_forms_total_quantity': context['GIS_compartible_forms_total_quantity'],
        'GIS_compartible_forms_unit_cost': context['GIS_compartible_forms_unit_cost'],
        'GIS_compartible_forms_total_cost': context['GIS_compartible_forms_total_cost'],
        'GIS_compartible_forms_annual_depreciation': context['GIS_compartible_forms_annual_depreciation'],
        'GIS_compartible_forms_annual_cost': context['GIS_compartible_forms_annual_cost'],
        'GIS_compartible_forms_remarks': context['GIS_compartible_forms_remarks'],
        'server_fees_total_quantity': context['server_fees_total_quantity'],
        'server_fees_unit_cost': context['server_fees_unit_cost'],
        'server_fees_total_cost': context['server_fees_total_cost'],
        'server_fees_annual_depreciation': context['server_fees_annual_depreciation'],
        'server_fees_annual_cost': context['server_fees_annual_cost'],
        'server_fees_remarks': context['server_fees_remarks'],
        'digital_pen_licenses_total_quantity': context['digital_pen_licenses_total_quantity'],
        'digital_pen_licenses_unit_cost': context['digital_pen_licenses_unit_cost'],
        'digital_pen_licenses_total_cost': context['digital_pen_licenses_total_cost'],
        'digital_pen_licenses_annual_depreciation': context['digital_pen_licenses_annual_depreciation'],
        'digital_pen_licenses_annual_cost': context['digital_pen_licenses_annual_cost'],
        'digital_pen_licenses_remarks': context['digital_pen_licenses_remarks'],
        'passive_surveillance_total_annual_cost': context['passive_surveillance_total_annual_cost'],
    }

    return render(request,'passive_surveillance.html',context2)

def active_surveillance(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['active_surveillance']

    context = {
        '47counties_quantity': 23500,
        '47counties_unit_cost': 0,
        '47counties_total_cost': 0,
        'vet_personnel_VO_quantity': 235,
        'vet_personnel_VO_unit_cost': 0,
        'vet_personnel_VO_total_cost': 0,
        'vet_personnel_socio_economist_quantity': 235,
        'vet_personnel_socio_economist_unit_cost': 0,
        'vet_personnel_socio_economist_total_cost': 0,
        'vet_personnel_VO_local_quantity': 235,
        'vet_personnel_VO_local_unit_cost': 0,
        'vet_personnel_VO_local_total_cost': 0,
        'vet_personnel_technician_quantity': 235,
        'vet_personnel_technician_unit_cost': 0,
        'vet_personnel_technician_total_cost': 0,
        'vet_personnel_driver_quantity': 470,
        'vet_personnel_driver_unit_cost': 0,
        'vet_personnel_driver_total_cost': 0,
        'vet_personnel_security_quantity': 470,
        'vet_personnel_security_unit_cost': 0,
        'vet_personnel_security_total_cost': 0,
        'vet_personnel_translator_quantity': 235,
        'vet_personnel_translator_unit_cost': 0,
        'vet_personnel_translator_total_cost': 0,
        'vet_personnel_livestock_handlers_quantity': 470,
        'vet_personnel_livestock_handlers_unit_cost': 0,
        'vet_personnel_livestock_handlers_total_cost': 0,
        'medical_personnel_CHO_quantity': 235,
        'medical_personnel_CHO_unit_cost': 0,
        'medical_personnel_CHO_total_cost': 0,
        'medical_personnel_local_doctor_quantity': 235,
        'medical_personnel_local_doctor_unit_cost': 0,
        'medical_personnel_local_doctor_total_cost': 0,
        'medical_personnel_local_clinician_quantity': 235,
        'medical_personnel_local_clinician_unit_cost': 0,
        'medical_personnel_local_clinician_total_cost': 0,
        'medical_personnel_technician_quantity': 705,
        'medical_personnel_technician_unit_cost': 0,
        'medical_personnel_technician_total_cost': 0,
        'county_to_Nairobi_transport_quantity': 900,
        'county_to_Nairobi_transport_unit_cost': 28200,
        'county_to_Nairobi_transport_total_cost': 0,
        'disease_search_transport_quantity': 29100,
        'disease_search_transport_unit_cost': 0,
        'disease_search_transport_total_cost': 0,
        'total_distance_transport_quantity': 2910,
        'total_distance_transport_unit_cost': 0,
        'total_distance_transport_total_cost': 0,
        'transport_fuel_quantity': 94,
        'transport_fuel_unit_cost': 0,
        'transport_fuel_total_cost': 0,
        'vehicle_maintenance_quantity': 705,
        'vehicle_maintenance_unit_cost': 0,
        'vehicle_maintenance_total_cost': 0,
        'stationery_quantity': 47,
        'stationery_unit_cost': 0,
        'stationery_total_cost': 0,
        'questionnaires_quantity': 2350,
        'questionnaires_unit_cost': 0,
        'questionnaires_total_cost': 0,
        'sample_collection_materials_quantity': 47,
        'sample_collection_materials_unit_cost': 0,
        'sample_collection_materials_total_cost': 0,
        'shoats_ear_tags_quantity': 4700,
        'shoats_ear_tags_unit_cost': 0,
        'shoats_ear_tags_total_cost': 0,
        'cattle_ear_tags_quantity': 4700,
        'cattle_ear_tags_unit_cost': 0,
        'cattle_ear_tags_total_cost': 0,
        'camels_ear_tags_quantity': 4700,
        'camels_ear_tags_unit_cost': 0,
        'camels_ear_tags_total_cost': 0,
        'active_surveillance_total_per_quarter_cost': 0,
        'active_surveillance_total_annual_cost': 0,
    }

    if (request.method == "POST"):
        _47counties_quantity = request.POST['47counties_quantity']
        _47counties_unit_cost = request.POST['47counties_unit_cost']
        _47counties_total_cost = request.POST['47counties_total_cost']
        vet_personnel_VO_quantity = request.POST['vet_personnel_VO_quantity']
        vet_personnel_VO_unit_cost = request.POST['vet_personnel_VO_unit_cost']
        vet_personnel_VO_total_cost = request.POST['vet_personnel_VO_total_cost']
        vet_personnel_socio_economist_quantity = request.POST['vet_personnel_socio_economist_quantity']
        vet_personnel_socio_economist_unit_cost = request.POST['vet_personnel_socio_economist_unit_cost']
        vet_personnel_socio_economist_total_cost = request.POST['vet_personnel_socio_economist_total_cost']
        vet_personnel_VO_local_quantity = request.POST['vet_personnel_VO_local_quantity']
        vet_personnel_VO_local_unit_cost = request.POST['vet_personnel_VO_local_unit_cost']
        vet_personnel_VO_local_total_cost = request.POST['vet_personnel_VO_local_total_cost']
        vet_personnel_technician_quantity = request.POST['vet_personnel_technician_quantity']
        vet_personnel_technician_unit_cost = request.POST['vet_personnel_technician_unit_cost']
        vet_personnel_technician_total_cost = request.POST['vet_personnel_technician_total_cost']
        vet_personnel_driver_quantity = request.POST['vet_personnel_driver_quantity']
        vet_personnel_driver_unit_cost = request.POST['vet_personnel_driver_unit_cost']
        vet_personnel_driver_total_cost = request.POST['vet_personnel_driver_total_cost']
        vet_personnel_security_quantity = request.POST['vet_personnel_security_quantity']
        vet_personnel_security_unit_cost = request.POST['vet_personnel_security_unit_cost']
        vet_personnel_security_total_cost = request.POST['vet_personnel_security_total_cost']
        vet_personnel_translator_quantity = request.POST['vet_personnel_translator_quantity']
        vet_personnel_translator_unit_cost = request.POST['vet_personnel_translator_unit_cost']
        vet_personnel_translator_total_cost = request.POST['vet_personnel_translator_total_cost']
        vet_personnel_livestock_handlers_quantity = request.POST['vet_personnel_livestock_handlers_quantity']
        vet_personnel_livestock_handlers_unit_cost = request.POST['vet_personnel_livestock_handlers_unit_cost']
        vet_personnel_livestock_handlers_total_cost = request.POST['vet_personnel_livestock_handlers_total_cost']
        medical_personnel_CHO_quantity = request.POST['medical_personnel_CHO_quantity']
        medical_personnel_CHO_unit_cost = request.POST['medical_personnel_CHO_unit_cost']
        medical_personnel_CHO_total_cost = request.POST['medical_personnel_CHO_total_cost']
        medical_personnel_local_doctor_quantity = request.POST['medical_personnel_local_doctor_quantity']
        medical_personnel_local_doctor_unit_cost = request.POST['medical_personnel_local_doctor_unit_cost']
        medical_personnel_local_doctor_total_cost = request.POST['medical_personnel_local_doctor_total_cost']
        medical_personnel_local_clinician_quantity = request.POST['medical_personnel_local_clinician_quantity']
        medical_personnel_local_clinician_unit_cost = request.POST['medical_personnel_local_clinician_unit_cost']
        medical_personnel_local_clinician_total_cost = request.POST['medical_personnel_local_clinician_total_cost']
        medical_personnel_technician_quantity = request.POST['medical_personnel_technician_quantity']
        medical_personnel_technician_unit_cost = request.POST['medical_personnel_technician_unit_cost']
        medical_personnel_technician_total_cost = request.POST['medical_personnel_technician_total_cost']
        county_to_Nairobi_transport_quantity = request.POST['county_to_Nairobi_transport_quantity']
        county_to_Nairobi_transport_unit_cost = request.POST['county_to_Nairobi_transport_unit_cost']
        county_to_Nairobi_transport_total_cost = request.POST['county_to_Nairobi_transport_total_cost']
        disease_search_transport_quantity = request.POST['disease_search_transport_quantity']
        disease_search_transport_unit_cost = request.POST['disease_search_transport_unit_cost']
        disease_search_transport_total_cost = request.POST['disease_search_transport_total_cost']
        total_distance_transport_quantity = request.POST['total_distance_transport_quantity']
        total_distance_transport_unit_cost = request.POST['total_distance_transport_unit_cost']
        total_distance_transport_total_cost = request.POST['total_distance_transport_total_cost']
        transport_fuel_quantity = request.POST['transport_fuel_quantity']
        transport_fuel_unit_cost = request.POST['transport_fuel_unit_cost']
        transport_fuel_total_cost = request.POST['transport_fuel_total_cost']
        vehicle_maintenance_quantity = request.POST['vehicle_maintenance_quantity']
        vehicle_maintenance_unit_cost = request.POST['vehicle_maintenance_unit_cost']
        vehicle_maintenance_total_cost = request.POST['vehicle_maintenance_total_cost']
        stationery_quantity = request.POST['stationery_quantity']
        stationery_unit_cost = request.POST['stationery_unit_cost']
        stationery_total_cost = request.POST['stationery_total_cost']
        questionnaires_quantity = request.POST['questionnaires_quantity']
        questionnaires_unit_cost = request.POST['questionnaires_unit_cost']
        questionnaires_total_cost = request.POST['questionnaires_total_cost']
        sample_collection_materials_quantity = request.POST['sample_collection_materials_quantity']
        sample_collection_materials_unit_cost = request.POST['sample_collection_materials_unit_cost']
        sample_collection_materials_total_cost = request.POST['sample_collection_materials_total_cost']
        shoats_ear_tags_quantity = request.POST['shoats_ear_tags_quantity']
        shoats_ear_tags_unit_cost = request.POST['shoats_ear_tags_unit_cost']
        shoats_ear_tags_total_cost = request.POST['shoats_ear_tags_total_cost']
        cattle_ear_tags_quantity = request.POST['cattle_ear_tags_quantity']
        cattle_ear_tags_unit_cost = request.POST['cattle_ear_tags_unit_cost']
        cattle_ear_tags_total_cost = request.POST['cattle_ear_tags_total_cost']
        camels_ear_tags_quantity = request.POST['camels_ear_tags_quantity']
        camels_ear_tags_unit_cost = request.POST['camels_ear_tags_unit_cost']
        camels_ear_tags_total_cost = request.POST['camels_ear_tags_total_cost']
        active_surveillance_total_per_quarter_cost = request.POST['active_surveillance_total_per_quarter_cost']
        active_surveillance_total_annual_cost = request.POST['active_surveillance_total_annual_cost']

        x = rvf_initial_collection.insert_one({
            '47counties_quantity': _47counties_quantity,
            '47counties_unit_cost': _47counties_unit_cost,
            '47counties_total_cost': int(_47counties_quantity) * int(_47counties_unit_cost),
            'vet_personnel_VO_quantity': vet_personnel_VO_quantity,
            'vet_personnel_VO_unit_cost': vet_personnel_VO_unit_cost,
            'vet_personnel_VO_total_cost': int(vet_personnel_VO_quantity) * int(vet_personnel_VO_unit_cost),
            'vet_personnel_socio_economist_quantity': vet_personnel_socio_economist_quantity,
            'vet_personnel_socio_economist_unit_cost': vet_personnel_socio_economist_unit_cost,
            'vet_personnel_socio_economist_total_cost': int(vet_personnel_socio_economist_quantity) * int(
                vet_personnel_socio_economist_unit_cost),
            'vet_personnel_VO_local_quantity': vet_personnel_VO_local_quantity,
            'vet_personnel_VO_local_unit_cost': vet_personnel_VO_local_unit_cost,
            'vet_personnel_VO_local_total_cost': int(vet_personnel_VO_local_quantity) * int(
                vet_personnel_VO_local_unit_cost),
            'vet_personnel_technician_quantity': vet_personnel_technician_quantity,
            'vet_personnel_technician_unit_cost': vet_personnel_technician_unit_cost,
            'vet_personnel_technician_total_cost': int(vet_personnel_technician_quantity) * int(
                vet_personnel_technician_unit_cost),
            'vet_personnel_driver_quantity': vet_personnel_driver_quantity,
            'vet_personnel_driver_unit_cost': vet_personnel_driver_unit_cost,
            'vet_personnel_driver_total_cost': int(vet_personnel_driver_quantity) * int(vet_personnel_driver_unit_cost),
            'vet_personnel_security_quantity': vet_personnel_security_quantity,
            'vet_personnel_security_unit_cost': vet_personnel_security_unit_cost,
            'vet_personnel_security_total_cost': int(vet_personnel_security_quantity) * int(
                vet_personnel_security_unit_cost),
            'vet_personnel_translator_quantity': vet_personnel_translator_quantity,
            'vet_personnel_translator_unit_cost': vet_personnel_translator_unit_cost,
            'vet_personnel_translator_total_cost': int(vet_personnel_translator_quantity) * int(
                vet_personnel_translator_unit_cost),
            'vet_personnel_livestock_handlers_quantity': vet_personnel_livestock_handlers_quantity,
            'vet_personnel_livestock_handlers_unit_cost': vet_personnel_livestock_handlers_unit_cost,
            'vet_personnel_livestock_handlers_total_cost': int(vet_personnel_livestock_handlers_quantity) * int(
                vet_personnel_livestock_handlers_unit_cost),
            'medical_personnel_CHO_quantity': medical_personnel_CHO_quantity,
            'medical_personnel_CHO_unit_cost': medical_personnel_CHO_unit_cost,
            'medical_personnel_CHO_total_cost': int(medical_personnel_CHO_quantity) * int(
                medical_personnel_CHO_unit_cost),
            'medical_personnel_local_doctor_quantity': medical_personnel_local_doctor_quantity,
            'medical_personnel_local_doctor_unit_cost': medical_personnel_local_doctor_unit_cost,
            'medical_personnel_local_doctor_total_cost': int(medical_personnel_local_doctor_quantity) * int(
                medical_personnel_local_doctor_unit_cost),
            'medical_personnel_local_clinician_quantity': medical_personnel_local_clinician_quantity,
            'medical_personnel_local_clinician_unit_cost': medical_personnel_local_clinician_unit_cost,
            'medical_personnel_local_clinician_total_cost': int(medical_personnel_local_clinician_quantity) * int(
                medical_personnel_local_clinician_unit_cost),
            'medical_personnel_technician_quantity': medical_personnel_technician_quantity,
            'medical_personnel_technician_unit_cost': medical_personnel_technician_unit_cost,
            'medical_personnel_technician_total_cost': int(medical_personnel_technician_quantity) * int(
                medical_personnel_technician_unit_cost),
            'county_to_Nairobi_transport_quantity': county_to_Nairobi_transport_quantity,
            'county_to_Nairobi_transport_unit_cost': county_to_Nairobi_transport_unit_cost,
            'county_to_Nairobi_transport_total_cost': int(county_to_Nairobi_transport_quantity) * int(
                county_to_Nairobi_transport_unit_cost),
            'disease_search_transport_quantity': disease_search_transport_quantity,
            'disease_search_transport_unit_cost': disease_search_transport_unit_cost,
            'disease_search_transport_total_cost': int(disease_search_transport_quantity) * int(
                disease_search_transport_unit_cost),
            'total_distance_transport_quantity': total_distance_transport_quantity,
            'total_distance_transport_unit_cost': total_distance_transport_unit_cost,
            'total_distance_transport_total_cost': int(total_distance_transport_quantity) * int(
                total_distance_transport_unit_cost),
            'transport_fuel_quantity': transport_fuel_quantity,
            'transport_fuel_unit_cost': transport_fuel_unit_cost,
            'transport_fuel_total_cost': int(transport_fuel_quantity) * int(transport_fuel_unit_cost),
            'vehicle_maintenance_quantity': vehicle_maintenance_quantity,
            'vehicle_maintenance_unit_cost': vehicle_maintenance_unit_cost,
            'vehicle_maintenance_total_cost': int(vehicle_maintenance_quantity) * int(vehicle_maintenance_unit_cost),
            'stationery_quantity': stationery_quantity,
            'stationery_unit_cost': stationery_unit_cost,
            'stationery_total_cost': int(stationery_quantity) * int(stationery_unit_cost),
            'questionnaires_quantity': questionnaires_quantity,
            'questionnaires_unit_cost': questionnaires_unit_cost,
            'questionnaires_total_cost': int(questionnaires_quantity) * int(questionnaires_unit_cost),
            'sample_collection_materials_quantity': sample_collection_materials_quantity,
            'sample_collection_materials_unit_cost': sample_collection_materials_unit_cost,
            'sample_collection_materials_total_cost': int(sample_collection_materials_quantity) * int(
                sample_collection_materials_unit_cost),
            'shoats_ear_tags_quantity': shoats_ear_tags_quantity,
            'shoats_ear_tags_unit_cost': shoats_ear_tags_unit_cost,
            'shoats_ear_tags_total_cost': int(shoats_ear_tags_quantity) * int(shoats_ear_tags_unit_cost),
            'cattle_ear_tags_quantity': cattle_ear_tags_quantity,
            'cattle_ear_tags_unit_cost': cattle_ear_tags_unit_cost,
            'cattle_ear_tags_total_cost': int(cattle_ear_tags_quantity) * int(cattle_ear_tags_unit_cost),
            'camels_ear_tags_quantity': camels_ear_tags_quantity,
            'camels_ear_tags_unit_cost': camels_ear_tags_unit_cost,
            'camels_ear_tags_total_cost': int(camels_ear_tags_quantity) * int(camels_ear_tags_unit_cost),
            'active_surveillance_total_per_quarter_cost': int(_47counties_total_cost) + int(
                vet_personnel_VO_total_cost) +
                                                          int(vet_personnel_socio_economist_total_cost) + int(
                vet_personnel_VO_local_total_cost) +
                                                          int(vet_personnel_technician_total_cost) + int(
                vet_personnel_driver_total_cost) +
                                                          int(vet_personnel_security_total_cost) + int(
                vet_personnel_translator_total_cost) +
                                                          int(vet_personnel_livestock_handlers_total_cost) + int(
                medical_personnel_CHO_total_cost) +
                                                          int(medical_personnel_local_doctor_total_cost) + int(
                medical_personnel_local_clinician_total_cost) +
                                                          int(medical_personnel_technician_total_cost) + int(
                county_to_Nairobi_transport_total_cost) +
                                                          int(disease_search_transport_total_cost) + int(
                total_distance_transport_total_cost) +
                                                          int(transport_fuel_total_cost) + int(
                vehicle_maintenance_total_cost) +
                                                          int(stationery_total_cost) + int(questionnaires_total_cost) +
                                                          int(sample_collection_materials_total_cost) + int(
                shoats_ear_tags_total_cost) +
                                                          int(cattle_ear_tags_total_cost) + int(
                camels_ear_tags_total_cost),
            'active_surveillance_total_annual_cost': (int(_47counties_total_cost) + int(vet_personnel_VO_total_cost) +
                                                      int(vet_personnel_socio_economist_total_cost) + int(
                        vet_personnel_VO_local_total_cost) +
                                                      int(vet_personnel_technician_total_cost) + int(
                        vet_personnel_driver_total_cost) +
                                                      int(vet_personnel_security_total_cost) + int(
                        vet_personnel_translator_total_cost) +
                                                      int(vet_personnel_livestock_handlers_total_cost) + int(
                        medical_personnel_CHO_total_cost) +
                                                      int(medical_personnel_local_doctor_total_cost) + int(
                        medical_personnel_local_clinician_total_cost) +
                                                      int(medical_personnel_technician_total_cost) + int(
                        county_to_Nairobi_transport_total_cost) +
                                                      int(disease_search_transport_total_cost) + int(
                        total_distance_transport_total_cost) +
                                                      int(transport_fuel_total_cost) + int(
                        vehicle_maintenance_total_cost) +
                                                      int(stationery_total_cost) + int(questionnaires_total_cost) +
                                                      int(sample_collection_materials_total_cost) + int(
                        shoats_ear_tags_total_cost) +
                                                      int(cattle_ear_tags_total_cost) + int(
                        camels_ear_tags_total_cost)) * 4,
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        '47counties_quantity': context['47counties_quantity'],
        '47counties_unit_cost': context['47counties_unit_cost'],
        '47counties_total_cost': context['47counties_total_cost'],
        'vet_personnel_VO_quantity': context['vet_personnel_VO_quantity'],
        'vet_personnel_VO_unit_cost': context['vet_personnel_VO_unit_cost'],
        'vet_personnel_VO_total_cost': context['vet_personnel_VO_total_cost'],
        'vet_personnel_socio_economist_quantity': context['vet_personnel_socio_economist_quantity'],
        'vet_personnel_socio_economist_unit_cost': context['vet_personnel_socio_economist_unit_cost'],
        'vet_personnel_socio_economist_total_cost': context['vet_personnel_socio_economist_total_cost'],
        'vet_personnel_VO_local_quantity': context['vet_personnel_VO_local_quantity'],
        'vet_personnel_VO_local_unit_cost': context['vet_personnel_VO_local_unit_cost'],
        'vet_personnel_VO_local_total_cost': context['vet_personnel_VO_local_total_cost'],
        'vet_personnel_technician_quantity': context['vet_personnel_technician_quantity'],
        'vet_personnel_technician_unit_cost': context['vet_personnel_technician_unit_cost'],
        'vet_personnel_technician_total_cost': context['vet_personnel_technician_total_cost'],
        'vet_personnel_driver_quantity': context['vet_personnel_driver_quantity'],
        'vet_personnel_driver_unit_cost': context['vet_personnel_driver_unit_cost'],
        'vet_personnel_driver_total_cost': context['vet_personnel_driver_total_cost'],
        'vet_personnel_security_quantity': context['vet_personnel_security_quantity'],
        'vet_personnel_security_unit_cost': context['vet_personnel_security_unit_cost'],
        'vet_personnel_security_total_cost': context['vet_personnel_security_total_cost'],
        'vet_personnel_translator_quantity': context['vet_personnel_translator_quantity'],
        'vet_personnel_translator_unit_cost': context['vet_personnel_translator_unit_cost'],
        'vet_personnel_translator_total_cost': context['vet_personnel_translator_total_cost'],
        'vet_personnel_livestock_handlers_quantity': context['vet_personnel_livestock_handlers_quantity'],
        'vet_personnel_livestock_handlers_unit_cost': context['vet_personnel_livestock_handlers_unit_cost'],
        'vet_personnel_livestock_handlers_total_cost': context['vet_personnel_livestock_handlers_total_cost'],
        'medical_personnel_CHO_quantity': context['medical_personnel_CHO_quantity'],
        'medical_personnel_CHO_unit_cost': context['medical_personnel_CHO_unit_cost'],
        'medical_personnel_CHO_total_cost': context['medical_personnel_CHO_total_cost'],
        'medical_personnel_local_doctor_quantity': context['medical_personnel_local_doctor_quantity'],
        'medical_personnel_local_doctor_unit_cost': context['medical_personnel_local_doctor_unit_cost'],
        'medical_personnel_local_doctor_total_cost': context['medical_personnel_local_doctor_total_cost'],
        'medical_personnel_local_clinician_quantity': context['medical_personnel_local_clinician_quantity'],
        'medical_personnel_local_clinician_unit_cost': context['medical_personnel_local_clinician_unit_cost'],
        'medical_personnel_local_clinician_total_cost': context['medical_personnel_local_clinician_total_cost'],
        'medical_personnel_technician_quantity': context['medical_personnel_technician_quantity'],
        'medical_personnel_technician_unit_cost': context['medical_personnel_technician_unit_cost'],
        'medical_personnel_technician_total_cost': context['medical_personnel_technician_total_cost'],
        'county_to_Nairobi_transport_quantity': context['county_to_Nairobi_transport_quantity'],
        'county_to_Nairobi_transport_unit_cost': context['county_to_Nairobi_transport_unit_cost'],
        'county_to_Nairobi_transport_total_cost': context['county_to_Nairobi_transport_total_cost'],
        'disease_search_transport_quantity': context['disease_search_transport_quantity'],
        'disease_search_transport_unit_cost': context['disease_search_transport_unit_cost'],
        'disease_search_transport_total_cost': context['disease_search_transport_total_cost'],
        'total_distance_transport_quantity': context['total_distance_transport_quantity'],
        'total_distance_transport_unit_cost': context['total_distance_transport_unit_cost'],
        'total_distance_transport_total_cost': context['total_distance_transport_total_cost'],
        'transport_fuel_quantity': context['transport_fuel_quantity'],
        'transport_fuel_unit_cost': context['transport_fuel_unit_cost'],
        'transport_fuel_total_cost': context['transport_fuel_total_cost'],
        'vehicle_maintenance_quantity': context['vehicle_maintenance_quantity'],
        'vehicle_maintenance_unit_cost': context['vehicle_maintenance_unit_cost'],
        'vehicle_maintenance_total_cost': context['vehicle_maintenance_total_cost'],
        'stationery_quantity': context['stationery_quantity'],
        'stationery_unit_cost': context['stationery_unit_cost'],
        'stationery_total_cost': context['stationery_total_cost'],
        'questionnaires_quantity': context['questionnaires_quantity'],
        'questionnaires_unit_cost': context['questionnaires_unit_cost'],
        'questionnaires_total_cost': context['questionnaires_total_cost'],
        'sample_collection_materials_quantity': context['sample_collection_materials_quantity'],
        'sample_collection_materials_unit_cost': context['sample_collection_materials_unit_cost'],
        'sample_collection_materials_total_cost': context['sample_collection_materials_total_cost'],
        'shoats_ear_tags_quantity': context['shoats_ear_tags_quantity'],
        'shoats_ear_tags_unit_cost': context['shoats_ear_tags_unit_cost'],
        'shoats_ear_tags_total_cost': context['shoats_ear_tags_total_cost'],
        'cattle_ear_tags_quantity': context['cattle_ear_tags_quantity'],
        'cattle_ear_tags_unit_cost': context['cattle_ear_tags_unit_cost'],
        'cattle_ear_tags_total_cost': context['cattle_ear_tags_total_cost'],
        'camels_ear_tags_quantity': context['camels_ear_tags_quantity'],
        'camels_ear_tags_unit_cost': context['camels_ear_tags_unit_cost'],
        'camels_ear_tags_total_cost': context['camels_ear_tags_total_cost'],
        'active_surveillance_total_per_quarter_cost': context['active_surveillance_total_per_quarter_cost'],
        'active_surveillance_total_annual_cost': context['active_surveillance_total_annual_cost'],
    }

    return render(request,'active_surveillance.html',context2)

def lab_diagnosis(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['lab_diagnosis']

    context = {
        'RT_PCR_Machine_quantity': 1,
        'RT_PCR_Machine_unit_cost': 1100000,
        'RT_PCR_Machine_total_cost': 0,
        'RT_PCR_Machine_lifespan': 5,
        'RT_PCR_Machine_salvage_value': 0,
        'RT_PCR_Machine_annual_depreciation': 0,
        'RT_PCR_Machine_annual_cost': 0,
        'pipettes_quantity': 12,
        'pipettes_unit_cost': 70000,
        'pipettes_total_cost': 0,
        'pipettes_lifespan': 3,
        'pipettes_salvage_value': 0,
        'pipettes_annual_depreciation': 0,
        'pipettes_annual_cost': 0,
        'reagents_quantity': 1,
        'reagents_unit_cost': 1500000,
        'reagents_total_cost': 0,
        'reagents_lifespan': 0,
        'reagents_salvage_value': 0,
        'reagents_annual_depreciation': 0,
        'reagents_annual_cost': 0,
        'consumables_quantity': 1,
        'consumables_unit_cost': 200000,
        'consumables_total_cost': 0,
        'consumables_lifespan': 0,
        'consumables_salvage_value': 0,
        'consumables_annual_depreciation': 0,
        'consumables_annual_cost': 0,
        'computer_quantity': 2,
        'computer_unit_cost': 120000,
        'computer_total_cost': 0,
        'computer_lifespan': 5,
        'computer_salvage_value': 5000,
        'computer_annual_depreciation': 0,
        'computer_annual_cost': 0,
        'PCR_staff_working_quantity': 4,
        'PCR_staff_working_unit_cost': 0,
        'PCR_staff_working_total_cost': 0,
        'PCR_staff_working_lifespan': 0,
        'PCR_staff_working_salvage_value': 0,
        'PCR_staff_working_annual_depreciation': 0,
        'PCR_staff_working_annual_cost': 0,
        'incubator_quantity': 2,
        'incubator_unit_cost': 1500000,
        'incubator_total_cost': 0,
        'incubator_lifespan': 20,
        'incubator_salvage_value': 0,
        'incubator_annual_depreciation': 0,
        'incubator_annual_cost': 0,
        'dissection_microscope_quantity': 2,
        'dissection_microscope_unit_cost': 1500000,
        'dissection_microscope_total_cost': 0,
        'dissection_microscope_lifespan': 20,
        'dissection_microscope_salvage_value': 0,
        'dissection_microscope_annual_depreciation': 0,
        'dissection_microscope_annual_cost': 0,
        'VNT_reagents_quantity': 1,
        'VNT_reagents_unit_cost': 1500000,
        'VNT_reagents_total_cost': 0,
        'VNT_reagents_lifespan': 0,
        'VNT_reagents_salvage_value': 0,
        'VNT_reagents_annual_depreciation': 0,
        'VNT_reagents_annual_cost': 0,
        'VNT_consumables_quantity': 1,
        'VNT_consumables_unit_cost': 200000,
        'VNT_consumables_total_cost': 0,
        'VNT_consumables_lifespan': 0,
        'VNT_consumables_salvage_value': 0,
        'VNT_consumables_annual_depreciation': 0,
        'VNT_consumables_annual_cost': 0,
        'VNT_staff_working_quantity': 4,
        'VNT_staff_working_unit_cost': 0,
        'VNT_staff_working_total_cost': 0,
        'VNT_staff_working_lifespan': 0,
        'VNT_staff_working_salvage_value': 0,
        'VNT_staff_working_annual_depreciation': 0,
        'VNT_staff_working_annual_cost': 0,
        'ELISA_reader_quantity': 2,
        'ELISA_reader_unit_cost': 600000,
        'ELISA_reader_total_cost': 0,
        'ELISA_reader_lifespan': 5,
        'ELISA_reader_salvage_value': 0,
        'ELISA_reader_annual_depreciation': 0,
        'ELISA_reader_annual_cost': 0,
        'ELISA_kits_quantity': 20,
        'ELISA_kits_unit_cost': 500000,
        'ELISA_kits_total_cost': 0,
        'ELISA_kits_lifespan': 0,
        'ELISA_kits_salvage_value': 0,
        'ELISA_kits_annual_depreciation': 0,
        'ELISA_kits_annual_cost': 0,
        'ELISA_computer_quantity': 2,
        'ELISA_computer_unit_cost': 120000,
        'ELISA_computer_total_cost': 0,
        'ELISA_computer_lifespan': 5,
        'ELISA_computer_salvage_value': 5000,
        'ELISA_computer_annual_depreciation': 0,
        'ELISA_computer_annual_cost': 0,
        'ELISA_incubator_shaker_quantity': 4,
        'ELISA_incubator_shaker_unit_cost': 500000,
        'ELISA_incubator_shaker_total_cost': 0,
        'ELISA_incubator_shaker_lifespan': 10,
        'ELISA_incubator_shaker_salvage_value': 0,
        'ELISA_incubator_shaker_annual_depreciation': 0,
        'ELISA_incubator_shaker_annual_cost': 0,
        'ELISA_platewasher_quantity': 6,
        'ELISA_platewasher_unit_cost': 100000,
        'ELISA_platewasher_total_cost': 0,
        'ELISA_platewasher_lifespan': 10,
        'ELISA_platewasher_salvage_value': 0,
        'ELISA_platewasher_annual_depreciation': 0,
        'ELISA_platewasher_annual_cost': 0,
        'ELISA_consumables_quantity': 1,
        'ELISA_consumables_unit_cost': 200000,
        'ELISA_consumables_total_cost': 0,
        'ELISA_consumables_lifespan': 0,
        'ELISA_consumables_salvage_value': 0,
        'ELISA_consumables_annual_depreciation': 0,
        'ELISA_consumables_annual_cost': 0,
        'ELISA_staff_working_quantity': 4,
        'ELISA_staff_working_unit_cost': 0,
        'ELISA_staff_working_total_cost': 0,
        'ELISA_staff_working_lifespan': 0,
        'ELISA_staff_working_salvage_value': 0,
        'ELISA_staff_working_annual_depreciation': 0,
        'ELISA_staff_working_annual_cost': 0,
        'laboratory_generator_quantity': 2,
        'laboratory_generator_unit_cost': 500000,
        'laboratory_generator_total_cost': 0,
        'laboratory_generator_lifespan': 10,
        'laboratory_generator_salvage_value': 100000,
        'laboratory_generator_annual_depreciation': 0,
        'laboratory_generator_annual_cost': 0,
        'freezers_quantity': 3,
        'freezers_unit_cost': 500000,
        'freezers_total_cost': 0,
        'freezers_lifespan': 10,
        'freezers_salvage_value': 50000,
        'freezers_annual_depreciation': 0,
        'freezers_annual_cost': 0,
        'refrigerators_quantity': 3,
        'refrigerators_unit_cost': 120000,
        'refrigerators_total_cost': 0,
        'refrigerators_lifespan': 5,
        'refrigerators_salvage_value': 20000,
        'refrigerators_annual_depreciation': 0,
        'refrigerators_annual_cost': 0,
        'water_quantity': 1,
        'water_unit_cost': 100000,
        'water_total_cost': 0,
        'water_lifespan': 0,
        'water_salvage_value': 0,
        'water_annual_depreciation': 0,
        'water_annual_cost': 0,
        'electricity_quantity': 1,
        'electricity_unit_cost': 500000,
        'electricity_total_cost': 0,
        'electricity_lifespan': 0,
        'electricity_salvage_value': 0,
        'electricity_annual_depreciation': 0,
        'electricity_annual_cost': 0,
        'equipment_calibration_quantity': 1,
        'equipment_calibration_unit_cost': 1000000,
        'equipment_calibration_total_cost': 0,
        'equipment_calibration_lifespan': 0,
        'equipment_calibration_salvage_value': 0,
        'equipment_calibration_annual_depreciation': 0,
        'equipment_calibration_annual_cost': 0,
        'expert_consultation_quantity': 15,
        'expert_consultation_unit_cost': 10000,
        'expert_consultation_total_cost': 0,
        'expert_consultation_lifespan': 5,
        'expert_consultation_salvage_value': 0,
        'expert_consultation_annual_depreciation': 0,
        'expert_consultation_annual_cost': 0,
        'water_still_quantity': 1,
        'water_still_unit_cost': 1000000,
        'water_still_total_cost': 0,
        'water_still_lifespan': 10,
        'water_still_salvage_value': 0,
        'water_still_annual_depreciation': 0,
        'water_still_annual_cost': 0,
        'micropore_filtration_system_quantity': 1,
        'micropore_filtration_system_unit_cost': 1000000,
        'micropore_filtration_system_total_cost': 0,
        'micropore_filtration_system_lifespan': 10,
        'micropore_filtration_system_salvage_value': 0,
        'micropore_filtration_system_annual_depreciation': 0,
        'micropore_filtration_system_annual_cost': 0,
        'generator_fuel_quantity': 12000,
        'generator_fuel_unit_cost': 120,
        'generator_fuel_total_cost': 0,
        'generator_fuel_lifespan': 0,
        'generator_fuel_salvage_value': 0,
        'generator_fuel_annual_depreciation': 0,
        'generator_fuel_annual_cost': 0,
        'lab_staff_training_quantity': 1,
        'lab_staff_training_unit_cost': 1500000,
        'lab_staff_training_total_cost': 0,
        'lab_staff_training_lifespan': 0,
        'lab_staff_training_salvage_value': 0,
        'lab_staff_training_annual_depreciation': 0,
        'lab_staff_training_annual_cost': 0,
        'lab_staff_DSA_training_quantity': 60,
        'lab_staff_DSA_training_unit_cost': 2000,
        'lab_staff_DSA_training_total_cost': 0,
        'lab_staff_DSA_training_lifespan': 0,
        'lab_staff_DSA_training_salvage_value': 0,
        'lab_staff_DSA_training_annual_depreciation': 0,
        'lab_staff_DSA_training_annual_cost': 0,
        'lab_staff_training_transport_quantity': 150,
        'lab_staff_training_transport_unit_cost': 120,
        'lab_staff_training_transport_total_cost': 0,
        'lab_staff_training_transport_lifespan': 0,
        'lab_staff_training_transport_salvage_value': 0,
        'lab_staff_training_transport_annual_depreciation': 0,
        'lab_staff_training_transport_annual_cost': 0,
        'lab_diagnosis_total': 0,
    }

    if (request.method == "POST"):
        RT_PCR_Machine_quantity = request.POST['RT_PCR_Machine_quantity']
        RT_PCR_Machine_unit_cost = request.POST['RT_PCR_Machine_unit_cost']
        RT_PCR_Machine_total_cost = request.POST['RT_PCR_Machine_total_cost']
        RT_PCR_Machine_lifespan = request.POST['RT_PCR_Machine_lifespan']
        RT_PCR_Machine_salvage_value = request.POST['RT_PCR_Machine_salvage_value']
        RT_PCR_Machine_annual_depreciation = request.POST['RT_PCR_Machine_annual_depreciation']
        RT_PCR_Machine_annual_cost = request.POST['RT_PCR_Machine_annual_cost']
        pipettes_quantity = request.POST['pipettes_quantity']
        pipettes_unit_cost = request.POST['pipettes_unit_cost']
        pipettes_total_cost = request.POST['pipettes_total_cost']
        pipettes_lifespan = request.POST['pipettes_lifespan']
        pipettes_salvage_value = request.POST['pipettes_salvage_value']
        pipettes_annual_depreciation = request.POST['pipettes_annual_depreciation']
        pipettes_annual_cost = request.POST['pipettes_annual_cost']
        reagents_quantity = request.POST['reagents_quantity']
        reagents_unit_cost = request.POST['reagents_unit_cost']
        reagents_total_cost = request.POST['reagents_total_cost']
        reagents_lifespan = request.POST['reagents_lifespan']
        reagents_salvage_value = request.POST['reagents_salvage_value']
        reagents_annual_depreciation = request.POST['reagents_annual_depreciation']
        reagents_annual_cost = request.POST['reagents_annual_cost']
        consumables_quantity = request.POST['consumables_quantity']
        consumables_unit_cost = request.POST['consumables_unit_cost']
        consumables_total_cost = request.POST['consumables_total_cost']
        consumables_lifespan = request.POST['consumables_lifespan']
        consumables_salvage_value = request.POST['consumables_salvage_value']
        consumables_annual_depreciation = request.POST['consumables_annual_depreciation']
        consumables_annual_cost = request.POST['consumables_annual_cost']
        computer_quantity = request.POST['computer_quantity']
        computer_unit_cost = request.POST['computer_unit_cost']
        computer_total_cost = request.POST['computer_total_cost']
        computer_lifespan = request.POST['computer_lifespan']
        computer_salvage_value = request.POST['computer_salvage_value']
        computer_annual_depreciation = request.POST['computer_annual_depreciation']
        computer_annual_cost = request.POST['computer_annual_cost']
        PCR_staff_working_quantity = request.POST['PCR_staff_working_quantity']
        PCR_staff_working_unit_cost = request.POST['PCR_staff_working_unit_cost']
        PCR_staff_working_total_cost = request.POST['PCR_staff_working_total_cost']
        PCR_staff_working_lifespan = request.POST['PCR_staff_working_lifespan']
        PCR_staff_working_salvage_value = request.POST['PCR_staff_working_salvage_value']
        PCR_staff_working_annual_depreciation = request.POST['PCR_staff_working_annual_depreciation']
        PCR_staff_working_annual_cost = request.POST['PCR_staff_working_annual_cost']
        incubator_quantity = request.POST['incubator_quantity']
        incubator_unit_cost = request.POST['incubator_unit_cost']
        incubator_total_cost = request.POST['incubator_total_cost']
        incubator_lifespan = request.POST['incubator_lifespan']
        incubator_salvage_value = request.POST['incubator_salvage_value']
        incubator_annual_depreciation = request.POST['incubator_annual_depreciation']
        incubator_annual_cost = request.POST['incubator_annual_cost']
        dissection_microscope_quantity = request.POST['dissection_microscope_quantity']
        dissection_microscope_unit_cost = request.POST['dissection_microscope_unit_cost']
        dissection_microscope_total_cost = request.POST['dissection_microscope_total_cost']
        dissection_microscope_lifespan = request.POST['dissection_microscope_lifespan']
        dissection_microscope_salvage_value = request.POST['dissection_microscope_salvage_value']
        dissection_microscope_annual_depreciation = request.POST['dissection_microscope_annual_depreciation']
        dissection_microscope_annual_cost = request.POST['dissection_microscope_annual_cost']
        VNT_reagents_quantity = request.POST['VNT_reagents_quantity']
        VNT_reagents_unit_cost = request.POST['VNT_reagents_unit_cost']
        VNT_reagents_total_cost = request.POST['VNT_reagents_total_cost']
        VNT_reagents_lifespan = request.POST['VNT_reagents_lifespan']
        VNT_reagents_salvage_value = request.POST['VNT_reagents_salvage_value']
        VNT_reagents_annual_depreciation = request.POST['VNT_reagents_annual_depreciation']
        VNT_reagents_annual_cost = request.POST['VNT_reagents_annual_cost']
        VNT_consumables_quantity = request.POST['VNT_consumables_quantity']
        VNT_consumables_unit_cost = request.POST['VNT_consumables_unit_cost']
        VNT_consumables_total_cost = request.POST['VNT_consumables_total_cost']
        VNT_consumables_lifespan = request.POST['VNT_consumables_lifespan']
        VNT_consumables_salvage_value = request.POST['VNT_consumables_salvage_value']
        VNT_consumables_annual_depreciation = request.POST['VNT_consumables_annual_depreciation']
        VNT_consumables_annual_cost = request.POST['VNT_consumables_annual_cost']
        VNT_staff_working_quantity = request.POST['VNT_staff_working_quantity']
        VNT_staff_working_unit_cost = request.POST['VNT_staff_working_unit_cost']
        VNT_staff_working_total_cost = request.POST['VNT_staff_working_total_cost']
        VNT_staff_working_lifespan = request.POST['VNT_staff_working_lifespan']
        VNT_staff_working_salvage_value = request.POST['VNT_staff_working_salvage_value']
        VNT_staff_working_annual_depreciation = request.POST['VNT_staff_working_annual_depreciation']
        VNT_staff_working_annual_cost = request.POST['VNT_staff_working_annual_cost']
        ELISA_reader_quantity = request.POST['ELISA_reader_quantity']
        ELISA_reader_unit_cost = request.POST['ELISA_reader_unit_cost']
        ELISA_reader_total_cost = request.POST['ELISA_reader_total_cost']
        ELISA_reader_lifespan = request.POST['ELISA_reader_lifespan']
        ELISA_reader_salvage_value = request.POST['ELISA_reader_salvage_value']
        ELISA_reader_annual_depreciation = request.POST['ELISA_reader_annual_depreciation']
        ELISA_reader_annual_cost = request.POST['ELISA_reader_annual_cost']
        ELISA_kits_quantity = request.POST['ELISA_kits_quantity']
        ELISA_kits_unit_cost = request.POST['ELISA_kits_unit_cost']
        ELISA_kits_total_cost = request.POST['ELISA_kits_total_cost']
        ELISA_kits_lifespan = request.POST['ELISA_kits_lifespan']
        ELISA_kits_salvage_value = request.POST['ELISA_kits_salvage_value']
        ELISA_kits_annual_depreciation = request.POST['ELISA_kits_annual_depreciation']
        ELISA_kits_annual_cost = request.POST['ELISA_kits_annual_cost']
        ELISA_computer_quantity = request.POST['ELISA_computer_quantity']
        ELISA_computer_unit_cost = request.POST['ELISA_computer_unit_cost']
        ELISA_computer_total_cost = request.POST['ELISA_computer_total_cost']
        ELISA_computer_lifespan = request.POST['ELISA_computer_lifespan']
        ELISA_computer_salvage_value = request.POST['ELISA_computer_salvage_value']
        ELISA_computer_annual_depreciation = request.POST['ELISA_computer_annual_depreciation']
        ELISA_computer_annual_cost = request.POST['ELISA_computer_annual_cost']
        ELISA_incubator_shaker_quantity = request.POST['ELISA_incubator_shaker_quantity']
        ELISA_incubator_shaker_unit_cost = request.POST['ELISA_incubator_shaker_unit_cost']
        ELISA_incubator_shaker_total_cost = request.POST['ELISA_incubator_shaker_total_cost']
        ELISA_incubator_shaker_lifespan = request.POST['ELISA_incubator_shaker_lifespan']
        ELISA_incubator_shaker_salvage_value = request.POST['ELISA_incubator_shaker_salvage_value']
        ELISA_incubator_shaker_annual_depreciation = request.POST['ELISA_incubator_shaker_annual_depreciation']
        ELISA_incubator_shaker_annual_cost = request.POST['ELISA_incubator_shaker_annual_cost']
        ELISA_platewasher_quantity = request.POST['ELISA_platewasher_quantity']
        ELISA_platewasher_unit_cost = request.POST['ELISA_platewasher_unit_cost']
        ELISA_platewasher_total_cost = request.POST['ELISA_platewasher_total_cost']
        ELISA_platewasher_lifespan = request.POST['ELISA_platewasher_lifespan']
        ELISA_platewasher_salvage_value = request.POST['ELISA_platewasher_salvage_value']
        ELISA_platewasher_annual_depreciation = request.POST['ELISA_platewasher_annual_depreciation']
        ELISA_platewasher_annual_cost = request.POST['ELISA_platewasher_annual_cost']
        ELISA_consumables_quantity = request.POST['ELISA_consumables_quantity']
        ELISA_consumables_unit_cost = request.POST['ELISA_consumables_unit_cost']
        ELISA_consumables_total_cost = request.POST['ELISA_consumables_total_cost']
        ELISA_consumables_lifespan = request.POST['ELISA_consumables_lifespan']
        ELISA_consumables_salvage_value = request.POST['ELISA_consumables_salvage_value']
        ELISA_consumables_annual_depreciation = request.POST['ELISA_consumables_annual_depreciation']
        ELISA_consumables_annual_cost = request.POST['ELISA_consumables_annual_cost']
        ELISA_staff_working_quantity = request.POST['ELISA_staff_working_quantity']
        ELISA_staff_working_unit_cost = request.POST['ELISA_staff_working_unit_cost']
        ELISA_staff_working_total_cost = request.POST['ELISA_staff_working_total_cost']
        ELISA_staff_working_lifespan = request.POST['ELISA_staff_working_lifespan']
        ELISA_staff_working_salvage_value = request.POST['ELISA_staff_working_salvage_value']
        ELISA_staff_working_annual_depreciation = request.POST['ELISA_staff_working_annual_depreciation']
        ELISA_staff_working_annual_cost = request.POST['ELISA_staff_working_annual_cost']
        laboratory_generator_quantity = request.POST['laboratory_generator_quantity']
        laboratory_generator_unit_cost = request.POST['laboratory_generator_unit_cost']
        laboratory_generator_total_cost = request.POST['laboratory_generator_total_cost']
        laboratory_generator_lifespan = request.POST['laboratory_generator_lifespan']
        laboratory_generator_salvage_value = request.POST['laboratory_generator_salvage_value']
        laboratory_generator_annual_depreciation = request.POST['laboratory_generator_annual_depreciation']
        laboratory_generator_annual_cost = request.POST['laboratory_generator_annual_cost']
        freezers_quantity = request.POST['freezers_quantity']
        freezers_unit_cost = request.POST['freezers_unit_cost']
        freezers_total_cost = request.POST['freezers_total_cost']
        freezers_lifespan = request.POST['freezers_lifespan']
        freezers_salvage_value = request.POST['freezers_salvage_value']
        freezers_annual_depreciation = request.POST['freezers_annual_depreciation']
        freezers_annual_cost = request.POST['freezers_annual_cost']
        refrigerators_quantity = request.POST['refrigerators_quantity']
        refrigerators_unit_cost = request.POST['refrigerators_unit_cost']
        refrigerators_total_cost = request.POST['refrigerators_total_cost']
        refrigerators_lifespan = request.POST['refrigerators_lifespan']
        refrigerators_salvage_value = request.POST['refrigerators_salvage_value']
        refrigerators_annual_depreciation = request.POST['refrigerators_annual_depreciation']
        refrigerators_annual_cost = request.POST['refrigerators_annual_cost']
        water_quantity = request.POST['water_quantity']
        water_unit_cost = request.POST['water_unit_cost']
        water_total_cost = request.POST['water_total_cost']
        water_lifespan = request.POST['water_lifespan']
        water_salvage_value = request.POST['water_salvage_value']
        water_annual_depreciation = request.POST['water_annual_depreciation']
        water_annual_cost = request.POST['water_annual_cost']
        electricity_quantity = request.POST['electricity_quantity']
        electricity_unit_cost = request.POST['electricity_unit_cost']
        electricity_total_cost = request.POST['electricity_total_cost']
        electricity_lifespan = request.POST['electricity_lifespan']
        electricity_salvage_value = request.POST['electricity_salvage_value']
        electricity_annual_depreciation = request.POST['electricity_annual_depreciation']
        electricity_annual_cost = request.POST['electricity_annual_cost']
        equipment_calibration_quantity = request.POST['equipment_calibration_quantity']
        equipment_calibration_unit_cost = request.POST['equipment_calibration_unit_cost']
        equipment_calibration_total_cost = request.POST['equipment_calibration_total_cost']
        equipment_calibration_lifespan = request.POST['equipment_calibration_lifespan']
        equipment_calibration_salvage_value = request.POST['equipment_calibration_salvage_value']
        equipment_calibration_annual_depreciation = request.POST['equipment_calibration_annual_depreciation']
        equipment_calibration_annual_cost = request.POST['equipment_calibration_annual_cost']
        expert_consultation_quantity = request.POST['expert_consultation_quantity']
        expert_consultation_unit_cost = request.POST['expert_consultation_unit_cost']
        expert_consultation_total_cost = request.POST['expert_consultation_total_cost']
        expert_consultation_lifespan = request.POST['expert_consultation_lifespan']
        expert_consultation_salvage_value = request.POST['expert_consultation_salvage_value']
        expert_consultation_annual_depreciation = request.POST['expert_consultation_annual_depreciation']
        expert_consultation_annual_cost = request.POST['expert_consultation_annual_cost']
        water_still_quantity = request.POST['water_still_quantity']
        water_still_unit_cost = request.POST['water_still_unit_cost']
        water_still_total_cost = request.POST['water_still_total_cost']
        water_still_lifespan = request.POST['water_still_lifespan']
        water_still_salvage_value = request.POST['water_still_salvage_value']
        water_still_annual_depreciation = request.POST['water_still_annual_depreciation']
        water_still_annual_cost = request.POST['water_still_annual_cost']
        micropore_filtration_system_quantity = request.POST['micropore_filtration_system_quantity']
        micropore_filtration_system_unit_cost = request.POST['micropore_filtration_system_unit_cost']
        micropore_filtration_system_total_cost = request.POST['micropore_filtration_system_total_cost']
        micropore_filtration_system_lifespan = request.POST['micropore_filtration_system_lifespan']
        micropore_filtration_system_salvage_value = request.POST['micropore_filtration_system_salvage_value']
        micropore_filtration_system_annual_depreciation = request.POST['micropore_filtration_system_annual_depreciation']
        micropore_filtration_system_annual_cost = request.POST['micropore_filtration_system_annual_cost']
        generator_fuel_quantity = request.POST['generator_fuel_quantity']
        generator_fuel_unit_cost = request.POST['generator_fuel_unit_cost']
        generator_fuel_total_cost = request.POST['generator_fuel_total_cost']
        generator_fuel_lifespan = request.POST['generator_fuel_lifespan']
        generator_fuel_salvage_value = request.POST['generator_fuel_salvage_value']
        generator_fuel_annual_depreciation = request.POST['generator_fuel_annual_depreciation']
        generator_fuel_annual_cost = request.POST['generator_fuel_annual_cost']
        lab_staff_training_quantity = request.POST['lab_staff_training_quantity']
        lab_staff_training_unit_cost = request.POST['lab_staff_training_unit_cost']
        lab_staff_training_total_cost = request.POST['lab_staff_training_total_cost']
        lab_staff_training_lifespan = request.POST['lab_staff_training_lifespan']
        lab_staff_training_salvage_value = request.POST['lab_staff_training_salvage_value']
        lab_staff_training_annual_depreciation = request.POST['lab_staff_training_annual_depreciation']
        lab_staff_training_annual_cost = request.POST['lab_staff_training_annual_cost']
        lab_staff_DSA_training_quantity = request.POST['lab_staff_DSA_training_quantity']
        lab_staff_DSA_training_unit_cost = request.POST['lab_staff_DSA_training_unit_cost']
        lab_staff_DSA_training_total_cost = request.POST['lab_staff_DSA_training_total_cost']
        lab_staff_DSA_training_lifespan = request.POST['lab_staff_DSA_training_lifespan']
        lab_staff_DSA_training_salvage_value = request.POST['lab_staff_DSA_training_salvage_value']
        lab_staff_DSA_training_annual_depreciation = request.POST['lab_staff_DSA_training_annual_depreciation']
        lab_staff_DSA_training_annual_cost = request.POST['lab_staff_DSA_training_annual_cost']
        lab_staff_training_transport_quantity = request.POST['lab_staff_training_transport_quantity']
        lab_staff_training_transport_unit_cost = request.POST['lab_staff_training_transport_unit_cost']
        lab_staff_training_transport_total_cost = request.POST['lab_staff_training_transport_total_cost']
        lab_staff_training_transport_lifespan = request.POST['lab_staff_training_transport_lifespan']
        lab_staff_training_transport_salvage_value = request.POST['lab_staff_training_transport_salvage_value']
        lab_staff_training_transport_annual_depreciation = request.POST['lab_staff_training_transport_annual_depreciation']
        lab_staff_training_transport_annual_cost = request.POST['lab_staff_training_transport_annual_cost']
        lab_diagnosis_total = request.POST['lab_diagnosis_total']

        x = rvf_initial_collection.insert_one({
            'RT_PCR_Machine_quantity': RT_PCR_Machine_quantity,
            'RT_PCR_Machine_unit_cost': RT_PCR_Machine_unit_cost,
            'RT_PCR_Machine_total_cost': float(RT_PCR_Machine_quantity) * float(RT_PCR_Machine_unit_cost),
            'RT_PCR_Machine_lifespan': RT_PCR_Machine_lifespan,
            'RT_PCR_Machine_salvage_value': RT_PCR_Machine_salvage_value,
            'RT_PCR_Machine_annual_depreciation': (float(RT_PCR_Machine_total_cost) / float(RT_PCR_Machine_lifespan)),
            'RT_PCR_Machine_annual_cost': (float(RT_PCR_Machine_total_cost) / float(RT_PCR_Machine_lifespan)),
            'pipettes_quantity': pipettes_quantity,
            'pipettes_unit_cost': pipettes_unit_cost,
            'pipettes_total_cost': float(pipettes_quantity) * float(pipettes_unit_cost),
            'pipettes_lifespan': pipettes_lifespan,
            'pipettes_salvage_value': pipettes_salvage_value,
            'pipettes_annual_depreciation': (float(pipettes_total_cost) / float(pipettes_lifespan)),
            'pipettes_annual_cost': (float(pipettes_total_cost) / float(pipettes_lifespan)),
            'reagents_quantity': reagents_quantity,
            'reagents_unit_cost': reagents_unit_cost,
            'reagents_total_cost': float(reagents_quantity) * float(reagents_unit_cost),
            'reagents_lifespan': reagents_lifespan,
            'reagents_salvage_value': reagents_salvage_value,
            'reagents_annual_depreciation': reagents_annual_depreciation,
            'reagents_annual_cost': (float(reagents_quantity) * float(reagents_unit_cost)),
            'consumables_quantity': consumables_quantity,
            'consumables_unit_cost': consumables_unit_cost,
            'consumables_total_cost': float(consumables_quantity) * float(consumables_unit_cost),
            'consumables_lifespan': consumables_lifespan,
            'consumables_salvage_value': consumables_salvage_value,
            'consumables_annual_depreciation': consumables_annual_depreciation,
            'consumables_annual_cost': (float(consumables_quantity) * float(consumables_unit_cost)),
            'computer_quantity': computer_quantity,
            'computer_unit_cost': computer_unit_cost,
            'computer_total_cost': float(computer_quantity) * float(computer_unit_cost),
            'computer_lifespan': computer_lifespan,
            'computer_salvage_value': computer_salvage_value,
            'computer_annual_depreciation': (float(computer_total_cost) - float(computer_salvage_value)) / float(
                computer_lifespan),
            'computer_annual_cost': (float(computer_total_cost) - float(computer_salvage_value)) / float(
                computer_lifespan),
            'PCR_staff_working_quantity': PCR_staff_working_quantity,
            'PCR_staff_working_unit_cost': PCR_staff_working_unit_cost,
            'PCR_staff_working_total_cost': float(PCR_staff_working_quantity) * float(PCR_staff_working_unit_cost),
            'PCR_staff_working_lifespan': PCR_staff_working_lifespan,
            'PCR_staff_working_salvage_value': PCR_staff_working_salvage_value,
            'PCR_staff_working_annual_depreciation': PCR_staff_working_annual_depreciation,
            'PCR_staff_working_annual_cost': (float(PCR_staff_working_quantity) * float(PCR_staff_working_unit_cost)),
            'incubator_quantity': incubator_quantity,
            'incubator_unit_cost': incubator_unit_cost,
            'incubator_total_cost': float(incubator_quantity) * float(incubator_unit_cost),
            'incubator_lifespan': incubator_lifespan,
            'incubator_salvage_value': incubator_salvage_value,
            'incubator_annual_depreciation': (float(incubator_total_cost) / float(incubator_lifespan)),
            'incubator_annual_cost': (float(incubator_total_cost) / float(incubator_lifespan)),
            'dissection_microscope_quantity': dissection_microscope_quantity,
            'dissection_microscope_unit_cost': dissection_microscope_unit_cost,
            'dissection_microscope_total_cost': float(dissection_microscope_quantity) * float(
                dissection_microscope_unit_cost),
            'dissection_microscope_lifespan': dissection_microscope_lifespan,
            'dissection_microscope_salvage_value': dissection_microscope_salvage_value,
            'dissection_microscope_annual_depreciation': (
                        float(dissection_microscope_total_cost) / float(dissection_microscope_lifespan)),
            'dissection_microscope_annual_cost': (
                        float(dissection_microscope_total_cost) / float(dissection_microscope_lifespan)),
            'VNT_reagents_quantity': VNT_reagents_quantity,
            'VNT_reagents_unit_cost': VNT_reagents_unit_cost,
            'VNT_reagents_total_cost': float(VNT_reagents_quantity) * float(VNT_reagents_unit_cost),
            'VNT_reagents_lifespan': VNT_reagents_lifespan,
            'VNT_reagents_salvage_value': VNT_reagents_salvage_value,
            'VNT_reagents_annual_depreciation': VNT_reagents_annual_depreciation,
            'VNT_reagents_annual_cost': float(VNT_reagents_quantity) * float(VNT_reagents_unit_cost),
            'VNT_consumables_quantity': VNT_consumables_quantity,
            'VNT_consumables_unit_cost': VNT_consumables_unit_cost,
            'VNT_consumables_total_cost': float(VNT_consumables_quantity) * float(VNT_consumables_unit_cost),
            'VNT_consumables_lifespan': VNT_consumables_lifespan,
            'VNT_consumables_salvage_value': VNT_consumables_salvage_value,
            'VNT_consumables_annual_depreciation': VNT_consumables_annual_depreciation,
            'VNT_consumables_annual_cost': float(VNT_consumables_quantity) * float(VNT_consumables_unit_cost),
            'VNT_staff_working_quantity': VNT_staff_working_quantity,
            'VNT_staff_working_unit_cost': VNT_staff_working_unit_cost,
            'VNT_staff_working_total_cost': float(VNT_staff_working_quantity) * float(VNT_staff_working_unit_cost),
            'VNT_staff_working_lifespan': VNT_staff_working_lifespan,
            'VNT_staff_working_salvage_value': VNT_staff_working_salvage_value,
            'VNT_staff_working_annual_depreciation': VNT_staff_working_annual_depreciation,
            'VNT_staff_working_annual_cost': float(VNT_staff_working_quantity) * float(VNT_staff_working_unit_cost),
            'ELISA_reader_quantity': ELISA_reader_quantity,
            'ELISA_reader_unit_cost': ELISA_reader_unit_cost,
            'ELISA_reader_total_cost': float(ELISA_reader_quantity) * float(ELISA_reader_unit_cost),
            'ELISA_reader_lifespan': ELISA_reader_lifespan,
            'ELISA_reader_salvage_value': ELISA_reader_salvage_value,
            'ELISA_reader_annual_depreciation': (float(ELISA_reader_total_cost) / float(ELISA_reader_lifespan)),
            'ELISA_reader_annual_cost': (float(ELISA_reader_total_cost) / float(ELISA_reader_lifespan)),
            'ELISA_kits_quantity': ELISA_kits_quantity,
            'ELISA_kits_unit_cost': ELISA_kits_unit_cost,
            'ELISA_kits_total_cost': float(ELISA_kits_quantity) * float(ELISA_kits_unit_cost),
            'ELISA_kits_lifespan': ELISA_kits_lifespan,
            'ELISA_kits_salvage_value': ELISA_kits_salvage_value,
            'ELISA_kits_annual_depreciation': ELISA_kits_annual_depreciation,
            'ELISA_kits_annual_cost': float(ELISA_kits_quantity) * float(ELISA_kits_unit_cost),
            'ELISA_computer_quantity': ELISA_computer_quantity,
            'ELISA_computer_unit_cost': ELISA_computer_unit_cost,
            'ELISA_computer_total_cost': float(ELISA_computer_quantity) * float(ELISA_computer_unit_cost),
            'ELISA_computer_lifespan': ELISA_computer_lifespan,
            'ELISA_computer_salvage_value': ELISA_computer_salvage_value,
            'ELISA_computer_annual_depreciation': (float(ELISA_computer_total_cost) - float(
                ELISA_computer_salvage_value)) / float(ELISA_computer_lifespan),
            'ELISA_computer_annual_cost': (float(ELISA_computer_total_cost) - float(
                ELISA_computer_salvage_value)) / float(ELISA_computer_lifespan),
            'ELISA_incubator_shaker_quantity': ELISA_incubator_shaker_quantity,
            'ELISA_incubator_shaker_unit_cost': ELISA_incubator_shaker_unit_cost,
            'ELISA_incubator_shaker_total_cost': float(ELISA_incubator_shaker_quantity) * float(
                ELISA_incubator_shaker_unit_cost),
            'ELISA_incubator_shaker_lifespan': ELISA_incubator_shaker_lifespan,
            'ELISA_incubator_shaker_salvage_value': ELISA_incubator_shaker_salvage_value,
            'ELISA_incubator_shaker_annual_depreciation': (
                        float(ELISA_incubator_shaker_total_cost) / float(ELISA_incubator_shaker_lifespan)),
            'ELISA_incubator_shaker_annual_cost': (
                        float(ELISA_incubator_shaker_total_cost) / float(ELISA_incubator_shaker_lifespan)),
            'ELISA_platewasher_quantity': ELISA_platewasher_quantity,
            'ELISA_platewasher_unit_cost': ELISA_platewasher_unit_cost,
            'ELISA_platewasher_total_cost': float(ELISA_platewasher_quantity) * float(ELISA_platewasher_unit_cost),
            'ELISA_platewasher_lifespan': ELISA_platewasher_lifespan,
            'ELISA_platewasher_salvage_value': ELISA_platewasher_salvage_value,
            'ELISA_platewasher_annual_depreciation': (
                        float(ELISA_platewasher_total_cost) / float(ELISA_platewasher_lifespan)),
            'ELISA_platewasher_annual_cost': (float(ELISA_platewasher_total_cost) / float(ELISA_platewasher_lifespan)),
            'ELISA_consumables_quantity': ELISA_consumables_quantity,
            'ELISA_consumables_unit_cost': ELISA_consumables_unit_cost,
            'ELISA_consumables_total_cost': float(ELISA_consumables_quantity) * float(ELISA_consumables_unit_cost),
            'ELISA_consumables_lifespan': ELISA_consumables_lifespan,
            'ELISA_consumables_salvage_value': ELISA_consumables_salvage_value,
            'ELISA_consumables_annual_depreciation': ELISA_consumables_annual_depreciation,
            'ELISA_consumables_annual_cost': float(ELISA_consumables_quantity) * float(ELISA_consumables_unit_cost),
            'ELISA_staff_working_quantity': ELISA_staff_working_quantity,
            'ELISA_staff_working_unit_cost': ELISA_staff_working_unit_cost,
            'ELISA_staff_working_total_cost': float(ELISA_staff_working_quantity) * float(
                ELISA_staff_working_unit_cost),
            'ELISA_staff_working_lifespan': ELISA_staff_working_lifespan,
            'ELISA_staff_working_salvage_value': ELISA_staff_working_salvage_value,
            'ELISA_staff_working_annual_depreciation': ELISA_staff_working_annual_depreciation,
            'ELISA_staff_working_annual_cost': float(ELISA_staff_working_quantity) * float(
                ELISA_staff_working_unit_cost),
            'laboratory_generator_quantity': laboratory_generator_quantity,
            'laboratory_generator_unit_cost': laboratory_generator_unit_cost,
            'laboratory_generator_total_cost': float(laboratory_generator_quantity) * float(
                laboratory_generator_unit_cost),
            'laboratory_generator_lifespan': laboratory_generator_lifespan,
            'laboratory_generator_salvage_value': laboratory_generator_salvage_value,
            'laboratory_generator_annual_depreciation': (float(laboratory_generator_total_cost) - float(
                laboratory_generator_salvage_value)) / float(laboratory_generator_lifespan),
            'laboratory_generator_annual_cost': (float(laboratory_generator_total_cost) - float(
                laboratory_generator_salvage_value)) / float(laboratory_generator_lifespan),
            'freezers_quantity': freezers_quantity,
            'freezers_unit_cost': freezers_unit_cost,
            'freezers_total_cost': float(freezers_quantity) * float(freezers_unit_cost),
            'freezers_lifespan': freezers_lifespan,
            'freezers_salvage_value': freezers_salvage_value,
            'freezers_annual_depreciation': (float(freezers_total_cost) - float(freezers_salvage_value)) / float(
                freezers_lifespan),
            'freezers_annual_cost': (float(freezers_total_cost) - float(freezers_salvage_value)) / float(
                freezers_lifespan),
            'refrigerators_quantity': refrigerators_quantity,
            'refrigerators_unit_cost': refrigerators_unit_cost,
            'refrigerators_total_cost': float(refrigerators_quantity) * float(refrigerators_unit_cost),
            'refrigerators_lifespan': refrigerators_lifespan,
            'refrigerators_salvage_value': refrigerators_salvage_value,
            'refrigerators_annual_depreciation': (float(refrigerators_total_cost) - float(
                refrigerators_salvage_value)) / float(refrigerators_lifespan),
            'refrigerators_annual_cost': (float(refrigerators_total_cost) - float(refrigerators_salvage_value)) / float(
                refrigerators_lifespan),
            'water_quantity': water_quantity,
            'water_unit_cost': water_unit_cost,
            'water_total_cost': float(water_quantity) * float(water_unit_cost),
            'water_lifespan': water_lifespan,
            'water_salvage_value': water_salvage_value,
            'water_annual_depreciation': water_annual_depreciation,
            'water_annual_cost': float(water_quantity) * float(water_unit_cost),
            'electricity_quantity': electricity_quantity,
            'electricity_unit_cost': electricity_unit_cost,
            'electricity_total_cost': float(electricity_quantity) * float(electricity_unit_cost),
            'electricity_lifespan': electricity_lifespan,
            'electricity_salvage_value': electricity_salvage_value,
            'electricity_annual_depreciation': electricity_annual_depreciation,
            'electricity_annual_cost': float(electricity_quantity) * float(electricity_unit_cost),
            'equipment_calibration_quantity': equipment_calibration_quantity,
            'equipment_calibration_unit_cost': equipment_calibration_unit_cost,
            'equipment_calibration_total_cost': float(equipment_calibration_quantity) * float(
                equipment_calibration_unit_cost),
            'equipment_calibration_lifespan': equipment_calibration_lifespan,
            'equipment_calibration_salvage_value': equipment_calibration_salvage_value,
            'equipment_calibration_annual_depreciation': equipment_calibration_annual_depreciation,
            'equipment_calibration_annual_cost': float(equipment_calibration_quantity) * float(
                equipment_calibration_unit_cost),
            'expert_consultation_quantity': expert_consultation_quantity,
            'expert_consultation_unit_cost': expert_consultation_unit_cost,
            'expert_consultation_total_cost': float(expert_consultation_quantity) * float(
                expert_consultation_unit_cost),
            'expert_consultation_lifespan': expert_consultation_lifespan,
            'expert_consultation_salvage_value': expert_consultation_salvage_value,
            'expert_consultation_annual_depreciation': expert_consultation_annual_depreciation,
            'expert_consultation_annual_cost': float(expert_consultation_quantity) * float(
                expert_consultation_unit_cost),
            'water_still_quantity': water_still_quantity,
            'water_still_unit_cost': water_still_unit_cost,
            'water_still_total_cost': float(water_still_quantity) * float(water_still_unit_cost),
            'water_still_lifespan': water_still_lifespan,
            'water_still_salvage_value': water_still_salvage_value,
            'water_still_annual_depreciation': (float(water_still_total_cost) / float(water_still_lifespan)),
            'water_still_annual_cost': (float(water_still_total_cost) / float(water_still_lifespan)),
            'micropore_filtration_system_quantity': micropore_filtration_system_quantity,
            'micropore_filtration_system_unit_cost': micropore_filtration_system_unit_cost,
            'micropore_filtration_system_total_cost': float(micropore_filtration_system_quantity) * float(
                micropore_filtration_system_unit_cost),
            'micropore_filtration_system_lifespan': micropore_filtration_system_lifespan,
            'micropore_filtration_system_salvage_value': micropore_filtration_system_salvage_value,
            'micropore_filtration_system_annual_depreciation': (
                        float(micropore_filtration_system_total_cost) / float(micropore_filtration_system_lifespan)),
            'micropore_filtration_system_annual_cost': (
                        float(micropore_filtration_system_total_cost) / float(micropore_filtration_system_lifespan)),
            'generator_fuel_quantity': generator_fuel_quantity,
            'generator_fuel_unit_cost': generator_fuel_unit_cost,
            'generator_fuel_total_cost': float(generator_fuel_quantity) * float(generator_fuel_unit_cost),
            'generator_fuel_lifespan': generator_fuel_lifespan,
            'generator_fuel_salvage_value': generator_fuel_salvage_value,
            'generator_fuel_annual_depreciation': generator_fuel_annual_depreciation,
            'generator_fuel_annual_cost': float(generator_fuel_quantity) * float(generator_fuel_unit_cost),
            'lab_staff_training_quantity': lab_staff_training_quantity,
            'lab_staff_training_unit_cost': lab_staff_training_unit_cost,
            'lab_staff_training_total_cost': float(lab_staff_training_quantity) * float(lab_staff_training_unit_cost),
            'lab_staff_training_lifespan': lab_staff_training_lifespan,
            'lab_staff_training_salvage_value': lab_staff_training_salvage_value,
            'lab_staff_training_annual_depreciation': lab_staff_training_annual_depreciation,
            'lab_staff_training_annual_cost': float(lab_staff_training_quantity) * float(lab_staff_training_unit_cost),
            'lab_staff_DSA_training_quantity': lab_staff_DSA_training_quantity,
            'lab_staff_DSA_training_unit_cost': lab_staff_DSA_training_unit_cost,
            'lab_staff_DSA_training_total_cost': float(lab_staff_DSA_training_quantity) * float(
                lab_staff_DSA_training_unit_cost),
            'lab_staff_DSA_training_lifespan': lab_staff_DSA_training_lifespan,
            'lab_staff_DSA_training_salvage_value': lab_staff_DSA_training_salvage_value,
            'lab_staff_DSA_training_annual_depreciation': lab_staff_DSA_training_annual_depreciation,
            'lab_staff_DSA_training_annual_cost': float(lab_staff_DSA_training_quantity) * float(
                lab_staff_DSA_training_unit_cost),
            'lab_staff_training_transport_quantity': lab_staff_training_transport_quantity,
            'lab_staff_training_transport_unit_cost': lab_staff_training_transport_unit_cost,
            'lab_staff_training_transport_total_cost': float(lab_staff_training_transport_quantity) * float(
                lab_staff_training_transport_unit_cost),
            'lab_staff_training_transport_lifespan': lab_staff_training_transport_lifespan,
            'lab_staff_training_transport_salvage_value': lab_staff_training_transport_salvage_value,
            'lab_staff_training_transport_annual_depreciation': lab_staff_training_transport_annual_depreciation,
            'lab_staff_training_transport_annual_cost': float(lab_staff_training_transport_quantity) * float(
                lab_staff_training_transport_unit_cost),
            'lab_diagnosis_total': (float(RT_PCR_Machine_total_cost) / float(RT_PCR_Machine_lifespan)) +
                               (float(pipettes_total_cost) / float(pipettes_lifespan)) +
                               (float(reagents_total_cost)) +
                               (float(consumables_total_cost)) +
                               ((float(computer_total_cost) - float(computer_salvage_value)) / float(computer_lifespan)) +
                                (float(PCR_staff_working_total_cost)) +
                                (float(incubator_total_cost) / float(incubator_lifespan)) +
                                (float(dissection_microscope_total_cost) / float(dissection_microscope_lifespan)) +
                                (float(VNT_reagents_total_cost)) +
                                (float(VNT_consumables_total_cost)) +
                                (float(VNT_staff_working_total_cost)) +
                                (float(ELISA_reader_total_cost) / float(ELISA_reader_lifespan)) +
                                (float(ELISA_kits_total_cost)) +
                                ((float(ELISA_computer_total_cost) - float(ELISA_computer_salvage_value)) / float(ELISA_computer_lifespan)) +
                                (float(ELISA_incubator_shaker_total_cost) / float(ELISA_incubator_shaker_lifespan)) +
                                (float(ELISA_platewasher_total_cost) / float(ELISA_platewasher_lifespan)) +
                                (float(ELISA_consumables_total_cost)) +
                                (float(ELISA_staff_working_total_cost)) +
                                ((float(laboratory_generator_total_cost) - float(laboratory_generator_salvage_value)) / float(laboratory_generator_lifespan)) +
                                ((float(freezers_total_cost) - float(freezers_salvage_value)) / float(freezers_lifespan)) +
                                ((float(refrigerators_total_cost) - float(refrigerators_salvage_value)) / float(refrigerators_lifespan)) +
                                (float(water_total_cost)) +
                                (float(electricity_total_cost)) +
                                (float(equipment_calibration_total_cost)) +
                                (float(expert_consultation_total_cost)) +
                                (float(water_still_total_cost) / float(water_still_lifespan)) +
                                (float(micropore_filtration_system_total_cost) / float(micropore_filtration_system_lifespan)) +
                                (float(generator_fuel_total_cost)) +
                                (float(lab_staff_training_total_cost)) +
                                (float(lab_staff_DSA_training_total_cost)) +
                                (float(lab_staff_training_transport_total_cost)),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'RT_PCR_Machine_quantity': context['RT_PCR_Machine_quantity'],
        'RT_PCR_Machine_unit_cost': context['RT_PCR_Machine_unit_cost'],
        'RT_PCR_Machine_total_cost': context['RT_PCR_Machine_total_cost'],
        'RT_PCR_Machine_lifespan': context['RT_PCR_Machine_lifespan'],
        'RT_PCR_Machine_salvage_value': context['RT_PCR_Machine_salvage_value'],
        'RT_PCR_Machine_annual_depreciation': float(context['RT_PCR_Machine_total_cost']) / float(
            context['RT_PCR_Machine_lifespan']),
        'RT_PCR_Machine_annual_cost': float(context['RT_PCR_Machine_total_cost']) / float(
            context['RT_PCR_Machine_lifespan']),
        'pipettes_quantity': context['pipettes_quantity'],
        'pipettes_unit_cost': context['pipettes_unit_cost'],
        'pipettes_total_cost': context['pipettes_total_cost'],
        'pipettes_lifespan': context['pipettes_lifespan'],
        'pipettes_salvage_value': context['pipettes_salvage_value'],
        'pipettes_annual_depreciation': float(context['pipettes_total_cost']) / float(context['pipettes_lifespan']),
        'pipettes_annual_cost': float(context['pipettes_total_cost']) / float(context['pipettes_lifespan']),
        'reagents_quantity': context['reagents_quantity'],
        'reagents_unit_cost': context['reagents_unit_cost'],
        'reagents_total_cost': context['reagents_total_cost'],
        'reagents_lifespan': context['reagents_lifespan'],
        'reagents_salvage_value': context['reagents_salvage_value'],
        'reagents_annual_depreciation': context['reagents_annual_depreciation'],
        'reagents_annual_cost': context['reagents_total_cost'],
        'consumables_quantity': context['consumables_quantity'],
        'consumables_unit_cost': context['consumables_unit_cost'],
        'consumables_total_cost': context['consumables_total_cost'],
        'consumables_lifespan': context['consumables_lifespan'],
        'consumables_salvage_value': context['consumables_salvage_value'],
        'consumables_annual_depreciation': context['consumables_annual_depreciation'],
        'consumables_annual_cost': context['consumables_total_cost'],
        'computer_quantity': context['computer_quantity'],
        'computer_unit_cost': context['computer_unit_cost'],
        'computer_total_cost': context['computer_total_cost'],
        'computer_lifespan': context['computer_lifespan'],
        'computer_salvage_value': context['computer_salvage_value'],
        'computer_annual_depreciation': (float(context['computer_total_cost']) - float(
            context['computer_salvage_value'])) / float(context['computer_lifespan']),
        'computer_annual_cost': (float(context['computer_total_cost']) - float(
            context['computer_salvage_value'])) / float(context['computer_lifespan']),
        'PCR_staff_working_quantity': context['PCR_staff_working_quantity'],
        'PCR_staff_working_unit_cost': context['PCR_staff_working_unit_cost'],
        'PCR_staff_working_total_cost': context['PCR_staff_working_total_cost'],
        'PCR_staff_working_lifespan': context['PCR_staff_working_lifespan'],
        'PCR_staff_working_salvage_value': context['PCR_staff_working_salvage_value'],
        'PCR_staff_working_annual_depreciation': context['PCR_staff_working_annual_depreciation'],
        'PCR_staff_working_annual_cost': context['PCR_staff_working_total_cost'],
        'incubator_quantity': context['incubator_quantity'],
        'incubator_unit_cost': context['incubator_unit_cost'],
        'incubator_total_cost': context['incubator_total_cost'],
        'incubator_lifespan': context['incubator_lifespan'],
        'incubator_salvage_value': context['incubator_salvage_value'],
        'incubator_annual_depreciation': float(context['incubator_total_cost']) / float(context['incubator_lifespan']),
        'incubator_annual_cost': float(context['incubator_total_cost']) / float(context['incubator_lifespan']),
        'dissection_microscope_quantity': context['dissection_microscope_quantity'],
        'dissection_microscope_unit_cost': context['dissection_microscope_unit_cost'],
        'dissection_microscope_total_cost': context['dissection_microscope_total_cost'],
        'dissection_microscope_lifespan': context['dissection_microscope_lifespan'],
        'dissection_microscope_salvage_value': context['dissection_microscope_salvage_value'],
        'dissection_microscope_annual_depreciation': float(context['dissection_microscope_total_cost']) / float(
            context['dissection_microscope_lifespan']),
        'dissection_microscope_annual_cost': float(context['dissection_microscope_total_cost']) / float(
            context['dissection_microscope_lifespan']),
        'VNT_reagents_quantity': context['VNT_reagents_quantity'],
        'VNT_reagents_unit_cost': context['VNT_reagents_unit_cost'],
        'VNT_reagents_total_cost': context['VNT_reagents_total_cost'],
        'VNT_reagents_lifespan': context['VNT_reagents_lifespan'],
        'VNT_reagents_salvage_value': context['VNT_reagents_salvage_value'],
        'VNT_reagents_annual_depreciation': context['VNT_reagents_annual_depreciation'],
        'VNT_reagents_annual_cost': context['VNT_reagents_total_cost'],
        'VNT_consumables_quantity': context['VNT_consumables_quantity'],
        'VNT_consumables_unit_cost': context['VNT_consumables_unit_cost'],
        'VNT_consumables_total_cost': context['VNT_consumables_total_cost'],
        'VNT_consumables_lifespan': context['VNT_consumables_lifespan'],
        'VNT_consumables_salvage_value': context['VNT_consumables_salvage_value'],
        'VNT_consumables_annual_depreciation': context['VNT_consumables_annual_depreciation'],
        'VNT_consumables_annual_cost': context['VNT_consumables_total_cost'],
        'VNT_staff_working_quantity': context['VNT_staff_working_quantity'],
        'VNT_staff_working_unit_cost': context['VNT_staff_working_unit_cost'],
        'VNT_staff_working_total_cost': context['VNT_staff_working_total_cost'],
        'VNT_staff_working_lifespan': context['VNT_staff_working_lifespan'],
        'VNT_staff_working_salvage_value': context['VNT_staff_working_salvage_value'],
        'VNT_staff_working_annual_depreciation': context['VNT_staff_working_annual_depreciation'],
        'VNT_staff_working_annual_cost': context['VNT_staff_working_total_cost'],
        'ELISA_reader_quantity': context['ELISA_reader_quantity'],
        'ELISA_reader_unit_cost': context['ELISA_reader_unit_cost'],
        'ELISA_reader_total_cost': context['ELISA_reader_total_cost'],
        'ELISA_reader_lifespan': context['ELISA_reader_lifespan'],
        'ELISA_reader_salvage_value': context['ELISA_reader_salvage_value'],
        'ELISA_reader_annual_depreciation': float(context['ELISA_reader_total_cost']) / float(
            context['ELISA_reader_lifespan']),
        'ELISA_reader_annual_cost': float(context['ELISA_reader_total_cost']) / float(context['ELISA_reader_lifespan']),
        'ELISA_kits_quantity': context['ELISA_kits_quantity'],
        'ELISA_kits_unit_cost': context['ELISA_kits_unit_cost'],
        'ELISA_kits_total_cost': context['ELISA_kits_total_cost'],
        'ELISA_kits_lifespan': context['ELISA_kits_lifespan'],
        'ELISA_kits_salvage_value': context['ELISA_kits_salvage_value'],
        'ELISA_kits_annual_depreciation': context['ELISA_kits_annual_depreciation'],
        'ELISA_kits_annual_cost': context['ELISA_kits_total_cost'],
        'ELISA_computer_quantity': context['ELISA_computer_quantity'],
        'ELISA_computer_unit_cost': context['ELISA_computer_unit_cost'],
        'ELISA_computer_total_cost': context['ELISA_computer_total_cost'],
        'ELISA_computer_lifespan': context['ELISA_computer_lifespan'],
        'ELISA_computer_salvage_value': context['ELISA_computer_salvage_value'],
        'ELISA_computer_annual_depreciation': (float(context['ELISA_computer_total_cost']) - float(
            context['ELISA_computer_salvage_value'])) / float(context['ELISA_computer_lifespan']),
        'ELISA_computer_annual_cost': (float(context['ELISA_computer_total_cost']) - float(
            context['ELISA_computer_salvage_value'])) / float(context['ELISA_computer_lifespan']),
        'ELISA_incubator_shaker_quantity': context['ELISA_incubator_shaker_quantity'],
        'ELISA_incubator_shaker_unit_cost': context['ELISA_incubator_shaker_unit_cost'],
        'ELISA_incubator_shaker_total_cost': context['ELISA_incubator_shaker_total_cost'],
        'ELISA_incubator_shaker_lifespan': context['ELISA_incubator_shaker_lifespan'],
        'ELISA_incubator_shaker_salvage_value': context['ELISA_incubator_shaker_salvage_value'],
        'ELISA_incubator_shaker_annual_depreciation': float(context['ELISA_incubator_shaker_total_cost']) / float(
            context['ELISA_incubator_shaker_lifespan']),
        'ELISA_incubator_shaker_annual_cost': float(context['ELISA_incubator_shaker_total_cost']) / float(
            context['ELISA_incubator_shaker_lifespan']),
        'ELISA_platewasher_quantity': context['ELISA_platewasher_quantity'],
        'ELISA_platewasher_unit_cost': context['ELISA_platewasher_unit_cost'],
        'ELISA_platewasher_total_cost': context['ELISA_platewasher_total_cost'],
        'ELISA_platewasher_lifespan': context['ELISA_platewasher_lifespan'],
        'ELISA_platewasher_salvage_value': context['ELISA_platewasher_salvage_value'],
        'ELISA_platewasher_annual_depreciation': float(context['ELISA_platewasher_total_cost']) / float(
            context['ELISA_platewasher_lifespan']),
        'ELISA_platewasher_annual_cost': float(context['ELISA_platewasher_total_cost']) / float(
            context['ELISA_platewasher_lifespan']),
        'ELISA_consumables_quantity': context['ELISA_consumables_quantity'],
        'ELISA_consumables_unit_cost': context['ELISA_consumables_unit_cost'],
        'ELISA_consumables_total_cost': context['ELISA_consumables_total_cost'],
        'ELISA_consumables_lifespan': context['ELISA_consumables_lifespan'],
        'ELISA_consumables_salvage_value': context['ELISA_consumables_salvage_value'],
        'ELISA_consumables_annual_depreciation': context['ELISA_consumables_annual_depreciation'],
        'ELISA_consumables_annual_cost': context['ELISA_consumables_total_cost'],
        'ELISA_staff_working_quantity': context['ELISA_staff_working_quantity'],
        'ELISA_staff_working_unit_cost': context['ELISA_staff_working_unit_cost'],
        'ELISA_staff_working_total_cost': context['ELISA_staff_working_total_cost'],
        'ELISA_staff_working_lifespan': context['ELISA_staff_working_lifespan'],
        'ELISA_staff_working_salvage_value': context['ELISA_staff_working_salvage_value'],
        'ELISA_staff_working_annual_depreciation': context['ELISA_staff_working_annual_depreciation'],
        'ELISA_staff_working_annual_cost': context['ELISA_staff_working_total_cost'],
        'laboratory_generator_quantity': context['laboratory_generator_quantity'],
        'laboratory_generator_unit_cost': context['laboratory_generator_unit_cost'],
        'laboratory_generator_total_cost': context['laboratory_generator_total_cost'],
        'laboratory_generator_lifespan': context['laboratory_generator_lifespan'],
        'laboratory_generator_salvage_value': context['laboratory_generator_salvage_value'],
        'laboratory_generator_annual_depreciation': (float(context['laboratory_generator_total_cost']) - float(
            context['laboratory_generator_salvage_value'])) / float(context['laboratory_generator_lifespan']),
        'laboratory_generator_annual_cost': (float(context['laboratory_generator_total_cost']) - float(
            context['laboratory_generator_salvage_value'])) / float(context['laboratory_generator_lifespan']),
        'freezers_quantity': context['freezers_quantity'],
        'freezers_unit_cost': context['freezers_unit_cost'],
        'freezers_total_cost': context['freezers_total_cost'],
        'freezers_lifespan': context['freezers_lifespan'],
        'freezers_salvage_value': context['freezers_salvage_value'],
        'freezers_annual_depreciation': (float(context['freezers_total_cost']) - float(
            context['freezers_salvage_value'])) / float(context['freezers_lifespan']),
        'freezers_annual_cost': (float(context['freezers_total_cost']) - float(
            context['freezers_salvage_value'])) / float(context['freezers_lifespan']),
        'refrigerators_quantity': context['refrigerators_quantity'],
        'refrigerators_unit_cost': context['refrigerators_unit_cost'],
        'refrigerators_total_cost': context['refrigerators_total_cost'],
        'refrigerators_lifespan': context['refrigerators_lifespan'],
        'refrigerators_salvage_value': context['refrigerators_salvage_value'],
        'refrigerators_annual_depreciation': (float(context['refrigerators_total_cost']) - float(
            context['refrigerators_salvage_value'])) / float(context['refrigerators_lifespan']),
        'refrigerators_annual_cost': (float(context['refrigerators_total_cost']) - float(
            context['refrigerators_salvage_value'])) / float(context['refrigerators_lifespan']),
        'water_quantity': context['water_quantity'],
        'water_unit_cost': context['water_unit_cost'],
        'water_total_cost': context['water_total_cost'],
        'water_lifespan': context['water_lifespan'],
        'water_salvage_value': context['water_salvage_value'],
        'water_annual_depreciation': context['water_annual_depreciation'],
        'water_annual_cost': context['water_total_cost'],
        'electricity_quantity': context['electricity_quantity'],
        'electricity_unit_cost': context['electricity_unit_cost'],
        'electricity_total_cost': context['electricity_total_cost'],
        'electricity_lifespan': context['electricity_lifespan'],
        'electricity_salvage_value': context['electricity_salvage_value'],
        'electricity_annual_depreciation': context['electricity_annual_depreciation'],
        'electricity_annual_cost': context['electricity_total_cost'],
        'equipment_calibration_quantity': context['equipment_calibration_quantity'],
        'equipment_calibration_unit_cost': context['equipment_calibration_unit_cost'],
        'equipment_calibration_total_cost': context['equipment_calibration_total_cost'],
        'equipment_calibration_lifespan': context['equipment_calibration_lifespan'],
        'equipment_calibration_salvage_value': context['equipment_calibration_salvage_value'],
        'equipment_calibration_annual_depreciation': context['equipment_calibration_annual_depreciation'],
        'equipment_calibration_annual_cost': context['equipment_calibration_total_cost'],
        'expert_consultation_quantity': context['expert_consultation_quantity'],
        'expert_consultation_unit_cost': context['expert_consultation_unit_cost'],
        'expert_consultation_total_cost': context['expert_consultation_total_cost'],
        'expert_consultation_lifespan': context['expert_consultation_lifespan'],
        'expert_consultation_salvage_value': context['expert_consultation_salvage_value'],
        'expert_consultation_annual_depreciation': context['expert_consultation_annual_depreciation'],
        'expert_consultation_annual_cost': context['expert_consultation_total_cost'],
        'water_still_quantity': context['water_still_quantity'],
        'water_still_unit_cost': context['water_still_unit_cost'],
        'water_still_total_cost': context['water_still_total_cost'],
        'water_still_lifespan': context['water_still_lifespan'],
        'water_still_salvage_value': context['water_still_salvage_value'],
        'water_still_annual_depreciation': float(context['water_still_total_cost']) / float(
            context['water_still_lifespan']),
        'water_still_annual_cost': float(context['water_still_total_cost']) / float(context['water_still_lifespan']),
        'micropore_filtration_system_quantity': context['micropore_filtration_system_quantity'],
        'micropore_filtration_system_unit_cost': context['micropore_filtration_system_unit_cost'],
        'micropore_filtration_system_total_cost': context['micropore_filtration_system_total_cost'],
        'micropore_filtration_system_lifespan': context['micropore_filtration_system_lifespan'],
        'micropore_filtration_system_salvage_value': context['micropore_filtration_system_salvage_value'],
        'micropore_filtration_system_annual_depreciation': float(
            context['micropore_filtration_system_total_cost']) / float(context['micropore_filtration_system_lifespan']),
        'micropore_filtration_system_annual_cost': float(context['micropore_filtration_system_total_cost']) / float(
            context['micropore_filtration_system_lifespan']),
        'generator_fuel_quantity': context['generator_fuel_quantity'],
        'generator_fuel_unit_cost': context['generator_fuel_unit_cost'],
        'generator_fuel_total_cost': context['generator_fuel_total_cost'],
        'generator_fuel_lifespan': context['generator_fuel_lifespan'],
        'generator_fuel_salvage_value': context['generator_fuel_salvage_value'],
        'generator_fuel_annual_depreciation': context['generator_fuel_annual_depreciation'],
        'generator_fuel_annual_cost': context['generator_fuel_total_cost'],
        'lab_staff_training_quantity': context['lab_staff_training_quantity'],
        'lab_staff_training_unit_cost': context['lab_staff_training_unit_cost'],
        'lab_staff_training_total_cost': context['lab_staff_training_total_cost'],
        'lab_staff_training_lifespan': context['lab_staff_training_lifespan'],
        'lab_staff_training_salvage_value': context['lab_staff_training_salvage_value'],
        'lab_staff_training_annual_depreciation': context['lab_staff_training_annual_depreciation'],
        'lab_staff_training_annual_cost': context['lab_staff_training_total_cost'],
        'lab_staff_DSA_training_quantity': context['lab_staff_DSA_training_quantity'],
        'lab_staff_DSA_training_unit_cost': context['lab_staff_DSA_training_unit_cost'],
        'lab_staff_DSA_training_total_cost': context['lab_staff_DSA_training_total_cost'],
        'lab_staff_DSA_training_lifespan': context['lab_staff_DSA_training_lifespan'],
        'lab_staff_DSA_training_salvage_value': context['lab_staff_DSA_training_salvage_value'],
        'lab_staff_DSA_training_annual_depreciation': context['lab_staff_DSA_training_annual_depreciation'],
        'lab_staff_DSA_training_annual_cost': context['lab_staff_DSA_training_total_cost'],
        'lab_staff_training_transport_quantity': context['lab_staff_training_transport_quantity'],
        'lab_staff_training_transport_unit_cost': context['lab_staff_training_transport_unit_cost'],
        'lab_staff_training_transport_total_cost': context['lab_staff_training_transport_total_cost'],
        'lab_staff_training_transport_lifespan': context['lab_staff_training_transport_lifespan'],
        'lab_staff_training_transport_salvage_value': context['lab_staff_training_transport_salvage_value'],
        'lab_staff_training_transport_annual_depreciation': context['lab_staff_training_transport_annual_depreciation'],
        'lab_staff_training_transport_annual_cost': context['lab_staff_training_transport_total_cost'],
        'lab_diagnosis_total': (float(context['RT_PCR_Machine_total_cost']) / float( context['RT_PCR_Machine_lifespan'])) +
                               (float(context['pipettes_total_cost']) / float(context['pipettes_lifespan'])) +
                               (float(context['reagents_total_cost'])) +
                               (float(context['consumables_total_cost'])) +
                               ((float(context['computer_total_cost']) - float(context['computer_salvage_value'])) / float(context['computer_lifespan'])) +
                                (float(context['PCR_staff_working_total_cost'])) +
                                (float(context['incubator_total_cost']) / float(context['incubator_lifespan'])) +
                                (float(context['dissection_microscope_total_cost']) / float(context['dissection_microscope_lifespan'])) +
                                (float(context['VNT_reagents_total_cost'])) +
                                (float(context['VNT_consumables_total_cost'])) +
                                (float(context['VNT_staff_working_total_cost'])) +
                                (float(context['ELISA_reader_total_cost']) / float(context['ELISA_reader_lifespan'])) +
                                (float(context['ELISA_kits_total_cost'])) +
                                ((float(context['ELISA_computer_total_cost']) - float(context['ELISA_computer_salvage_value'])) / float(context['ELISA_computer_lifespan'])) +
                                (float(context['ELISA_incubator_shaker_total_cost']) / float(context['ELISA_incubator_shaker_lifespan'])) +
                                (float(context['ELISA_platewasher_total_cost']) / float(context['ELISA_platewasher_lifespan'])) +
                                (float(context['ELISA_consumables_total_cost'])) +
                                (float(context['ELISA_staff_working_total_cost'])) +
                                ((float(context['laboratory_generator_total_cost']) - float(context['laboratory_generator_salvage_value'])) / float(context['laboratory_generator_lifespan'])) +
                                ((float(context['freezers_total_cost']) - float(context['freezers_salvage_value'])) / float(context['freezers_lifespan'])) +
                                ((float(context['refrigerators_total_cost']) - float(context['refrigerators_salvage_value'])) / float(context['refrigerators_lifespan'])) +
                                (float(context['water_total_cost'])) +
                                (float(context['electricity_total_cost'])) +
                                (float(context['equipment_calibration_total_cost'])) +
                                (float(context['expert_consultation_total_cost'])) +
                                (float(context['water_still_total_cost']) / float(context['water_still_lifespan'])) +
                                (float(context['micropore_filtration_system_total_cost']) / float(context['micropore_filtration_system_lifespan'])) +
                                (float(context['generator_fuel_total_cost'])) +
                                (float(context['lab_staff_training_total_cost'])) +
                                (float(context['lab_staff_DSA_training_total_cost'])) +
                                (float(context['lab_staff_training_transport_total_cost'])),
    }

    return render(request,'lab_diagnosis.html',context2)

def coord_and_comm(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['coord_and_comm']

    context = {
        '47lang_training_material_design_per_county_quantity': 0,
        '47lang_training_material_design_total_quantity': 0,
        '47lang_training_material_design_unit_cost': 0,
        '47lang_training_material_design_total_cost': 0,
        'print_materials_per_county_quantity': 0,
        'print_materials_total_quantity': 0,
        'print_materials_unit_cost': 0,
        'print_materials_total_cost': 0,
        '15lang_radiospots_per_county_quantity': 0,
        '15lang_radiospots_total_quantity': 0,
        '15lang_radiospots_unit_cost': 0,
        '15lang_radiospots_total_cost': 0,
        'en_swa_radiospots_per_county_quantity': 0,
        'en_swa_radiospots_total_quantity': 0,
        'en_swa_radiospots_unit_cost': 0,
        'en_swa_radiospots_total_cost': 0,
        'tv_commercials_per_county_quantity': 0,
        'tv_commercials_total_quantity': 0,
        'tv_commercials_unit_cost': 0,
        'tv_commercials_total_cost': 0,
        'sensitization_of_HQ_per_county_quantity': 0,
        'sensitization_of_HQ_total_quantity': 0,
        'sensitization_of_HQ_unit_cost': 0,
        'sensitization_of_HQ_total_cost': 0,
        'print_materials_distribution_per_county_quantity': 0,
        'print_materials_distribution_total_quantity': 0,
        'print_materials_distribution_unit_cost': 0,
        'print_materials_distribution_total_cost': 0,
        'publicity_evaluation_per_county_quantity': 0,
        'publicity_evaluation_total_quantity': 0,
        'publicity_evaluation_unit_cost': 0,
        'publicity_evaluation_total_cost': 0,
        'community_sensitization_meetings_per_county_quantity': 0,
        'community_sensitization_meetings_total_quantity': 0,
        'community_sensitization_meetings_unit_cost': 0,
        'community_sensitization_meetings_total_cost': 0,
        'clinician_training_per_county_quantity': 0,
        'clinician_training_total_quantity': 0,
        'clinician_training_unit_cost': 0,
        'clinician_training_total_cost': 0,
        'transport_per_county_quantity': 0,
        'transport_total_quantity': 0,
        'transport_unit_cost': 0,
        'transport_total_cost': 0,
        'translator_allowance_per_county_quantity': 0,
        'translator_allowance_total_quantity': 0,
        'translator_allowance_unit_cost': 0,
        'translator_allowance_total_cost': 0,
        'vet_epidemiologist_per_county_quantity': 0,
        'vet_epidemiologist_total_quantity': 0,
        'vet_epidemiologist_unit_cost': 0,
        'vet_epidemiologist_total_cost': 0,
        'medical_epidemiologist_per_county_quantity': 0,
        'medical_epidemiologist_total_quantity': 0,
        'medical_epidemiologist_unit_cost': 0,
        'medical_epidemiologist_total_cost': 0,
        'socio_economist_per_county_quantity': 0,
        'socio_economist_total_quantity': 0,
        'socio_economist_unit_cost': 0,
        'socio_economist_total_cost': 0,
        'technician_per_county_quantity': 0,
        'technician_total_quantity': 0,
        'technician_unit_cost': 0,
        'technician_total_cost': 0,
        'driver_per_county_quantity': 0,
        'driver_total_quantity': 0,
        'driver_unit_cost': 0,
        'driver_total_cost': 0,
        'early_detection_total_cost': 0,
    }

    if (request.method == "POST"):
        _47lang_training_material_design_per_county_quantity = request.POST[
            '47lang_training_material_design_per_county_quantity']
        _47lang_training_material_design_total_quantity = request.POST['47lang_training_material_design_total_quantity']
        _47lang_training_material_design_unit_cost = request.POST['47lang_training_material_design_unit_cost']
        _47lang_training_material_design_total_cost = request.POST['47lang_training_material_design_total_cost']
        print_materials_per_county_quantity = request.POST['print_materials_per_county_quantity']
        print_materials_total_quantity = request.POST['print_materials_total_quantity']
        print_materials_unit_cost = request.POST['print_materials_unit_cost']
        print_materials_total_cost = request.POST['print_materials_total_cost']
        _15lang_radiospots_per_county_quantity = request.POST['15lang_radiospots_per_county_quantity']
        _15lang_radiospots_total_quantity = request.POST['15lang_radiospots_total_quantity']
        _15lang_radiospots_unit_cost = request.POST['15lang_radiospots_unit_cost']
        _15lang_radiospots_total_cost = request.POST['15lang_radiospots_total_cost']
        en_swa_radiospots_per_county_quantity = request.POST['en_swa_radiospots_per_county_quantity']
        en_swa_radiospots_total_quantity = request.POST['en_swa_radiospots_total_quantity']
        en_swa_radiospots_unit_cost = request.POST['en_swa_radiospots_unit_cost']
        en_swa_radiospots_total_cost = request.POST['en_swa_radiospots_total_cost']
        tv_commercials_per_county_quantity = request.POST['tv_commercials_per_county_quantity']
        tv_commercials_total_quantity = request.POST['tv_commercials_total_quantity']
        tv_commercials_unit_cost = request.POST['tv_commercials_unit_cost']
        tv_commercials_total_cost = request.POST['tv_commercials_total_cost']
        sensitization_of_HQ_per_county_quantity = request.POST['sensitization_of_HQ_per_county_quantity']
        sensitization_of_HQ_total_quantity = request.POST['sensitization_of_HQ_total_quantity']
        sensitization_of_HQ_unit_cost = request.POST['sensitization_of_HQ_unit_cost']
        sensitization_of_HQ_total_cost = request.POST['sensitization_of_HQ_total_cost']
        print_materials_distribution_per_county_quantity = request.POST[
            'print_materials_distribution_per_county_quantity']
        print_materials_distribution_total_quantity = request.POST['print_materials_distribution_total_quantity']
        print_materials_distribution_unit_cost = request.POST['print_materials_distribution_unit_cost']
        print_materials_distribution_total_cost = request.POST['print_materials_distribution_total_cost']
        publicity_evaluation_per_county_quantity = request.POST['publicity_evaluation_per_county_quantity']
        publicity_evaluation_total_quantity = request.POST['publicity_evaluation_total_quantity']
        publicity_evaluation_unit_cost = request.POST['publicity_evaluation_unit_cost']
        publicity_evaluation_total_cost = request.POST['publicity_evaluation_total_cost']
        community_sensitization_meetings_per_county_quantity = request.POST[
            'community_sensitization_meetings_per_county_quantity']
        community_sensitization_meetings_total_quantity = request.POST[
            'community_sensitization_meetings_total_quantity']
        community_sensitization_meetings_unit_cost = request.POST['community_sensitization_meetings_unit_cost']
        community_sensitization_meetings_total_cost = request.POST['community_sensitization_meetings_total_cost']
        transport_per_county_quantity = request.POST['transport_per_county_quantity']
        transport_total_quantity = request.POST['transport_total_quantity']
        transport_unit_cost = request.POST['transport_unit_cost']
        transport_total_cost = request.POST['transport_total_cost']
        translator_allowance_per_county_quantity = request.POST['translator_allowance_per_county_quantity']
        translator_allowance_total_quantity = request.POST['translator_allowance_total_quantity']
        translator_allowance_unit_cost = request.POST['translator_allowance_unit_cost']
        translator_allowance_total_cost = request.POST['translator_allowance_total_cost']
        vet_epidemiologist_per_county_quantity = request.POST['vet_epidemiologist_per_county_quantity']
        vet_epidemiologist_total_quantity = request.POST['vet_epidemiologist_total_quantity']
        vet_epidemiologist_unit_cost = request.POST['vet_epidemiologist_unit_cost']
        vet_epidemiologist_total_cost = request.POST['vet_epidemiologist_total_cost']
        medical_epidemiologist_per_county_quantity = request.POST['medical_epidemiologist_per_county_quantity']
        medical_epidemiologist_total_quantity = request.POST['medical_epidemiologist_total_quantity']
        medical_epidemiologist_unit_cost = request.POST['medical_epidemiologist_unit_cost']
        medical_epidemiologist_total_cost = request.POST['medical_epidemiologist_total_cost']
        socio_economist_per_county_quantity = request.POST['socio_economist_per_county_quantity']
        socio_economist_total_quantity = request.POST['socio_economist_total_quantity']
        socio_economist_unit_cost = request.POST['socio_economist_unit_cost']
        socio_economist_total_cost = request.POST['socio_economist_total_cost']
        technician_per_county_quantity = request.POST['technician_per_county_quantity']
        technician_total_quantity = request.POST['technician_total_quantity']
        technician_unit_cost = request.POST['technician_unit_cost']
        technician_total_cost = request.POST['technician_total_cost']
        driver_per_county_quantity = request.POST['driver_per_county_quantity']
        driver_total_quantity = request.POST['driver_total_quantity']
        driver_unit_cost = request.POST['driver_unit_cost']
        driver_total_cost = request.POST['driver_total_cost']
        early_detection_total_cost = request.POST['early_detection_total_cost']

        x = rvf_initial_collection.insert_one({
            '47lang_training_material_design_per_county_quantity': _47lang_training_material_design_per_county_quantity,
            '47lang_training_material_design_total_quantity': _47lang_training_material_design_total_quantity,
            '47lang_training_material_design_unit_cost': _47lang_training_material_design_unit_cost,
            '47lang_training_material_design_total_cost': _47lang_training_material_design_total_cost,
            'print_materials_per_county_quantity': print_materials_per_county_quantity,
            'print_materials_total_quantity': print_materials_total_quantity,
            'print_materials_unit_cost': print_materials_unit_cost,
            'print_materials_total_cost': print_materials_total_cost,
            '15lang_radiospots_per_county_quantity': _15lang_radiospots_per_county_quantity,
            '15lang_radiospots_total_quantity': _15lang_radiospots_total_quantity,
            '15lang_radiospots_unit_cost': _15lang_radiospots_unit_cost,
            '15_lang_radiospots_total_cost': _15lang_radiospots_total_cost,
            'en_swa_radiospots_per_county_quantity': en_swa_radiospots_per_county_quantity,
            'en_swa_radiospots_total_quantity': en_swa_radiospots_total_quantity,
            'en_swa_radiospots_unit_cost': en_swa_radiospots_unit_cost,
            'en_swa_radiospots_total_cost': en_swa_radiospots_total_cost,
            'tv_commercials_per_county_quantity': tv_commercials_per_county_quantity,
            'tv_commercials_total_quantity': tv_commercials_total_quantity,
            'tv_commercials_unit_cost': tv_commercials_unit_cost,
            'tv_commercials_total_cost': tv_commercials_total_cost,
            'sensitization_of_HQ_per_county_quantity': sensitization_of_HQ_per_county_quantity,
            'sensitization_of_HQ_total_quantity': sensitization_of_HQ_total_quantity,
            'sensitization_of_HQ_unit_cost': sensitization_of_HQ_unit_cost,
            'sensitization_of_HQ_total_cost': sensitization_of_HQ_total_cost,
            'print_materials_distribution_per_county_quantity': print_materials_distribution_per_county_quantity,
            'print_materials_distribution_total_quantity': print_materials_distribution_total_quantity,
            'print_materials_distribution_unit_cost': print_materials_distribution_unit_cost,
            'print_materials_distribution_total_cost': print_materials_distribution_total_cost,
            'publicity_evaluation_per_county_quantity': publicity_evaluation_per_county_quantity,
            'publicity_evaluation_total_quantity': publicity_evaluation_total_quantity,
            'publicity_evaluation_unit_cost': publicity_evaluation_unit_cost,
            'publicity_evaluation_total_cost': publicity_evaluation_total_cost,
            'community_sensitization_meetings_per_county_quantity': community_sensitization_meetings_per_county_quantity,
            'community_sensitization_meetings_total_quantity': community_sensitization_meetings_total_quantity,
            'community_sensitization_meetings_unit_cost': community_sensitization_meetings_unit_cost,
            'community_sensitization_meetings_total_cost': community_sensitization_meetings_total_cost,
            'transport_per_county_quantity': transport_per_county_quantity,
            'transport_total_quantity': transport_total_quantity,
            'transport_unit_cost': transport_unit_cost,
            'transport_total_cost': transport_total_cost,
            'translator_allowance_per_county_quantity': translator_allowance_per_county_quantity,
            'translator_allowance_total_quantity': translator_allowance_total_quantity,
            'translator_allowance_unit_cost': translator_allowance_unit_cost,
            'translator_allowance_total_cost': translator_allowance_total_cost,
            'vet_epidemiologist_per_county_quantity': vet_epidemiologist_per_county_quantity,
            'vet_epidemiologist_total_quantity': vet_epidemiologist_total_quantity,
            'vet_epidemiologist_unit_cost': vet_epidemiologist_unit_cost,
            'vet_epidemiologist_total_cost': vet_epidemiologist_total_cost,
            'medical_epidemiologist_per_county_quantity': medical_epidemiologist_per_county_quantity,
            'medical_epidemiologist_total_quantity': medical_epidemiologist_total_quantity,
            'medical_epidemiologist_unit_cost': medical_epidemiologist_unit_cost,
            'medical_epidemiologist_total_cost': medical_epidemiologist_total_cost,
            'socio_economist_per_county_quantity': socio_economist_per_county_quantity,
            'socio_economist_total_quantity': socio_economist_total_quantity,
            'socio_economist_unit_cost': socio_economist_unit_cost,
            'socio_economist_total_cost': socio_economist_total_cost,
            'technician_per_county_quantity': technician_per_county_quantity,
            'technician_total_quantity': technician_total_quantity,
            'technician_unit_cost': technician_unit_cost,
            'technician_total_cost': technician_total_cost,
            'driver_per_county_quantity': driver_per_county_quantity,
            'driver_total_quantity': driver_total_quantity,
            'driver_unit_cost': driver_unit_cost,
            'driver_total_cost': driver_total_cost,
            'early_detection_total_cost': int(_47lang_training_material_design_total_cost)+
                                            int(print_materials_total_cost),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        '47lang_training_material_design_per_county_quantity': context[
            '47lang_training_material_design_per_county_quantity'],
        '47lang_training_material_design_total_quantity': int(
            context['47lang_training_material_design_per_county_quantity']) * 47,
        '47lang_training_material_design_unit_cost': context['47lang_training_material_design_unit_cost'],
        '47lang_training_material_design_total_cost': int(
            context['47lang_training_material_design_total_quantity']) * int(
            context['47lang_training_material_design_unit_cost']),
        'print_materials_per_county_quantity': context['print_materials_per_county_quantity'],
        'print_materials_total_quantity': int(context['print_materials_per_county_quantity']) * 47,
        'print_materials_unit_cost': context['print_materials_unit_cost'],
        'print_materials_total_cost': int(context['print_materials_total_quantity']) * int(
            context['print_materials_unit_cost']),'15lang_radiospots_per_county_quantity': context[
            '15lang_radiospots_per_county_quantity'],
        '15lang_radiospots_total_quantity': int(context['15lang_radiospots_per_county_quantity']) * 15,
        '15lang_radiospots_unit_cost': context['15lang_radiospots_unit_cost'],
        '15lang_radiospots_total_cost': int(context['15lang_radiospots_total_quantity']) * int(
            context['15lang_radiospots_unit_cost']),
        'en_swa_radiospots_per_county_quantity': context['en_swa_radiospots_per_county_quantity'],
        'en_swa_radiospots_total_quantity': 2,
        'en_swa_radiospots_unit_cost': context['en_swa_radiospots_unit_cost'],
        'en_swa_radiospots_total_cost': int(context['en_swa_radiospots_total_quantity']) * int(
            context['en_swa_radiospots_unit_cost']),
        'tv_commercials_per_county_quantity': context['tv_commercials_per_county_quantity'],
        'tv_commercials_total_quantity': int(context['tv_commercials_per_county_quantity']) * 20,
        'tv_commercials_unit_cost': context['tv_commercials_unit_cost'],
        'tv_commercials_total_cost': int(context['tv_commercials_total_quantity']) * int(context['tv_commercials_unit_cost']), 'sensitization_of_HQ_per_county_quantity': context[
            'sensitization_of_HQ_per_county_quantity'],
        'sensitization_of_HQ_total_quantity': int(context['sensitization_of_HQ_per_county_quantity']) * 47,
        'sensitization_of_HQ_unit_cost': context['sensitization_of_HQ_unit_cost'],
        'sensitization_of_HQ_total_cost': int(context['sensitization_of_HQ_total_quantity']) * int(
            context['sensitization_of_HQ_unit_cost']),
        'print_materials_distribution_per_county_quantity': context['print_materials_distribution_per_county_quantity'],
        'print_materials_distribution_total_quantity': int(context['print_materials_distribution_per_county_quantity']) * 47,
        'print_materials_distribution_unit_cost': context['print_materials_distribution_unit_cost'],
        'print_materials_distribution_total_cost': int(context['print_materials_distribution_total_quantity']) * int(
            context['print_materials_distribution_unit_cost']),
        'publicity_evaluation_per_county_quantity': context['publicity_evaluation_per_county_quantity'],
        'publicity_evaluation_total_quantity': int(context['publicity_evaluation_per_county_quantity']) * 47,
        'publicity_evaluation_unit_cost': context['publicity_evaluation_unit_cost'],
        'publicity_evaluation_total_cost': int(context['publicity_evaluation_total_quantity']) * int(context['publicity_evaluation_unit_cost']),
        'community_sensitization_meetings_per_county_quantity': context['community_sensitization_meetings_per_county_quantity'],
        'community_sensitization_meetings_total_quantity': int(context['community_sensitization_meetings_per_county_quantity']) * 47,
        'community_sensitization_meetings_unit_cost': context['community_sensitization_meetings_unit_cost'],
        'community_sensitization_meetings_total_cost': int(context['community_sensitization_meetings_total_quantity']) * int(context['community_sensitization_meetings_unit_cost']),
        'transport_per_county_quantity': context['transport_per_county_quantity'],
        'transport_total_quantity': int(context['transport_per_county_quantity']) * 3,
        'transport_unit_cost': context['transport_unit_cost'],
        'transport_total_cost': int(context['transport_total_quantity']) * int(context['transport_unit_cost']),
        'translator_allowance_per_county_quantity': context['translator_allowance_per_county_quantity'],
        'translator_allowance_total_quantity': int(context['translator_allowance_per_county_quantity']) * 2,
        'translator_allowance_unit_cost': context['translator_allowance_unit_cost'],
        'translator_allowance_total_cost': int(context['translator_allowance_total_quantity']) * int(
            context['translator_allowance_unit_cost']),
        'vet_epidemiologist_per_county_quantity': context['vet_epidemiologist_per_county_quantity'],
        'vet_epidemiologist_total_quantity': int(context['vet_epidemiologist_per_county_quantity']) * 3,
        'vet_epidemiologist_unit_cost': context['vet_epidemiologist_unit_cost'],
        'vet_epidemiologist_total_cost': int(context['vet_epidemiologist_total_quantity']) * int(
            context['vet_epidemiologist_unit_cost']),
        'medical_epidemiologist_per_county_quantity': context['medical_epidemiologist_per_county_quantity'],
        'medical_epidemiologist_total_quantity': int(context['medical_epidemiologist_per_county_quantity']) * 3,
        'medical_epidemiologist_unit_cost': context['medical_epidemiologist_unit_cost'],
        'medical_epidemiologist_total_cost': int(context['medical_epidemiologist_total_quantity']) * int(
            context['medical_epidemiologist_unit_cost']),
        'socio_economist_per_county_quantity': context['socio_economist_per_county_quantity'],
        'socio_economist_total_quantity': int(context['socio_economist_per_county_quantity']) * 3,
        'socio_economist_unit_cost': context['socio_economist_unit_cost'],
        'socio_economist_total_cost': int(context['socio_economist_total_quantity']) * int(
            context['socio_economist_unit_cost']),
        'technician_per_county_quantity': context['technician_per_county_quantity'],
        'technician_total_quantity': int(context['technician_per_county_quantity']) * 3,
        'technician_unit_cost': context['technician_unit_cost'],
        'technician_total_cost': int(context['technician_total_quantity']) * int(context['technician_unit_cost']),
        'driver_per_county_quantity': context['driver_per_county_quantity'],
        'driver_total_quantity': int(context['driver_per_county_quantity']) * 3,
        'driver_unit_cost': context['driver_unit_cost'],
        'driver_total_cost': int(context['driver_total_quantity']) * int(context['driver_unit_cost']),
        'early_detection_total_cost': context['early_detection_total_cost'],
    }

    return render(request,'coord_and_comm.html',context2)

def movement_control(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['movement_control']

    context = {
        'movement_control_assumptions': 0,
        'police_salary_no': 188,
        'police_salary_unit_cost': 35000,
        'police_salary_salvage_value': 0,
        'police_salary_useful_life': 0,
        'police_salary_annual_cost': 0,
        'roadblock_offices_no': 20,
        'roadblock_offices_unit_cost': 100000,
        'roadblock_offices_salvage_value': 5000,
        'roadblock_offices_useful_life': 3,
        'roadblock_offices_annual_cost': 0,
        'manning_border_police_salary_no': 70,
        'manning_border_police_salary_unit_cost': 35000,
        'manning_border_police_salary_salvage_value': 0,
        'manning_border_police_salary_useful_life': 0,
        'manning_border_police_salary_annual_cost': 0,
        'movement_control_offices_no': 28,
        'movement_control_offices_unit_cost': 100000,
        'movement_control_offices_salvage_value': 5000,
        'movement_control_offices_useful_life': 3,
        'movement_control_offices_annual_cost': 0,
        'movement_control_landcruisers_no': 12,
        'movement_control_landcruisers_unit_cost': 3000000,
        'movement_control_landcruisers_salvage_value': 300000,
        'movement_control_landcruisers_useful_life': 15,
        'movement_control_landcruisers_annual_cost': 0,
        'movement_control_fuel_no': 37440,
        'movement_control_fuel_unit_cost': 120,
        'movement_control_fuel_salvage_value': 0,
        'movement_control_fuel_useful_life': 0,
        'movement_control_fuel_annual_cost': 0,
        'movement_control_total_cost': 0,
    }

    if (request.method == "POST"):
        movement_control_assumptions = request.POST['movement_control_assumptions']
        police_salary_no = request.POST['police_salary_no']
        police_salary_unit_cost = request.POST['police_salary_unit_cost']
        police_salary_salvage_value = request.POST['police_salary_salvage_value']
        police_salary_useful_life = request.POST['police_salary_useful_life']
        police_salary_annual_cost = request.POST['police_salary_annual_cost']
        roadblock_offices_no = request.POST['roadblock_offices_no']
        roadblock_offices_unit_cost = request.POST['roadblock_offices_unit_cost']
        roadblock_offices_salvage_value = request.POST['roadblock_offices_salvage_value']
        roadblock_offices_useful_life = request.POST['roadblock_offices_useful_life']
        roadblock_offices_annual_cost = request.POST['roadblock_offices_annual_cost']
        manning_border_police_salary_no = request.POST['manning_border_police_salary_no']
        manning_border_police_salary_unit_cost = request.POST['manning_border_police_salary_unit_cost']
        manning_border_police_salary_salvage_value = request.POST['manning_border_police_salary_salvage_value']
        manning_border_police_salary_useful_life = request.POST['manning_border_police_salary_useful_life']
        manning_border_police_salary_annual_cost = request.POST['manning_border_police_salary_annual_cost']
        movement_control_offices_no = request.POST['movement_control_offices_no']
        movement_control_offices_unit_cost = request.POST['movement_control_offices_unit_cost']
        movement_control_offices_salvage_value = request.POST['movement_control_offices_salvage_value']
        movement_control_offices_useful_life = request.POST['movement_control_offices_useful_life']
        movement_control_offices_annual_cost = request.POST['movement_control_offices_annual_cost']
        movement_control_landcruisers_no = request.POST['movement_control_landcruisers_no']
        movement_control_landcruisers_unit_cost = request.POST['movement_control_landcruisers_unit_cost']
        movement_control_landcruisers_salvage_value = request.POST['movement_control_landcruisers_salvage_value']
        movement_control_landcruisers_useful_life = request.POST['movement_control_landcruisers_useful_life']
        movement_control_landcruisers_annual_cost = request.POST['movement_control_landcruisers_annual_cost']
        movement_control_fuel_no = request.POST['movement_control_fuel_no']
        movement_control_fuel_unit_cost = request.POST['movement_control_fuel_unit_cost']
        movement_control_fuel_salvage_value = request.POST['movement_control_fuel_salvage_value']
        movement_control_fuel_useful_life = request.POST['movement_control_fuel_useful_life']
        movement_control_fuel_annual_cost = request.POST['movement_control_fuel_annual_cost']
        movement_control_total_cost = request.POST['movement_control_total_cost']

        x = rvf_initial_collection.insert_one({
            'movement_control_assumptions': movement_control_assumptions,
            'police_salary_no': police_salary_no,
            'police_salary_unit_cost': police_salary_unit_cost,
            'police_salary_salvage_value': police_salary_salvage_value,
            'police_salary_useful_life': police_salary_useful_life,
            'police_salary_annual_cost': float(police_salary_no) * float(police_salary_unit_cost) * 12,
            'roadblock_offices_no': roadblock_offices_no,
            'roadblock_offices_unit_cost': roadblock_offices_unit_cost,
            'roadblock_offices_salvage_value': roadblock_offices_salvage_value,
            'roadblock_offices_useful_life': roadblock_offices_useful_life,
            'roadblock_offices_annual_cost': ((float(roadblock_offices_unit_cost) - float(
                roadblock_offices_salvage_value)) / float(roadblock_offices_unit_cost)) * float(roadblock_offices_no),
            'manning_border_police_salary_no': manning_border_police_salary_no,
            'manning_border_police_salary_unit_cost': manning_border_police_salary_unit_cost,
            'manning_border_police_salary_salvage_value': manning_border_police_salary_salvage_value,
            'manning_border_police_salary_useful_life': manning_border_police_salary_useful_life,
            'manning_border_police_salary_annual_cost': float(manning_border_police_salary_no) * float(
                manning_border_police_salary_unit_cost) * 12,
            'movement_control_offices_no': movement_control_offices_no,
            'movement_control_offices_unit_cost': movement_control_offices_unit_cost,
            'movement_control_offices_salvage_value': movement_control_offices_salvage_value,
            'movement_control_offices_useful_life': movement_control_offices_useful_life,
            'movement_control_offices_annual_cost': ((float(movement_control_offices_unit_cost) - float(
                movement_control_offices_salvage_value)) / float(movement_control_offices_unit_cost)) * float(
                movement_control_offices_no),
            'movement_control_landcruisers_no': movement_control_landcruisers_no,
            'movement_control_landcruisers_unit_cost': movement_control_landcruisers_unit_cost,
            'movement_control_landcruisers_salvage_value': movement_control_landcruisers_salvage_value,
            'movement_control_landcruisers_useful_life': movement_control_landcruisers_useful_life,
            'movement_control_landcruisers_annual_cost': ((float(movement_control_landcruisers_unit_cost) - float(
                movement_control_landcruisers_salvage_value)) / float(movement_control_landcruisers_unit_cost)) * float(
                movement_control_landcruisers_no),
            'movement_control_fuel_no': movement_control_fuel_no,
            'movement_control_fuel_unit_cost': movement_control_fuel_unit_cost,
            'movement_control_fuel_salvage_value': movement_control_fuel_salvage_value,
            'movement_control_fuel_useful_life': movement_control_fuel_useful_life,
            'movement_control_fuel_annual_cost': float(movement_control_fuel_no) * float(
                movement_control_fuel_unit_cost),

            'movement_control_total_cost': (float(police_salary_no) * float(police_salary_unit_cost) * 12) +
                                           (((float(roadblock_offices_unit_cost) - float(
                                               roadblock_offices_salvage_value)) / float(
                                               roadblock_offices_unit_cost)) * float(roadblock_offices_no)) +
                                           (float(manning_border_police_salary_no) * float(
                                               manning_border_police_salary_unit_cost) * 12) +
                                           (((float(movement_control_offices_unit_cost) - float(
                                               movement_control_offices_salvage_value)) / float(
                                               movement_control_offices_unit_cost)) * float(
                                               movement_control_offices_no)) +
                                           (((float(movement_control_landcruisers_unit_cost) - float(
                                               movement_control_landcruisers_salvage_value)) / float(
                                               movement_control_landcruisers_unit_cost)) * float(
                                               movement_control_landcruisers_no)) +
                                           (float(movement_control_fuel_no) * float(
                                               movement_control_fuel_unit_cost)),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'movement_control_assumptions': context['movement_control_assumptions'],
        'police_salary_no': context['police_salary_no'],
        'police_salary_unit_cost': context['police_salary_unit_cost'],
        'police_salary_salvage_value': context['police_salary_salvage_value'],
        'police_salary_useful_life': context['police_salary_useful_life'],
        'police_salary_annual_cost': float(context['police_salary_no']) * float(
            context['police_salary_unit_cost']) * 12,
        'roadblock_offices_no': context['roadblock_offices_no'],
        'roadblock_offices_unit_cost': context['roadblock_offices_unit_cost'],
        'roadblock_offices_salvage_value': context['roadblock_offices_salvage_value'],
        'roadblock_offices_useful_life': context['roadblock_offices_useful_life'],
        'roadblock_offices_annual_cost': ((float(context['roadblock_offices_unit_cost']) - float(
            context['roadblock_offices_salvage_value'])) / float(context['roadblock_offices_useful_life'])) * float(
            context['roadblock_offices_no']),
        'manning_border_police_salary_no': context['manning_border_police_salary_no'],
        'manning_border_police_salary_unit_cost': context['manning_border_police_salary_unit_cost'],
        'manning_border_police_salary_salvage_value': context['manning_border_police_salary_salvage_value'],
        'manning_border_police_salary_useful_life': context['manning_border_police_salary_useful_life'],
        'manning_border_police_salary_annual_cost': float(context['manning_border_police_salary_no']) * float(
            context['manning_border_police_salary_unit_cost']) * 12,
        'movement_control_offices_no': context['movement_control_offices_no'],
        'movement_control_offices_unit_cost': context['movement_control_offices_unit_cost'],
        'movement_control_offices_salvage_value': context['movement_control_offices_salvage_value'],
        'movement_control_offices_useful_life': context['movement_control_offices_useful_life'],
        'movement_control_offices_annual_cost': ((float(context['movement_control_offices_unit_cost']) - float(
            context['movement_control_offices_salvage_value'])) / float(
            context['movement_control_offices_useful_life'])) * float(context['movement_control_offices_no']),
        'movement_control_landcruisers_no': context['movement_control_landcruisers_no'],
        'movement_control_landcruisers_unit_cost': context['movement_control_landcruisers_unit_cost'],
        'movement_control_landcruisers_salvage_value': context['movement_control_landcruisers_salvage_value'],
        'movement_control_landcruisers_useful_life': context['movement_control_landcruisers_useful_life'],
        'movement_control_landcruisers_annual_cost': ((float(
            context['movement_control_landcruisers_unit_cost']) - float(
            context['movement_control_landcruisers_salvage_value'])) / float(
            context['movement_control_landcruisers_useful_life'])) * float(context['movement_control_landcruisers_no']),
        'movement_control_fuel_no': context['movement_control_fuel_no'],
        'movement_control_fuel_unit_cost': context['movement_control_fuel_unit_cost'],
        'movement_control_fuel_salvage_value': context['movement_control_fuel_salvage_value'],
        'movement_control_fuel_useful_life': context['movement_control_fuel_useful_life'],
        'movement_control_fuel_annual_cost': float(context['movement_control_fuel_no']) * float(
            context['movement_control_fuel_unit_cost']),
        'movement_control_total_cost': (float(context['police_salary_no']) * float(
            context['police_salary_unit_cost']) * 12) +
                                       (((float(context['roadblock_offices_unit_cost']) - float(
                                           context['roadblock_offices_salvage_value'])) / float(
                                           context['roadblock_offices_useful_life'])) * float(
                                           context['roadblock_offices_no'])) +
                                       (float(context['manning_border_police_salary_no']) * float(
                                           context['manning_border_police_salary_unit_cost']) * 12) +
                                       (((float(context['movement_control_offices_unit_cost']) - float(
                                           context['movement_control_offices_salvage_value'])) / float(
                                           context['movement_control_offices_useful_life'])) * float(
                                           context['movement_control_offices_no'])) +
                                       (((float(context['movement_control_landcruisers_unit_cost']) - float(
                                           context['movement_control_landcruisers_salvage_value'])) / float(
                                           context['movement_control_landcruisers_useful_life'])) * float(
                                           context['movement_control_landcruisers_no'])) +
                                       (float(context['movement_control_fuel_no']) * float(
                                           context['movement_control_fuel_unit_cost']) ),
    }

    return render(request,'movement_control.html',context2)

def strategic_vaccination(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['strategic_vaccination']

    context = {
        'RVF_preventive_vacc_no': 32567544.5,
        'RVF_preventive_vacc_unit_cost': 12,
        'RVF_preventive_vacc_total_cost': 0,
        'RVF_preventive_vacc_print_source': 0,
        'rabies_preventive_vacc_no': 2000000,
        'rabies_preventive_vacc_unit_cost': 60,
        'rabies_preventive_vacc_total_cost': 0,
        'rabies_preventive_vacc_print_source': 0,
        'preventive_vaccination_sub_total': 0,
        'RVF_ring_vacc_animals_no': 80000,
        'RVF_ring_vacc_outbreak_no': 1,
        'RVF_ring_vacc_coverage': 0.8,
        'RVF_ring_vacc_no': 0,
        'RVF_ring_vacc_unit_cost': 12,
        'RVF_ring_vacc_total_cost': 0,
        'rabies_ring_vacc_animals_no': 40000,
        'rabies_ring_vacc_outbreak_no': 1,
        'rabies_ring_vacc_coverage': 0.8,
        'rabies_ring_vacc_no': 0,
        'rabies_ring_vacc_unit_cost': 60,
        'rabies_ring_vacc_total_cost': 0,
        'disease_ring_vacc_total': 0,
        'RVF_vacc_doses_quantity': 500000,
        'RVF_vacc_doses_unit_cost': 10,
        'RVF_vacc_doses_total_cost': 0,
        'RVF_vacc_bioreactors_quantity': 4,
        'RVF_vacc_bioreactors_unit_cost': 21744800,
        'RVF_vacc_bioreactors_total_cost': 0,
        'RVF_vacc_power_quantity': 48,
        'RVF_vacc_power_unit_cost': 3000,
        'RVF_vacc_power_total_cost': 0,
        'RVF_vacc_maintenance_quantity': 4,
        'RVF_vacc_maintenance_unit_cost': 50000,
        'RVF_vacc_maintenance_total_cost': 0,
        'RVF_vacc_labor_quantity': 4,
        'RVF_vacc_labor_unit_cost': 22000,
        'RVF_vacc_labor_total_cost': 0,
        'RVF_vacc_technical_monitoring_quantity': 24,
        'RVF_vacc_technical_monitoring_unit_cost': 15000,
        'RVF_vacc_technical_monitoring_total_cost': 0,
        'RVF_vacc_storage_sub_title': 0,
        'rabies_vacc_doses_quantity': 5000000,
        'rabies_vacc_doses_unit_cost': 15,
        'rabies_vacc_doses_total_cost': 0,
        'rabies_vacc_bioreactors_quantity': 4,
        'rabies_vacc_bioreactors_unit_cost': 21744800,
        'rabies_vacc_bioreactors_total_cost': 0,
        'rabies_vacc_power_quantity': 48,
        'rabies_vacc_power_unit_cost': 3000,
        'rabies_vacc_power_total_cost': 0,
        'rabies_vacc_maintenance_quantity': 4,
        'rabies_vacc_maintenance_unit_cost': 50000,
        'rabies_vacc_maintenance_total_cost': 0,
        'rabies_vacc_labor_quantity': 4,
        'rabies_vacc_labor_unit_cost': 22000,
        'rabies_vacc_labor_total_cost': 0,
        'rabies_vacc_technical_monitoring_quantity': 24,
        'rabies_vacc_technical_monitoring_unit_cost': 15000,
        'rabies_vacc_technical_monitoring_total_cost': 0,
        'rabies_vacc_storage_sub_title': 0,
        'strategic_vaccination_total': 0,
    }

    if (request.method == "POST"):
        RVF_preventive_vacc_no = request.POST['RVF_preventive_vacc_no']
        RVF_preventive_vacc_unit_cost = request.POST['RVF_preventive_vacc_unit_cost']
        RVF_preventive_vacc_total_cost = request.POST['RVF_preventive_vacc_total_cost']
        RVF_preventive_vacc_print_source = request.POST['RVF_preventive_vacc_print_source']
        rabies_preventive_vacc_no = request.POST['rabies_preventive_vacc_no']
        rabies_preventive_vacc_unit_cost = request.POST['rabies_preventive_vacc_unit_cost']
        rabies_preventive_vacc_total_cost = request.POST['rabies_preventive_vacc_total_cost']
        rabies_preventive_vacc_print_source = request.POST['rabies_preventive_vacc_print_source']
        preventive_vaccination_sub_total = request.POST['preventive_vaccination_sub_total']
        RVF_ring_vacc_animals_no = request.POST['RVF_ring_vacc_animals_no']
        RVF_ring_vacc_outbreak_no = request.POST['RVF_ring_vacc_outbreak_no']
        RVF_ring_vacc_coverage = request.POST['RVF_ring_vacc_coverage']
        RVF_ring_vacc_no = request.POST['RVF_ring_vacc_no']
        RVF_ring_vacc_unit_cost = request.POST['RVF_ring_vacc_unit_cost']
        RVF_ring_vacc_total_cost = request.POST['RVF_ring_vacc_total_cost']
        rabies_ring_vacc_animals_no = request.POST['rabies_ring_vacc_animals_no']
        rabies_ring_vacc_outbreak_no = request.POST['rabies_ring_vacc_outbreak_no']
        rabies_ring_vacc_coverage = request.POST['rabies_ring_vacc_coverage']
        rabies_ring_vacc_no = request.POST['rabies_ring_vacc_no']
        rabies_ring_vacc_unit_cost = request.POST['rabies_ring_vacc_unit_cost']
        rabies_ring_vacc_total_cost = request.POST['rabies_ring_vacc_total_cost']
        disease_ring_vacc_total = request.POST['disease_ring_vacc_total']

        RVF_vacc_doses_quantity = request.POST['RVF_vacc_doses_quantity']
        RVF_vacc_doses_unit_cost = request.POST['RVF_vacc_doses_unit_cost']
        RVF_vacc_doses_total_cost = request.POST['RVF_vacc_doses_total_cost']
        RVF_vacc_bioreactors_quantity = request.POST['RVF_vacc_bioreactors_quantity']
        RVF_vacc_bioreactors_unit_cost = request.POST['RVF_vacc_bioreactors_unit_cost']
        RVF_vacc_bioreactors_total_cost = request.POST['RVF_vacc_bioreactors_total_cost']
        RVF_vacc_power_quantity = request.POST['RVF_vacc_power_quantity']
        RVF_vacc_power_unit_cost = request.POST['RVF_vacc_power_unit_cost']
        RVF_vacc_power_total_cost = request.POST['RVF_vacc_power_total_cost']
        RVF_vacc_maintenance_quantity = request.POST['RVF_vacc_maintenance_quantity']
        RVF_vacc_maintenance_unit_cost = request.POST['RVF_vacc_maintenance_unit_cost']
        RVF_vacc_maintenance_total_cost = request.POST['RVF_vacc_maintenance_total_cost']
        RVF_vacc_labor_quantity = request.POST['RVF_vacc_labor_quantity']
        RVF_vacc_labor_unit_cost = request.POST['RVF_vacc_labor_unit_cost']
        RVF_vacc_labor_total_cost = request.POST['RVF_vacc_labor_total_cost']
        RVF_vacc_technical_monitoring_quantity = request.POST['RVF_vacc_technical_monitoring_quantity']
        RVF_vacc_technical_monitoring_unit_cost = request.POST['RVF_vacc_technical_monitoring_unit_cost']
        RVF_vacc_technical_monitoring_total_cost = request.POST['RVF_vacc_technical_monitoring_total_cost']
        RVF_vacc_storage_sub_title = request.POST['RVF_vacc_storage_sub_title']

        rabies_vacc_doses_quantity = request.POST['rabies_vacc_doses_quantity']
        rabies_vacc_doses_unit_cost = request.POST['rabies_vacc_doses_unit_cost']
        rabies_vacc_doses_total_cost = request.POST['rabies_vacc_doses_total_cost']
        rabies_vacc_bioreactors_quantity = request.POST['rabies_vacc_bioreactors_quantity']
        rabies_vacc_bioreactors_unit_cost = request.POST['rabies_vacc_bioreactors_unit_cost']
        rabies_vacc_bioreactors_total_cost = request.POST['rabies_vacc_bioreactors_total_cost']
        rabies_vacc_power_quantity = request.POST['rabies_vacc_power_quantity']
        rabies_vacc_power_unit_cost = request.POST['rabies_vacc_power_unit_cost']
        rabies_vacc_power_total_cost = request.POST['rabies_vacc_power_total_cost']
        rabies_vacc_maintenance_quantity = request.POST['rabies_vacc_maintenance_quantity']
        rabies_vacc_maintenance_unit_cost = request.POST['rabies_vacc_maintenance_unit_cost']
        rabies_vacc_maintenance_total_cost = request.POST['rabies_vacc_maintenance_total_cost']
        rabies_vacc_labor_quantity = request.POST['rabies_vacc_labor_quantity']
        rabies_vacc_labor_unit_cost = request.POST['rabies_vacc_labor_unit_cost']
        rabies_vacc_labor_total_cost = request.POST['rabies_vacc_labor_total_cost']
        rabies_vacc_technical_monitoring_quantity = request.POST['rabies_vacc_technical_monitoring_quantity']
        rabies_vacc_technical_monitoring_unit_cost = request.POST['rabies_vacc_technical_monitoring_unit_cost']
        rabies_vacc_technical_monitoring_total_cost = request.POST['rabies_vacc_technical_monitoring_total_cost']
        rabies_vacc_storage_sub_title = request.POST['rabies_vacc_storage_sub_title']
        strategic_vaccination_total = request.POST['strategic_vaccination_total']

        x = rvf_initial_collection.insert_one({
            'RVF_preventive_vacc_no': RVF_preventive_vacc_no,
            'RVF_preventive_vacc_unit_cost': RVF_preventive_vacc_unit_cost,
            'RVF_preventive_vacc_total_cost': float(RVF_preventive_vacc_no) * float(
                RVF_preventive_vacc_unit_cost) * 0.8,
            'RVF_preventive_vacc_print_source': RVF_preventive_vacc_print_source,
            'rabies_preventive_vacc_no': rabies_preventive_vacc_no,
            'rabies_preventive_vacc_unit_cost': rabies_preventive_vacc_unit_cost,
            'rabies_preventive_vacc_total_cost': float(rabies_preventive_vacc_no) * float(
                rabies_preventive_vacc_unit_cost) * 0.8,
            'rabies_preventive_vacc_print_source': rabies_preventive_vacc_print_source,
            'preventive_vaccination_sub_total': (float(RVF_preventive_vacc_no) * float(
                RVF_preventive_vacc_unit_cost) * 0.8) + (float(rabies_preventive_vacc_no) * float(
                rabies_preventive_vacc_unit_cost) * 0.8),

            'RVF_ring_vacc_animals_no': RVF_ring_vacc_animals_no,
            'RVF_ring_vacc_outbreak_no': RVF_ring_vacc_outbreak_no,
            'RVF_ring_vacc_coverage': RVF_ring_vacc_coverage,
            'RVF_ring_vacc_no': float(RVF_ring_vacc_animals_no) * float(RVF_ring_vacc_outbreak_no) * float(
                RVF_ring_vacc_coverage),
            'RVF_ring_vacc_unit_cost': RVF_ring_vacc_unit_cost,
            'RVF_ring_vacc_total_cost': float(RVF_ring_vacc_animals_no) * float(RVF_ring_vacc_outbreak_no) * float(
                RVF_ring_vacc_coverage) * float(RVF_ring_vacc_unit_cost),
            'rabies_ring_vacc_animals_no': rabies_ring_vacc_animals_no,
            'rabies_ring_vacc_outbreak_no': rabies_ring_vacc_outbreak_no,
            'rabies_ring_vacc_coverage': rabies_ring_vacc_coverage,
            'rabies_ring_vacc_no': float(rabies_ring_vacc_animals_no) * float(rabies_ring_vacc_outbreak_no) * float(
                rabies_ring_vacc_coverage),
            'rabies_ring_vacc_unit_cost': rabies_ring_vacc_unit_cost,
            'rabies_ring_vacc_total_cost': float(rabies_ring_vacc_animals_no) * float(
                rabies_ring_vacc_outbreak_no) * float(rabies_ring_vacc_coverage) * float(rabies_ring_vacc_unit_cost),

            'disease_ring_vacc_total': (float(RVF_ring_vacc_animals_no) * float(RVF_ring_vacc_outbreak_no) * float(
                RVF_ring_vacc_coverage) * float(RVF_ring_vacc_unit_cost)) +
                                       (float(rabies_ring_vacc_animals_no) * float(
                                           rabies_ring_vacc_outbreak_no) * float(rabies_ring_vacc_coverage) * float(
                                           rabies_ring_vacc_unit_cost)),

            'RVF_vacc_doses_quantity': RVF_vacc_doses_quantity,
            'RVF_vacc_doses_unit_cost': RVF_vacc_doses_unit_cost,
            'RVF_vacc_doses_total_cost': float(RVF_vacc_doses_quantity) * float(RVF_vacc_doses_unit_cost),
            'RVF_vacc_bioreactors_quantity': RVF_vacc_bioreactors_quantity,
            'RVF_vacc_bioreactors_unit_cost': RVF_vacc_bioreactors_unit_cost,
            'RVF_vacc_bioreactors_total_cost': float(RVF_vacc_bioreactors_quantity) * float(
                RVF_vacc_bioreactors_unit_cost),
            'RVF_vacc_power_quantity': RVF_vacc_power_quantity,
            'RVF_vacc_power_unit_cost': RVF_vacc_power_unit_cost,
            'RVF_vacc_power_total_cost': float(RVF_vacc_power_quantity) * float(RVF_vacc_power_unit_cost),
            'RVF_vacc_maintenance_quantity': RVF_vacc_maintenance_quantity,
            'RVF_vacc_maintenance_unit_cost': RVF_vacc_maintenance_unit_cost,
            'RVF_vacc_maintenance_total_cost': float(RVF_vacc_maintenance_quantity) * float(
                RVF_vacc_maintenance_unit_cost),
            'RVF_vacc_labor_quantity': RVF_vacc_labor_quantity,
            'RVF_vacc_labor_unit_cost': RVF_vacc_labor_unit_cost,
            'RVF_vacc_labor_total_cost': float(RVF_vacc_labor_quantity) * float(RVF_vacc_labor_unit_cost),
            'RVF_vacc_technical_monitoring_quantity': RVF_vacc_technical_monitoring_quantity,
            'RVF_vacc_technical_monitoring_unit_cost': RVF_vacc_technical_monitoring_unit_cost,
            'RVF_vacc_technical_monitoring_total_cost': float(RVF_vacc_technical_monitoring_quantity) * float(
                RVF_vacc_technical_monitoring_unit_cost),

            'RVF_vacc_storage_sub_title': (float(RVF_vacc_doses_quantity) * float(RVF_vacc_doses_unit_cost)) +
                                          (float(RVF_vacc_bioreactors_quantity) * float(
                                              RVF_vacc_bioreactors_unit_cost)) +
                                          (float(RVF_vacc_power_quantity) * float(RVF_vacc_power_unit_cost)) +
                                          (float(RVF_vacc_maintenance_quantity) * float(
                                              RVF_vacc_maintenance_unit_cost)) +
                                          (float(RVF_vacc_labor_quantity) * float(RVF_vacc_labor_unit_cost)) +
                                          (float(RVF_vacc_technical_monitoring_quantity) * float(
                                              RVF_vacc_technical_monitoring_unit_cost)),

            'rabies_vacc_doses_quantity': rabies_vacc_doses_quantity,
            'rabies_vacc_doses_unit_cost': rabies_vacc_doses_unit_cost,
            'rabies_vacc_doses_total_cost': float(rabies_vacc_doses_quantity) * float(rabies_vacc_doses_unit_cost),
            'rabies_vacc_bioreactors_quantity': rabies_vacc_bioreactors_quantity,
            'rabies_vacc_bioreactors_unit_cost': rabies_vacc_bioreactors_unit_cost,
            'rabies_vacc_bioreactors_total_cost': float(rabies_vacc_bioreactors_quantity) * float(
                rabies_vacc_bioreactors_unit_cost),
            'rabies_vacc_power_quantity': rabies_vacc_power_quantity,
            'rabies_vacc_power_unit_cost': rabies_vacc_power_unit_cost,
            'rabies_vacc_power_total_cost': float(rabies_vacc_power_quantity) * float(rabies_vacc_power_unit_cost),
            'rabies_vacc_maintenance_quantity': rabies_vacc_maintenance_quantity,
            'rabies_vacc_maintenance_unit_cost': rabies_vacc_maintenance_unit_cost,
            'rabies_vacc_maintenance_total_cost': float(rabies_vacc_maintenance_quantity) * float(
                rabies_vacc_maintenance_unit_cost),
            'rabies_vacc_labor_quantity': rabies_vacc_labor_quantity,
            'rabies_vacc_labor_unit_cost': rabies_vacc_labor_unit_cost,
            'rabies_vacc_labor_total_cost': float(rabies_vacc_labor_quantity) * float(rabies_vacc_labor_unit_cost),
            'rabies_vacc_technical_monitoring_quantity': rabies_vacc_technical_monitoring_quantity,
            'rabies_vacc_technical_monitoring_unit_cost': rabies_vacc_technical_monitoring_unit_cost,
            'rabies_vacc_technical_monitoring_total_cost': float(rabies_vacc_technical_monitoring_quantity) * float(
                rabies_vacc_technical_monitoring_unit_cost),

            'rabies_vacc_storage_sub_title': (float(rabies_vacc_doses_quantity) * float(rabies_vacc_doses_unit_cost)) +
                                             (float(rabies_vacc_bioreactors_quantity) * float(
                                                 rabies_vacc_bioreactors_unit_cost)) +
                                             (float(rabies_vacc_power_quantity) * float(rabies_vacc_power_unit_cost)) +
                                             (float(rabies_vacc_maintenance_quantity) * float(
                                                 rabies_vacc_maintenance_unit_cost)) +
                                             (float(rabies_vacc_labor_quantity) * float(rabies_vacc_labor_unit_cost)) +
                                             (float(rabies_vacc_technical_monitoring_quantity) * float(
                                                 rabies_vacc_technical_monitoring_unit_cost)),

            'strategic_vaccination_total': (float(RVF_preventive_vacc_no) * float(
                RVF_preventive_vacc_unit_cost) * 0.8) +
                                           (float(rabies_preventive_vacc_no) * float(
                                               rabies_preventive_vacc_unit_cost) * 0.8) +
                                           (float(RVF_ring_vacc_animals_no) * float(RVF_ring_vacc_outbreak_no) * float(
                                               RVF_ring_vacc_coverage) * float(RVF_ring_vacc_unit_cost)) +
                                           (float(rabies_ring_vacc_animals_no) * float(
                                               rabies_ring_vacc_outbreak_no) * float(rabies_ring_vacc_coverage) * float(
                                               rabies_ring_vacc_unit_cost)) +
                                           (float(RVF_vacc_doses_quantity) * float(RVF_vacc_doses_unit_cost)) +
                                           (float(RVF_vacc_bioreactors_quantity) * float(
                                               RVF_vacc_bioreactors_unit_cost)) +
                                           (float(RVF_vacc_power_quantity) * float(RVF_vacc_power_unit_cost)) +
                                           (float(RVF_vacc_maintenance_quantity) * float(
                                               RVF_vacc_maintenance_unit_cost)) +
                                           (float(RVF_vacc_labor_quantity) * float(RVF_vacc_labor_unit_cost)) +
                                           (float(RVF_vacc_technical_monitoring_quantity) * float(
                                               RVF_vacc_technical_monitoring_unit_cost)),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'RVF_preventive_vacc_no': context['RVF_preventive_vacc_no'],
        'RVF_preventive_vacc_unit_cost': context['RVF_preventive_vacc_unit_cost'],
        'RVF_preventive_vacc_total_cost': float(context['RVF_preventive_vacc_no']) * float(
            context['RVF_preventive_vacc_unit_cost']) * 0.8,
        'RVF_preventive_vacc_print_source': context['RVF_preventive_vacc_print_source'],
        'rabies_preventive_vacc_no': context['rabies_preventive_vacc_no'],
        'rabies_preventive_vacc_unit_cost': context['rabies_preventive_vacc_unit_cost'],
        'rabies_preventive_vacc_total_cost': float(context['rabies_preventive_vacc_no']) * float(
            context['rabies_preventive_vacc_unit_cost']) * 0.8,
        'rabies_preventive_vacc_print_source': context['rabies_preventive_vacc_print_source'],
        'preventive_vaccination_sub_total': (float(context['RVF_preventive_vacc_no']) * float(
            context['RVF_preventive_vacc_unit_cost']) * 0.8) + (float(context['rabies_preventive_vacc_no']) * float(
            context['rabies_preventive_vacc_unit_cost']) * 0.8),
        'RVF_ring_vacc_animals_no': context['RVF_ring_vacc_animals_no'],
        'RVF_ring_vacc_outbreak_no': context['RVF_ring_vacc_outbreak_no'],
        'RVF_ring_vacc_coverage': context['RVF_ring_vacc_coverage'],
        'RVF_ring_vacc_no': float(context['RVF_ring_vacc_animals_no']) * float(
            context['RVF_ring_vacc_outbreak_no']) * float(context['RVF_ring_vacc_coverage']),
        'RVF_ring_vacc_unit_cost': context['RVF_ring_vacc_unit_cost'],
        'RVF_ring_vacc_total_cost': float(context['RVF_ring_vacc_animals_no']) * float(
            context['RVF_ring_vacc_outbreak_no']) * float(context['RVF_ring_vacc_coverage']) * float(
            context['RVF_ring_vacc_unit_cost']),
        'rabies_ring_vacc_animals_no': context['rabies_ring_vacc_animals_no'],
        'rabies_ring_vacc_outbreak_no': context['rabies_ring_vacc_outbreak_no'],
        'rabies_ring_vacc_coverage': context['rabies_ring_vacc_coverage'],
        'rabies_ring_vacc_no': float(context['rabies_ring_vacc_animals_no']) * float(
            context['rabies_ring_vacc_outbreak_no']) * float(context['rabies_ring_vacc_coverage']),
        'rabies_ring_vacc_unit_cost': context['rabies_ring_vacc_unit_cost'],
        'rabies_ring_vacc_total_cost': float(context['rabies_ring_vacc_animals_no']) * float(
            context['rabies_ring_vacc_outbreak_no']) * float(context['rabies_ring_vacc_coverage']) * float(
            context['rabies_ring_vacc_unit_cost']),
        'disease_ring_vacc_total': (float(context['RVF_ring_vacc_animals_no']) * float(
            context['RVF_ring_vacc_outbreak_no']) * float(context['RVF_ring_vacc_coverage']) * float(
            context['RVF_ring_vacc_unit_cost'])) +
                                   (float(context['rabies_ring_vacc_animals_no']) * float(
                                       context['rabies_ring_vacc_outbreak_no']) * float(
                                       context['rabies_ring_vacc_coverage']) * float(
                                       context['rabies_ring_vacc_unit_cost'])),

        'RVF_vacc_doses_quantity': context['RVF_vacc_doses_quantity'],
        'RVF_vacc_doses_unit_cost': context['RVF_vacc_doses_unit_cost'],
        'RVF_vacc_doses_total_cost': float(context['RVF_vacc_doses_quantity']) * float(
            context['RVF_vacc_doses_unit_cost']),
        'RVF_vacc_bioreactors_quantity': context['RVF_vacc_bioreactors_quantity'],
        'RVF_vacc_bioreactors_unit_cost': context['RVF_vacc_bioreactors_unit_cost'],
        'RVF_vacc_bioreactors_total_cost': float(context['RVF_vacc_bioreactors_quantity']) * float(
            context['RVF_vacc_bioreactors_unit_cost']),
        'RVF_vacc_power_quantity': context['RVF_vacc_power_quantity'],
        'RVF_vacc_power_unit_cost': context['RVF_vacc_power_unit_cost'],
        'RVF_vacc_power_total_cost': float(context['RVF_vacc_power_quantity']) * float(
            context['RVF_vacc_power_unit_cost']),
        'RVF_vacc_maintenance_quantity': context['RVF_vacc_maintenance_quantity'],
        'RVF_vacc_maintenance_unit_cost': context['RVF_vacc_maintenance_unit_cost'],
        'RVF_vacc_maintenance_total_cost': float(context['RVF_vacc_maintenance_quantity']) * float(
            context['RVF_vacc_maintenance_unit_cost']),
        'RVF_vacc_labor_quantity': context['RVF_vacc_labor_quantity'],
        'RVF_vacc_labor_unit_cost': context['RVF_vacc_labor_unit_cost'],
        'RVF_vacc_labor_total_cost': float(context['RVF_vacc_labor_quantity']) * float(
            context['RVF_vacc_labor_unit_cost']),
        'RVF_vacc_technical_monitoring_quantity': context['RVF_vacc_technical_monitoring_quantity'],
        'RVF_vacc_technical_monitoring_unit_cost': context['RVF_vacc_technical_monitoring_unit_cost'],
        'RVF_vacc_technical_monitoring_total_cost': float(context['RVF_vacc_technical_monitoring_quantity']) * float(
            context['RVF_vacc_technical_monitoring_unit_cost']),

        'RVF_vacc_storage_sub_title': (float(context['RVF_vacc_doses_quantity']) * float(
            context['RVF_vacc_doses_unit_cost'])) +
                                      (float(context['RVF_vacc_bioreactors_quantity']) * float(
                                          context['RVF_vacc_bioreactors_unit_cost'])) +
                                      (float(context['RVF_vacc_power_quantity']) * float(
                                          context['RVF_vacc_power_unit_cost'])) +
                                      (float(context['RVF_vacc_maintenance_quantity']) * float(
                                          context['RVF_vacc_maintenance_unit_cost'])) +
                                      (float(context['RVF_vacc_labor_quantity']) * float(
                                          context['RVF_vacc_labor_unit_cost'])) +
                                      (float(context['RVF_vacc_technical_monitoring_quantity']) * float(
                                          context['RVF_vacc_technical_monitoring_unit_cost'])),

        'rabies_vacc_doses_quantity': context['rabies_vacc_doses_quantity'],
        'rabies_vacc_doses_unit_cost': context['rabies_vacc_doses_unit_cost'],
        'rabies_vacc_doses_total_cost': float(context['rabies_vacc_doses_quantity']) * float(
            context['rabies_vacc_doses_unit_cost']),
        'rabies_vacc_bioreactors_quantity': context['rabies_vacc_bioreactors_quantity'],
        'rabies_vacc_bioreactors_unit_cost': context['rabies_vacc_bioreactors_unit_cost'],
        'rabies_vacc_bioreactors_total_cost': float(context['rabies_vacc_bioreactors_quantity']) * float(
            context['rabies_vacc_bioreactors_unit_cost']),
        'rabies_vacc_power_quantity': context['rabies_vacc_power_quantity'],
        'rabies_vacc_power_unit_cost': context['rabies_vacc_power_unit_cost'],
        'rabies_vacc_power_total_cost': float(context['rabies_vacc_power_quantity']) * float(
            context['rabies_vacc_power_unit_cost']),
        'rabies_vacc_maintenance_quantity': context['rabies_vacc_maintenance_quantity'],
        'rabies_vacc_maintenance_unit_cost': context['rabies_vacc_maintenance_unit_cost'],
        'rabies_vacc_maintenance_total_cost': float(context['rabies_vacc_maintenance_quantity']) * float(
            context['rabies_vacc_maintenance_unit_cost']),
        'rabies_vacc_labor_quantity': context['rabies_vacc_labor_quantity'],
        'rabies_vacc_labor_unit_cost': context['rabies_vacc_labor_unit_cost'],
        'rabies_vacc_labor_total_cost': float(context['rabies_vacc_labor_quantity']) * float(
            context['rabies_vacc_labor_unit_cost']),
        'rabies_vacc_technical_monitoring_quantity': context['rabies_vacc_technical_monitoring_quantity'],
        'rabies_vacc_technical_monitoring_unit_cost': context['rabies_vacc_technical_monitoring_unit_cost'],
        'rabies_vacc_technical_monitoring_total_cost': float(
            context['rabies_vacc_technical_monitoring_quantity']) * float(
            context['rabies_vacc_technical_monitoring_unit_cost']),

        'rabies_vacc_storage_sub_title': (float(context['rabies_vacc_doses_quantity']) * float(
            context['rabies_vacc_doses_unit_cost'])) +
                                         (float(context['rabies_vacc_bioreactors_quantity']) * float(
                                             context['rabies_vacc_bioreactors_unit_cost'])) +
                                         (float(context['rabies_vacc_power_quantity']) * float(
                                             context['rabies_vacc_power_unit_cost'])) +
                                         (float(context['rabies_vacc_maintenance_quantity']) * float(
                                             context['rabies_vacc_maintenance_unit_cost'])) +
                                         (float(context['rabies_vacc_labor_quantity']) * float(
                                             context['rabies_vacc_labor_unit_cost'])) +
                                         (float(context['rabies_vacc_technical_monitoring_quantity']) * float(
                                             context['rabies_vacc_technical_monitoring_unit_cost'])),
        'strategic_vaccination_total': (float(context['RVF_preventive_vacc_no']) * float(
            context['RVF_preventive_vacc_unit_cost']) * 0.8) +
                                       (float(context['rabies_preventive_vacc_no']) * float(
                                           context['rabies_preventive_vacc_unit_cost']) * 0.8) +
                                       (float(context['RVF_ring_vacc_animals_no']) * float(
                                           context['RVF_ring_vacc_outbreak_no']) * float(
                                           context['RVF_ring_vacc_coverage']) * float(
                                           context['RVF_ring_vacc_unit_cost'])) +
                                       (float(context['rabies_ring_vacc_animals_no']) * float(
                                           context['rabies_ring_vacc_outbreak_no']) * float(
                                           context['rabies_ring_vacc_coverage']) * float(
                                           context['rabies_ring_vacc_unit_cost'])) +
                                       (float(context['RVF_vacc_doses_quantity']) * float(
                                           context['RVF_vacc_doses_unit_cost'])) +
                                       (float(context['RVF_vacc_bioreactors_quantity']) * float(
                                           context['RVF_vacc_bioreactors_unit_cost'])) +
                                       (float(context['RVF_vacc_power_quantity']) * float(
                                           context['RVF_vacc_power_unit_cost'])) +
                                       (float(context['RVF_vacc_maintenance_quantity']) * float(
                                           context['RVF_vacc_maintenance_unit_cost'])) +
                                       (float(context['RVF_vacc_labor_quantity']) * float(
                                           context['RVF_vacc_labor_unit_cost'])) +
                                       (float(context['RVF_vacc_technical_monitoring_quantity']) * float(
                                           context['RVF_vacc_technical_monitoring_unit_cost'])),
    }

    return render(request,'strategic_vaccination.html',context2)

def salary_allowances(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['salary_allowances']

    context = {
        'S_min': 100620,
        'S_max': 127980,
        'S_average': 0,
        'S_nairobi_house_allowance': 40000,
        'S_medical_all': 5000,
        'S_commuter_all': 16000,
        'S_risk_all': 0,
        'S_airtime': 8000,
        'S_annual_peak': 0,
        'S_leave_all': 10000,
        'S_total_annual_emoluments': 0,
        'S_salary_no': 1,
        'S_annual_cost': 0,
        'R_min': 1,
        'R_max': 1,
        'R_average': 0,
        'R_nairobi_house_allowance': 0,
        'R_medical_all': 0,
        'R_commuter_all': 0,
        'R_risk_all': 0,
        'R_airtime': 0,
        'R_annual_peak': 0,
        'R_leave_all': 0,
        'R_total_annual_emoluments': 0,
        'R_salary_no': 0,
        'R_annual_cost': 0,
        'Q_min': 1,
        'Q_max': 1,
        'Q_average': 0,
        'Q_nairobi_house_allowance': 0,
        'Q_medical_all': 0,
        'Q_commuter_all': 0,
        'Q_risk_all': 0,
        'Q_airtime': 0,
        'Q_annual_peak': 0,
        'Q_leave_all': 0,
        'Q_total_annual_emoluments': 0,
        'Q_salary_no': 0,
        'Q_annual_cost': 0,
        'P_min': 1,
        'P_max': 1,
        'P_average': 0,
        'P_nairobi_house_allowance': 0,
        'P_medical_all': 0,
        'P_commuter_all': 0,
        'P_risk_all': 0,
        'P_airtime': 0,
        'P_annual_peak': 0,
        'P_leave_all': 0,
        'P_total_annual_emoluments': 0,
        'P_salary_no': 0,
        'P_annual_cost': 0,
        'N_min': 1,
        'N_max': 1,
        'N_average': 0,
        'N_nairobi_house_allowance': 0,
        'N_medical_all': 0,
        'N_commuter_all': 0,
        'N_risk_all': 0,
        'N_airtime': 0,
        'N_annual_peak': 0,
        'N_leave_all': 0,
        'N_total_annual_emoluments': 0,
        'N_salary_no': 0,
        'N_annual_cost': 0,
        'M_min': 1,
        'M_max': 1,
        'M_average': 0,
        'M_nairobi_house_allowance': 0,
        'M_medical_all': 0,
        'M_commuter_all': 0,
        'M_risk_all': 0,
        'M_airtime': 0,
        'M_annual_peak': 0,
        'M_leave_all': 0,
        'M_total_annual_emoluments': 0,
        'M_salary_no': 0,
        'M_annual_cost': 0,
        'L_min': 1,
        'L_max': 1,
        'L_average': 0,
        'L_nairobi_house_allowance': 0,
        'L_medical_all': 0,
        'L_commuter_all': 0,
        'L_risk_all': 0,
        'L_airtime': 0,
        'L_annual_peak': 0,
        'L_leave_all': 0,
        'L_total_annual_emoluments': 0,
        'L_salary_no': 0,
        'L_annual_cost': 0,
        'K_min': 1,
        'K_max': 1,
        'K_average': 0,
        'K_nairobi_house_allowance': 0,
        'K_medical_all': 0,
        'K_commuter_all': 0,
        'K_risk_all': 0,
        'K_airtime': 0,
        'K_annual_peak': 0,
        'K_leave_all': 0,
        'K_total_annual_emoluments': 0,
        'K_salary_no': 0,
        'K_annual_cost': 0,
        'J_min': 1,
        'J_max': 1,
        'J_average': 0,
        'J_nairobi_house_allowance': 0,
        'J_medical_all': 0,
        'J_commuter_all': 0,
        'J_risk_all': 0,
        'J_airtime': 0,
        'J_annual_peak': 0,
        'J_leave_all': 0,
        'J_total_annual_emoluments': 0,
        'J_salary_no': 0,
        'J_annual_cost': 0,
        'H_min': 1,
        'H_max': 1,
        'H_average': 0,
        'H_nairobi_house_allowance': 0,
        'H_medical_all': 0,
        'H_commuter_all': 0,
        'H_risk_all': 0,
        'H_airtime': 0,
        'H_annual_peak': 0,
        'H_leave_all': 0,
        'H_total_annual_emoluments': 0,
        'H_salary_no': 0,
        'H_annual_cost': 0,
        'G_min': 1,
        'G_max': 1,
        'G_average': 0,
        'G_nairobi_house_allowance': 0,
        'G_medical_all': 0,
        'G_commuter_all': 0,
        'G_risk_all': 0,
        'G_airtime': 0,
        'G_annual_peak': 0,
        'G_leave_all': 0,
        'G_total_annual_emoluments': 0,
        'G_salary_no': 0,
        'G_annual_cost': 0,
        'F_min': 1,
        'F_max': 1,
        'F_average': 0,
        'F_nairobi_house_allowance': 0,
        'F_medical_all': 0,
        'F_commuter_all': 0,
        'F_risk_all': 0,
        'F_airtime': 0,
        'F_annual_peak': 0,
        'F_leave_all': 0,
        'F_total_annual_emoluments': 0,
        'F_salary_no': 0,
        'F_annual_cost': 0,
        'salary_allowance_total': 0,
    }

    if (request.method == "POST"):
        S_min = request.POST['S_min']
        S_max = request.POST['S_max']
        S_average = request.POST['S_average']
        S_nairobi_house_allowance = request.POST['S_nairobi_house_allowance']
        S_medical_all = request.POST['S_medical_all']
        S_commuter_all = request.POST['S_commuter_all']
        S_risk_all = request.POST['S_risk_all']
        S_airtime = request.POST['S_airtime']
        S_annual_peak = request.POST['S_annual_peak']
        S_leave_all = request.POST['S_leave_all']
        S_total_annual_emoluments = request.POST['S_total_annual_emoluments']
        S_salary_no = request.POST['S_salary_no']
        S_annual_cost = request.POST['S_annual_cost']
        R_min = request.POST['R_min']
        R_max = request.POST['R_max']
        R_average = request.POST['R_average']
        R_nairobi_house_allowance = request.POST['R_nairobi_house_allowance']
        R_medical_all = request.POST['R_medical_all']
        R_commuter_all = request.POST['R_commuter_all']
        R_risk_all = request.POST['R_risk_all']
        R_airtime = request.POST['R_airtime']
        R_annual_peak = request.POST['R_annual_peak']
        R_leave_all = request.POST['R_leave_all']
        R_total_annual_emoluments = request.POST['R_total_annual_emoluments']
        R_salary_no = request.POST['R_salary_no']
        R_annual_cost = request.POST['R_annual_cost']
        Q_min = request.POST['Q_min']
        Q_max = request.POST['Q_max']
        Q_average = request.POST['Q_average']
        Q_nairobi_house_allowance = request.POST['Q_nairobi_house_allowance']
        Q_medical_all = request.POST['Q_medical_all']
        Q_commuter_all = request.POST['Q_commuter_all']
        Q_risk_all = request.POST['Q_risk_all']
        Q_airtime = request.POST['Q_airtime']
        Q_annual_peak = request.POST['Q_annual_peak']
        Q_leave_all = request.POST['Q_leave_all']
        Q_total_annual_emoluments = request.POST['Q_total_annual_emoluments']
        Q_salary_no = request.POST['Q_salary_no']
        Q_annual_cost = request.POST['Q_annual_cost']
        P_min = request.POST['P_min']
        P_max = request.POST['P_max']
        P_average = request.POST['P_average']
        P_nairobi_house_allowance = request.POST['P_nairobi_house_allowance']
        P_medical_all = request.POST['P_medical_all']
        P_commuter_all = request.POST['P_commuter_all']
        P_risk_all = request.POST['P_risk_all']
        P_airtime = request.POST['P_airtime']
        P_annual_peak = request.POST['P_annual_peak']
        P_leave_all = request.POST['P_leave_all']
        P_total_annual_emoluments = request.POST['P_total_annual_emoluments']
        P_salary_no = request.POST['P_salary_no']
        P_annual_cost = request.POST['P_annual_cost']
        N_min = request.POST['N_min']
        N_max = request.POST['N_max']
        N_average = request.POST['N_average']
        N_nairobi_house_allowance = request.POST['N_nairobi_house_allowance']
        N_medical_all = request.POST['N_medical_all']
        N_commuter_all = request.POST['N_commuter_all']
        N_risk_all = request.POST['N_risk_all']
        N_airtime = request.POST['N_airtime']
        N_annual_peak = request.POST['N_annual_peak']
        N_leave_all = request.POST['N_leave_all']
        N_total_annual_emoluments = request.POST['N_total_annual_emoluments']
        N_salary_no = request.POST['N_salary_no']
        N_annual_cost = request.POST['N_annual_cost']
        M_min = request.POST['M_min']
        M_max = request.POST['M_max']
        M_average = request.POST['M_average']
        M_nairobi_house_allowance = request.POST['M_nairobi_house_allowance']
        M_medical_all = request.POST['M_medical_all']
        M_commuter_all = request.POST['M_commuter_all']
        M_risk_all = request.POST['M_risk_all']
        M_airtime = request.POST['M_airtime']
        M_annual_peak = request.POST['M_annual_peak']
        M_leave_all = request.POST['M_leave_all']
        M_total_annual_emoluments = request.POST['M_total_annual_emoluments']
        M_salary_no = request.POST['M_salary_no']
        M_annual_cost = request.POST['M_annual_cost']
        L_min = request.POST['L_min']
        L_max = request.POST['L_max']
        L_average = request.POST['L_average']
        L_nairobi_house_allowance = request.POST['L_nairobi_house_allowance']
        L_medical_all = request.POST['L_medical_all']
        L_commuter_all = request.POST['L_commuter_all']
        L_risk_all = request.POST['L_risk_all']
        L_airtime = request.POST['L_airtime']
        L_annual_peak = request.POST['L_annual_peak']
        L_leave_all = request.POST['L_leave_all']
        L_total_annual_emoluments = request.POST['L_total_annual_emoluments']
        L_salary_no = request.POST['L_salary_no']
        L_annual_cost = request.POST['L_annual_cost']
        K_min = request.POST['K_min']
        K_max = request.POST['K_max']
        K_average = request.POST['K_average']
        K_nairobi_house_allowance = request.POST['K_nairobi_house_allowance']
        K_medical_all = request.POST['K_medical_all']
        K_commuter_all = request.POST['K_commuter_all']
        K_risk_all = request.POST['K_risk_all']
        K_airtime = request.POST['K_airtime']
        K_annual_peak = request.POST['K_annual_peak']
        K_leave_all = request.POST['K_leave_all']
        K_total_annual_emoluments = request.POST['K_total_annual_emoluments']
        K_salary_no = request.POST['K_salary_no']
        K_annual_cost = request.POST['K_annual_cost']
        J_min = request.POST['J_min']
        J_max = request.POST['J_max']
        J_average = request.POST['J_average']
        J_nairobi_house_allowance = request.POST['J_nairobi_house_allowance']
        J_medical_all = request.POST['J_medical_all']
        J_commuter_all = request.POST['J_commuter_all']
        J_risk_all = request.POST['J_risk_all']
        J_airtime = request.POST['J_airtime']
        J_annual_peak = request.POST['J_annual_peak']
        J_leave_all = request.POST['J_leave_all']
        J_total_annual_emoluments = request.POST['J_total_annual_emoluments']
        J_salary_no = request.POST['J_salary_no']
        J_annual_cost = request.POST['J_annual_cost']
        H_min = request.POST['H_min']
        H_max = request.POST['H_max']
        H_average = request.POST['H_average']
        H_nairobi_house_allowance = request.POST['H_nairobi_house_allowance']
        H_medical_all = request.POST['H_medical_all']
        H_commuter_all = request.POST['H_commuter_all']
        H_risk_all = request.POST['H_risk_all']
        H_airtime = request.POST['H_airtime']
        H_annual_peak = request.POST['H_annual_peak']
        H_leave_all = request.POST['H_leave_all']
        H_total_annual_emoluments = request.POST['H_total_annual_emoluments']
        H_salary_no = request.POST['H_salary_no']
        H_annual_cost = request.POST['H_annual_cost']
        G_min = request.POST['G_min']
        G_max = request.POST['G_max']
        G_average = request.POST['G_average']
        G_nairobi_house_allowance = request.POST['G_nairobi_house_allowance']
        G_medical_all = request.POST['G_medical_all']
        G_commuter_all = request.POST['G_commuter_all']
        G_risk_all = request.POST['G_risk_all']
        G_airtime = request.POST['G_airtime']
        G_annual_peak = request.POST['G_annual_peak']
        G_leave_all = request.POST['G_leave_all']
        G_total_annual_emoluments = request.POST['G_total_annual_emoluments']
        G_salary_no = request.POST['G_salary_no']
        G_annual_cost = request.POST['G_annual_cost']
        F_min = request.POST['F_min']
        F_max = request.POST['F_max']
        F_average = request.POST['F_average']
        F_nairobi_house_allowance = request.POST['F_nairobi_house_allowance']
        F_medical_all = request.POST['F_medical_all']
        F_commuter_all = request.POST['F_commuter_all']
        F_risk_all = request.POST['F_risk_all']
        F_airtime = request.POST['F_airtime']
        F_annual_peak = request.POST['F_annual_peak']
        F_leave_all = request.POST['F_leave_all']
        F_total_annual_emoluments = request.POST['F_total_annual_emoluments']
        F_salary_no = request.POST['F_salary_no']
        F_annual_cost = request.POST['F_annual_cost']
        salary_allowance_total = request.POST['salary_allowance_total']

        x = rvf_initial_collection.insert_one({
            'S_min': S_min,
            'S_max': S_max,
            'S_average': (float(S_min) + float(S_max)) / 2,
            'S_nairobi_house_allowance': S_nairobi_house_allowance,
            'S_medical_all': S_medical_all,
            'S_commuter_all': S_commuter_all,
            'S_risk_all': S_risk_all,
            'S_airtime': S_airtime,
            'S_annual_peak': (((float(S_min) + float(S_max)) / 2) + float(S_nairobi_house_allowance) + float(
                S_medical_all) + float(S_commuter_all) + float(S_risk_all) + float(S_airtime)) * 12,
            'S_leave_all': S_leave_all,
            'S_total_annual_emoluments': ((((float(S_min) + float(S_max)) / 2) + float(
                S_nairobi_house_allowance) + float(S_medical_all) + float(S_commuter_all) + float(S_risk_all) + float(
                S_airtime)) * 12) + float(S_leave_all),
            'S_salary_no': S_salary_no,
            'S_annual_cost': (((((float(S_min) + float(S_max)) / 2) + float(S_nairobi_house_allowance) + float(
                S_medical_all) + float(S_commuter_all) + float(S_risk_all) + float(S_airtime)) * 12) + float(
                S_leave_all)) * float(S_salary_no),
            'R_min': R_min,
            'R_max': R_max,
            'R_average': (float(R_min) + float(R_max)) / 2,
            'R_nairobi_house_allowance': R_nairobi_house_allowance,
            'R_medical_all': R_medical_all,
            'R_commuter_all': R_commuter_all,
            'R_risk_all': R_risk_all,
            'R_airtime': R_airtime,
            'R_annual_peak': (((float(R_min) + float(R_max)) / 2) + float(R_nairobi_house_allowance) + float(
                R_medical_all) + float(R_commuter_all) + float(R_risk_all) + float(R_airtime)) * 12,
            'R_leave_all': R_leave_all,
            'R_total_annual_emoluments': ((((float(R_min) + float(R_max)) / 2) + float(
                R_nairobi_house_allowance) + float(R_medical_all) + float(R_commuter_all) + float(R_risk_all) + float(
                R_airtime)) * 12) + float(R_leave_all),
            'R_salary_no': R_salary_no,
            'R_annual_cost': (((((float(R_min) + float(R_max)) / 2) + float(R_nairobi_house_allowance) + float(
                R_medical_all) + float(R_commuter_all) + float(R_risk_all) + float(R_airtime)) * 12) + float(
                R_leave_all)) * float(R_salary_no),
            'Q_min': Q_min,
            'Q_max': Q_max,
            'Q_average': (float(Q_min) + float(Q_max)) / 2,
            'Q_nairobi_house_allowance': Q_nairobi_house_allowance,
            'Q_medical_all': Q_medical_all,
            'Q_commuter_all': Q_commuter_all,
            'Q_risk_all': Q_risk_all,
            'Q_airtime': Q_airtime,
            'Q_annual_peak': (((float(Q_min) + float(Q_max)) / 2) + float(Q_nairobi_house_allowance) + float(
                Q_medical_all) + float(Q_commuter_all) + float(Q_risk_all) + float(Q_airtime)) * 12,
            'Q_leave_all': Q_leave_all,
            'Q_total_annual_emoluments': ((((float(Q_min) + float(Q_max)) / 2) + float(
                Q_nairobi_house_allowance) + float(Q_medical_all) + float(Q_commuter_all) + float(Q_risk_all) + float(
                Q_airtime)) * 12) + float(Q_leave_all),
            'Q_salary_no': Q_salary_no,
            'Q_annual_cost': (((((float(Q_min) + float(Q_max)) / 2) + float(Q_nairobi_house_allowance) + float(
                Q_medical_all) + float(Q_commuter_all) + float(Q_risk_all) + float(Q_airtime)) * 12) + float(
                Q_leave_all)) * float(Q_salary_no),
            'P_min': P_min,
            'P_max': P_max,
            'P_average': (float(P_min) + float(P_max)) / 2,
            'P_nairobi_house_allowance': P_nairobi_house_allowance,
            'P_medical_all': P_medical_all,
            'P_commuter_all': P_commuter_all,
            'P_risk_all': P_risk_all,
            'P_airtime': P_airtime,
            'P_annual_peak': (((float(P_min) + float(P_max)) / 2) + float(P_nairobi_house_allowance) + float(
                P_medical_all) + float(P_commuter_all) + float(P_risk_all) + float(P_airtime)) * 12,
            'P_leave_all': P_leave_all,
            'P_total_annual_emoluments': ((((float(P_min) + float(P_max)) / 2) + float(
                P_nairobi_house_allowance) + float(P_medical_all) + float(P_commuter_all) + float(P_risk_all) + float(
                P_airtime)) * 12) + float(P_leave_all),
            'P_salary_no': P_salary_no,
            'P_annual_cost': (((((float(P_min) + float(P_max)) / 2) + float(P_nairobi_house_allowance) + float(
                P_medical_all) + float(P_commuter_all) + float(P_risk_all) + float(P_airtime)) * 12) + float(
                P_leave_all)) * float(P_salary_no),
            'N_min': N_min,
            'N_max': N_max,
            'N_average': (float(N_min) + float(N_max)) / 2,
            'N_nairobi_house_allowance': N_nairobi_house_allowance,
            'N_medical_all': N_medical_all,
            'N_commuter_all': N_commuter_all,
            'N_risk_all': N_risk_all,
            'N_airtime': N_airtime,
            'N_annual_peak': (((float(N_min) + float(N_max)) / 2) + float(N_nairobi_house_allowance) + float(
                N_medical_all) + float(N_commuter_all) + float(N_risk_all) + float(N_airtime)) * 12,
            'N_leave_all': N_leave_all,
            'N_total_annual_emoluments': ((((float(N_min) + float(N_max)) / 2) + float(
                N_nairobi_house_allowance) + float(N_medical_all) + float(N_commuter_all) + float(N_risk_all) + float(
                N_airtime)) * 12) + float(N_leave_all),
            'N_salary_no': N_salary_no,
            'N_annual_cost': (((((float(N_min) + float(N_max)) / 2) + float(N_nairobi_house_allowance) + float(
                N_medical_all) + float(N_commuter_all) + float(N_risk_all) + float(N_airtime)) * 12) + float(
                N_leave_all)) * float(N_salary_no),
            'M_min': M_min,
            'M_max': M_max,
            'M_average': (float(M_min) + float(M_max)) / 2,
            'M_nairobi_house_allowance': M_nairobi_house_allowance,
            'M_medical_all': M_medical_all,
            'M_commuter_all': M_commuter_all,
            'M_risk_all': M_risk_all,
            'M_airtime': M_airtime,
            'M_annual_peak': (((float(M_min) + float(M_max)) / 2) + float(M_nairobi_house_allowance) + float(
                M_medical_all) + float(M_commuter_all) + float(M_risk_all) + float(M_airtime)) * 12,
            'M_leave_all': M_leave_all,
            'M_total_annual_emoluments': ((((float(M_min) + float(M_max)) / 2) + float(
                M_nairobi_house_allowance) + float(M_medical_all) + float(M_commuter_all) + float(M_risk_all) + float(
                M_airtime)) * 12) + float(M_leave_all),
            'M_salary_no': M_salary_no,
            'M_annual_cost': (((((float(M_min) + float(M_max)) / 2) + float(M_nairobi_house_allowance) + float(
                M_medical_all) + float(M_commuter_all) + float(M_risk_all) + float(M_airtime)) * 12) + float(
                M_leave_all)) * float(M_salary_no),
            'L_min': L_min,
            'L_max': L_max,
            'L_average': (float(L_min) + float(L_max)) / 2,
            'L_nairobi_house_allowance': L_nairobi_house_allowance,
            'L_medical_all': L_medical_all,
            'L_commuter_all': L_commuter_all,
            'L_risk_all': L_risk_all,
            'L_airtime': L_airtime,
            'L_annual_peak': (((float(L_min) + float(L_max)) / 2) + float(L_nairobi_house_allowance) + float(
                L_medical_all) + float(L_commuter_all) + float(L_risk_all) + float(L_airtime)) * 12,
            'L_leave_all': L_leave_all,
            'L_total_annual_emoluments': ((((float(L_min) + float(L_max)) / 2) + float(
                L_nairobi_house_allowance) + float(L_medical_all) + float(L_commuter_all) + float(L_risk_all) + float(
                L_airtime)) * 12) + float(L_leave_all),
            'L_salary_no': L_salary_no,
            'L_annual_cost': (((((float(L_min) + float(L_max)) / 2) + float(L_nairobi_house_allowance) + float(
                L_medical_all) + float(L_commuter_all) + float(L_risk_all) + float(L_airtime)) * 12) + float(
                L_leave_all)) * float(L_salary_no),
            'K_min': K_min,
            'K_max': K_max,
            'K_average': (float(K_min) + float(K_max)) / 2,
            'K_nairobi_house_allowance': K_nairobi_house_allowance,
            'K_medical_all': K_medical_all,
            'K_commuter_all': K_commuter_all,
            'K_risk_all': K_risk_all,
            'K_airtime': K_airtime,
            'K_annual_peak': (((float(K_min) + float(K_max)) / 2) + float(K_nairobi_house_allowance) + float(
                K_medical_all) + float(K_commuter_all) + float(K_risk_all) + float(K_airtime)) * 12,
            'K_leave_all': K_leave_all,
            'K_total_annual_emoluments': ((((float(K_min) + float(K_max)) / 2) + float(
                K_nairobi_house_allowance) + float(K_medical_all) + float(K_commuter_all) + float(K_risk_all) + float(
                K_airtime)) * 12) + float(K_leave_all),
            'K_salary_no': K_salary_no,
            'K_annual_cost': (((((float(K_min) + float(K_max)) / 2) + float(K_nairobi_house_allowance) + float(
                K_medical_all) + float(K_commuter_all) + float(K_risk_all) + float(K_airtime)) * 12) + float(
                K_leave_all)) * float(K_salary_no),
            'J_min': J_min,
            'J_max': J_max,
            'J_average': (float(J_min) + float(J_max)) / 2,
            'J_nairobi_house_allowance': J_nairobi_house_allowance,
            'J_medical_all': J_medical_all,
            'J_commuter_all': J_commuter_all,
            'J_risk_all': J_risk_all,
            'J_airtime': J_airtime,
            'J_annual_peak': (((float(J_min) + float(J_max)) / 2) + float(J_nairobi_house_allowance) + float(
                J_medical_all) + float(J_commuter_all) + float(J_risk_all) + float(J_airtime)) * 12,
            'J_leave_all': J_leave_all,
            'J_total_annual_emoluments': ((((float(J_min) + float(J_max)) / 2) + float(
                J_nairobi_house_allowance) + float(J_medical_all) + float(J_commuter_all) + float(J_risk_all) + float(
                J_airtime)) * 12) + float(J_leave_all),
            'J_salary_no': J_salary_no,
            'J_annual_cost': (((((float(J_min) + float(J_max)) / 2) + float(J_nairobi_house_allowance) + float(
                J_medical_all) + float(J_commuter_all) + float(J_risk_all) + float(J_airtime)) * 12) + float(
                J_leave_all)) * float(J_salary_no),
            'H_min': H_min,
            'H_max': H_max,
            'H_average': (float(H_min) + float(H_max)) / 2,
            'H_nairobi_house_allowance': H_nairobi_house_allowance,
            'H_medical_all': H_medical_all,
            'H_commuter_all': H_commuter_all,
            'H_risk_all': H_risk_all,
            'H_airtime': H_airtime,
            'H_annual_peak': (((float(H_min) + float(H_max)) / 2) + float(H_nairobi_house_allowance) + float(
                H_medical_all) + float(H_commuter_all) + float(H_risk_all) + float(H_airtime)) * 12,
            'H_leave_all': H_leave_all,
            'H_total_annual_emoluments': ((((float(H_min) + float(H_max)) / 2) + float(
                H_nairobi_house_allowance) + float(H_medical_all) + float(H_commuter_all) + float(H_risk_all) + float(
                H_airtime)) * 12) + float(H_leave_all),
            'H_salary_no': H_salary_no,
            'H_annual_cost': (((((float(H_min) + float(H_max)) / 2) + float(H_nairobi_house_allowance) + float(
                H_medical_all) + float(H_commuter_all) + float(H_risk_all) + float(H_airtime)) * 12) + float(
                H_leave_all)) * float(H_salary_no),
            'G_min': G_min,
            'G_max': G_max,
            'G_average': (float(G_min) + float(G_max)) / 2,
            'G_nairobi_house_allowance': G_nairobi_house_allowance,
            'G_medical_all': G_medical_all,
            'G_commuter_all': G_commuter_all,
            'G_risk_all': G_risk_all,
            'G_airtime': G_airtime,
            'G_annual_peak': (((float(G_min) + float(G_max)) / 2) + float(G_nairobi_house_allowance) + float(
                G_medical_all) + float(G_commuter_all) + float(G_risk_all) + float(G_airtime)) * 12,
            'G_leave_all': G_leave_all,
            'G_total_annual_emoluments': ((((float(G_min) + float(G_max)) / 2) + float(
                G_nairobi_house_allowance) + float(G_medical_all) + float(G_commuter_all) + float(G_risk_all) + float(
                G_airtime)) * 12) + float(G_leave_all),
            'G_salary_no': G_salary_no,
            'G_annual_cost': (((((float(G_min) + float(G_max)) / 2) + float(G_nairobi_house_allowance) + float(
                G_medical_all) + float(G_commuter_all) + float(G_risk_all) + float(G_airtime)) * 12) + float(
                G_leave_all)) * float(G_salary_no),
            'F_min': F_min,
            'F_max': F_max,
            'F_average': (float(F_min) + float(F_max)) / 2,
            'F_nairobi_house_allowance': F_nairobi_house_allowance,
            'F_medical_all': F_medical_all,
            'F_commuter_all': F_commuter_all,
            'F_risk_all': F_risk_all,
            'F_airtime': F_airtime,
            'F_annual_peak': (((float(F_min) + float(F_max)) / 2) + float(F_nairobi_house_allowance) + float(
                F_medical_all) + float(F_commuter_all) + float(F_risk_all) + float(F_airtime)) * 12,
            'F_leave_all': F_leave_all,
            'F_total_annual_emoluments': ((((float(F_min) + float(F_max)) / 2) + float(
                F_nairobi_house_allowance) + float(F_medical_all) + float(F_commuter_all) + float(F_risk_all) + float(
                F_airtime)) * 12) + float(F_leave_all),
            'F_salary_no': F_salary_no,
            'F_annual_cost': (((((float(F_min) + float(F_max)) / 2) + float(F_nairobi_house_allowance) + float(
                F_medical_all) + float(F_commuter_all) + float(F_risk_all) + float(F_airtime)) * 12) + float(
                F_leave_all)) * float(F_salary_no),
            'salary_allowance_total': ((((((float(S_min)+float(S_max))/2)+float(S_nairobi_house_allowance)+float(S_medical_all)+float(S_commuter_all)+float(S_risk_all)+float(S_airtime))*12)+float(S_leave_all))*float(S_salary_no))+
                            ((((((float(R_min)+float(R_max))/2)+float(R_nairobi_house_allowance)+float(R_medical_all)+float(R_commuter_all)+float(R_risk_all)+float(R_airtime))*12)+float(R_leave_all))*float(R_salary_no))+
                            ((((((float(Q_min)+float(Q_max))/2)+float(Q_nairobi_house_allowance)+float(Q_medical_all)+float(Q_commuter_all)+float(Q_risk_all)+float(Q_airtime))*12)+float(Q_leave_all))*float(Q_salary_no))+
                            ((((((float(P_min)+float(P_max))/2)+float(P_nairobi_house_allowance)+float(P_medical_all)+float(P_commuter_all)+float(P_risk_all)+float(P_airtime))*12)+float(P_leave_all))*float(P_salary_no))+
                            ((((((float(N_min)+float(N_max))/2)+float(N_nairobi_house_allowance)+float(N_medical_all)+float(N_commuter_all)+float(N_risk_all)+float(N_airtime))*12)+float(N_leave_all))*float(N_salary_no))+
                            ((((((float(M_min)+float(M_max))/2)+float(M_nairobi_house_allowance)+float(M_medical_all)+float(M_commuter_all)+float(M_risk_all)+float(M_airtime))*12)+float(M_leave_all))*float(M_salary_no))+
                            ((((((float(L_min)+float(L_max))/2)+float(L_nairobi_house_allowance)+float(L_medical_all)+float(L_commuter_all)+float(L_risk_all)+float(L_airtime))*12)+float(L_leave_all))*float(L_salary_no))+
                            ((((((float(K_min)+float(K_max))/2)+float(K_nairobi_house_allowance)+float(K_medical_all)+float(K_commuter_all)+float(K_risk_all)+float(K_airtime))*12)+float(K_leave_all))*float(K_salary_no))+
                            ((((((float(J_min)+float(J_max))/2)+float(J_nairobi_house_allowance)+float(J_medical_all)+float(J_commuter_all)+float(J_risk_all)+float(J_airtime))*12)+float(J_leave_all))*float(J_salary_no))+
                            ((((((float(H_min)+float(H_max))/2)+float(H_nairobi_house_allowance)+float(H_medical_all)+float(H_commuter_all)+float(H_risk_all)+float(H_airtime))*12)+float(H_leave_all))*float(H_salary_no))+
                            ((((((float(G_min)+float(G_max))/2)+float(G_nairobi_house_allowance)+float(G_medical_all)+float(G_commuter_all)+float(G_risk_all)+float(G_airtime))*12)+float(G_leave_all))*float(G_salary_no))+
                            ((((((float(F_min)+float(F_max))/2)+float(F_nairobi_house_allowance)+float(F_medical_all)+float(F_commuter_all)+float(F_risk_all)+float(F_airtime))*12)+float(F_leave_all))*float(F_salary_no)),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'S_min': context['S_min'],
        'S_max': context['S_max'],
        'S_average': (float(context['S_min']) + float(context['S_max'])) / 2,
        'S_nairobi_house_allowance': context['S_nairobi_house_allowance'],
        'S_medical_all': context['S_medical_all'],
        'S_commuter_all': context['S_commuter_all'],
        'S_risk_all': context['S_risk_all'],
        'S_airtime': context['S_airtime'],
        'S_annual_peak': (((float(context['S_min']) + float(context['S_max'])) / 2) + float(
            context['S_nairobi_house_allowance']) + float(context['S_medical_all']) + float(
            context['S_commuter_all']) + float(context['S_risk_all']) + float(context['S_airtime'])) * 12,
        'S_leave_all': context['S_leave_all'],
        'S_total_annual_emoluments': ((((float(context['S_min']) + float(context['S_max'])) / 2) + float(
            context['S_nairobi_house_allowance']) + float(context['S_medical_all']) + float(
            context['S_commuter_all']) + float(context['S_risk_all']) + float(context['S_airtime'])) * 12) + float(
            context['S_leave_all']),
        'S_salary_no': context['S_salary_no'],
        'S_annual_cost': (((((float(context['S_min']) + float(context['S_max'])) / 2) + float(
            context['S_nairobi_house_allowance']) + float(context['S_medical_all']) + float(
            context['S_commuter_all']) + float(context['S_risk_all']) + float(context['S_airtime'])) * 12) + float(
            context['S_leave_all'])) * float(context['S_salary_no']),
        'R_min': context['R_min'],
        'R_max': context['R_max'],
        'R_average': (float(context['R_min']) + float(context['R_max'])) / 2,
        'R_nairobi_house_allowance': context['R_nairobi_house_allowance'],
        'R_medical_all': context['R_medical_all'],
        'R_commuter_all': context['R_commuter_all'],
        'R_risk_all': context['R_risk_all'],
        'R_airtime': context['R_airtime'],
        'R_annual_peak': (((float(context['R_min']) + float(context['R_max'])) / 2) + float(
            context['R_nairobi_house_allowance']) + float(context['R_medical_all']) + float(
            context['R_commuter_all']) + float(context['R_risk_all']) + float(context['R_airtime'])) * 12,
        'R_leave_all': context['R_leave_all'],
        'R_total_annual_emoluments': ((((float(context['R_min']) + float(context['R_max'])) / 2) + float(
            context['R_nairobi_house_allowance']) + float(context['R_medical_all']) + float(
            context['R_commuter_all']) + float(context['R_risk_all']) + float(context['R_airtime'])) * 12) + float(
            context['R_leave_all']),
        'R_salary_no': context['R_salary_no'],
        'R_annual_cost': (((((float(context['R_min']) + float(context['R_max'])) / 2) + float(
            context['R_nairobi_house_allowance']) + float(context['R_medical_all']) + float(
            context['R_commuter_all']) + float(context['R_risk_all']) + float(context['R_airtime'])) * 12) + float(
            context['R_leave_all'])) * float(context['R_salary_no']),
        'Q_min': context['Q_min'],
        'Q_max': context['Q_max'],
        'Q_average': (float(context['Q_min']) + float(context['Q_max'])) / 2,
        'Q_nairobi_house_allowance': context['Q_nairobi_house_allowance'],
        'Q_medical_all': context['Q_medical_all'],
        'Q_commuter_all': context['Q_commuter_all'],
        'Q_risk_all': context['Q_risk_all'],
        'Q_airtime': context['Q_airtime'],
        'Q_annual_peak': (((float(context['Q_min']) + float(context['Q_max'])) / 2) + float(
            context['Q_nairobi_house_allowance']) + float(context['Q_medical_all']) + float(
            context['Q_commuter_all']) + float(context['Q_risk_all']) + float(context['Q_airtime'])) * 12,
        'Q_leave_all': context['Q_leave_all'],
        'Q_total_annual_emoluments': ((((float(context['Q_min']) + float(context['Q_max'])) / 2) + float(
            context['Q_nairobi_house_allowance']) + float(context['Q_medical_all']) + float(
            context['Q_commuter_all']) + float(context['Q_risk_all']) + float(context['Q_airtime'])) * 12) + float(
            context['Q_leave_all']),
        'Q_salary_no': context['Q_salary_no'],
        'Q_annual_cost': (((((float(context['Q_min']) + float(context['Q_max'])) / 2) + float(
            context['Q_nairobi_house_allowance']) + float(context['Q_medical_all']) + float(
            context['Q_commuter_all']) + float(context['Q_risk_all']) + float(context['Q_airtime'])) * 12) + float(
            context['Q_leave_all'])) * float(context['Q_salary_no']),
        'P_min': context['P_min'],
        'P_max': context['P_max'],
        'P_average': (float(context['P_min']) + float(context['P_max'])) / 2,
        'P_nairobi_house_allowance': context['P_nairobi_house_allowance'],
        'P_medical_all': context['P_medical_all'],
        'P_commuter_all': context['P_commuter_all'],
        'P_risk_all': context['P_risk_all'],
        'P_airtime': context['P_airtime'],
        'P_annual_peak': (((float(context['P_min']) + float(context['P_max'])) / 2) + float(
            context['P_nairobi_house_allowance']) + float(context['P_medical_all']) + float(
            context['P_commuter_all']) + float(context['P_risk_all']) + float(context['P_airtime'])) * 12,
        'P_leave_all': context['P_leave_all'],
        'P_total_annual_emoluments': ((((float(context['P_min']) + float(context['P_max'])) / 2) + float(
            context['P_nairobi_house_allowance']) + float(context['P_medical_all']) + float(
            context['P_commuter_all']) + float(context['P_risk_all']) + float(context['P_airtime'])) * 12) + float(
            context['P_leave_all']),
        'P_salary_no': context['P_salary_no'],
        'P_annual_cost': (((((float(context['P_min']) + float(context['P_max'])) / 2) + float(
            context['P_nairobi_house_allowance']) + float(context['P_medical_all']) + float(
            context['P_commuter_all']) + float(context['P_risk_all']) + float(context['P_airtime'])) * 12) + float(
            context['P_leave_all'])) * float(context['P_salary_no']),
        'N_min': context['N_min'],
        'N_max': context['N_max'],
        'N_average': (float(context['N_min']) + float(context['N_max'])) / 2,
        'N_nairobi_house_allowance': context['N_nairobi_house_allowance'],
        'N_medical_all': context['N_medical_all'],
        'N_commuter_all': context['N_commuter_all'],
        'N_risk_all': context['N_risk_all'],
        'N_airtime': context['N_airtime'],
        'N_annual_peak': (((float(context['N_min']) + float(context['N_max'])) / 2) + float(
            context['N_nairobi_house_allowance']) + float(context['N_medical_all']) + float(
            context['N_commuter_all']) + float(context['N_risk_all']) + float(context['N_airtime'])) * 12,
        'N_leave_all': context['N_leave_all'],
        'N_total_annual_emoluments': ((((float(context['N_min']) + float(context['N_max'])) / 2) + float(
            context['N_nairobi_house_allowance']) + float(context['N_medical_all']) + float(
            context['N_commuter_all']) + float(context['N_risk_all']) + float(context['N_airtime'])) * 12) + float(
            context['N_leave_all']),
        'N_salary_no': context['N_salary_no'],
        'N_annual_cost': (((((float(context['N_min']) + float(context['N_max'])) / 2) + float(
            context['N_nairobi_house_allowance']) + float(context['N_medical_all']) + float(
            context['N_commuter_all']) + float(context['N_risk_all']) + float(context['N_airtime'])) * 12) + float(
            context['N_leave_all'])) * float(context['N_salary_no']),
        'M_min': context['M_min'],
        'M_max': context['M_max'],
        'M_average': (float(context['M_min']) + float(context['M_max'])) / 2,
        'M_nairobi_house_allowance': context['M_nairobi_house_allowance'],
        'M_medical_all': context['M_medical_all'],
        'M_commuter_all': context['M_commuter_all'],
        'M_risk_all': context['M_risk_all'],
        'M_airtime': context['M_airtime'],
        'M_annual_peak': (((float(context['M_min']) + float(context['M_max'])) / 2) + float(
            context['M_nairobi_house_allowance']) + float(context['M_medical_all']) + float(
            context['M_commuter_all']) + float(context['M_risk_all']) + float(context['M_airtime'])) * 12,
        'M_leave_all': context['M_leave_all'],
        'M_total_annual_emoluments': ((((float(context['M_min']) + float(context['M_max'])) / 2) + float(
            context['M_nairobi_house_allowance']) + float(context['M_medical_all']) + float(
            context['M_commuter_all']) + float(context['M_risk_all']) + float(context['M_airtime'])) * 12) + float(
            context['M_leave_all']),
        'M_salary_no': context['M_salary_no'],
        'M_annual_cost': (((((float(context['M_min']) + float(context['M_max'])) / 2) + float(
            context['M_nairobi_house_allowance']) + float(context['M_medical_all']) + float(
            context['M_commuter_all']) + float(context['M_risk_all']) + float(context['M_airtime'])) * 12) + float(
            context['M_leave_all'])) * float(context['M_salary_no']),
        'L_min': context['L_min'],
        'L_max': context['L_max'],
        'L_average': (float(context['L_min']) + float(context['L_max'])) / 2,
        'L_nairobi_house_allowance': context['L_nairobi_house_allowance'],
        'L_medical_all': context['L_medical_all'],
        'L_commuter_all': context['L_commuter_all'],
        'L_risk_all': context['L_risk_all'],
        'L_airtime': context['L_airtime'],
        'L_annual_peak': (((float(context['L_min']) + float(context['L_max'])) / 2) + float(
            context['L_nairobi_house_allowance']) + float(context['L_medical_all']) + float(
            context['L_commuter_all']) + float(context['L_risk_all']) + float(context['L_airtime'])) * 12,
        'L_leave_all': context['L_leave_all'],
        'L_total_annual_emoluments': ((((float(context['L_min']) + float(context['L_max'])) / 2) + float(
            context['L_nairobi_house_allowance']) + float(context['L_medical_all']) + float(
            context['L_commuter_all']) + float(context['L_risk_all']) + float(context['L_airtime'])) * 12) + float(
            context['L_leave_all']),
        'L_salary_no': context['L_salary_no'],
        'L_annual_cost': (((((float(context['L_min']) + float(context['L_max'])) / 2) + float(
            context['L_nairobi_house_allowance']) + float(context['L_medical_all']) + float(
            context['L_commuter_all']) + float(context['L_risk_all']) + float(context['L_airtime'])) * 12) + float(
            context['L_leave_all'])) * float(context['L_salary_no']),
        'K_min': context['K_min'],
        'K_max': context['K_max'],
        'K_average': (float(context['K_min']) + float(context['K_max'])) / 2,
        'K_nairobi_house_allowance': context['K_nairobi_house_allowance'],
        'K_medical_all': context['K_medical_all'],
        'K_commuter_all': context['K_commuter_all'],
        'K_risk_all': context['K_risk_all'],
        'K_airtime': context['K_airtime'],
        'K_annual_peak': (((float(context['K_min']) + float(context['K_max'])) / 2) + float(
            context['K_nairobi_house_allowance']) + float(context['K_medical_all']) + float(
            context['K_commuter_all']) + float(context['K_risk_all']) + float(context['K_airtime'])) * 12,
        'K_leave_all': context['K_leave_all'],
        'K_total_annual_emoluments': ((((float(context['K_min']) + float(context['K_max'])) / 2) + float(
            context['K_nairobi_house_allowance']) + float(context['K_medical_all']) + float(
            context['K_commuter_all']) + float(context['K_risk_all']) + float(context['K_airtime'])) * 12) + float(
            context['K_leave_all']),
        'K_salary_no': context['K_salary_no'],
        'K_annual_cost': (((((float(context['K_min']) + float(context['K_max'])) / 2) + float(
            context['K_nairobi_house_allowance']) + float(context['K_medical_all']) + float(
            context['K_commuter_all']) + float(context['K_risk_all']) + float(context['K_airtime'])) * 12) + float(
            context['K_leave_all'])) * float(context['K_salary_no']),
        'J_min': context['J_min'],
        'J_max': context['J_max'],
        'J_average': (float(context['J_min']) + float(context['J_max'])) / 2,
        'J_nairobi_house_allowance': context['J_nairobi_house_allowance'],
        'J_medical_all': context['J_medical_all'],
        'J_commuter_all': context['J_commuter_all'],
        'J_risk_all': context['J_risk_all'],
        'J_airtime': context['J_airtime'],
        'J_annual_peak': (((float(context['J_min']) + float(context['J_max'])) / 2) + float(
            context['J_nairobi_house_allowance']) + float(context['J_medical_all']) + float(
            context['J_commuter_all']) + float(context['J_risk_all']) + float(context['J_airtime'])) * 12,
        'J_leave_all': context['J_leave_all'],
        'J_total_annual_emoluments': ((((float(context['J_min']) + float(context['J_max'])) / 2) + float(
            context['J_nairobi_house_allowance']) + float(context['J_medical_all']) + float(
            context['J_commuter_all']) + float(context['J_risk_all']) + float(context['J_airtime'])) * 12) + float(
            context['J_leave_all']),
        'J_salary_no': context['J_salary_no'],
        'J_annual_cost': (((((float(context['J_min']) + float(context['J_max'])) / 2) + float(
            context['J_nairobi_house_allowance']) + float(context['J_medical_all']) + float(
            context['J_commuter_all']) + float(context['J_risk_all']) + float(context['J_airtime'])) * 12) + float(
            context['J_leave_all'])) * float(context['J_salary_no']),
        'H_min': context['H_min'],
        'H_max': context['H_max'],
        'H_average': (float(context['H_min']) + float(context['H_max'])) / 2,
        'H_nairobi_house_allowance': context['H_nairobi_house_allowance'],
        'H_medical_all': context['H_medical_all'],
        'H_commuter_all': context['H_commuter_all'],
        'H_risk_all': context['H_risk_all'],
        'H_airtime': context['H_airtime'],
        'H_annual_peak': (((float(context['H_min']) + float(context['H_max'])) / 2) + float(
            context['H_nairobi_house_allowance']) + float(context['H_medical_all']) + float(
            context['H_commuter_all']) + float(context['H_risk_all']) + float(context['H_airtime'])) * 12,
        'H_leave_all': context['H_leave_all'],
        'H_total_annual_emoluments': ((((float(context['H_min']) + float(context['H_max'])) / 2) + float(
            context['H_nairobi_house_allowance']) + float(context['H_medical_all']) + float(
            context['H_commuter_all']) + float(context['H_risk_all']) + float(context['H_airtime'])) * 12) + float(
            context['H_leave_all']),
        'H_salary_no': context['H_salary_no'],
        'H_annual_cost': (((((float(context['H_min']) + float(context['H_max'])) / 2) + float(
            context['H_nairobi_house_allowance']) + float(context['H_medical_all']) + float(
            context['H_commuter_all']) + float(context['H_risk_all']) + float(context['H_airtime'])) * 12) + float(
            context['H_leave_all'])) * float(context['H_salary_no']),
        'G_min': context['G_min'],
        'G_max': context['G_max'],
        'G_average': (float(context['G_min']) + float(context['G_max'])) / 2,
        'G_nairobi_house_allowance': context['G_nairobi_house_allowance'],
        'G_medical_all': context['G_medical_all'],
        'G_commuter_all': context['G_commuter_all'],
        'G_risk_all': context['G_risk_all'],
        'G_airtime': context['G_airtime'],
        'G_annual_peak': (((float(context['G_min']) + float(context['G_max'])) / 2) + float(
            context['G_nairobi_house_allowance']) + float(context['G_medical_all']) + float(
            context['G_commuter_all']) + float(context['G_risk_all']) + float(context['G_airtime'])) * 12,
        'G_leave_all': context['G_leave_all'],
        'G_total_annual_emoluments': ((((float(context['G_min']) + float(context['G_max'])) / 2) + float(
            context['G_nairobi_house_allowance']) + float(context['G_medical_all']) + float(
            context['G_commuter_all']) + float(context['G_risk_all']) + float(context['G_airtime'])) * 12) + float(
            context['G_leave_all']),
        'G_salary_no': context['G_salary_no'],
        'G_annual_cost': (((((float(context['G_min']) + float(context['G_max'])) / 2) + float(
            context['G_nairobi_house_allowance']) + float(context['G_medical_all']) + float(
            context['G_commuter_all']) + float(context['G_risk_all']) + float(context['G_airtime'])) * 12) + float(
            context['G_leave_all'])) * float(context['G_salary_no']),
        'F_min': context['F_min'],
        'F_max': context['F_max'],
        'F_average': (float(context['F_min']) + float(context['F_max'])) / 2,
        'F_nairobi_house_allowance': context['F_nairobi_house_allowance'],
        'F_medical_all': context['F_medical_all'],
        'F_commuter_all': context['F_commuter_all'],
        'F_risk_all': context['F_risk_all'],
        'F_airtime': context['F_airtime'],
        'F_annual_peak': (((float(context['F_min']) + float(context['F_max'])) / 2) + float(
            context['F_nairobi_house_allowance']) + float(context['F_medical_all']) + float(
            context['F_commuter_all']) + float(context['F_risk_all']) + float(context['F_airtime'])) * 12,
        'F_leave_all': context['F_leave_all'],
        'F_total_annual_emoluments': ((((float(context['F_min']) + float(context['F_max'])) / 2) + float(
            context['F_nairobi_house_allowance']) + float(context['F_medical_all']) + float(
            context['F_commuter_all']) + float(context['F_risk_all']) + float(context['F_airtime'])) * 12) + float(
            context['F_leave_all']),
        'F_salary_no': context['F_salary_no'],
        'F_annual_cost': (((((float(context['F_min']) + float(context['F_max'])) / 2) + float(
            context['F_nairobi_house_allowance']) + float(context['F_medical_all']) + float(
            context['F_commuter_all']) + float(context['F_risk_all']) + float(context['F_airtime'])) * 12) + float(
            context['F_leave_all'])) * float(context['F_salary_no']),
        'salary_allowance_total': ((((((float(context['S_min'])+float(context['S_max']))/2)+float(context['S_nairobi_house_allowance'])+float(context['S_medical_all'])+float(context['S_commuter_all'])+float(context['S_risk_all'])+float(context['S_airtime']))*12)+float(context['S_leave_all']))*float(context['S_salary_no']))+
                            ((((((float(context['R_min'])+float(context['R_max']))/2)+float(context['R_nairobi_house_allowance'])+float(context['R_medical_all'])+float(context['R_commuter_all'])+float(context['R_risk_all'])+float(context['R_airtime']))*12)+float(context['R_leave_all']))*float(context['R_salary_no']))+
                            ((((((float(context['Q_min'])+float(context['Q_max']))/2)+float(context['Q_nairobi_house_allowance'])+float(context['Q_medical_all'])+float(context['Q_commuter_all'])+float(context['Q_risk_all'])+float(context['Q_airtime']))*12)+float(context['Q_leave_all']))*float(context['Q_salary_no']))+
                            ((((((float(context['P_min'])+float(context['P_max']))/2)+float(context['P_nairobi_house_allowance'])+float(context['P_medical_all'])+float(context['P_commuter_all'])+float(context['P_risk_all'])+float(context['P_airtime']))*12)+float(context['P_leave_all']))*float(context['P_salary_no']))+
                            ((((((float(context['N_min'])+float(context['N_max']))/2)+float(context['N_nairobi_house_allowance'])+float(context['N_medical_all'])+float(context['N_commuter_all'])+float(context['N_risk_all'])+float(context['N_airtime']))*12)+float(context['N_leave_all']))*float(context['N_salary_no']))+
                            ((((((float(context['M_min'])+float(context['M_max']))/2)+float(context['M_nairobi_house_allowance'])+float(context['M_medical_all'])+float(context['M_commuter_all'])+float(context['M_risk_all'])+float(context['M_airtime']))*12)+float(context['M_leave_all']))*float(context['M_salary_no']))+
                            ((((((float(context['L_min'])+float(context['L_max']))/2)+float(context['L_nairobi_house_allowance'])+float(context['L_medical_all'])+float(context['L_commuter_all'])+float(context['L_risk_all'])+float(context['L_airtime']))*12)+float(context['L_leave_all']))*float(context['L_salary_no']))+
                            ((((((float(context['K_min'])+float(context['K_max']))/2)+float(context['K_nairobi_house_allowance'])+float(context['K_medical_all'])+float(context['K_commuter_all'])+float(context['K_risk_all'])+float(context['K_airtime']))*12)+float(context['K_leave_all']))*float(context['K_salary_no']))+
                            ((((((float(context['J_min'])+float(context['J_max']))/2)+float(context['J_nairobi_house_allowance'])+float(context['J_medical_all'])+float(context['J_commuter_all'])+float(context['J_risk_all'])+float(context['J_airtime']))*12)+float(context['J_leave_all']))*float(context['J_salary_no']))+
                            ((((((float(context['H_min'])+float(context['H_max']))/2)+float(context['H_nairobi_house_allowance'])+float(context['H_medical_all'])+float(context['H_commuter_all'])+float(context['H_risk_all'])+float(context['H_airtime']))*12)+float(context['H_leave_all']))*float(context['H_salary_no']))+
                            ((((((float(context['G_min'])+float(context['G_max']))/2)+float(context['G_nairobi_house_allowance'])+float(context['G_medical_all'])+float(context['G_commuter_all'])+float(context['G_risk_all'])+float(context['G_airtime']))*12)+float(context['G_leave_all']))*float(context['G_salary_no']))+
                            ((((((float(context['F_min'])+float(context['F_max']))/2)+float(context['F_nairobi_house_allowance'])+float(context['F_medical_all'])+float(context['F_commuter_all'])+float(context['F_risk_all'])+float(context['F_airtime']))*12)+float(context['F_leave_all']))*float(context['F_salary_no'])),
    }

    return render(request,'salary_allowances.html',context2)

def capital_costs(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_initial_collection = rvf_db['capital_costs']

    context = {
        'capital_costs_assumptions': 0,
        'surveillance_land_cruisers_number': 94,
        'surveillance_land_cruisers_replacement_unit_cost': 0,
        'surveillance_land_cruisers_setup_costs': 0,
        'surveillance_land_cruisers_salvage_value': 0,
        'surveillance_land_cruisers_productive_lifespan': 15,
        'surveillance_land_cruisers_annual_cost': 0,
        'supervisor_land_cruisers_number': 47,
        'supervisor_land_cruisers_replacement_unit_cost': 0,
        'supervisor_land_cruisers_setup_costs': 0,
        'supervisor_land_cruisers_salvage_value': 0,
        'supervisor_land_cruisers_productive_lifespan': 15,
        'supervisor_land_cruisers_annual_cost': 0,
        '10ml_auto_syringes_number': 752,
        '10ml_auto_syringes_replacement_unit_cost': 0,
        '10ml_auto_syringes_setup_costs': 0,
        '10ml_auto_syringes_salvage_value': 0,
        '10ml_auto_syringes_productive_lifespan': 3,
        '10ml_auto_syringes_annual_cost': 0,
        '30ml_auto_syringes_number': 188,
        '30ml_auto_syringes_replacement_unit_cost': 0,
        '30ml_auto_syringes_setup_costs': 0,
        '30ml_auto_syringes_salvage_value': 0,
        '30ml_auto_syringes_productive_lifespan': 3,
        '30ml_auto_syringes_annual_cost': 0,
        '50ml_auto_syringes_number': 188,
        '50ml_auto_syringes_replacement_unit_cost': 0,
        '50ml_auto_syringes_setup_costs': 0,
        '50ml_auto_syringes_salvage_value': 0,
        '50ml_auto_syringes_productive_lifespan': 3,
        '50ml_auto_syringes_annual_cost': 0,
        'camping_equipment_number': 188,
        'camping_equipment_replacement_unit_cost': 0,
        'camping_equipment_setup_costs': 0,
        'camping_equipment_salvage_value': 0,
        'camping_equipment_productive_lifespan': 5,
        'camping_equipment_annual_cost': 0,
        'refrigerator_number': 188,
        'refrigerator_replacement_unit_cost': 0,
        'refrigerator_setup_costs': 0,
        'refrigerator_salvage_value': 0,
        'refrigerator_productive_lifespan': 10,
        'refrigerator_annual_cost': 0,
        'offices_number': 60,
        'offices_replacement_unit_cost': 0,
        'offices_setup_costs': 0,
        'offices_salvage_value': 0,
        'offices_productive_lifespan': 5,
        'offices_annual_cost': 0,
        'freezers_number': 47,
        'freezers_replacement_unit_cost': 0,
        'freezers_setup_costs': 0,
        'freezers_salvage_value': 0,
        'freezers_productive_lifespan': 10,
        'freezers_annual_cost': 0,
        'gas_cylinder_number': 188,
        'gas_cylinder_replacement_unit_cost': 0,
        'gas_cylinder_setup_costs': 0,
        'gas_cylinder_salvage_value': 0,
        'gas_cylinder_productive_lifespan': 10,
        'gas_cylinder_annual_cost': 0,
        'crushes_number': 188,
        'crushes_replacement_unit_cost': 0,
        'crushes_setup_costs': 0,
        'crushes_salvage_value': 0,
        'crushes_productive_lifespan': 10,
        'crushes_annual_cost': 0,
        'tally_counters_number': 188,
        'tally_counters_replacement_unit_cost': 0,
        'tally_counters_setup_costs': 0,
        'tally_counters_salvage_value': 0,
        'tally_counters_productive_lifespan': 3,
        'tally_counters_annual_cost': 0,
        'generators_number': 188,
        'generators_replacement_unit_cost': 0,
        'generators_setup_costs': 0,
        'generators_salvage_value': 0,
        'generators_productive_lifespan': 10,
        'generators_annual_cost': 0,
        'ice_maker_number': 47,
        'ice_maker_replacement_unit_cost': 0,
        'ice_maker_setup_costs': 0,
        'ice_maker_salvage_value': 0,
        'ice_maker_productive_lifespan': 10,
        'ice_maker_annual_cost': 0,
        'ear_notchers_number': 188,
        'ear_notchers_replacement_unit_cost': 0,
        'ear_notchers_setup_costs': 0,
        'ear_notchers_salvage_value': 0,
        'ear_notchers_productive_lifespan': 2,
        'ear_notchers_annual_cost': 0,
        'vaccine_production_unit_number': 1,
        'vaccine_production_unit_replacement_unit_cost': 0,
        'vaccine_production_unit_setup_costs': 0,
        'vaccine_production_unit_salvage_value': 0,
        'vaccine_production_unit_productive_lifespan': 10,
        'vaccine_production_unit_annual_cost': 0,
        'diagnostic_labs_number': 3,
        'diagnostic_labs_replacement_unit_cost': 0,
        'diagnostic_labs_setup_costs': 0,
        'diagnostic_labs_salvage_value': 0,
        'diagnostic_labs_productive_lifespan': 5,
        'diagnostic_labs_annual_cost': 0,
        'equipment_repair_number': 188,
        'equipment_repair_replacement_unit_cost': 0,
        'equipment_repair_setup_costs': 0,
        'equipment_repair_annual_cost': 0,
        'vehicle_repair_number': 141,
        'vehicle_repair_replacement_unit_cost': 0,
        'vehicle_repair_setup_costs': 0,
        'vehicle_repair_annual_cost': 0,
        'crush_survey_repair_number': 188,
        'crush_survey_repair_replacement_unit_cost': 0,
        'crush_survey_repair_setup_costs': 0,
        'crush_survey_repair_annual_cost': 0,
        'electricity_number': 188,
        'electricity_replacement_unit_cost': 0,
        'electricity_setup_costs': 0,
        'electricity_annual_cost': 0,
        'setup_capital_total_cost': 0,
        'annual_capital_total_cost': 0,
    }

    if (request.method == "POST"):
        capital_costs_assumptions = request.POST['capital_costs_assumptions']
        surveillance_land_cruisers_number = request.POST['surveillance_land_cruisers_number']
        surveillance_land_cruisers_replacement_unit_cost = request.POST['surveillance_land_cruisers_replacement_unit_cost']
        surveillance_land_cruisers_setup_costs = request.POST['surveillance_land_cruisers_setup_costs']
        surveillance_land_cruisers_salvage_value = request.POST['surveillance_land_cruisers_salvage_value']
        surveillance_land_cruisers_productive_lifespan = request.POST['surveillance_land_cruisers_productive_lifespan']
        surveillance_land_cruisers_annual_cost = request.POST['surveillance_land_cruisers_annual_cost']
        supervisor_land_cruisers_number = request.POST['supervisor_land_cruisers_number']
        supervisor_land_cruisers_replacement_unit_cost = request.POST['supervisor_land_cruisers_replacement_unit_cost']
        supervisor_land_cruisers_setup_costs = request.POST['supervisor_land_cruisers_setup_costs']
        supervisor_land_cruisers_salvage_value = request.POST['supervisor_land_cruisers_salvage_value']
        supervisor_land_cruisers_productive_lifespan = request.POST['supervisor_land_cruisers_productive_lifespan']
        supervisor_land_cruisers_annual_cost = request.POST['supervisor_land_cruisers_annual_cost']
        _10ml_auto_syringes_number = request.POST['10ml_auto_syringes_number']
        _10ml_auto_syringes_replacement_unit_cost = request.POST['10ml_auto_syringes_replacement_unit_cost']
        _10ml_auto_syringes_setup_costs = request.POST['10ml_auto_syringes_setup_costs']
        _10ml_auto_syringes_salvage_value = request.POST['10ml_auto_syringes_salvage_value']
        _10ml_auto_syringes_productive_lifespan = request.POST['10ml_auto_syringes_productive_lifespan']
        _10ml_auto_syringes_annual_cost = request.POST['10ml_auto_syringes_annual_cost']
        _30ml_auto_syringes_number = request.POST['30ml_auto_syringes_number']
        _30ml_auto_syringes_replacement_unit_cost = request.POST['30ml_auto_syringes_replacement_unit_cost']
        _30ml_auto_syringes_setup_costs = request.POST['30ml_auto_syringes_setup_costs']
        _30ml_auto_syringes_salvage_value = request.POST['30ml_auto_syringes_salvage_value']
        _30ml_auto_syringes_productive_lifespan = request.POST['30ml_auto_syringes_productive_lifespan']
        _30ml_auto_syringes_annual_cost = request.POST['30ml_auto_syringes_annual_cost']
        _50ml_auto_syringes_number = request.POST['50ml_auto_syringes_number']
        _50ml_auto_syringes_replacement_unit_cost = request.POST['50ml_auto_syringes_replacement_unit_cost']
        _50ml_auto_syringes_setup_costs = request.POST['50ml_auto_syringes_setup_costs']
        _50ml_auto_syringes_salvage_value = request.POST['50ml_auto_syringes_salvage_value']
        _50ml_auto_syringes_productive_lifespan = request.POST['50ml_auto_syringes_productive_lifespan']
        _50ml_auto_syringes_annual_cost = request.POST['50ml_auto_syringes_annual_cost']
        camping_equipment_number = request.POST['camping_equipment_number']
        camping_equipment_replacement_unit_cost = request.POST['camping_equipment_replacement_unit_cost']
        camping_equipment_setup_costs = request.POST['camping_equipment_setup_costs']
        camping_equipment_salvage_value = request.POST['camping_equipment_salvage_value']
        camping_equipment_productive_lifespan = request.POST['camping_equipment_productive_lifespan']
        camping_equipment_annual_cost = request.POST['camping_equipment_annual_cost']
        refrigerator_number = request.POST['refrigerator_number']
        refrigerator_replacement_unit_cost = request.POST['refrigerator_replacement_unit_cost']
        refrigerator_setup_costs = request.POST['refrigerator_setup_costs']
        refrigerator_salvage_value = request.POST['refrigerator_salvage_value']
        refrigerator_productive_lifespan = request.POST['refrigerator_productive_lifespan']
        refrigerator_annual_cost = request.POST['refrigerator_annual_cost']
        offices_number = request.POST['offices_number']
        offices_replacement_unit_cost = request.POST['offices_replacement_unit_cost']
        offices_setup_costs = request.POST['offices_setup_costs']
        offices_salvage_value = request.POST['offices_salvage_value']
        offices_productive_lifespan = request.POST['offices_productive_lifespan']
        offices_annual_cost = request.POST['offices_annual_cost']
        freezers_number = request.POST['freezers_number']
        freezers_replacement_unit_cost = request.POST['freezers_replacement_unit_cost']
        freezers_setup_costs = request.POST['freezers_setup_costs']
        freezers_salvage_value = request.POST['freezers_salvage_value']
        freezers_productive_lifespan = request.POST['freezers_productive_lifespan']
        freezers_annual_cost = request.POST['freezers_annual_cost']
        gas_cylinder_number = request.POST['gas_cylinder_number']
        gas_cylinder_replacement_unit_cost = request.POST['gas_cylinder_replacement_unit_cost']
        gas_cylinder_setup_costs = request.POST['gas_cylinder_setup_costs']
        gas_cylinder_salvage_value = request.POST['gas_cylinder_salvage_value']
        gas_cylinder_productive_lifespan = request.POST['gas_cylinder_productive_lifespan']
        gas_cylinder_annual_cost = request.POST['gas_cylinder_annual_cost']
        crushes_number = request.POST['crushes_number']
        crushes_replacement_unit_cost = request.POST['crushes_replacement_unit_cost']
        crushes_setup_costs = request.POST['crushes_setup_costs']
        crushes_salvage_value = request.POST['crushes_salvage_value']
        crushes_productive_lifespan = request.POST['crushes_productive_lifespan']
        crushes_annual_cost = request.POST['crushes_annual_cost']
        tally_counters_number = request.POST['tally_counters_number']
        tally_counters_replacement_unit_cost = request.POST['tally_counters_replacement_unit_cost']
        tally_counters_setup_costs = request.POST['tally_counters_setup_costs']
        tally_counters_salvage_value = request.POST['tally_counters_salvage_value']
        tally_counters_productive_lifespan = request.POST['tally_counters_productive_lifespan']
        tally_counters_annual_cost = request.POST['tally_counters_annual_cost']
        generators_number = request.POST['generators_number']
        generators_replacement_unit_cost = request.POST['generators_replacement_unit_cost']
        generators_setup_costs = request.POST['generators_setup_costs']
        generators_salvage_value = request.POST['generators_salvage_value']
        generators_productive_lifespan = request.POST['generators_productive_lifespan']
        generators_annual_cost = request.POST['generators_annual_cost']
        ice_maker_number = request.POST['ice_maker_number']
        ice_maker_replacement_unit_cost = request.POST['ice_maker_replacement_unit_cost']
        ice_maker_setup_costs = request.POST['ice_maker_setup_costs']
        ice_maker_salvage_value = request.POST['ice_maker_salvage_value']
        ice_maker_productive_lifespan = request.POST['ice_maker_productive_lifespan']
        ice_maker_annual_cost = request.POST['ice_maker_annual_cost']
        ear_notchers_number = request.POST['ear_notchers_number']
        ear_notchers_replacement_unit_cost = request.POST['ear_notchers_replacement_unit_cost']
        ear_notchers_setup_costs = request.POST['ear_notchers_setup_costs']
        ear_notchers_salvage_value = request.POST['ear_notchers_salvage_value']
        ear_notchers_productive_lifespan = request.POST['ear_notchers_productive_lifespan']
        ear_notchers_annual_cost = request.POST['ear_notchers_annual_cost']
        vaccine_production_unit_number = request.POST['vaccine_production_unit_number']
        vaccine_production_unit_replacement_unit_cost = request.POST['vaccine_production_unit_replacement_unit_cost']
        vaccine_production_unit_setup_costs = request.POST['vaccine_production_unit_setup_costs']
        vaccine_production_unit_salvage_value = request.POST['vaccine_production_unit_salvage_value']
        vaccine_production_unit_productive_lifespan = request.POST['vaccine_production_unit_productive_lifespan']
        vaccine_production_unit_annual_cost = request.POST['vaccine_production_unit_annual_cost']
        diagnostic_labs_number = request.POST['diagnostic_labs_number']
        diagnostic_labs_replacement_unit_cost = request.POST['diagnostic_labs_replacement_unit_cost']
        diagnostic_labs_setup_costs = request.POST['diagnostic_labs_setup_costs']
        diagnostic_labs_salvage_value = request.POST['diagnostic_labs_salvage_value']
        diagnostic_labs_productive_lifespan = request.POST['diagnostic_labs_productive_lifespan']
        diagnostic_labs_annual_cost = request.POST['diagnostic_labs_annual_cost']
        equipment_repair_number = request.POST['equipment_repair_number']
        equipment_repair_replacement_unit_cost = request.POST['equipment_repair_replacement_unit_cost']
        equipment_repair_setup_costs = request.POST['equipment_repair_setup_costs']
        equipment_repair_annual_cost = request.POST['equipment_repair_annual_cost']
        vehicle_repair_number = request.POST['vehicle_repair_number']
        vehicle_repair_replacement_unit_cost = request.POST['vehicle_repair_replacement_unit_cost']
        vehicle_repair_setup_costs = request.POST['vehicle_repair_setup_costs']
        vehicle_repair_annual_cost = request.POST['vehicle_repair_annual_cost']
        crush_survey_repair_number = request.POST['crush_survey_repair_number']
        crush_survey_repair_replacement_unit_cost = request.POST['crush_survey_repair_replacement_unit_cost']
        crush_survey_repair_setup_costs = request.POST['crush_survey_repair_setup_costs']
        crush_survey_repair_annual_cost = request.POST['crush_survey_repair_annual_cost']
        electricity_number = request.POST['electricity_number']
        electricity_replacement_unit_cost = request.POST['electricity_replacement_unit_cost']
        electricity_setup_costs = request.POST['electricity_setup_costs']
        electricity_annual_cost = request.POST['electricity_annual_cost']
        setup_capital_total_cost = request.POST['setup_capital_total_cost']
        annual_capital_total_cost = request.POST['annual_capital_total_cost']

        x = rvf_initial_collection.insert_one({
            'capital_costs_assumptions': capital_costs_assumptions,
            'surveillance_land_cruisers_number': surveillance_land_cruisers_number,
            'surveillance_land_cruisers_replacement_unit_cost': surveillance_land_cruisers_replacement_unit_cost,
            'surveillance_land_cruisers_setup_costs': float(surveillance_land_cruisers_number) * float(
                surveillance_land_cruisers_replacement_unit_cost),
            'surveillance_land_cruisers_salvage_value': surveillance_land_cruisers_salvage_value,
            'surveillance_land_cruisers_productive_lifespan': surveillance_land_cruisers_productive_lifespan,
            'surveillance_land_cruisers_annual_cost': float(surveillance_land_cruisers_number) * ((float(
                surveillance_land_cruisers_replacement_unit_cost) - float(
                surveillance_land_cruisers_salvage_value)) / float(surveillance_land_cruisers_productive_lifespan)),
            'supervisor_land_cruisers_number': supervisor_land_cruisers_number,
            'supervisor_land_cruisers_replacement_unit_cost': supervisor_land_cruisers_replacement_unit_cost,
            'supervisor_land_cruisers_setup_costs': float(supervisor_land_cruisers_number) * float(
                supervisor_land_cruisers_replacement_unit_cost),
            'supervisor_land_cruisers_salvage_value': supervisor_land_cruisers_salvage_value,
            'supervisor_land_cruisers_productive_lifespan': supervisor_land_cruisers_productive_lifespan,
            'supervisor_land_cruisers_annual_cost': float(supervisor_land_cruisers_number) * ((float(
                supervisor_land_cruisers_replacement_unit_cost) - float(
                supervisor_land_cruisers_salvage_value)) / float(supervisor_land_cruisers_productive_lifespan)),
            '10ml_auto_syringes_number': _10ml_auto_syringes_number,
            '10ml_auto_syringes_replacement_unit_cost': _10ml_auto_syringes_replacement_unit_cost,
            '10ml_auto_syringes_setup_costs': float(_10ml_auto_syringes_number) * float(
                _10ml_auto_syringes_replacement_unit_cost),
            '10ml_auto_syringes_salvage_value': _10ml_auto_syringes_salvage_value,
            '10ml_auto_syringes_productive_lifespan': _10ml_auto_syringes_productive_lifespan,
            '10ml_auto_syringes_annual_cost': float(_10ml_auto_syringes_number) * ((float(
                _10ml_auto_syringes_replacement_unit_cost) - float(_10ml_auto_syringes_salvage_value)) / float(
                _10ml_auto_syringes_productive_lifespan)),
            '30ml_auto_syringes_number': _30ml_auto_syringes_number,
            '30ml_auto_syringes_replacement_unit_cost': _30ml_auto_syringes_replacement_unit_cost,
            '30ml_auto_syringes_setup_costs': float(_30ml_auto_syringes_number) * float(
                _30ml_auto_syringes_replacement_unit_cost),
            '30ml_auto_syringes_salvage_value': _30ml_auto_syringes_salvage_value,
            '30ml_auto_syringes_productive_lifespan': _30ml_auto_syringes_productive_lifespan,
            '30ml_auto_syringes_annual_cost': float(_30ml_auto_syringes_number) * ((float(
                _30ml_auto_syringes_replacement_unit_cost) - float(_30ml_auto_syringes_salvage_value)) / float(
                _30ml_auto_syringes_productive_lifespan)),
            '50ml_auto_syringes_number': _50ml_auto_syringes_number,
            '50ml_auto_syringes_replacement_unit_cost': _50ml_auto_syringes_replacement_unit_cost,
            '50ml_auto_syringes_setup_costs': float(_50ml_auto_syringes_number) * float(
                _50ml_auto_syringes_replacement_unit_cost),
            '50ml_auto_syringes_salvage_value': _50ml_auto_syringes_salvage_value,
            '50ml_auto_syringes_productive_lifespan': _50ml_auto_syringes_productive_lifespan,
            '50ml_auto_syringes_annual_cost': float(_50ml_auto_syringes_number) * ((float(
                _50ml_auto_syringes_replacement_unit_cost) - float(_50ml_auto_syringes_salvage_value)) / float(
                _50ml_auto_syringes_productive_lifespan)),
            'camping_equipment_number': camping_equipment_number,
            'camping_equipment_replacement_unit_cost': camping_equipment_replacement_unit_cost,
            'camping_equipment_setup_costs': float(camping_equipment_number) * float(
                camping_equipment_replacement_unit_cost),
            'camping_equipment_salvage_value': camping_equipment_salvage_value,
            'camping_equipment_productive_lifespan': camping_equipment_productive_lifespan,
            'camping_equipment_annual_cost': float(camping_equipment_number) * ((float(
                camping_equipment_replacement_unit_cost) - float(camping_equipment_salvage_value)) / float(
                camping_equipment_productive_lifespan)),
            'refrigerator_number': refrigerator_number,
            'refrigerator_replacement_unit_cost': refrigerator_replacement_unit_cost,
            'refrigerator_setup_costs': float(refrigerator_number) * float(refrigerator_replacement_unit_cost),
            'refrigerator_salvage_value': refrigerator_salvage_value,
            'refrigerator_productive_lifespan': refrigerator_productive_lifespan,
            'refrigerator_annual_cost': float(refrigerator_number) * (
                        (float(refrigerator_replacement_unit_cost) - float(refrigerator_salvage_value)) / float(
                    refrigerator_productive_lifespan)),
            'offices_number': offices_number,
            'offices_replacement_unit_cost': offices_replacement_unit_cost,
            'offices_setup_costs': float(offices_number) * float(offices_replacement_unit_cost),
            'offices_salvage_value': offices_salvage_value,
            'offices_productive_lifespan': offices_productive_lifespan,
            'offices_annual_cost': float(offices_number) * (
                        (float(offices_replacement_unit_cost) - float(offices_salvage_value)) / float(
                    offices_productive_lifespan)),
            'freezers_number': freezers_number,
            'freezers_replacement_unit_cost': freezers_replacement_unit_cost,
            'freezers_setup_costs': float(freezers_number) * float(freezers_replacement_unit_cost),
            'freezers_salvage_value': freezers_salvage_value,
            'freezers_productive_lifespan': freezers_productive_lifespan,
            'freezers_annual_cost': float(freezers_number) * (
                        (float(freezers_replacement_unit_cost) - float(freezers_salvage_value)) / float(
                    freezers_productive_lifespan)),
            'gas_cylinder_number': gas_cylinder_number,
            'gas_cylinder_replacement_unit_cost': gas_cylinder_replacement_unit_cost,
            'gas_cylinder_setup_costs': float(gas_cylinder_number) * float(gas_cylinder_replacement_unit_cost),
            'gas_cylinder_salvage_value': gas_cylinder_salvage_value,
            'gas_cylinder_productive_lifespan': gas_cylinder_productive_lifespan,
            'gas_cylinder_annual_cost': float(gas_cylinder_number) * (
                        (float(gas_cylinder_replacement_unit_cost) - float(gas_cylinder_salvage_value)) / float(
                    gas_cylinder_productive_lifespan)),
            'crushes_number': crushes_number,
            'crushes_replacement_unit_cost': crushes_replacement_unit_cost,
            'crushes_setup_costs': float(crushes_number) * float(crushes_replacement_unit_cost),
            'crushes_salvage_value': crushes_salvage_value,
            'crushes_productive_lifespan': crushes_productive_lifespan,
            'crushes_annual_cost': float(crushes_number) * (
                        (float(crushes_replacement_unit_cost) - float(crushes_salvage_value)) / float(
                    crushes_productive_lifespan)),
            'tally_counters_number': tally_counters_number,
            'tally_counters_replacement_unit_cost': tally_counters_replacement_unit_cost,
            'tally_counters_setup_costs': float(tally_counters_number) * float(tally_counters_replacement_unit_cost),
            'tally_counters_salvage_value': tally_counters_salvage_value,
            'tally_counters_productive_lifespan': tally_counters_productive_lifespan,
            'tally_counters_annual_cost': float(tally_counters_number) * (
                        (float(tally_counters_replacement_unit_cost) - float(tally_counters_salvage_value)) / float(
                    tally_counters_productive_lifespan)),
            'generators_number': generators_number,
            'generators_replacement_unit_cost': generators_replacement_unit_cost,
            'generators_setup_costs': float(generators_number) * float(generators_replacement_unit_cost),
            'generators_salvage_value': generators_salvage_value,
            'generators_productive_lifespan': generators_productive_lifespan,
            'generators_annual_cost': float(generators_number) * (
                        (float(generators_replacement_unit_cost) - float(generators_salvage_value)) / float(
                    generators_productive_lifespan)),
            'ice_maker_number': ice_maker_number,
            'ice_maker_replacement_unit_cost': ice_maker_replacement_unit_cost,
            'ice_maker_setup_costs': float(ice_maker_number) * float(ice_maker_replacement_unit_cost),
            'ice_maker_salvage_value': ice_maker_salvage_value,
            'ice_maker_productive_lifespan': ice_maker_productive_lifespan,
            'ice_maker_annual_cost': float(ice_maker_number) * (
                        (float(ice_maker_replacement_unit_cost) - float(ice_maker_salvage_value)) / float(
                    ice_maker_productive_lifespan)),
            'ear_notchers_number': ear_notchers_number,
            'ear_notchers_replacement_unit_cost': ear_notchers_replacement_unit_cost,
            'ear_notchers_setup_costs': float(ear_notchers_number) * float(ear_notchers_replacement_unit_cost),
            'ear_notchers_salvage_value': ear_notchers_salvage_value,
            'ear_notchers_productive_lifespan': ear_notchers_productive_lifespan,
            'ear_notchers_annual_cost': float(ear_notchers_number) * (
                        (float(ear_notchers_replacement_unit_cost) - float(ear_notchers_salvage_value)) / float(
                    ear_notchers_productive_lifespan)),
            'vaccine_production_unit_number': vaccine_production_unit_number,
            'vaccine_production_unit_replacement_unit_cost': vaccine_production_unit_replacement_unit_cost,
            'vaccine_production_unit_setup_costs': float(vaccine_production_unit_number) * float(
                vaccine_production_unit_replacement_unit_cost),
            'vaccine_production_unit_salvage_value': vaccine_production_unit_salvage_value,
            'vaccine_production_unit_productive_lifespan': vaccine_production_unit_productive_lifespan,
            'vaccine_production_unit_annual_cost': float(vaccine_production_unit_number) * ((float(
                vaccine_production_unit_replacement_unit_cost) - float(vaccine_production_unit_salvage_value)) / float(
                vaccine_production_unit_productive_lifespan)),
            'diagnostic_labs_number': diagnostic_labs_number,
            'diagnostic_labs_replacement_unit_cost': diagnostic_labs_replacement_unit_cost,
            'diagnostic_labs_setup_costs': float(diagnostic_labs_number) * float(diagnostic_labs_replacement_unit_cost),
            'diagnostic_labs_salvage_value': diagnostic_labs_salvage_value,
            'diagnostic_labs_productive_lifespan': diagnostic_labs_productive_lifespan,
            'diagnostic_labs_annual_cost': float(diagnostic_labs_number) * (
                        (float(diagnostic_labs_replacement_unit_cost) - float(diagnostic_labs_salvage_value)) / float(
                    diagnostic_labs_productive_lifespan)),
            'equipment_repair_number': equipment_repair_number,
            'equipment_repair_replacement_unit_cost': equipment_repair_replacement_unit_cost,
            'equipment_repair_setup_costs': float(equipment_repair_number) * float(
                equipment_repair_replacement_unit_cost),
            'equipment_repair_annual_cost': float(equipment_repair_number) * float(
                equipment_repair_replacement_unit_cost),
            'vehicle_repair_number': vehicle_repair_number,
            'vehicle_repair_replacement_unit_cost': vehicle_repair_replacement_unit_cost,
            'vehicle_repair_setup_costs': float(vehicle_repair_number) * float(vehicle_repair_replacement_unit_cost),
            'vehicle_repair_annual_cost': float(vehicle_repair_number) * float(vehicle_repair_replacement_unit_cost),
            'crush_survey_repair_number': crush_survey_repair_number,
            'crush_survey_repair_replacement_unit_cost': crush_survey_repair_replacement_unit_cost,
            'crush_survey_repair_setup_costs': float(crush_survey_repair_number) * float(
                crush_survey_repair_replacement_unit_cost),
            'crush_survey_repair_annual_cost': float(crush_survey_repair_number) * float(
                crush_survey_repair_replacement_unit_cost),
            'electricity_number': electricity_number,
            'electricity_replacement_unit_cost': electricity_replacement_unit_cost,
            'electricity_setup_costs': float(electricity_number) * float(electricity_replacement_unit_cost),
            'electricity_annual_cost': float(electricity_number) * float(electricity_replacement_unit_cost),
            'setup_capital_total_cost': (float(surveillance_land_cruisers_number) * float(
                surveillance_land_cruisers_replacement_unit_cost)) +
                                        (float(supervisor_land_cruisers_number) * float(
                                            supervisor_land_cruisers_replacement_unit_cost)) +
                                        (float(_10ml_auto_syringes_number) * float(
                                            _10ml_auto_syringes_replacement_unit_cost)) +
                                        (float(_30ml_auto_syringes_number) * float(
                                            _30ml_auto_syringes_replacement_unit_cost)) +
                                        (float(_50ml_auto_syringes_number) * float(
                                            _50ml_auto_syringes_replacement_unit_cost)) +
                                        (float(camping_equipment_number) * float(
                                            camping_equipment_replacement_unit_cost)) +
                                        (float(refrigerator_number) * float(refrigerator_replacement_unit_cost)) +
                                        (float(offices_number) * float(offices_replacement_unit_cost)) +
                                        (float(freezers_number) * float(freezers_replacement_unit_cost)) +
                                        (float(gas_cylinder_number) * float(gas_cylinder_replacement_unit_cost)) +
                                        (float(crushes_number) * float(crushes_replacement_unit_cost)) +
                                        (float(tally_counters_number) * float(tally_counters_replacement_unit_cost)) +
                                        (float(generators_number) * float(generators_replacement_unit_cost)) +
                                        (float(ice_maker_number) * float(ice_maker_replacement_unit_cost)) +
                                        (float(ear_notchers_number) * float(ear_notchers_replacement_unit_cost)) +
                                        (float(vaccine_production_unit_number) * float(
                                            vaccine_production_unit_replacement_unit_cost)) +
                                        (float(diagnostic_labs_number) * float(diagnostic_labs_replacement_unit_cost)) +
                                        (float(equipment_repair_number) * float(
                                            equipment_repair_replacement_unit_cost)) +
                                        (float(vehicle_repair_number) * float(vehicle_repair_replacement_unit_cost)) +
                                        (float(crush_survey_repair_number) * float(
                                            crush_survey_repair_replacement_unit_cost)) +
                                        (float(electricity_number) * float(electricity_replacement_unit_cost)),

            'annual_capital_total_cost': (float(surveillance_land_cruisers_number) * ((float(
                surveillance_land_cruisers_replacement_unit_cost) - float(
                surveillance_land_cruisers_salvage_value)) / float(surveillance_land_cruisers_productive_lifespan))) +
                                         (float(supervisor_land_cruisers_number) * ((float(
                                             supervisor_land_cruisers_replacement_unit_cost) - float(
                                             supervisor_land_cruisers_salvage_value)) / float(
                                             supervisor_land_cruisers_productive_lifespan))) +
                                         (float(_10ml_auto_syringes_number) * ((float(
                                             _10ml_auto_syringes_replacement_unit_cost) - float(
                                             _10ml_auto_syringes_salvage_value)) / float(
                                             _10ml_auto_syringes_productive_lifespan))) +
                                         (float(_30ml_auto_syringes_number) * ((float(
                                             _30ml_auto_syringes_replacement_unit_cost) - float(
                                             _30ml_auto_syringes_salvage_value)) / float(
                                             _30ml_auto_syringes_productive_lifespan))) +
                                         (float(_50ml_auto_syringes_number) * ((float(
                                             _50ml_auto_syringes_replacement_unit_cost) - float(
                                             _50ml_auto_syringes_salvage_value)) / float(
                                             _50ml_auto_syringes_productive_lifespan))) +
                                         (float(camping_equipment_number) * ((float(
                                             camping_equipment_replacement_unit_cost) - float(
                                             camping_equipment_salvage_value)) / float(
                                             camping_equipment_productive_lifespan))) +
                                         (float(refrigerator_number) * ((float(
                                             refrigerator_replacement_unit_cost) - float(
                                             refrigerator_salvage_value)) / float(refrigerator_productive_lifespan))) +
                                         (float(offices_number) * ((float(offices_replacement_unit_cost) - float(
                                             offices_salvage_value)) / float(offices_productive_lifespan))) +
                                         (float(freezers_number) * ((float(freezers_replacement_unit_cost) - float(
                                             freezers_salvage_value)) / float(freezers_productive_lifespan))) +
                                         (float(gas_cylinder_number) * ((float(
                                             gas_cylinder_replacement_unit_cost) - float(
                                             gas_cylinder_salvage_value)) / float(gas_cylinder_productive_lifespan))) +
                                         (float(crushes_number) * ((float(crushes_replacement_unit_cost) - float(
                                             crushes_salvage_value)) / float(crushes_productive_lifespan))) +
                                         (float(tally_counters_number) * ((float(
                                             tally_counters_replacement_unit_cost) - float(
                                             tally_counters_salvage_value)) / float(
                                             tally_counters_productive_lifespan))) +
                                         (float(generators_number) * ((float(generators_replacement_unit_cost) - float(
                                             generators_salvage_value)) / float(generators_productive_lifespan))) +
                                         (float(ice_maker_number) * ((float(ice_maker_replacement_unit_cost) - float(
                                             ice_maker_salvage_value)) / float(ice_maker_productive_lifespan))) +
                                         (float(ear_notchers_number) * ((float(
                                             ear_notchers_replacement_unit_cost) - float(
                                             ear_notchers_salvage_value)) / float(ear_notchers_productive_lifespan))) +
                                         (float(vaccine_production_unit_number) * ((float(
                                             vaccine_production_unit_replacement_unit_cost) - float(
                                             vaccine_production_unit_salvage_value)) / float(
                                             vaccine_production_unit_productive_lifespan))) +
                                         (float(diagnostic_labs_number) * ((float(
                                             diagnostic_labs_replacement_unit_cost) - float(
                                             diagnostic_labs_salvage_value)) / float(
                                             diagnostic_labs_productive_lifespan))) +
                                         (float(equipment_repair_number) * float(
                                             equipment_repair_replacement_unit_cost)) +
                                         (float(vehicle_repair_number) * float(vehicle_repair_replacement_unit_cost)) +
                                         (float(crush_survey_repair_number) * float(
                                             crush_survey_repair_replacement_unit_cost)) +
                                         (float(electricity_number) * float(electricity_replacement_unit_cost)),
        })

    for x in rvf_initial_collection.find({}, {"_id": 0}):
        context = x

    context2 = {
        'capital_costs_assumptions': context['capital_costs_assumptions'],
        'surveillance_land_cruisers_number': context['surveillance_land_cruisers_number'],
        'surveillance_land_cruisers_replacement_unit_cost': context['surveillance_land_cruisers_replacement_unit_cost'],
        'surveillance_land_cruisers_setup_costs': float(context['surveillance_land_cruisers_number']) * float(
            context['surveillance_land_cruisers_replacement_unit_cost']),
        'surveillance_land_cruisers_salvage_value': context['surveillance_land_cruisers_salvage_value'],
        'surveillance_land_cruisers_productive_lifespan': context['surveillance_land_cruisers_productive_lifespan'],
        'surveillance_land_cruisers_annual_cost': float(context['surveillance_land_cruisers_number']) * ((float(
            context['surveillance_land_cruisers_replacement_unit_cost']) - float(
            context['surveillance_land_cruisers_salvage_value'])) / float(
            context['surveillance_land_cruisers_productive_lifespan'])),
        'supervisor_land_cruisers_number': context['supervisor_land_cruisers_number'],
        'supervisor_land_cruisers_replacement_unit_cost': context['supervisor_land_cruisers_replacement_unit_cost'],
        'supervisor_land_cruisers_setup_costs': float(context['supervisor_land_cruisers_number']) * float(
            context['supervisor_land_cruisers_replacement_unit_cost']),
        'supervisor_land_cruisers_salvage_value': context['supervisor_land_cruisers_salvage_value'],
        'supervisor_land_cruisers_productive_lifespan': context['supervisor_land_cruisers_productive_lifespan'],
        'supervisor_land_cruisers_annual_cost': float(context['supervisor_land_cruisers_number']) * ((float(
            context['supervisor_land_cruisers_replacement_unit_cost']) - float(
            context['supervisor_land_cruisers_salvage_value'])) / float(
            context['supervisor_land_cruisers_productive_lifespan'])),
        '10ml_auto_syringes_number': context['10ml_auto_syringes_number'],
        '10ml_auto_syringes_replacement_unit_cost': context['10ml_auto_syringes_replacement_unit_cost'],
        '10ml_auto_syringes_setup_costs': float(context['10ml_auto_syringes_number']) * float(
            context['10ml_auto_syringes_replacement_unit_cost']),
        '10ml_auto_syringes_salvage_value': context['10ml_auto_syringes_salvage_value'],
        '10ml_auto_syringes_productive_lifespan': context['10ml_auto_syringes_productive_lifespan'],
        '10ml_auto_syringes_annual_cost': float(context['10ml_auto_syringes_number']) * ((float(
            context['10ml_auto_syringes_replacement_unit_cost']) - float(
            context['10ml_auto_syringes_salvage_value'])) / float(context['10ml_auto_syringes_productive_lifespan'])),
        '30ml_auto_syringes_number': context['30ml_auto_syringes_number'],
        '30ml_auto_syringes_replacement_unit_cost': context['30ml_auto_syringes_replacement_unit_cost'],
        '30ml_auto_syringes_setup_costs': float(context['30ml_auto_syringes_number']) * float(
            context['30ml_auto_syringes_replacement_unit_cost']),
        '30ml_auto_syringes_salvage_value': context['30ml_auto_syringes_salvage_value'],
        '30ml_auto_syringes_productive_lifespan': context['30ml_auto_syringes_productive_lifespan'],
        '30ml_auto_syringes_annual_cost': float(context['30ml_auto_syringes_number']) * ((float(
            context['30ml_auto_syringes_replacement_unit_cost']) - float(
            context['30ml_auto_syringes_salvage_value'])) / float(context['30ml_auto_syringes_productive_lifespan'])),
        '50ml_auto_syringes_number': context['50ml_auto_syringes_number'],
        '50ml_auto_syringes_replacement_unit_cost': context['50ml_auto_syringes_replacement_unit_cost'],
        '50ml_auto_syringes_setup_costs': float(context['50ml_auto_syringes_number']) * float(
            context['50ml_auto_syringes_replacement_unit_cost']),
        '50ml_auto_syringes_salvage_value': context['50ml_auto_syringes_salvage_value'],
        '50ml_auto_syringes_productive_lifespan': context['50ml_auto_syringes_productive_lifespan'],
        '50ml_auto_syringes_annual_cost': float(context['50ml_auto_syringes_number']) * ((float(
            context['50ml_auto_syringes_replacement_unit_cost']) - float(
            context['50ml_auto_syringes_salvage_value'])) / float(context['50ml_auto_syringes_productive_lifespan'])),
        'camping_equipment_number': context['camping_equipment_number'],
        'camping_equipment_replacement_unit_cost': context['camping_equipment_replacement_unit_cost'],
        'camping_equipment_setup_costs': float(context['camping_equipment_number']) * float(
            context['camping_equipment_replacement_unit_cost']),
        'camping_equipment_salvage_value': context['camping_equipment_salvage_value'],
        'camping_equipment_productive_lifespan': context['camping_equipment_productive_lifespan'],
        'camping_equipment_annual_cost': float(context['camping_equipment_number']) * ((float(
            context['camping_equipment_replacement_unit_cost']) - float(
            context['camping_equipment_salvage_value'])) / float(context['camping_equipment_productive_lifespan'])),
        'refrigerator_number': context['refrigerator_number'],
        'refrigerator_replacement_unit_cost': context['refrigerator_replacement_unit_cost'],
        'refrigerator_setup_costs': float(context['refrigerator_number']) * float(
            context['refrigerator_replacement_unit_cost']),
        'refrigerator_salvage_value': context['refrigerator_salvage_value'],
        'refrigerator_productive_lifespan': context['refrigerator_productive_lifespan'],
        'refrigerator_annual_cost': float(context['refrigerator_number']) * ((float(
            context['refrigerator_replacement_unit_cost']) - float(context['refrigerator_salvage_value'])) / float(
            context['refrigerator_productive_lifespan'])),
        'offices_number': context['offices_number'],
        'offices_replacement_unit_cost': context['offices_replacement_unit_cost'],
        'offices_setup_costs': float(context['offices_number']) * float(context['offices_replacement_unit_cost']),
        'offices_salvage_value': context['offices_salvage_value'],
        'offices_productive_lifespan': context['offices_productive_lifespan'],
        'offices_annual_cost': float(context['offices_number']) * (
                    (float(context['offices_replacement_unit_cost']) - float(context['offices_salvage_value'])) / float(
                context['offices_productive_lifespan'])),
        'freezers_number': context['freezers_number'],
        'freezers_replacement_unit_cost': context['freezers_replacement_unit_cost'],
        'freezers_setup_costs': float(context['freezers_number']) * float(context['freezers_replacement_unit_cost']),
        'freezers_salvage_value': context['freezers_salvage_value'],
        'freezers_productive_lifespan': context['freezers_productive_lifespan'],
        'freezers_annual_cost': float(context['freezers_number']) * ((float(
            context['freezers_replacement_unit_cost']) - float(context['freezers_salvage_value'])) / float(
            context['freezers_productive_lifespan'])),
        'gas_cylinder_number': context['gas_cylinder_number'],
        'gas_cylinder_replacement_unit_cost': context['gas_cylinder_replacement_unit_cost'],
        'gas_cylinder_setup_costs': float(context['gas_cylinder_number']) * float(
            context['gas_cylinder_replacement_unit_cost']),
        'gas_cylinder_salvage_value': context['gas_cylinder_salvage_value'],
        'gas_cylinder_productive_lifespan': context['gas_cylinder_productive_lifespan'],
        'gas_cylinder_annual_cost': float(context['gas_cylinder_number']) * ((float(
            context['gas_cylinder_replacement_unit_cost']) - float(context['gas_cylinder_salvage_value'])) / float(
            context['gas_cylinder_productive_lifespan'])),
        'crushes_number': context['crushes_number'],
        'crushes_replacement_unit_cost': context['crushes_replacement_unit_cost'],
        'crushes_setup_costs': float(context['crushes_number']) * float(context['crushes_replacement_unit_cost']),
        'crushes_salvage_value': context['crushes_salvage_value'],
        'crushes_productive_lifespan': context['crushes_productive_lifespan'],
        'crushes_annual_cost': float(context['crushes_number']) * (
                    (float(context['crushes_replacement_unit_cost']) - float(context['crushes_salvage_value'])) / float(
                context['crushes_productive_lifespan'])),
        'tally_counters_number': context['tally_counters_number'],
        'tally_counters_replacement_unit_cost': context['tally_counters_replacement_unit_cost'],
        'tally_counters_setup_costs': float(context['tally_counters_number']) * float(
            context['tally_counters_replacement_unit_cost']),
        'tally_counters_salvage_value': context['tally_counters_salvage_value'],
        'tally_counters_productive_lifespan': context['tally_counters_productive_lifespan'],
        'tally_counters_annual_cost': float(context['tally_counters_number']) * ((float(
            context['tally_counters_replacement_unit_cost']) - float(context['tally_counters_salvage_value'])) / float(
            context['tally_counters_productive_lifespan'])),
        'generators_number': context['generators_number'],
        'generators_replacement_unit_cost': context['generators_replacement_unit_cost'],
        'generators_setup_costs': float(context['generators_number']) * float(
            context['generators_replacement_unit_cost']),
        'generators_salvage_value': context['generators_salvage_value'],
        'generators_productive_lifespan': context['generators_productive_lifespan'],
        'generators_annual_cost': float(context['generators_number']) * ((float(
            context['generators_replacement_unit_cost']) - float(context['generators_salvage_value'])) / float(
            context['generators_productive_lifespan'])),
        'ice_maker_number': context['ice_maker_number'],
        'ice_maker_replacement_unit_cost': context['ice_maker_replacement_unit_cost'],
        'ice_maker_setup_costs': float(context['ice_maker_number']) * float(context['ice_maker_replacement_unit_cost']),
        'ice_maker_salvage_value': context['ice_maker_salvage_value'],
        'ice_maker_productive_lifespan': context['ice_maker_productive_lifespan'],
        'ice_maker_annual_cost': float(context['ice_maker_number']) * ((float(
            context['ice_maker_replacement_unit_cost']) - float(context['ice_maker_salvage_value'])) / float(
            context['ice_maker_productive_lifespan'])),
        'ear_notchers_number': context['ear_notchers_number'],
        'ear_notchers_replacement_unit_cost': context['ear_notchers_replacement_unit_cost'],
        'ear_notchers_setup_costs': float(context['ear_notchers_number']) * float(
            context['ear_notchers_replacement_unit_cost']),
        'ear_notchers_salvage_value': context['ear_notchers_salvage_value'],
        'ear_notchers_productive_lifespan': context['ear_notchers_productive_lifespan'],
        'ear_notchers_annual_cost': float(context['ear_notchers_number']) * ((float(
            context['ear_notchers_replacement_unit_cost']) - float(context['ear_notchers_salvage_value'])) / float(
            context['ear_notchers_productive_lifespan'])),
        'vaccine_production_unit_number': context['vaccine_production_unit_number'],
        'vaccine_production_unit_replacement_unit_cost': context['vaccine_production_unit_replacement_unit_cost'],
        'vaccine_production_unit_setup_costs': float(context['vaccine_production_unit_number']) * float(
            context['vaccine_production_unit_replacement_unit_cost']),
        'vaccine_production_unit_salvage_value': context['vaccine_production_unit_salvage_value'],
        'vaccine_production_unit_productive_lifespan': context['vaccine_production_unit_productive_lifespan'],
        'vaccine_production_unit_annual_cost': float(context['vaccine_production_unit_number']) * ((float(
            context['vaccine_production_unit_replacement_unit_cost']) - float(
            context['vaccine_production_unit_salvage_value'])) / float(
            context['vaccine_production_unit_productive_lifespan'])),
        'diagnostic_labs_number': context['diagnostic_labs_number'],
        'diagnostic_labs_replacement_unit_cost': context['diagnostic_labs_replacement_unit_cost'],
        'diagnostic_labs_setup_costs': float(context['diagnostic_labs_number']) * float(
            context['diagnostic_labs_replacement_unit_cost']),
        'diagnostic_labs_salvage_value': context['diagnostic_labs_salvage_value'],
        'diagnostic_labs_productive_lifespan': context['diagnostic_labs_productive_lifespan'],
        'diagnostic_labs_annual_cost': float(context['diagnostic_labs_number']) * ((float(
            context['diagnostic_labs_replacement_unit_cost']) - float(
            context['diagnostic_labs_salvage_value'])) / float(context['diagnostic_labs_productive_lifespan'])),
        'equipment_repair_number': context['equipment_repair_number'],
        'equipment_repair_replacement_unit_cost': context['equipment_repair_replacement_unit_cost'],
        'equipment_repair_setup_costs': float(context['equipment_repair_number']) * float(
            context['equipment_repair_replacement_unit_cost']),
        'equipment_repair_annual_cost': float(context['equipment_repair_number']) * float(
            context['equipment_repair_replacement_unit_cost']),
        'vehicle_repair_number': context['vehicle_repair_number'],
        'vehicle_repair_replacement_unit_cost': context['vehicle_repair_replacement_unit_cost'],
        'vehicle_repair_setup_costs': float(context['vehicle_repair_number']) * float(
            context['vehicle_repair_replacement_unit_cost']),
        'vehicle_repair_annual_cost': float(context['vehicle_repair_number']) * float(
            context['vehicle_repair_replacement_unit_cost']),
        'crush_survey_repair_number': context['crush_survey_repair_number'],
        'crush_survey_repair_replacement_unit_cost': context['crush_survey_repair_replacement_unit_cost'],
        'crush_survey_repair_setup_costs': float(context['crush_survey_repair_number']) * float(
            context['crush_survey_repair_replacement_unit_cost']),
        'crush_survey_repair_annual_cost': float(context['crush_survey_repair_number']) * float(
            context['crush_survey_repair_replacement_unit_cost']),
        'electricity_number': context['electricity_number'],
        'electricity_replacement_unit_cost': context['electricity_replacement_unit_cost'],
        'electricity_setup_costs': float(context['electricity_number']) * float(
            context['electricity_replacement_unit_cost']),
        'electricity_annual_cost': float(context['electricity_number']) * float(
            context['electricity_replacement_unit_cost']),
        'setup_capital_total_cost': (float(context['surveillance_land_cruisers_number']) * float(
            context['surveillance_land_cruisers_replacement_unit_cost'])) +
                                    (float(context['supervisor_land_cruisers_number']) * float(
                                        context['supervisor_land_cruisers_replacement_unit_cost'])) +
                                    (float(context['10ml_auto_syringes_number']) * float(
                                        context['10ml_auto_syringes_replacement_unit_cost'])) +
                                    (float(context['30ml_auto_syringes_number']) * float(
                                        context['30ml_auto_syringes_replacement_unit_cost'])) +
                                    (float(context['50ml_auto_syringes_number']) * float(
                                        context['50ml_auto_syringes_replacement_unit_cost'])) +
                                    (float(context['camping_equipment_number']) * float(
                                        context['camping_equipment_replacement_unit_cost'])) +
                                    (float(context['refrigerator_number']) * float(
                                        context['refrigerator_replacement_unit_cost'])) +
                                    (float(context['offices_number']) * float(
                                        context['offices_replacement_unit_cost'])) +
                                    (float(context['freezers_number']) * float(
                                        context['freezers_replacement_unit_cost'])) +
                                    (float(context['gas_cylinder_number']) * float(
                                        context['gas_cylinder_replacement_unit_cost'])) +
                                    (float(context['crushes_number']) * float(
                                        context['crushes_replacement_unit_cost'])) +
                                    (float(context['tally_counters_number']) * float(
                                        context['tally_counters_replacement_unit_cost'])) +
                                    (float(context['generators_number']) * float(
                                        context['generators_replacement_unit_cost'])) +
                                    (float(context['ice_maker_number']) * float(
                                        context['ice_maker_replacement_unit_cost'])) +
                                    (float(context['ear_notchers_number']) * float(
                                        context['ear_notchers_replacement_unit_cost'])) +
                                    (float(context['vaccine_production_unit_number']) * float(
                                        context['vaccine_production_unit_replacement_unit_cost'])) +
                                    (float(context['diagnostic_labs_number']) * float(
                                        context['diagnostic_labs_replacement_unit_cost'])) +
                                    (float(context['equipment_repair_number']) * float(
                                        context['equipment_repair_replacement_unit_cost'])) +
                                    (float(context['vehicle_repair_number']) * float(
                                        context['vehicle_repair_replacement_unit_cost'])) +
                                    (float(context['crush_survey_repair_number']) * float(
                                        context['crush_survey_repair_replacement_unit_cost'])) +
                                    (float(context['electricity_number']) * float(
                                        context['electricity_replacement_unit_cost'])),

        'annual_capital_total_cost': (float(context['surveillance_land_cruisers_number']) * ((float(
            context['surveillance_land_cruisers_replacement_unit_cost']) - float(
            context['surveillance_land_cruisers_salvage_value'])) / float(
            context['surveillance_land_cruisers_productive_lifespan']))) +
                                     (float(context['supervisor_land_cruisers_number']) * ((float(
                                         context['supervisor_land_cruisers_replacement_unit_cost']) - float(
                                         context['supervisor_land_cruisers_salvage_value'])) / float(
                                         context['supervisor_land_cruisers_productive_lifespan']))) +
                                     (float(context['10ml_auto_syringes_number']) * ((float(
                                         context['10ml_auto_syringes_replacement_unit_cost']) - float(
                                         context['10ml_auto_syringes_salvage_value'])) / float(
                                         context['10ml_auto_syringes_productive_lifespan']))) +
                                     (float(context['30ml_auto_syringes_number']) * ((float(
                                         context['30ml_auto_syringes_replacement_unit_cost']) - float(
                                         context['30ml_auto_syringes_salvage_value'])) / float(
                                         context['30ml_auto_syringes_productive_lifespan']))) +
                                     (float(context['50ml_auto_syringes_number']) * ((float(
                                         context['50ml_auto_syringes_replacement_unit_cost']) - float(
                                         context['50ml_auto_syringes_salvage_value'])) / float(
                                         context['50ml_auto_syringes_productive_lifespan']))) +
                                     (float(context['camping_equipment_number']) * ((float(
                                         context['camping_equipment_replacement_unit_cost']) - float(
                                         context['camping_equipment_salvage_value'])) / float(
                                         context['camping_equipment_productive_lifespan']))) +
                                     (float(context['refrigerator_number']) * ((float(
                                         context['refrigerator_replacement_unit_cost']) - float(
                                         context['refrigerator_salvage_value'])) / float(
                                         context['refrigerator_productive_lifespan']))) +
                                     (float(context['offices_number']) * ((float(
                                         context['offices_replacement_unit_cost']) - float(
                                         context['offices_salvage_value'])) / float(
                                         context['offices_productive_lifespan']))) +
                                     (float(context['freezers_number']) * ((float(
                                         context['freezers_replacement_unit_cost']) - float(
                                         context['freezers_salvage_value'])) / float(
                                         context['freezers_productive_lifespan']))) +
                                     (float(context['gas_cylinder_number']) * ((float(
                                         context['gas_cylinder_replacement_unit_cost']) - float(
                                         context['gas_cylinder_salvage_value'])) / float(
                                         context['gas_cylinder_productive_lifespan']))) +
                                     (float(context['crushes_number']) * ((float(
                                         context['crushes_replacement_unit_cost']) - float(
                                         context['crushes_salvage_value'])) / float(
                                         context['crushes_productive_lifespan']))) +
                                     (float(context['tally_counters_number']) * ((float(
                                         context['tally_counters_replacement_unit_cost']) - float(
                                         context['tally_counters_salvage_value'])) / float(
                                         context['tally_counters_productive_lifespan']))) +
                                     (float(context['generators_number']) * ((float(
                                         context['generators_replacement_unit_cost']) - float(
                                         context['generators_salvage_value'])) / float(
                                         context['generators_productive_lifespan']))) +
                                     (float(context['ice_maker_number']) * ((float(
                                         context['ice_maker_replacement_unit_cost']) - float(
                                         context['ice_maker_salvage_value'])) / float(
                                         context['ice_maker_productive_lifespan']))) +
                                     (float(context['ear_notchers_number']) * ((float(
                                         context['ear_notchers_replacement_unit_cost']) - float(
                                         context['ear_notchers_salvage_value'])) / float(
                                         context['ear_notchers_productive_lifespan']))) +
                                     (float(context['vaccine_production_unit_number']) * ((float(
                                         context['vaccine_production_unit_replacement_unit_cost']) - float(
                                         context['vaccine_production_unit_salvage_value'])) / float(
                                         context['vaccine_production_unit_productive_lifespan']))) +
                                     (float(context['diagnostic_labs_number']) * ((float(
                                         context['diagnostic_labs_replacement_unit_cost']) - float(
                                         context['diagnostic_labs_salvage_value'])) / float(
                                         context['diagnostic_labs_productive_lifespan']))) +
                                     (float(context['equipment_repair_number']) * float(
                                         context['equipment_repair_replacement_unit_cost'])) +
                                     (float(context['vehicle_repair_number']) * float(
                                         context['vehicle_repair_replacement_unit_cost'])) +
                                     (float(context['crush_survey_repair_number']) * float(
                                         context['crush_survey_repair_replacement_unit_cost'])) +
                                     (float(context['electricity_number']) * float(
                                         context['electricity_replacement_unit_cost'])),
    }

    return render(request,'capital_costs.html',context2)

def total_annual_cost(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_total_annual_cost_collection = rvf_db['total_annual_cost']
    rvf_early_detection_collection = rvf_db['early_detection']
    rvf_passive_surveillance_collection = rvf_db['passive_surveillance']
    rvf_active_surveillance_collection = rvf_db['active_surveillance']
    rvf_lab_diagnosis_collection = rvf_db['lab_diagnosis']
    rvf_coord_and_comm_cost_collection = rvf_db['coord_and_comm']
    rvf_movement_control_cost_collection = rvf_db['movement_control']
    rvf_strategic_vaccination_cost_collection = rvf_db['strategic_vaccination']
    rvf_personnel_cost_collection = rvf_db['salary_allowances']
    rvf_capital_cost_collection = rvf_db['capital_costs']

    context = {
        'early_detection_cost_ksh': 0,
        'early_detection_cost_usd': 0,
        'passive_surveillance_cost_ksh': 0,
        'passive_surveillance_cost_usd': 0,
        'active_surveillance_cost_ksh': 0,
        'active_surveillance_cost_usd': 0,
        'lab_diagnosis_cost_ksh': 0,
        'lab_diagnosis_cost_usd': 0,
        'coord_and_comm_cost_ksh': 0,
        'coord_and_comm_cost_usd': 0,
        'movement_control_cost_ksh': 0,
        'movement_control_cost_usd': 0,
        'strategic_vaccination_cost_ksh': 0,
        'strategic_vaccination_cost_usd': 0,
        'personnel_cost_ksh': 0,
        'personnel_cost_usd': 0,
        'capital_cost_ksh': 0,
        'capital_cost_usd': 0,
        'total_cost_ksh': 0,
        'total_cost_usd': 0,
        'livestock_sam_multiplier_total': 0,
        '2010GDP_contribution_total': 0,
        'household_livestock_sam_multiplier_multiple': 0,
        'household_sam_multiplier_2010GDP': 0,
    }

    if (request.method == "POST"):
        early_detection_cost_ksh = request.POST['early_detection_cost_ksh']
        early_detection_cost_usd = request.POST['early_detection_cost_usd']
        passive_surveillance_ksh = request.POST['passive_surveillance_ksh']
        passive_surveillance_usd = request.POST['passive_surveillance_usd']
        active_surveillance_ksh = request.POST['active_surveillance_ksh']
        active_surveillance_usd = request.POST['active_surveillance_usd']
        lab_diagnosis_cost_ksh = request.POST['lab_diagnosis_cost_ksh']
        lab_diagnosis_cost_usd = request.POST['lab_diagnosis_cost_usd']
        coord_and_comm_cost_ksh = request.POST['coord_and_comm_cost_ksh']
        coord_and_comm_cost_usd = request.POST['coord_and_comm_cost_usd']
        movement_control_cost_ksh = request.POST['movement_control_cost_ksh']
        movement_control_cost_usd = request.POST['movement_control_cost_usd']
        strategic_vaccination_cost_ksh = request.POST['strategic_vaccination_cost_ksh']
        strategic_vaccination_cost_usd = request.POST['strategic_vaccination_cost_usd']
        personnel_cost_ksh = request.POST['personnel_cost_ksh']
        personnel_cost_usd = request.POST['personnel_cost_usd']
        capital_cost_ksh = request.POST['capital_cost_ksh']
        capital_cost_usd = request.POST['capital_cost_usd']
        total_cost_ksh = request.POST['total_cost_ksh']
        total_cost_usd = request.POST['total_cost_usd']
        livestock_sam_multiplier_total = request.POST['livestock_sam_multiplier_total']
        _2010GDP_contribution_total = request.POST['2010GDP_contribution_total']
        household_livestock_sam_multiplier_multiple = request.POST['household_livestock_sam_multiplier_multiple']
        household_sam_multiplier_2010GDP = request.POST['household_sam_multiplier_2010GDP']

        x = rvf_total_annual_cost_collection.insert_one({
            'early_detection_cost_ksh': early_detection_cost_ksh,
            'early_detection_cost_usd': float(early_detection_cost_ksh) / 100,
            'passive_surveillance_ksh': passive_surveillance_ksh,
            'passive_surveillance_usd': float(passive_surveillance_ksh) / 100,
            'active_surveillance_ksh': active_surveillance_ksh,
            'active_surveillance_usd': float(active_surveillance_ksh) / 100,
            'lab_diagnosis_cost_ksh': lab_diagnosis_cost_ksh,
            'lab_diagnosis_cost_usd': float(lab_diagnosis_cost_ksh) / 100,
            'coord_and_comm_cost_ksh': coord_and_comm_cost_ksh,
            'coord_and_comm_cost_usd': float(coord_and_comm_cost_ksh) / 100,
            'movement_control_cost_ksh': movement_control_cost_ksh,
            'movement_control_cost_usd': float(movement_control_cost_ksh) / 100,
            'strategic_vaccination_cost_ksh': strategic_vaccination_cost_ksh,
            'strategic_vaccination_cost_usd': float(strategic_vaccination_cost_ksh) / 100,
            'personnel_cost_ksh': personnel_cost_ksh,
            'personnel_cost_usd': float(personnel_cost_ksh) / 100,
            'capital_cost_ksh': capital_cost_ksh,
            'capital_cost_usd': float(capital_cost_ksh) / 100,
            'total_cost_ksh': total_cost_ksh,
            'total_cost_usd': total_cost_usd,
            'livestock_sam_multiplier_total': livestock_sam_multiplier_total,
            '2010GDP_contribution_total': _2010GDP_contribution_total,
            'household_livestock_sam_multiplier_multiple': household_livestock_sam_multiplier_multiple,
            'household_sam_multiplier_2010GDP': household_sam_multiplier_2010GDP,
        })

    for x in rvf_total_annual_cost_collection.find({}, {"_id": 0}):
        context = x

    for y in rvf_lab_diagnosis_collection.find({}, {"_id": 0}):
         lab_diagnosis_context = y

    for early in rvf_early_detection_collection.find({}, {"_id": 0}):
         early_detection_context = early

    for passive in rvf_passive_surveillance_collection.find({}, {"_id": 0}):
         passive_surveillance_context = passive

    for active in rvf_active_surveillance_collection.find({}, {"_id": 0}):
         active_surveillance_context = active

    for coord in rvf_coord_and_comm_cost_collection.find({}, {"_id": 0}):
         coord_and_comm_cost_context = coord

    for movement in rvf_movement_control_cost_collection.find({}, {"_id": 0}):
         movement_control_cost_context = movement

    for strategic in rvf_strategic_vaccination_cost_collection.find({}, {"_id": 0}):
         strategic_vaccination_cost_context = strategic

    for personnel in rvf_personnel_cost_collection.find({}, {"_id": 0}):
         personnel_cost_context = personnel

    for capital in rvf_capital_cost_collection.find({}, {"_id": 0}):
         capital_cost_context = capital

    context2 = {
        'early_detection_cost_ksh': early_detection_context['early_detection_total_cost'],
        'early_detection_cost_usd': float(early_detection_context['early_detection_total_cost']) / 100,
        'passive_surveillance_ksh': passive_surveillance_context['passive_surveillance_total_annual_cost'],
        'passive_surveillance_usd': float(passive_surveillance_context['passive_surveillance_total_annual_cost']) / 100,
        'active_surveillance_ksh': active_surveillance_context['active_surveillance_total_annual_cost'],
        'active_surveillance_usd': float(active_surveillance_context['active_surveillance_total_annual_cost']) / 100,
        'lab_diagnosis_cost_ksh': lab_diagnosis_context['lab_diagnosis_total'],
        'lab_diagnosis_cost_usd': float(lab_diagnosis_context['lab_diagnosis_total']) / 100,
        'coord_and_comm_cost_ksh': coord_and_comm_cost_context['early_detection_total_cost'],
        'coord_and_comm_cost_usd': float(coord_and_comm_cost_context['early_detection_total_cost']) / 100,
        'movement_control_cost_ksh': movement_control_cost_context['movement_control_total_cost'],
        'movement_control_cost_usd': float(movement_control_cost_context['movement_control_total_cost']) / 100,
        'strategic_vaccination_cost_ksh': strategic_vaccination_cost_context['strategic_vaccination_total'],
        'strategic_vaccination_cost_usd': float(
            strategic_vaccination_cost_context['strategic_vaccination_total']) / 100,
        'personnel_cost_ksh': personnel_cost_context['salary_allowance_total'],
        'personnel_cost_usd': float(personnel_cost_context['salary_allowance_total']) / 100,
        'capital_cost_ksh': capital_cost_context['annual_capital_total_cost'],
        'capital_cost_usd': float(capital_cost_context['annual_capital_total_cost']) / 100,
        'total_cost_ksh': float(early_detection_context['early_detection_total_cost']) +
                          float(passive_surveillance_context['passive_surveillance_total_annual_cost']) +
                          float(active_surveillance_context['active_surveillance_total_annual_cost']) +
                          float(lab_diagnosis_context['lab_diagnosis_total']) +
                          float(coord_and_comm_cost_context['early_detection_total_cost']) +
                          float(movement_control_cost_context['movement_control_total_cost']) +
                          float(strategic_vaccination_cost_context['strategic_vaccination_total']) +
                          float(personnel_cost_context['salary_allowance_total']) +
                          float(capital_cost_context['annual_capital_total_cost']),
        'total_cost_usd': (float(early_detection_context['early_detection_total_cost']) / 100) +
                          (float(passive_surveillance_context['passive_surveillance_total_annual_cost']) / 100) +
                          (float(active_surveillance_context['active_surveillance_total_annual_cost']) / 100) +
                          (float(lab_diagnosis_context['lab_diagnosis_total']) / 100) +
                          (float(coord_and_comm_cost_context['early_detection_total_cost']) / 100) +
                          (float(movement_control_cost_context['movement_control_total_cost']) / 100) +
                          (float(strategic_vaccination_cost_context['strategic_vaccination_total']) / 100) +
                          (float(personnel_cost_context['salary_allowance_total']) / 100) +
                          (float(capital_cost_context['annual_capital_total_cost']) / 100),

        'livestock_sam_multiplier_total': (float(early_detection_context['early_detection_total_cost']) +
                                           float(
                                               passive_surveillance_context['passive_surveillance_total_annual_cost']) +
                                           float(active_surveillance_context['active_surveillance_total_annual_cost']) +
                                           float(lab_diagnosis_context['lab_diagnosis_total']) +
                                           float(coord_and_comm_cost_context['early_detection_total_cost']) +
                                           float(movement_control_cost_context['movement_control_total_cost']) +
                                           float(strategic_vaccination_cost_context['strategic_vaccination_total']) +
                                           float(personnel_cost_context['salary_allowance_total']) +
                                           float(capital_cost_context['annual_capital_total_cost'])) * 2.89,

        '2010GDP_contribution_total': (((float(early_detection_context['early_detection_total_cost']) +
                                         float(passive_surveillance_context['passive_surveillance_total_annual_cost']) +
                                         float(active_surveillance_context['active_surveillance_total_annual_cost']) +
                                         float(lab_diagnosis_context['lab_diagnosis_total']) +
                                         float(coord_and_comm_cost_context['early_detection_total_cost']) +
                                         float(movement_control_cost_context['movement_control_total_cost']) +
                                         float(strategic_vaccination_cost_context['strategic_vaccination_total']) +
                                         float(personnel_cost_context['salary_allowance_total']) +
                                         float(capital_cost_context[
                                                   'annual_capital_total_cost'])) * 2.89) / 1086571000000) * 100,
        'household_livestock_sam_multiplier_multiple': (float(early_detection_context['early_detection_total_cost']) +
                                                        float(passive_surveillance_context[
                                                                  'passive_surveillance_total_annual_cost']) +
                                                        float(active_surveillance_context[
                                                                  'active_surveillance_total_annual_cost']) +
                                                        float(lab_diagnosis_context['lab_diagnosis_total']) +
                                                        float(
                                                            coord_and_comm_cost_context['early_detection_total_cost']) +
                                                        float(movement_control_cost_context[
                                                                  'movement_control_total_cost']) +
                                                        float(strategic_vaccination_cost_context[
                                                                  'strategic_vaccination_total']) +
                                                        float(personnel_cost_context['salary_allowance_total']) +
                                                        float(
                                                            capital_cost_context['annual_capital_total_cost'])) * 1.22,

        'household_sam_multiplier_2010GDP': (((float(early_detection_context['early_detection_total_cost']) +
                                               float(passive_surveillance_context[
                                                         'passive_surveillance_total_annual_cost']) +
                                               float(active_surveillance_context[
                                                         'active_surveillance_total_annual_cost']) +
                                               float(lab_diagnosis_context['lab_diagnosis_total']) +
                                               float(coord_and_comm_cost_context['early_detection_total_cost']) +
                                               float(movement_control_cost_context['movement_control_total_cost']) +
                                               float(
                                                   strategic_vaccination_cost_context['strategic_vaccination_total']) +
                                               float(personnel_cost_context['salary_allowance_total']) +
                                               float(capital_cost_context[
                                                         'annual_capital_total_cost'])) * 1.22) / 1086571000000) * 100,
    }

    return render(request,'total_annual_cost.html',context2)

def CBA(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_CBA_collection = rvf_db['CBA']
    rvf_capital_cost_collection = rvf_db['capital_costs']
    rvf_total_annual_cost_collection = rvf_db['total_annual_cost']

    context = {
        'ZDU_setup_costs_year': 0,
        'with_health_programme_benefits_year_0': 0,
        'with_health_programme_benefits_year_1': 0,
        'with_health_programme_benefits_year_2': 0,
        'with_health_programme_benefits_year_3': 0,
        'with_health_programme_benefits_year_4': 0,
        'with_health_programme_benefits_year_5': 0,
        'with_health_programme_benefits_year_6': 0,
        'with_health_programme_benefits_year_7': 0,
        'with_health_programme_benefits_year_8': 0,
        'with_health_programme_benefits_year_9': 0,
        'with_health_programme_benefits_year_10': 0,
        'with_health_programme_benefits_year_11': 0,
        'with_health_programme_benefits_year_12': 0,
        'with_health_programme_benefits_year_13': 0,
        'with_health_programme_benefits_year_14': 0,
        'with_health_programme_benefits_year_15': 0,
        'with_health_programme_benefits_year_16': 0,
        'with_health_programme_benefits_year_17': 0,
        'with_health_programme_benefits_year_18': 0,
        'with_health_programme_benefits_year_19': 0,
        'with_health_programme_benefits_year_20': 0,

        'without_health_programme_benefits_year_0': 0,
        'without_health_programme_benefits_year_1': 0,
        'without_health_programme_benefits_year_2': 0,
        'without_health_programme_benefits_year_3': 0,
        'without_health_programme_benefits_year_4': 0,
        'without_health_programme_benefits_year_5': 0,
        'without_health_programme_benefits_year_6': 0,
        'without_health_programme_benefits_year_7': 0,
        'without_health_programme_benefits_year_8': 0,
        'without_health_programme_benefits_year_9': 0,
        'without_health_programme_benefits_year_10': 0,
        'without_health_programme_benefits_year_11': 0,
        'without_health_programme_benefits_year_12': 0,
        'without_health_programme_benefits_year_13': 0,
        'without_health_programme_benefits_year_14': 0,
        'without_health_programme_benefits_year_15': 0,
        'without_health_programme_benefits_year_16': 0,
        'without_health_programme_benefits_year_17': 0,
        'without_health_programme_benefits_year_18': 0,
        'without_health_programme_benefits_year_19': 0,
        'without_health_programme_benefits_year_20': 0,

        'incremental_benefits_year_0': 0,
        'incremental_benefits_year_1': 0,
        'incremental_benefits_year_2': 0,
        'incremental_benefits_year_3': 0,
        'incremental_benefits_year_4': 0,
        'incremental_benefits_year_5': 0,
        'incremental_benefits_year_6': 0,
        'incremental_benefits_year_7': 0,
        'incremental_benefits_year_8': 0,
        'incremental_benefits_year_9': 0,
        'incremental_benefits_year_10': 0,
        'incremental_benefits_year_11': 0,
        'incremental_benefits_year_12': 0,
        'incremental_benefits_year_13': 0,
        'incremental_benefits_year_14': 0,
        'incremental_benefits_year_15': 0,
        'incremental_benefits_year_16': 0,
        'incremental_benefits_year_17': 0,
        'incremental_benefits_year_18': 0,
        'incremental_benefits_year_19': 0,
        'incremental_benefits_year_20': 0,

        'discounted_benefits_year_0': 0,
        'discounted_benefits_year_1': 0,
        'discounted_benefits_year_2': 0,
        'discounted_benefits_year_3': 0,
        'discounted_benefits_year_4': 0,
        'discounted_benefits_year_5': 0,
        'discounted_benefits_year_6': 0,
        'discounted_benefits_year_7': 0,
        'discounted_benefits_year_8': 0,
        'discounted_benefits_year_9': 0,
        'discounted_benefits_year_10': 0,
        'discounted_benefits_year_11': 0,
        'discounted_benefits_year_12': 0,
        'discounted_benefits_year_13': 0,
        'discounted_benefits_year_14': 0,
        'discounted_benefits_year_15': 0,
        'discounted_benefits_year_16': 0,
        'discounted_benefits_year_17': 0,
        'discounted_benefits_year_18': 0,
        'discounted_benefits_year_19': 0,
        'discounted_benefits_year_20': 0,

        'annual_programme_costs_year_0': 0,
        'annual_programme_costs_year_1': 0,
        'annual_programme_costs_year_2': 0,
        'annual_programme_costs_year_3': 0,
        'annual_programme_costs_year_4': 0,
        'annual_programme_costs_year_5': 0,
        'annual_programme_costs_year_6': 0,
        'annual_programme_costs_year_7': 0,
        'annual_programme_costs_year_8': 0,
        'annual_programme_costs_year_9': 0,
        'annual_programme_costs_year_10': 0,
        'annual_programme_costs_year_11': 0,
        'annual_programme_costs_year_12': 0,
        'annual_programme_costs_year_13': 0,
        'annual_programme_costs_year_14': 0,
        'annual_programme_costs_year_15': 0,
        'annual_programme_costs_year_16': 0,
        'annual_programme_costs_year_17': 0,
        'annual_programme_costs_year_18': 0,
        'annual_programme_costs_year_19': 0,
        'annual_programme_costs_year_20': 0,

        'discounted_costs_year_0': 0,
        'discounted_costs_year_1': 0,
        'discounted_costs_year_2': 0,
        'discounted_costs_year_3': 0,
        'discounted_costs_year_4': 0,
        'discounted_costs_year_5': 0,
        'discounted_costs_year_6': 0,
        'discounted_costs_year_7': 0,
        'discounted_costs_year_8': 0,
        'discounted_costs_year_9': 0,
        'discounted_costs_year_10': 0,
        'discounted_costs_year_11': 0,
        'discounted_costs_year_12': 0,
        'discounted_costs_year_13': 0,
        'discounted_costs_year_14': 0,
        'discounted_costs_year_15': 0,
        'discounted_costs_year_16': 0,
        'discounted_costs_year_17': 0,
        'discounted_costs_year_18': 0,
        'discounted_costs_year_19': 0,
        'discounted_costs_year_20': 0,

        'discounted_net_benefits_year_0': 0,
        'discounted_net_benefits_year_1': 0,
        'discounted_net_benefits_year_2': 0,
        'discounted_net_benefits_year_3': 0,
        'discounted_net_benefits_year_4': 0,
        'discounted_net_benefits_year_5': 0,
        'discounted_net_benefits_year_6': 0,
        'discounted_net_benefits_year_7': 0,
        'discounted_net_benefits_year_8': 0,
        'discounted_net_benefits_year_9': 0,
        'discounted_net_benefits_year_10': 0,
        'discounted_net_benefits_year_11': 0,
        'discounted_net_benefits_year_12': 0,
        'discounted_net_benefits_year_13': 0,
        'discounted_net_benefits_year_14': 0,
        'discounted_net_benefits_year_15': 0,
        'discounted_net_benefits_year_16': 0,
        'discounted_net_benefits_year_17': 0,
        'discounted_net_benefits_year_18': 0,
        'discounted_net_benefits_year_19': 0,
        'discounted_net_benefits_year_20': 0,

        'NPV_year': 0,
        'BCR_year': 0,
        'IRR_year': 0,

        'increase_in_annual_programme_costs_year_0': 0,
        'increase_in_annual_programme_costs_year_1': 0,
        'increase_in_annual_programme_costs_year_2': 0,
        'increase_in_annual_programme_costs_year_3': 0,
        'increase_in_annual_programme_costs_year_4': 0,
        'increase_in_annual_programme_costs_year_5': 0,
        'increase_in_annual_programme_costs_year_6': 0,
        'increase_in_annual_programme_costs_year_7': 0,
        'increase_in_annual_programme_costs_year_8': 0,
        'increase_in_annual_programme_costs_year_9': 0,
        'increase_in_annual_programme_costs_year_10': 0,
        'increase_in_annual_programme_costs_year_11': 0,
        'increase_in_annual_programme_costs_year_12': 0,
        'increase_in_annual_programme_costs_year_13': 0,
        'increase_in_annual_programme_costs_year_14': 0,
        'increase_in_annual_programme_costs_year_15': 0,
        'increase_in_annual_programme_costs_year_16': 0,
        'increase_in_annual_programme_costs_year_17': 0,
        'increase_in_annual_programme_costs_year_18': 0,
        'increase_in_annual_programme_costs_year_19': 0,
        'increase_in_annual_programme_costs_year_20': 0,

        'extra_discounted_costs_year_0': 0,
        'extra_discounted_costs_year_1': 0,
        'extra_discounted_costs_year_2': 0,
        'extra_discounted_costs_year_3': 0,
        'extra_discounted_costs_year_4': 0,
        'extra_discounted_costs_year_5': 0,
        'extra_discounted_costs_year_6': 0,
        'extra_discounted_costs_year_7': 0,
        'extra_discounted_costs_year_8': 0,
        'extra_discounted_costs_year_9': 0,
        'extra_discounted_costs_year_10': 0,
        'extra_discounted_costs_year_11': 0,
        'extra_discounted_costs_year_12': 0,
        'extra_discounted_costs_year_13': 0,
        'extra_discounted_costs_year_14': 0,
        'extra_discounted_costs_year_15': 0,
        'extra_discounted_costs_year_16': 0,
        'extra_discounted_costs_year_17': 0,
        'extra_discounted_costs_year_18': 0,
        'extra_discounted_costs_year_19': 0,
        'extra_discounted_costs_year_20': 0,

        'extra_NPV_year': 0,
        'extra_BCR_year': 0,
    }

    if (request.method == "POST"):
        ZDU_setup_costs_year = request.POST['ZDU_setup_costs_year']
        with_health_programme_benefits_year_0 = request.POST['with_health_programme_benefits_year_0']
        with_health_programme_benefits_year_1 = request.POST['with_health_programme_benefits_year_1']
        with_health_programme_benefits_year_2 = request.POST['with_health_programme_benefits_year_2']
        with_health_programme_benefits_year_3 = request.POST['with_health_programme_benefits_year_3']
        with_health_programme_benefits_year_4 = request.POST['with_health_programme_benefits_year_4']
        with_health_programme_benefits_year_5 = request.POST['with_health_programme_benefits_year_5']
        with_health_programme_benefits_year_6 = request.POST['with_health_programme_benefits_year_6']
        with_health_programme_benefits_year_7 = request.POST['with_health_programme_benefits_year_7']
        with_health_programme_benefits_year_8 = request.POST['with_health_programme_benefits_year_8']
        with_health_programme_benefits_year_9 = request.POST['with_health_programme_benefits_year_9']
        with_health_programme_benefits_year_10 = request.POST['with_health_programme_benefits_year_10']
        with_health_programme_benefits_year_11 = request.POST['with_health_programme_benefits_year_11']
        with_health_programme_benefits_year_12 = request.POST['with_health_programme_benefits_year_12']
        with_health_programme_benefits_year_13 = request.POST['with_health_programme_benefits_year_13']
        with_health_programme_benefits_year_14 = request.POST['with_health_programme_benefits_year_14']
        with_health_programme_benefits_year_15 = request.POST['with_health_programme_benefits_year_15']
        with_health_programme_benefits_year_16 = request.POST['with_health_programme_benefits_year_16']
        with_health_programme_benefits_year_17 = request.POST['with_health_programme_benefits_year_17']
        with_health_programme_benefits_year_18 = request.POST['with_health_programme_benefits_year_18']
        with_health_programme_benefits_year_19 = request.POST['with_health_programme_benefits_year_19']
        with_health_programme_benefits_year_20 = request.POST['with_health_programme_benefits_year_20']
        without_health_programme_benefits_year_0 = request.POST['without_health_programme_benefits_year_0']
        without_health_programme_benefits_year_1 = request.POST['without_health_programme_benefits_year_1']
        without_health_programme_benefits_year_2 = request.POST['without_health_programme_benefits_year_2']
        without_health_programme_benefits_year_3 = request.POST['without_health_programme_benefits_year_3']
        without_health_programme_benefits_year_4 = request.POST['without_health_programme_benefits_year_4']
        without_health_programme_benefits_year_5 = request.POST['without_health_programme_benefits_year_5']
        without_health_programme_benefits_year_6 = request.POST['without_health_programme_benefits_year_6']
        without_health_programme_benefits_year_7 = request.POST['without_health_programme_benefits_year_7']
        without_health_programme_benefits_year_8 = request.POST['without_health_programme_benefits_year_8']
        without_health_programme_benefits_year_9 = request.POST['without_health_programme_benefits_year_9']
        without_health_programme_benefits_year_10 = request.POST['without_health_programme_benefits_year_10']
        without_health_programme_benefits_year_11 = request.POST['without_health_programme_benefits_year_11']
        without_health_programme_benefits_year_12 = request.POST['without_health_programme_benefits_year_12']
        without_health_programme_benefits_year_13 = request.POST['without_health_programme_benefits_year_13']
        without_health_programme_benefits_year_14 = request.POST['without_health_programme_benefits_year_14']
        without_health_programme_benefits_year_15 = request.POST['without_health_programme_benefits_year_15']
        without_health_programme_benefits_year_16 = request.POST['without_health_programme_benefits_year_16']
        without_health_programme_benefits_year_17 = request.POST['without_health_programme_benefits_year_17']
        without_health_programme_benefits_year_18 = request.POST['without_health_programme_benefits_year_18']
        without_health_programme_benefits_year_19 = request.POST['without_health_programme_benefits_year_19']
        without_health_programme_benefits_year_20 = request.POST['without_health_programme_benefits_year_20']


        incremental_benefits_year_0 = request.POST['incremental_benefits_year_0']
        incremental_benefits_year_1 = request.POST['incremental_benefits_year_1']
        incremental_benefits_year_2 = request.POST['incremental_benefits_year_2']
        incremental_benefits_year_3 = request.POST['incremental_benefits_year_3']
        incremental_benefits_year_4 = request.POST['incremental_benefits_year_4']
        incremental_benefits_year_5 = request.POST['incremental_benefits_year_5']
        incremental_benefits_year_6 = request.POST['incremental_benefits_year_6']
        incremental_benefits_year_7 = request.POST['incremental_benefits_year_7']
        incremental_benefits_year_8 = request.POST['incremental_benefits_year_8']
        incremental_benefits_year_9 = request.POST['incremental_benefits_year_9']
        incremental_benefits_year_10 = request.POST['incremental_benefits_year_10']
        incremental_benefits_year_11 = request.POST['incremental_benefits_year_11']
        incremental_benefits_year_12 = request.POST['incremental_benefits_year_12']
        incremental_benefits_year_13 = request.POST['incremental_benefits_year_13']
        incremental_benefits_year_14 = request.POST['incremental_benefits_year_14']
        incremental_benefits_year_15 = request.POST['incremental_benefits_year_15']
        incremental_benefits_year_16 = request.POST['incremental_benefits_year_16']
        incremental_benefits_year_17 = request.POST['incremental_benefits_year_17']
        incremental_benefits_year_18 = request.POST['incremental_benefits_year_18']
        incremental_benefits_year_19 = request.POST['incremental_benefits_year_19']
        incremental_benefits_year_20 = request.POST['incremental_benefits_year_20']
        discounted_benefits_year_0 = request.POST['discounted_benefits_year_0']
        discounted_benefits_year_1 = request.POST['discounted_benefits_year_1']
        discounted_benefits_year_2 = request.POST['discounted_benefits_year_2']
        discounted_benefits_year_3 = request.POST['discounted_benefits_year_3']
        discounted_benefits_year_4 = request.POST['discounted_benefits_year_4']
        discounted_benefits_year_5 = request.POST['discounted_benefits_year_5']
        discounted_benefits_year_6 = request.POST['discounted_benefits_year_6']
        discounted_benefits_year_7 = request.POST['discounted_benefits_year_7']
        discounted_benefits_year_8 = request.POST['discounted_benefits_year_8']
        discounted_benefits_year_9 = request.POST['discounted_benefits_year_9']
        discounted_benefits_year_10 = request.POST['discounted_benefits_year_10']
        discounted_benefits_year_11 = request.POST['discounted_benefits_year_11']
        discounted_benefits_year_12 = request.POST['discounted_benefits_year_12']
        discounted_benefits_year_13 = request.POST['discounted_benefits_year_13']
        discounted_benefits_year_14 = request.POST['discounted_benefits_year_14']
        discounted_benefits_year_15 = request.POST['discounted_benefits_year_15']
        discounted_benefits_year_16 = request.POST['discounted_benefits_year_16']
        discounted_benefits_year_17 = request.POST['discounted_benefits_year_17']
        discounted_benefits_year_18 = request.POST['discounted_benefits_year_18']
        discounted_benefits_year_19 = request.POST['discounted_benefits_year_19']
        discounted_benefits_year_20 = request.POST['discounted_benefits_year_20']
        annual_programme_costs_year_0 = request.POST['annual_programme_costs_year_0']
        annual_programme_costs_year_1 = request.POST['annual_programme_costs_year_1']
        annual_programme_costs_year_2 = request.POST['annual_programme_costs_year_2']
        annual_programme_costs_year_3 = request.POST['annual_programme_costs_year_3']
        annual_programme_costs_year_4 = request.POST['annual_programme_costs_year_4']
        annual_programme_costs_year_5 = request.POST['annual_programme_costs_year_5']
        annual_programme_costs_year_6 = request.POST['annual_programme_costs_year_6']
        annual_programme_costs_year_7 = request.POST['annual_programme_costs_year_7']
        annual_programme_costs_year_8 = request.POST['annual_programme_costs_year_8']
        annual_programme_costs_year_9 = request.POST['annual_programme_costs_year_9']
        annual_programme_costs_year_10 = request.POST['annual_programme_costs_year_10']
        annual_programme_costs_year_11 = request.POST['annual_programme_costs_year_11']
        annual_programme_costs_year_12 = request.POST['annual_programme_costs_year_12']
        annual_programme_costs_year_13 = request.POST['annual_programme_costs_year_13']
        annual_programme_costs_year_14 = request.POST['annual_programme_costs_year_14']
        annual_programme_costs_year_15 = request.POST['annual_programme_costs_year_15']
        annual_programme_costs_year_16 = request.POST['annual_programme_costs_year_16']
        annual_programme_costs_year_17 = request.POST['annual_programme_costs_year_17']
        annual_programme_costs_year_18 = request.POST['annual_programme_costs_year_18']
        annual_programme_costs_year_19 = request.POST['annual_programme_costs_year_19']
        annual_programme_costs_year_20 = request.POST['annual_programme_costs_year_20']
        discounted_costs_year_0 = request.POST['discounted_costs_year_0']
        discounted_costs_year_1 = request.POST['discounted_costs_year_1']
        discounted_costs_year_2 = request.POST['discounted_costs_year_2']
        discounted_costs_year_3 = request.POST['discounted_costs_year_3']
        discounted_costs_year_4 = request.POST['discounted_costs_year_4']
        discounted_costs_year_5 = request.POST['discounted_costs_year_5']
        discounted_costs_year_6 = request.POST['discounted_costs_year_6']
        discounted_costs_year_7 = request.POST['discounted_costs_year_7']
        discounted_costs_year_8 = request.POST['discounted_costs_year_8']
        discounted_costs_year_9 = request.POST['discounted_costs_year_9']
        discounted_costs_year_10 = request.POST['discounted_costs_year_10']
        discounted_costs_year_11 = request.POST['discounted_costs_year_11']
        discounted_costs_year_12 = request.POST['discounted_costs_year_12']
        discounted_costs_year_13 = request.POST['discounted_costs_year_13']
        discounted_costs_year_14 = request.POST['discounted_costs_year_14']
        discounted_costs_year_15 = request.POST['discounted_costs_year_15']
        discounted_costs_year_16 = request.POST['discounted_costs_year_16']
        discounted_costs_year_17 = request.POST['discounted_costs_year_17']
        discounted_costs_year_18 = request.POST['discounted_costs_year_18']
        discounted_costs_year_19 = request.POST['discounted_costs_year_19']
        discounted_costs_year_20 = request.POST['discounted_costs_year_20']
        discounted_net_benefits_year_0 = request.POST['discounted_net_benefits_year_0']
        discounted_net_benefits_year_1 = request.POST['discounted_net_benefits_year_1']
        discounted_net_benefits_year_2 = request.POST['discounted_net_benefits_year_2']
        discounted_net_benefits_year_3 = request.POST['discounted_net_benefits_year_3']
        discounted_net_benefits_year_4 = request.POST['discounted_net_benefits_year_4']
        discounted_net_benefits_year_5 = request.POST['discounted_net_benefits_year_5']
        discounted_net_benefits_year_6 = request.POST['discounted_net_benefits_year_6']
        discounted_net_benefits_year_7 = request.POST['discounted_net_benefits_year_7']
        discounted_net_benefits_year_8 = request.POST['discounted_net_benefits_year_8']
        discounted_net_benefits_year_9 = request.POST['discounted_net_benefits_year_9']
        discounted_net_benefits_year_10 = request.POST['discounted_net_benefits_year_10']
        discounted_net_benefits_year_11 = request.POST['discounted_net_benefits_year_11']
        discounted_net_benefits_year_12 = request.POST['discounted_net_benefits_year_12']
        discounted_net_benefits_year_13 = request.POST['discounted_net_benefits_year_13']
        discounted_net_benefits_year_14 = request.POST['discounted_net_benefits_year_14']
        discounted_net_benefits_year_15 = request.POST['discounted_net_benefits_year_15']
        discounted_net_benefits_year_16 = request.POST['discounted_net_benefits_year_16']
        discounted_net_benefits_year_17 = request.POST['discounted_net_benefits_year_17']
        discounted_net_benefits_year_18 = request.POST['discounted_net_benefits_year_18']
        discounted_net_benefits_year_19 = request.POST['discounted_net_benefits_year_19']
        discounted_net_benefits_year_20 = request.POST['discounted_net_benefits_year_20']
        NPV_year = request.POST['NPV_year']
        BCR_year = request.POST['BCR_year']
        IRR_year = request.POST['IRR_year']
        increase_in_annual_programme_costs_year_0 = request.POST['increase_in_annual_programme_costs_year_0']
        increase_in_annual_programme_costs_year_1 = request.POST['increase_in_annual_programme_costs_year_1']
        increase_in_annual_programme_costs_year_2 = request.POST['increase_in_annual_programme_costs_year_2']
        increase_in_annual_programme_costs_year_3 = request.POST['increase_in_annual_programme_costs_year_3']
        increase_in_annual_programme_costs_year_4 = request.POST['increase_in_annual_programme_costs_year_4']
        increase_in_annual_programme_costs_year_5 = request.POST['increase_in_annual_programme_costs_year_5']
        increase_in_annual_programme_costs_year_6 = request.POST['increase_in_annual_programme_costs_year_6']
        increase_in_annual_programme_costs_year_7 = request.POST['increase_in_annual_programme_costs_year_7']
        increase_in_annual_programme_costs_year_8 = request.POST['increase_in_annual_programme_costs_year_8']
        increase_in_annual_programme_costs_year_9 = request.POST['increase_in_annual_programme_costs_year_9']
        increase_in_annual_programme_costs_year_10 = request.POST['increase_in_annual_programme_costs_year_10']
        increase_in_annual_programme_costs_year_11 = request.POST['increase_in_annual_programme_costs_year_11']
        increase_in_annual_programme_costs_year_12 = request.POST['increase_in_annual_programme_costs_year_12']
        increase_in_annual_programme_costs_year_13 = request.POST['increase_in_annual_programme_costs_year_13']
        increase_in_annual_programme_costs_year_14 = request.POST['increase_in_annual_programme_costs_year_14']
        increase_in_annual_programme_costs_year_15 = request.POST['increase_in_annual_programme_costs_year_15']
        increase_in_annual_programme_costs_year_16 = request.POST['increase_in_annual_programme_costs_year_16']
        increase_in_annual_programme_costs_year_17 = request.POST['increase_in_annual_programme_costs_year_17']
        increase_in_annual_programme_costs_year_18 = request.POST['increase_in_annual_programme_costs_year_18']
        increase_in_annual_programme_costs_year_19 = request.POST['increase_in_annual_programme_costs_year_19']
        increase_in_annual_programme_costs_year_20 = request.POST['increase_in_annual_programme_costs_year_20']
        extra_discounted_costs_year_0 = request.POST['extra_discounted_costs_year_0']
        extra_discounted_costs_year_1 = request.POST['extra_discounted_costs_year_1']
        extra_discounted_costs_year_2 = request.POST['extra_discounted_costs_year_2']
        extra_discounted_costs_year_3 = request.POST['extra_discounted_costs_year_3']
        extra_discounted_costs_year_4 = request.POST['extra_discounted_costs_year_4']
        extra_discounted_costs_year_5 = request.POST['extra_discounted_costs_year_5']
        extra_discounted_costs_year_6 = request.POST['extra_discounted_costs_year_6']
        extra_discounted_costs_year_7 = request.POST['extra_discounted_costs_year_7']
        extra_discounted_costs_year_8 = request.POST['extra_discounted_costs_year_8']
        extra_discounted_costs_year_9 = request.POST['extra_discounted_costs_year_9']
        extra_discounted_costs_year_10 = request.POST['extra_discounted_costs_year_10']
        extra_discounted_costs_year_11 = request.POST['extra_discounted_costs_year_11']
        extra_discounted_costs_year_12 = request.POST['extra_discounted_costs_year_12']
        extra_discounted_costs_year_13 = request.POST['extra_discounted_costs_year_13']
        extra_discounted_costs_year_14 = request.POST['extra_discounted_costs_year_14']
        extra_discounted_costs_year_15 = request.POST['extra_discounted_costs_year_15']
        extra_discounted_costs_year_16 = request.POST['extra_discounted_costs_year_16']
        extra_discounted_costs_year_17 = request.POST['extra_discounted_costs_year_17']
        extra_discounted_costs_year_18 = request.POST['extra_discounted_costs_year_18']
        extra_discounted_costs_year_19 = request.POST['extra_discounted_costs_year_19']
        extra_discounted_costs_year_20 = request.POST['extra_discounted_costs_year_20']
        extra_NPV_year = request.POST['extra_NPV_year']
        extra_BCR_year = request.POST['extra_BCR_year']

        x = rvf_CBA_collection.insert_one({
            'ZDU_setup_costs_year': ZDU_setup_costs_year,
            'with_health_programme_benefits_year_0': with_health_programme_benefits_year_0,
            'with_health_programme_benefits_year_1': with_health_programme_benefits_year_1,
            'with_health_programme_benefits_year_2': with_health_programme_benefits_year_2,
            'with_health_programme_benefits_year_3': with_health_programme_benefits_year_3,
            'with_health_programme_benefits_year_4': with_health_programme_benefits_year_4,
            'with_health_programme_benefits_year_5': with_health_programme_benefits_year_5,
            'with_health_programme_benefits_year_6': with_health_programme_benefits_year_6,
            'with_health_programme_benefits_year_7': with_health_programme_benefits_year_7,
            'with_health_programme_benefits_year_8': with_health_programme_benefits_year_8,
            'with_health_programme_benefits_year_9': with_health_programme_benefits_year_9,
            'with_health_programme_benefits_year_10': with_health_programme_benefits_year_10,
            'with_health_programme_benefits_year_11': with_health_programme_benefits_year_11,
            'with_health_programme_benefits_year_12': with_health_programme_benefits_year_12,
            'with_health_programme_benefits_year_13': with_health_programme_benefits_year_13,
            'with_health_programme_benefits_year_14': with_health_programme_benefits_year_14,
            'with_health_programme_benefits_year_15': with_health_programme_benefits_year_15,
            'with_health_programme_benefits_year_16': with_health_programme_benefits_year_16,
            'with_health_programme_benefits_year_17': with_health_programme_benefits_year_17,
            'with_health_programme_benefits_year_18': with_health_programme_benefits_year_18,
            'with_health_programme_benefits_year_19': with_health_programme_benefits_year_19,
            'with_health_programme_benefits_year_20': with_health_programme_benefits_year_20,
            'without_health_programme_benefits_year_0': without_health_programme_benefits_year_0,
            'without_health_programme_benefits_year_1': without_health_programme_benefits_year_1,
            'without_health_programme_benefits_year_2': without_health_programme_benefits_year_2,
            'without_health_programme_benefits_year_3': without_health_programme_benefits_year_3,
            'without_health_programme_benefits_year_4': without_health_programme_benefits_year_4,
            'without_health_programme_benefits_year_5': without_health_programme_benefits_year_5,
            'without_health_programme_benefits_year_6': without_health_programme_benefits_year_6,
            'without_health_programme_benefits_year_7': without_health_programme_benefits_year_7,
            'without_health_programme_benefits_year_8': without_health_programme_benefits_year_8,
            'without_health_programme_benefits_year_9': without_health_programme_benefits_year_9,
            'without_health_programme_benefits_year_10': without_health_programme_benefits_year_10,
            'without_health_programme_benefits_year_11': without_health_programme_benefits_year_11,
            'without_health_programme_benefits_year_12': without_health_programme_benefits_year_12,
            'without_health_programme_benefits_year_13': without_health_programme_benefits_year_13,
            'without_health_programme_benefits_year_14': without_health_programme_benefits_year_14,
            'without_health_programme_benefits_year_15': without_health_programme_benefits_year_15,
            'without_health_programme_benefits_year_16': without_health_programme_benefits_year_16,
            'without_health_programme_benefits_year_17': without_health_programme_benefits_year_17,
            'without_health_programme_benefits_year_18': without_health_programme_benefits_year_18,
            'without_health_programme_benefits_year_19': without_health_programme_benefits_year_19,
            'without_health_programme_benefits_year_20': without_health_programme_benefits_year_20,
            'incremental_benefits_year_0': incremental_benefits_year_0,
            'incremental_benefits_year_1': incremental_benefits_year_1,
            'incremental_benefits_year_2': incremental_benefits_year_2,
            'incremental_benefits_year_3': incremental_benefits_year_3,
            'incremental_benefits_year_4': incremental_benefits_year_4,
            'incremental_benefits_year_5': incremental_benefits_year_5,
            'incremental_benefits_year_6': incremental_benefits_year_6,
            'incremental_benefits_year_7': incremental_benefits_year_7,
            'incremental_benefits_year_8': incremental_benefits_year_8,
            'incremental_benefits_year_9': incremental_benefits_year_9,
            'incremental_benefits_year_10': incremental_benefits_year_10,
            'incremental_benefits_year_11': incremental_benefits_year_11,
            'incremental_benefits_year_12': incremental_benefits_year_12,
            'incremental_benefits_year_13': incremental_benefits_year_13,
            'incremental_benefits_year_14': incremental_benefits_year_14,
            'incremental_benefits_year_15': incremental_benefits_year_15,
            'incremental_benefits_year_16': incremental_benefits_year_16,
            'incremental_benefits_year_17': incremental_benefits_year_17,
            'incremental_benefits_year_18': incremental_benefits_year_18,
            'incremental_benefits_year_19': incremental_benefits_year_19,
            'incremental_benefits_year_20': incremental_benefits_year_20,
            'discounted_benefits_year_0': (1.0725**int(-0))*float(incremental_benefits_year_0),
            'discounted_benefits_year_1': (1.0725**int(-1))*float(incremental_benefits_year_1),
            'discounted_benefits_year_2': (1.0725**int(-2))*float(incremental_benefits_year_2),
            'discounted_benefits_year_3': (1.0725**int(-3))*float(incremental_benefits_year_3),
            'discounted_benefits_year_4': (1.0725**int(-4))*float(incremental_benefits_year_4),
            'discounted_benefits_year_5': (1.0725**int(-5))*float(incremental_benefits_year_5),
            'discounted_benefits_year_6': (1.0725**int(-6))*float(incremental_benefits_year_6),
            'discounted_benefits_year_7': (1.0725**int(-7))*float(incremental_benefits_year_7),
            'discounted_benefits_year_8': (1.0725**int(-8))*float(incremental_benefits_year_8),
            'discounted_benefits_year_9': (1.0725**int(-9))*float(incremental_benefits_year_9),
            'discounted_benefits_year_10': (1.0725**int(-10))*float(incremental_benefits_year_10),
            'discounted_benefits_year_11': (1.0725**int(-11))*float(incremental_benefits_year_11),
            'discounted_benefits_year_12': (1.0725**int(-12))*float(incremental_benefits_year_12),
            'discounted_benefits_year_13': (1.0725**int(-13))*float(incremental_benefits_year_13),
            'discounted_benefits_year_14': (1.0725**int(-14))*float(incremental_benefits_year_14),
            'discounted_benefits_year_15': (1.0725**int(-15))*float(incremental_benefits_year_15),
            'discounted_benefits_year_16': (1.0725**int(-16))*float(incremental_benefits_year_16),
            'discounted_benefits_year_17': (1.0725**int(-17))*float(incremental_benefits_year_17),
            'discounted_benefits_year_18': (1.0725**int(-18))*float(incremental_benefits_year_18),
            'discounted_benefits_year_19': (1.0725**int(-19))*float(incremental_benefits_year_19),
            'discounted_benefits_year_20': (1.0725**int(-20))*float(incremental_benefits_year_20),
            'annual_programme_costs_year_0': annual_programme_costs_year_0,
            'annual_programme_costs_year_1': annual_programme_costs_year_1,
            'annual_programme_costs_year_2': annual_programme_costs_year_2,
            'annual_programme_costs_year_3': annual_programme_costs_year_3,
            'annual_programme_costs_year_4': annual_programme_costs_year_4,
            'annual_programme_costs_year_5': annual_programme_costs_year_5,
            'annual_programme_costs_year_6': annual_programme_costs_year_6,
            'annual_programme_costs_year_7': annual_programme_costs_year_7,
            'annual_programme_costs_year_8': annual_programme_costs_year_8,
            'annual_programme_costs_year_9': annual_programme_costs_year_9,
            'annual_programme_costs_year_10': annual_programme_costs_year_10,
            'annual_programme_costs_year_11': annual_programme_costs_year_11,
            'annual_programme_costs_year_12': annual_programme_costs_year_12,
            'annual_programme_costs_year_13': annual_programme_costs_year_13,
            'annual_programme_costs_year_14': annual_programme_costs_year_14,
            'annual_programme_costs_year_15': annual_programme_costs_year_15,
            'annual_programme_costs_year_16': annual_programme_costs_year_16,
            'annual_programme_costs_year_17': annual_programme_costs_year_17,
            'annual_programme_costs_year_18': annual_programme_costs_year_18,
            'annual_programme_costs_year_19': annual_programme_costs_year_19,
            'annual_programme_costs_year_20': annual_programme_costs_year_20,
            'discounted_costs_year_0': (1.0725 ** int(-0)) * float(ZDU_setup_costs_year),
            'discounted_costs_year_1': (1.0725 ** int(-1)) * float(annual_programme_costs_year_1),
            'discounted_costs_year_2': (1.0725 ** int(-2)) * float(annual_programme_costs_year_2),
            'discounted_costs_year_3': (1.0725 ** int(-3)) * float(annual_programme_costs_year_3),
            'discounted_costs_year_4': (1.0725 ** int(-4)) * float(annual_programme_costs_year_4),
            'discounted_costs_year_5': (1.0725 ** int(-5)) * float(annual_programme_costs_year_5),
            'discounted_costs_year_6': (1.0725 ** int(-6)) * float(annual_programme_costs_year_6),
            'discounted_costs_year_7': (1.0725 ** int(-7)) * float(annual_programme_costs_year_7),
            'discounted_costs_year_8': (1.0725 ** int(-8)) * float(annual_programme_costs_year_8),
            'discounted_costs_year_9': (1.0725 ** int(-9)) * float(annual_programme_costs_year_9),
            'discounted_costs_year_10': (1.0725 ** int(-10)) * float(annual_programme_costs_year_10),
            'discounted_costs_year_11': (1.0725 ** int(-11)) * float(annual_programme_costs_year_11),
            'discounted_costs_year_12': (1.0725 ** int(-12)) * float(annual_programme_costs_year_12),
            'discounted_costs_year_13': (1.0725 ** int(-13)) * float(annual_programme_costs_year_13),
            'discounted_costs_year_14': (1.0725 ** int(-14)) * float(annual_programme_costs_year_14),
            'discounted_costs_year_15': (1.0725 ** int(-15)) * float(annual_programme_costs_year_15),
            'discounted_costs_year_16': (1.0725 ** int(-16)) * float(annual_programme_costs_year_16),
            'discounted_costs_year_17': (1.0725 ** int(-17)) * float(annual_programme_costs_year_17),
            'discounted_costs_year_18': (1.0725 ** int(-18)) * float(annual_programme_costs_year_18),
            'discounted_costs_year_19': (1.0725 ** int(-19)) * float(annual_programme_costs_year_19),
            'discounted_costs_year_20': (1.0725 ** int(-20)) * float(annual_programme_costs_year_20),
                        'discounted_net_benefits_year_0': ((1.0725 ** int(-0)) * float(incremental_benefits_year_0)) - (
                        (1.0725 ** int(-0)) * float(ZDU_setup_costs_year)),
            'discounted_net_benefits_year_1': ((1.0725 ** int(-1)) * float(incremental_benefits_year_1)) - (
                        (1.0725 ** int(-1)) * float(annual_programme_costs_year_1)),
            'discounted_net_benefits_year_2': ((1.0725 ** int(-2)) * float(incremental_benefits_year_2)) - (
                        (1.0725 ** int(-2)) * float(annual_programme_costs_year_2)),
            'discounted_net_benefits_year_3': ((1.0725 ** int(-3)) * float(incremental_benefits_year_3)) - (
                        (1.0725 ** int(-3)) * float(annual_programme_costs_year_3)),
            'discounted_net_benefits_year_4': ((1.0725 ** int(-4)) * float(incremental_benefits_year_4)) - (
                        (1.0725 ** int(-4)) * float(annual_programme_costs_year_4)),
            'discounted_net_benefits_year_5': ((1.0725 ** int(-5)) * float(incremental_benefits_year_5)) - (
                        (1.0725 ** int(-5)) * float(annual_programme_costs_year_5)),
            'discounted_net_benefits_year_6': ((1.0725 ** int(-6)) * float(incremental_benefits_year_6)) - (
                        (1.0725 ** int(-6)) * float(annual_programme_costs_year_6)),
            'discounted_net_benefits_year_7': ((1.0725 ** int(-7)) * float(incremental_benefits_year_7)) - (
                        (1.0725 ** int(-7)) * float(annual_programme_costs_year_7)),
            'discounted_net_benefits_year_8': ((1.0725 ** int(-8)) * float(incremental_benefits_year_8)) - (
                        (1.0725 ** int(-8)) * float(annual_programme_costs_year_8)),
            'discounted_net_benefits_year_9': ((1.0725 ** int(-9)) * float(incremental_benefits_year_9)) - (
                        (1.0725 ** int(-9)) * float(annual_programme_costs_year_9)),
            'discounted_net_benefits_year_10': ((1.0725 ** int(-10)) * float(incremental_benefits_year_10)) - (
                        (1.0725 ** int(-10)) * float(annual_programme_costs_year_10)),
            'discounted_net_benefits_year_11': ((1.0725 ** int(-11)) * float(incremental_benefits_year_11)) - (
                        (1.0725 ** int(-11)) * float(annual_programme_costs_year_11)),
            'discounted_net_benefits_year_12': ((1.0725 ** int(-12)) * float(incremental_benefits_year_12)) - (
                        (1.0725 ** int(-12)) * float(annual_programme_costs_year_12)),
            'discounted_net_benefits_year_13': ((1.0725 ** int(-13)) * float(incremental_benefits_year_13)) - (
                        (1.0725 ** int(-13)) * float(annual_programme_costs_year_13)),
            'discounted_net_benefits_year_14': ((1.0725 ** int(-14)) * float(incremental_benefits_year_14)) - (
                        (1.0725 ** int(-14)) * float(annual_programme_costs_year_14)),
            'discounted_net_benefits_year_15': ((1.0725 ** int(-15)) * float(incremental_benefits_year_15)) - (
                        (1.0725 ** int(-15)) * float(annual_programme_costs_year_15)),
            'discounted_net_benefits_year_16': ((1.0725 ** int(-16)) * float(incremental_benefits_year_16)) - (
                        (1.0725 ** int(-16)) * float(annual_programme_costs_year_16)),
            'discounted_net_benefits_year_17': ((1.0725 ** int(-17)) * float(incremental_benefits_year_17)) - (
                        (1.0725 ** int(-17)) * float(annual_programme_costs_year_17)),
            'discounted_net_benefits_year_18': ((1.0725 ** int(-18)) * float(incremental_benefits_year_18)) - (
                        (1.0725 ** int(-18)) * float(annual_programme_costs_year_18)),
            'discounted_net_benefits_year_19': ((1.0725 ** int(-19)) * float(incremental_benefits_year_19)) - (
                        (1.0725 ** int(-19)) * float(annual_programme_costs_year_19)),
            'discounted_net_benefits_year_20': ((1.0725 ** int(-20)) * float(incremental_benefits_year_20)) - (
                        (1.0725 ** int(-20)) * float(annual_programme_costs_year_20)),
            'NPV_year': (((1.0725 ** int(-0)) * float(incremental_benefits_year_0)) - (
                        (1.0725 ** int(-0)) * float(ZDU_setup_costs_year))) +
                        (((1.0725 ** int(-1)) * float(incremental_benefits_year_1)) - (
                                    (1.0725 ** int(-1)) * float(annual_programme_costs_year_1))) +
                        (((1.0725 ** int(-2)) * float(incremental_benefits_year_2)) - (
                                    (1.0725 ** int(-2)) * float(annual_programme_costs_year_2))) +
                        (((1.0725 ** int(-3)) * float(incremental_benefits_year_3)) - (
                                    (1.0725 ** int(-3)) * float(annual_programme_costs_year_3))) +
                        (((1.0725 ** int(-4)) * float(incremental_benefits_year_4)) - (
                                    (1.0725 ** int(-4)) * float(annual_programme_costs_year_4))) +
                        (((1.0725 ** int(-5)) * float(incremental_benefits_year_5)) - (
                                    (1.0725 ** int(-5)) * float(annual_programme_costs_year_5))) +
                        (((1.0725 ** int(-6)) * float(incremental_benefits_year_6)) - (
                                    (1.0725 ** int(-6)) * float(annual_programme_costs_year_6))) +
                        (((1.0725 ** int(-7)) * float(incremental_benefits_year_7)) - (
                                    (1.0725 ** int(-7)) * float(annual_programme_costs_year_7))) +
                        (((1.0725 ** int(-8)) * float(incremental_benefits_year_8)) - (
                                    (1.0725 ** int(-8)) * float(annual_programme_costs_year_8))) +
                        (((1.0725 ** int(-9)) * float(incremental_benefits_year_9)) - (
                                    (1.0725 ** int(-9)) * float(annual_programme_costs_year_9))) +
                        (((1.0725 ** int(-10)) * float(incremental_benefits_year_10)) - (
                                    (1.0725 ** int(-10)) * float(annual_programme_costs_year_10))) +
                        (((1.0725 ** int(-11)) * float(incremental_benefits_year_11)) - (
                                    (1.0725 ** int(-11)) * float(annual_programme_costs_year_11))) +
                        (((1.0725 ** int(-12)) * float(incremental_benefits_year_12)) - (
                                    (1.0725 ** int(-12)) * float(annual_programme_costs_year_12))) +
                        (((1.0725 ** int(-13)) * float(incremental_benefits_year_13)) - (
                                    (1.0725 ** int(-13)) * float(annual_programme_costs_year_13))) +
                        (((1.0725 ** int(-14)) * float(incremental_benefits_year_14)) - (
                                    (1.0725 ** int(-14)) * float(annual_programme_costs_year_14))) +
                        (((1.0725 ** int(-15)) * float(incremental_benefits_year_15)) - (
                                    (1.0725 ** int(-15)) * float(annual_programme_costs_year_15))) +
                        (((1.0725 ** int(-16)) * float(incremental_benefits_year_16)) - (
                                    (1.0725 ** int(-16)) * float(annual_programme_costs_year_16))) +
                        (((1.0725 ** int(-17)) * float(incremental_benefits_year_17)) - (
                                    (1.0725 ** int(-17)) * float(annual_programme_costs_year_17))) +
                        (((1.0725 ** int(-18)) * float(incremental_benefits_year_18)) - (
                                    (1.0725 ** int(-18)) * float(annual_programme_costs_year_18))) +
                        (((1.0725 ** int(-19)) * float(incremental_benefits_year_19)) - (
                                    (1.0725 ** int(-19)) * float(annual_programme_costs_year_19))) +
                        (((1.0725 ** int(-20)) * float(incremental_benefits_year_20)) - (
                                    (1.0725 ** int(-20)) * float(annual_programme_costs_year_20))),

            'BCR_year': (((1.0725 ** int(-0)) * float(incremental_benefits_year_0)) +
                         ((1.0725 ** int(-1)) * float(incremental_benefits_year_1)) +
                         ((1.0725 ** int(-2)) * float(incremental_benefits_year_2)) +
                         ((1.0725 ** int(-3)) * float(incremental_benefits_year_3)) +
                         ((1.0725 ** int(-4)) * float(incremental_benefits_year_4)) +
                         ((1.0725 ** int(-5)) * float(incremental_benefits_year_5)) +
                         ((1.0725 ** int(-6)) * float(incremental_benefits_year_6)) +
                         ((1.0725 ** int(-7)) * float(incremental_benefits_year_7)) +
                         ((1.0725 ** int(-8)) * float(incremental_benefits_year_8)) +
                         ((1.0725 ** int(-9)) * float(incremental_benefits_year_9)) +
                         ((1.0725 ** int(-10)) * float(incremental_benefits_year_10)) +
                         ((1.0725 ** int(-11)) * float(incremental_benefits_year_11)) +
                         ((1.0725 ** int(-12)) * float(incremental_benefits_year_12)) +
                         ((1.0725 ** int(-13)) * float(incremental_benefits_year_13)) +
                         ((1.0725 ** int(-14)) * float(incremental_benefits_year_14)) +
                         ((1.0725 ** int(-15)) * float(incremental_benefits_year_15)) +
                         ((1.0725 ** int(-16)) * float(incremental_benefits_year_16)) +
                         ((1.0725 ** int(-17)) * float(incremental_benefits_year_17)) +
                         ((1.0725 ** int(-18)) * float(incremental_benefits_year_18)) +
                         ((1.0725 ** int(-19)) * float(incremental_benefits_year_19)) +
                         ((1.0725 ** int(-20)) * float(incremental_benefits_year_20))) / (
                                    ((1.0725 ** int(-0)) * float(ZDU_setup_costs_year)) +
                                    ((1.0725 ** int(-1)) * float(annual_programme_costs_year_1)) +
                                    ((1.0725 ** int(-2)) * float(annual_programme_costs_year_2)) +
                                    ((1.0725 ** int(-3)) * float(annual_programme_costs_year_3)) +
                                    ((1.0725 ** int(-4)) * float(annual_programme_costs_year_4)) +
                                    ((1.0725 ** int(-5)) * float(annual_programme_costs_year_5)) +
                                    ((1.0725 ** int(-6)) * float(annual_programme_costs_year_6)) +
                                    ((1.0725 ** int(-7)) * float(annual_programme_costs_year_7)) +
                                    ((1.0725 ** int(-8)) * float(annual_programme_costs_year_8)) +
                                    ((1.0725 ** int(-9)) * float(annual_programme_costs_year_9)) +
                                    ((1.0725 ** int(-10)) * float(annual_programme_costs_year_10)) +
                                    ((1.0725 ** int(-11)) * float(annual_programme_costs_year_11)) +
                                    ((1.0725 ** int(-12)) * float(annual_programme_costs_year_12)) +
                                    ((1.0725 ** int(-13)) * float(annual_programme_costs_year_13)) +
                                    ((1.0725 ** int(-14)) * float(annual_programme_costs_year_14)) +
                                    ((1.0725 ** int(-15)) * float(annual_programme_costs_year_15)) +
                                    ((1.0725 ** int(-16)) * float(annual_programme_costs_year_16)) +
                                    ((1.0725 ** int(-17)) * float(annual_programme_costs_year_17)) +
                                    ((1.0725 ** int(-18)) * float(annual_programme_costs_year_18)) +
                                    ((1.0725 ** int(-19)) * float(annual_programme_costs_year_19)) +
                                    ((1.0725 ** int(-20)) * float(annual_programme_costs_year_20))),

            'increase_in_annual_programme_costs_year_0': annual_programme_costs_year_0,
            'increase_in_annual_programme_costs_year_1': 1.2 * float(annual_programme_costs_year_1),
            'increase_in_annual_programme_costs_year_2': 1.2 * float(annual_programme_costs_year_2),
            'increase_in_annual_programme_costs_year_3': 1.2 * float(annual_programme_costs_year_3),
            'increase_in_annual_programme_costs_year_4': 1.2 * float(annual_programme_costs_year_4),
            'increase_in_annual_programme_costs_year_5': 1.2 * float(annual_programme_costs_year_5),
            'increase_in_annual_programme_costs_year_6': 1.2 * float(annual_programme_costs_year_6),
            'increase_in_annual_programme_costs_year_7': 1.2 * float(annual_programme_costs_year_7),
            'increase_in_annual_programme_costs_year_8': 1.2 * float(annual_programme_costs_year_8),
            'increase_in_annual_programme_costs_year_9': 1.2 * float(annual_programme_costs_year_9),
            'increase_in_annual_programme_costs_year_10': 1.2 * float(annual_programme_costs_year_10),
            'increase_in_annual_programme_costs_year_11': 1.2 * float(annual_programme_costs_year_11),
            'increase_in_annual_programme_costs_year_12': 1.2 * float(annual_programme_costs_year_12),
            'increase_in_annual_programme_costs_year_13': 1.2 * float(annual_programme_costs_year_13),
            'increase_in_annual_programme_costs_year_14': 1.2 * float(annual_programme_costs_year_14),
            'increase_in_annual_programme_costs_year_15': 1.2 * float(annual_programme_costs_year_15),
            'increase_in_annual_programme_costs_year_16': 1.2 * float(annual_programme_costs_year_16),
            'increase_in_annual_programme_costs_year_17': 1.2 * float(annual_programme_costs_year_17),
            'increase_in_annual_programme_costs_year_18': 1.2 * float(annual_programme_costs_year_18),
            'increase_in_annual_programme_costs_year_19': 1.2 * float(annual_programme_costs_year_19),
            'increase_in_annual_programme_costs_year_20': 1.2 * float(annual_programme_costs_year_20),

            'extra_discounted_costs_year_0': (1.0725 ** int(-0)) * float(ZDU_setup_costs_year),
            'extra_discounted_costs_year_1': (1.0725 ** int(-1)) * 1.2 * float(annual_programme_costs_year_1),
            'extra_discounted_costs_year_2': (1.0725 ** int(-2)) * 1.2 * float(annual_programme_costs_year_2),
            'extra_discounted_costs_year_3': (1.0725 ** int(-3)) * 1.2 * float(annual_programme_costs_year_3),
            'extra_discounted_costs_year_4': (1.0725 ** int(-4)) * 1.2 * float(annual_programme_costs_year_4),
            'extra_discounted_costs_year_5': (1.0725 ** int(-5)) * 1.2 * float(annual_programme_costs_year_5),
            'extra_discounted_costs_year_6': (1.0725 ** int(-6)) * 1.2 * float(annual_programme_costs_year_6),
            'extra_discounted_costs_year_7': (1.0725 ** int(-7)) * 1.2 * float(annual_programme_costs_year_7),
            'extra_discounted_costs_year_8': (1.0725 ** int(-8)) * 1.2 * float(annual_programme_costs_year_8),
            'extra_discounted_costs_year_9': (1.0725 ** int(-9)) * 1.2 * float(annual_programme_costs_year_9),
            'extra_discounted_costs_year_10': (1.0725 ** int(-10)) * 1.2 * float(annual_programme_costs_year_10),
            'extra_discounted_costs_year_11': (1.0725 ** int(-11)) * 1.2 * float(annual_programme_costs_year_11),
            'extra_discounted_costs_year_12': (1.0725 ** int(-12)) * 1.2 * float(annual_programme_costs_year_12),
            'extra_discounted_costs_year_13': (1.0725 ** int(-13)) * 1.2 * float(annual_programme_costs_year_13),
            'extra_discounted_costs_year_14': (1.0725 ** int(-14)) * 1.2 * float(annual_programme_costs_year_14),
            'extra_discounted_costs_year_15': (1.0725 ** int(-15)) * 1.2 * float(annual_programme_costs_year_15),
            'extra_discounted_costs_year_16': (1.0725 ** int(-16)) * 1.2 * float(annual_programme_costs_year_16),
            'extra_discounted_costs_year_17': (1.0725 ** int(-17)) * 1.2 * float(annual_programme_costs_year_17),
            'extra_discounted_costs_year_18': (1.0725 ** int(-18)) * 1.2 * float(annual_programme_costs_year_18),
            'extra_discounted_costs_year_19': (1.0725 ** int(-19)) * 1.2 * float(annual_programme_costs_year_19),
            'extra_discounted_costs_year_20': (1.0725 ** int(-20)) * 1.2 * float(annual_programme_costs_year_20),
            'extra_NPV_year': ((((1.0725 ** int(-0)) * float(incremental_benefits_year_0)) - (
                        (1.0725 ** int(-0)) * float(ZDU_setup_costs_year))) +
                               (((1.0725 ** int(-1)) * float(incremental_benefits_year_1)) - (
                                           (1.0725 ** int(-1)) * float(annual_programme_costs_year_1))) +
                               (((1.0725 ** int(-2)) * float(incremental_benefits_year_2)) - (
                                           (1.0725 ** int(-2)) * float(annual_programme_costs_year_2))) +
                               (((1.0725 ** int(-3)) * float(incremental_benefits_year_3)) - (
                                           (1.0725 ** int(-3)) * float(annual_programme_costs_year_3))) +
                               (((1.0725 ** int(-4)) * float(incremental_benefits_year_4)) - (
                                           (1.0725 ** int(-4)) * float(annual_programme_costs_year_4))) +
                               (((1.0725 ** int(-5)) * float(incremental_benefits_year_5)) - (
                                           (1.0725 ** int(-5)) * float(annual_programme_costs_year_5))) +
                               (((1.0725 ** int(-6)) * float(incremental_benefits_year_6)) - (
                                           (1.0725 ** int(-6)) * float(annual_programme_costs_year_6))) +
                               (((1.0725 ** int(-7)) * float(incremental_benefits_year_7)) - (
                                           (1.0725 ** int(-7)) * float(annual_programme_costs_year_7))) +
                               (((1.0725 ** int(-8)) * float(incremental_benefits_year_8)) - (
                                           (1.0725 ** int(-8)) * float(annual_programme_costs_year_8))) +
                               (((1.0725 ** int(-9)) * float(incremental_benefits_year_9)) - (
                                           (1.0725 ** int(-9)) * float(annual_programme_costs_year_9))) +
                               (((1.0725 ** int(-10)) * float(incremental_benefits_year_10)) - (
                                           (1.0725 ** int(-10)) * float(annual_programme_costs_year_10))) +
                               (((1.0725 ** int(-11)) * float(incremental_benefits_year_11)) - (
                                           (1.0725 ** int(-11)) * float(annual_programme_costs_year_11))) +
                               (((1.0725 ** int(-12)) * float(incremental_benefits_year_12)) - (
                                           (1.0725 ** int(-12)) * float(annual_programme_costs_year_12))) +
                               (((1.0725 ** int(-13)) * float(incremental_benefits_year_13)) - (
                                           (1.0725 ** int(-13)) * float(annual_programme_costs_year_13))) +
                               (((1.0725 ** int(-14)) * float(incremental_benefits_year_14)) - (
                                           (1.0725 ** int(-14)) * float(annual_programme_costs_year_14))) +
                               (((1.0725 ** int(-15)) * float(incremental_benefits_year_15)) - (
                                           (1.0725 ** int(-15)) * float(annual_programme_costs_year_15))) +
                               (((1.0725 ** int(-16)) * float(incremental_benefits_year_16)) - (
                                           (1.0725 ** int(-16)) * float(annual_programme_costs_year_16))) +
                               (((1.0725 ** int(-17)) * float(incremental_benefits_year_17)) - (
                                           (1.0725 ** int(-17)) * float(annual_programme_costs_year_17))) +
                               (((1.0725 ** int(-18)) * float(incremental_benefits_year_18)) - (
                                           (1.0725 ** int(-18)) * float(annual_programme_costs_year_18))) +
                               (((1.0725 ** int(-19)) * float(incremental_benefits_year_19)) - (
                                           (1.0725 ** int(-19)) * float(annual_programme_costs_year_19))) +
                               (((1.0725 ** int(-20)) * float(incremental_benefits_year_20)) - (
                                           (1.0725 ** int(-20)) * float(annual_programme_costs_year_20)))) - (
                                          ((1.0725 ** int(-0)) * float(ZDU_setup_costs_year)) +
                                          ((1.0725 ** int(-1)) * 1.2 * float(annual_programme_costs_year_1)) +
                                          ((1.0725 ** int(-2)) * 1.2 * float(annual_programme_costs_year_2)) +
                                          ((1.0725 ** int(-3)) * 1.2 * float(annual_programme_costs_year_3)) +
                                          ((1.0725 ** int(-4)) * 1.2 * float(annual_programme_costs_year_4)) +
                                          ((1.0725 ** int(-5)) * 1.2 * float(annual_programme_costs_year_5)) +
                                          ((1.0725 ** int(-6)) * 1.2 * float(annual_programme_costs_year_6)) +
                                          ((1.0725 ** int(-7)) * 1.2 * float(annual_programme_costs_year_7)) +
                                          ((1.0725 ** int(-8)) * 1.2 * float(annual_programme_costs_year_8)) +
                                          ((1.0725 ** int(-9)) * 1.2 * float(annual_programme_costs_year_9)) +
                                          ((1.0725 ** int(-10)) * 1.2 * float(annual_programme_costs_year_10)) +
                                          ((1.0725 ** int(-11)) * 1.2 * float(annual_programme_costs_year_11)) +
                                          ((1.0725 ** int(-12)) * 1.2 * float(annual_programme_costs_year_12)) +
                                          ((1.0725 ** int(-13)) * 1.2 * float(annual_programme_costs_year_13)) +
                                          ((1.0725 ** int(-14)) * 1.2 * float(annual_programme_costs_year_14)) +
                                          ((1.0725 ** int(-15)) * 1.2 * float(annual_programme_costs_year_15)) +
                                          ((1.0725 ** int(-16)) * 1.2 * float(annual_programme_costs_year_16)) +
                                          ((1.0725 ** int(-17)) * 1.2 * float(annual_programme_costs_year_17)) +
                                          ((1.0725 ** int(-18)) * 1.2 * float(annual_programme_costs_year_18)) +
                                          ((1.0725 ** int(-19)) * 1.2 * float(annual_programme_costs_year_19)) +
                                          ((1.0725 ** int(-20)) * 1.2 * float(annual_programme_costs_year_20))),

            'extra_BCR_year': (((1.0725 ** int(-0)) * float(incremental_benefits_year_0)) +
                               ((1.0725 ** int(-1)) * float(incremental_benefits_year_1)) +
                               ((1.0725 ** int(-2)) * float(incremental_benefits_year_2)) +
                               ((1.0725 ** int(-3)) * float(incremental_benefits_year_3)) +
                               ((1.0725 ** int(-4)) * float(incremental_benefits_year_4)) +
                               ((1.0725 ** int(-5)) * float(incremental_benefits_year_5)) +
                               ((1.0725 ** int(-6)) * float(incremental_benefits_year_6)) +
                               ((1.0725 ** int(-7)) * float(incremental_benefits_year_7)) +
                               ((1.0725 ** int(-8)) * float(incremental_benefits_year_8)) +
                               ((1.0725 ** int(-9)) * float(incremental_benefits_year_9)) +
                               ((1.0725 ** int(-10)) * float(incremental_benefits_year_10)) +
                               ((1.0725 ** int(-11)) * float(incremental_benefits_year_11)) +
                               ((1.0725 ** int(-12)) * float(incremental_benefits_year_12)) +
                               ((1.0725 ** int(-13)) * float(incremental_benefits_year_13)) +
                               ((1.0725 ** int(-14)) * float(incremental_benefits_year_14)) +
                               ((1.0725 ** int(-15)) * float(incremental_benefits_year_15)) +
                               ((1.0725 ** int(-16)) * float(incremental_benefits_year_16)) +
                               ((1.0725 ** int(-17)) * float(incremental_benefits_year_17)) +
                               ((1.0725 ** int(-18)) * float(incremental_benefits_year_18)) +
                               ((1.0725 ** int(-19)) * float(incremental_benefits_year_19)) +
                               ((1.0725 ** int(-20)) * float(incremental_benefits_year_20))) / (
                                          ((1.0725 ** int(-0)) * float(ZDU_setup_costs_year)) +
                                          ((1.0725 ** int(-1)) * 1.2 * float(annual_programme_costs_year_1)) +
                                          ((1.0725 ** int(-2)) * 1.2 * float(annual_programme_costs_year_2)) +
                                          ((1.0725 ** int(-3)) * 1.2 * float(annual_programme_costs_year_3)) +
                                          ((1.0725 ** int(-4)) * 1.2 * float(annual_programme_costs_year_4)) +
                                          ((1.0725 ** int(-5)) * 1.2 * float(annual_programme_costs_year_5)) +
                                          ((1.0725 ** int(-6)) * 1.2 * float(annual_programme_costs_year_6)) +
                                          ((1.0725 ** int(-7)) * 1.2 * float(annual_programme_costs_year_7)) +
                                          ((1.0725 ** int(-8)) * 1.2 * float(annual_programme_costs_year_8)) +
                                          ((1.0725 ** int(-9)) * 1.2 * float(annual_programme_costs_year_9)) +
                                          ((1.0725 ** int(-10)) * 1.2 * float(annual_programme_costs_year_10)) +
                                          ((1.0725 ** int(-11)) * 1.2 * float(annual_programme_costs_year_11)) +
                                          ((1.0725 ** int(-12)) * 1.2 * float(annual_programme_costs_year_12)) +
                                          ((1.0725 ** int(-13)) * 1.2 * float(annual_programme_costs_year_13)) +
                                          ((1.0725 ** int(-14)) * 1.2 * float(annual_programme_costs_year_14)) +
                                          ((1.0725 ** int(-15)) * 1.2 * float(annual_programme_costs_year_15)) +
                                          ((1.0725 ** int(-16)) * 1.2 * float(annual_programme_costs_year_16)) +
                                          ((1.0725 ** int(-17)) * 1.2 * float(annual_programme_costs_year_17)) +
                                          ((1.0725 ** int(-18)) * 1.2 * float(annual_programme_costs_year_18)) +
                                          ((1.0725 ** int(-19)) * 1.2 * float(annual_programme_costs_year_19)) +
                                          ((1.0725 ** int(-20)) * 1.2 * float(annual_programme_costs_year_20))),
        })

    for x in rvf_CBA_collection.find({}, {"_id": 0}):
        context = x

    for total_annual_cost in rvf_total_annual_cost_collection.find({}, {"_id": 0}):
        total_annual_cost_context = total_annual_cost

    for capital in rvf_capital_cost_collection.find({}, {"_id": 0}):
        capital_cost_context = capital

    context2 = {
        'ZDU_setup_costs_year': capital_cost_context['setup_capital_total_cost'],
        'with_health_programme_benefits_year_0': context['with_health_programme_benefits_year_0'],
        'with_health_programme_benefits_year_1': context['with_health_programme_benefits_year_1'],
        'with_health_programme_benefits_year_2': context['with_health_programme_benefits_year_2'],
        'with_health_programme_benefits_year_3': context['with_health_programme_benefits_year_3'],
        'with_health_programme_benefits_year_4': context['with_health_programme_benefits_year_4'],
        'with_health_programme_benefits_year_5': context['with_health_programme_benefits_year_5'],
        'with_health_programme_benefits_year_6': context['with_health_programme_benefits_year_6'],
        'with_health_programme_benefits_year_7': context['with_health_programme_benefits_year_7'],
        'with_health_programme_benefits_year_8': context['with_health_programme_benefits_year_8'],
        'with_health_programme_benefits_year_9': context['with_health_programme_benefits_year_9'],
        'with_health_programme_benefits_year_10': context['with_health_programme_benefits_year_10'],
        'with_health_programme_benefits_year_11': context['with_health_programme_benefits_year_11'],
        'with_health_programme_benefits_year_12': context['with_health_programme_benefits_year_12'],
        'with_health_programme_benefits_year_13': context['with_health_programme_benefits_year_13'],
        'with_health_programme_benefits_year_14': context['with_health_programme_benefits_year_14'],
        'with_health_programme_benefits_year_15': context['with_health_programme_benefits_year_15'],
        'with_health_programme_benefits_year_16': context['with_health_programme_benefits_year_16'],
        'with_health_programme_benefits_year_17': context['with_health_programme_benefits_year_17'],
        'with_health_programme_benefits_year_18': context['with_health_programme_benefits_year_18'],
        'with_health_programme_benefits_year_19': context['with_health_programme_benefits_year_19'],
        'with_health_programme_benefits_year_20': context['with_health_programme_benefits_year_20'],

        'without_health_programme_benefits_year_0': context['without_health_programme_benefits_year_0'],
        'without_health_programme_benefits_year_1': context['without_health_programme_benefits_year_1'],
        'without_health_programme_benefits_year_2': context['without_health_programme_benefits_year_2'],
        'without_health_programme_benefits_year_3': context['without_health_programme_benefits_year_3'],
        'without_health_programme_benefits_year_4': context['without_health_programme_benefits_year_4'],
        'without_health_programme_benefits_year_5': context['without_health_programme_benefits_year_5'],
        'without_health_programme_benefits_year_6': context['without_health_programme_benefits_year_6'],
        'without_health_programme_benefits_year_7': context['without_health_programme_benefits_year_7'],
        'without_health_programme_benefits_year_8': context['without_health_programme_benefits_year_8'],
        'without_health_programme_benefits_year_9': context['without_health_programme_benefits_year_9'],
        'without_health_programme_benefits_year_10': context['without_health_programme_benefits_year_10'],
        'without_health_programme_benefits_year_11': context['without_health_programme_benefits_year_11'],
        'without_health_programme_benefits_year_12': context['without_health_programme_benefits_year_12'],
        'without_health_programme_benefits_year_13': context['without_health_programme_benefits_year_13'],
        'without_health_programme_benefits_year_14': context['without_health_programme_benefits_year_14'],
        'without_health_programme_benefits_year_15': context['without_health_programme_benefits_year_15'],
        'without_health_programme_benefits_year_16': context['without_health_programme_benefits_year_16'],
        'without_health_programme_benefits_year_17': context['without_health_programme_benefits_year_17'],
        'without_health_programme_benefits_year_18': context['without_health_programme_benefits_year_18'],
        'without_health_programme_benefits_year_19': context['without_health_programme_benefits_year_19'],
        'without_health_programme_benefits_year_20': context['without_health_programme_benefits_year_20'],

        'incremental_benefits_year_0': context['incremental_benefits_year_0'],
        'incremental_benefits_year_1': context['incremental_benefits_year_1'],
        'incremental_benefits_year_2': context['incremental_benefits_year_2'],
        'incremental_benefits_year_3': context['incremental_benefits_year_3'],
        'incremental_benefits_year_4': context['incremental_benefits_year_4'],
        'incremental_benefits_year_5': context['incremental_benefits_year_5'],
        'incremental_benefits_year_6': context['incremental_benefits_year_6'],
        'incremental_benefits_year_7': context['incremental_benefits_year_7'],
        'incremental_benefits_year_8': context['incremental_benefits_year_8'],
        'incremental_benefits_year_9': context['incremental_benefits_year_9'],
        'incremental_benefits_year_10': context['incremental_benefits_year_10'],
        'incremental_benefits_year_11': context['incremental_benefits_year_11'],
        'incremental_benefits_year_12': context['incremental_benefits_year_12'],
        'incremental_benefits_year_13': context['incremental_benefits_year_13'],
        'incremental_benefits_year_14': context['incremental_benefits_year_14'],
        'incremental_benefits_year_15': context['incremental_benefits_year_15'],
        'incremental_benefits_year_16': context['incremental_benefits_year_16'],
        'incremental_benefits_year_17': context['incremental_benefits_year_17'],
        'incremental_benefits_year_18': context['incremental_benefits_year_18'],
        'incremental_benefits_year_19': context['incremental_benefits_year_19'],
        'incremental_benefits_year_20': context['incremental_benefits_year_20'],

        'discounted_benefits_year_0': (1.0725**int(-0))*float(context['incremental_benefits_year_0']),
        'discounted_benefits_year_1': (1.0725**int(-1))*float(context['incremental_benefits_year_1']),
        'discounted_benefits_year_2': (1.0725**int(-2))*float(context['incremental_benefits_year_2']),
        'discounted_benefits_year_3': (1.0725**int(-3))*float(context['incremental_benefits_year_3']),
        'discounted_benefits_year_4': (1.0725**int(-4))*float(context['incremental_benefits_year_4']),
        'discounted_benefits_year_5': (1.0725**int(-5))*float(context['incremental_benefits_year_5']),
        'discounted_benefits_year_6': (1.0725**int(-6))*float(context['incremental_benefits_year_6']),
        'discounted_benefits_year_7': (1.0725**int(-7))*float(context['incremental_benefits_year_7']),
        'discounted_benefits_year_8': (1.0725**int(-8))*float(context['incremental_benefits_year_8']),
        'discounted_benefits_year_9': (1.0725**int(-9))*float(context['incremental_benefits_year_9']),
        'discounted_benefits_year_10': (1.0725**int(-10))*float(context['incremental_benefits_year_10']),
        'discounted_benefits_year_11': (1.0725**int(-11))*float(context['incremental_benefits_year_11']),
        'discounted_benefits_year_12': (1.0725**int(-12))*float(context['incremental_benefits_year_12']),
        'discounted_benefits_year_13': (1.0725**int(-13))*float(context['incremental_benefits_year_13']),
        'discounted_benefits_year_14': (1.0725**int(-14))*float(context['incremental_benefits_year_14']),
        'discounted_benefits_year_15': (1.0725**int(-15))*float(context['incremental_benefits_year_15']),
        'discounted_benefits_year_16': (1.0725**int(-16))*float(context['incremental_benefits_year_16']),
        'discounted_benefits_year_17': (1.0725**int(-17))*float(context['incremental_benefits_year_17']),
        'discounted_benefits_year_18': (1.0725**int(-18))*float(context['incremental_benefits_year_18']),
        'discounted_benefits_year_19': (1.0725**int(-19))*float(context['incremental_benefits_year_19']),
        'discounted_benefits_year_20': (1.0725**int(-20))*float(context['incremental_benefits_year_20']),

        'annual_programme_costs_year_0': context['annual_programme_costs_year_0'],
        'annual_programme_costs_year_1': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_2': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_3': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_4': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_5': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_6': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_7': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_8': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_9': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_10': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_11': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_12': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_13': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_14': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_15': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_16': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_17': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_18': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_19': total_annual_cost_context['total_cost_ksh'],
        'annual_programme_costs_year_20': total_annual_cost_context['total_cost_ksh'],

        'discounted_costs_year_0': (1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost']),
        'discounted_costs_year_1': (1.0725 ** int(-1)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_2': (1.0725 ** int(-2)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_3': (1.0725 ** int(-3)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_4': (1.0725 ** int(-4)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_5': (1.0725 ** int(-5)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_6': (1.0725 ** int(-6)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_7': (1.0725 ** int(-7)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_8': (1.0725 ** int(-8)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_9': (1.0725 ** int(-9)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_10': (1.0725 ** int(-10)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_11': (1.0725 ** int(-11)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_12': (1.0725 ** int(-12)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_13': (1.0725 ** int(-13)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_14': (1.0725 ** int(-14)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_15': (1.0725 ** int(-15)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_16': (1.0725 ** int(-16)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_17': (1.0725 ** int(-17)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_18': (1.0725 ** int(-18)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_19': (1.0725 ** int(-19)) * float(total_annual_cost_context['total_cost_ksh']),
        'discounted_costs_year_20': (1.0725 ** int(-20)) * float(total_annual_cost_context['total_cost_ksh']),

        'discounted_net_benefits_year_0': ((1.0725 ** int(-0)) * float(context['incremental_benefits_year_0'])) - (
                    (1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost'])),
        'discounted_net_benefits_year_1': ((1.0725 ** int(-1)) * float(context['incremental_benefits_year_1'])) - (
                    (1.0725 ** int(-1)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_2': ((1.0725 ** int(-2)) * float(context['incremental_benefits_year_2'])) - (
                    (1.0725 ** int(-2)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_3': ((1.0725 ** int(-3)) * float(context['incremental_benefits_year_3'])) - (
                    (1.0725 ** int(-3)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_4': ((1.0725 ** int(-4)) * float(context['incremental_benefits_year_4'])) - (
                    (1.0725 ** int(-4)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_5': ((1.0725 ** int(-5)) * float(context['incremental_benefits_year_5'])) - (
                    (1.0725 ** int(-5)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_6': ((1.0725 ** int(-6)) * float(context['incremental_benefits_year_6'])) - (
                    (1.0725 ** int(-6)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_7': ((1.0725 ** int(-7)) * float(context['incremental_benefits_year_7'])) - (
                    (1.0725 ** int(-7)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_8': ((1.0725 ** int(-8)) * float(context['incremental_benefits_year_8'])) - (
                    (1.0725 ** int(-8)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_9': ((1.0725 ** int(-9)) * float(context['incremental_benefits_year_9'])) - (
                    (1.0725 ** int(-9)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_10': ((1.0725 ** int(-10)) * float(context['incremental_benefits_year_10'])) - (
                    (1.0725 ** int(-10)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_11': ((1.0725 ** int(-11)) * float(context['incremental_benefits_year_11'])) - (
                    (1.0725 ** int(-11)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_12': ((1.0725 ** int(-12)) * float(context['incremental_benefits_year_12'])) - (
                    (1.0725 ** int(-12)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_13': ((1.0725 ** int(-13)) * float(context['incremental_benefits_year_13'])) - (
                    (1.0725 ** int(-13)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_14': ((1.0725 ** int(-14)) * float(context['incremental_benefits_year_14'])) - (
                    (1.0725 ** int(-14)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_15': ((1.0725 ** int(-15)) * float(context['incremental_benefits_year_15'])) - (
                    (1.0725 ** int(-15)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_16': ((1.0725 ** int(-16)) * float(context['incremental_benefits_year_16'])) - (
                    (1.0725 ** int(-16)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_17': ((1.0725 ** int(-17)) * float(context['incremental_benefits_year_17'])) - (
                    (1.0725 ** int(-17)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_18': ((1.0725 ** int(-18)) * float(context['incremental_benefits_year_18'])) - (
                    (1.0725 ** int(-18)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_19': ((1.0725 ** int(-19)) * float(context['incremental_benefits_year_19'])) - (
                    (1.0725 ** int(-19)) * float(total_annual_cost_context['total_cost_ksh'])),
        'discounted_net_benefits_year_20': ((1.0725 ** int(-20)) * float(context['incremental_benefits_year_20'])) - (
                    (1.0725 ** int(-20)) * float(total_annual_cost_context['total_cost_ksh'])),

        'NPV_year': (((1.0725 ** int(-0)) * float(context['incremental_benefits_year_0'])) - (
                    (1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost']))) +
                    (((1.0725 ** int(-1)) * float(context['incremental_benefits_year_1'])) - (
                                (1.0725 ** int(-1)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-2)) * float(context['incremental_benefits_year_2'])) - (
                                (1.0725 ** int(-2)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-3)) * float(context['incremental_benefits_year_3'])) - (
                                (1.0725 ** int(-3)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-4)) * float(context['incremental_benefits_year_4'])) - (
                                (1.0725 ** int(-4)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-5)) * float(context['incremental_benefits_year_5'])) - (
                                (1.0725 ** int(-5)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-6)) * float(context['incremental_benefits_year_6'])) - (
                                (1.0725 ** int(-6)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-7)) * float(context['incremental_benefits_year_7'])) - (
                                (1.0725 ** int(-7)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-8)) * float(context['incremental_benefits_year_8'])) - (
                                (1.0725 ** int(-8)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-9)) * float(context['incremental_benefits_year_9'])) - (
                                (1.0725 ** int(-9)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-10)) * float(context['incremental_benefits_year_10'])) - (
                                (1.0725 ** int(-10)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-11)) * float(context['incremental_benefits_year_11'])) - (
                                (1.0725 ** int(-11)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-12)) * float(context['incremental_benefits_year_12'])) - (
                                (1.0725 ** int(-12)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-13)) * float(context['incremental_benefits_year_13'])) - (
                                (1.0725 ** int(-13)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-14)) * float(context['incremental_benefits_year_14'])) - (
                                (1.0725 ** int(-14)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-15)) * float(context['incremental_benefits_year_15'])) - (
                                (1.0725 ** int(-15)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-16)) * float(context['incremental_benefits_year_16'])) - (
                                (1.0725 ** int(-16)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-17)) * float(context['incremental_benefits_year_17'])) - (
                                (1.0725 ** int(-17)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-18)) * float(context['incremental_benefits_year_18'])) - (
                                (1.0725 ** int(-18)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-19)) * float(context['incremental_benefits_year_19'])) - (
                                (1.0725 ** int(-19)) * float(total_annual_cost_context['total_cost_ksh']))) +
                    (((1.0725 ** int(-20)) * float(context['incremental_benefits_year_20'])) - (
                                (1.0725 ** int(-20)) * float(total_annual_cost_context['total_cost_ksh']))),

        'BCR_year': (((1.0725 ** int(-0)) * float(context['incremental_benefits_year_0'])) +
                     ((1.0725 ** int(-1)) * float(context['incremental_benefits_year_1'])) +
                     ((1.0725 ** int(-2)) * float(context['incremental_benefits_year_2'])) +
                     ((1.0725 ** int(-3)) * float(context['incremental_benefits_year_3'])) +
                     ((1.0725 ** int(-4)) * float(context['incremental_benefits_year_4'])) +
                     ((1.0725 ** int(-5)) * float(context['incremental_benefits_year_5'])) +
                     ((1.0725 ** int(-6)) * float(context['incremental_benefits_year_6'])) +
                     ((1.0725 ** int(-7)) * float(context['incremental_benefits_year_7'])) +
                     ((1.0725 ** int(-8)) * float(context['incremental_benefits_year_8'])) +
                     ((1.0725 ** int(-9)) * float(context['incremental_benefits_year_9'])) +
                     ((1.0725 ** int(-10)) * float(context['incremental_benefits_year_10'])) +
                     ((1.0725 ** int(-11)) * float(context['incremental_benefits_year_11'])) +
                     ((1.0725 ** int(-12)) * float(context['incremental_benefits_year_12'])) +
                     ((1.0725 ** int(-13)) * float(context['incremental_benefits_year_13'])) +
                     ((1.0725 ** int(-14)) * float(context['incremental_benefits_year_14'])) +
                     ((1.0725 ** int(-15)) * float(context['incremental_benefits_year_15'])) +
                     ((1.0725 ** int(-16)) * float(context['incremental_benefits_year_16'])) +
                     ((1.0725 ** int(-17)) * float(context['incremental_benefits_year_17'])) +
                     ((1.0725 ** int(-18)) * float(context['incremental_benefits_year_18'])) +
                     ((1.0725 ** int(-19)) * float(context['incremental_benefits_year_19'])) +
                     ((1.0725 ** int(-20)) * float(context['incremental_benefits_year_20']))
                     ) / (((1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost'])) +
                          ((1.0725 ** int(-1)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-2)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-3)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-4)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-5)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-6)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-7)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-8)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-9)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-10)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-11)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-12)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-13)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-14)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-15)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-16)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-17)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-18)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-19)) * float(total_annual_cost_context['total_cost_ksh'])) +
                          ((1.0725 ** int(-20)) * float(total_annual_cost_context['total_cost_ksh']))
                          ),

        'increase_in_annual_programme_costs_year_0': context['annual_programme_costs_year_0'],
        'increase_in_annual_programme_costs_year_1': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_2': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_3': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_4': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_5': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_6': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_7': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_8': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_9': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_10': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_11': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_12': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_13': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_14': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_15': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_16': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_17': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_18': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_19': 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'increase_in_annual_programme_costs_year_20': 1.2 * float(total_annual_cost_context['total_cost_ksh']),

        'extra_discounted_costs_year_0': (1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost']),
        'extra_discounted_costs_year_1': (1.0725 ** int(-1)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_2': (1.0725 ** int(-2)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_3': (1.0725 ** int(-3)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_4': (1.0725 ** int(-4)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_5': (1.0725 ** int(-5)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_6': (1.0725 ** int(-6)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_7': (1.0725 ** int(-7)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_8': (1.0725 ** int(-8)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_9': (1.0725 ** int(-9)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_10': (1.0725 ** int(-10)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_11': (1.0725 ** int(-11)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_12': (1.0725 ** int(-12)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_13': (1.0725 ** int(-13)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_14': (1.0725 ** int(-14)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_15': (1.0725 ** int(-15)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_16': (1.0725 ** int(-16)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_17': (1.0725 ** int(-17)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_18': (1.0725 ** int(-18)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_19': (1.0725 ** int(-19)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_discounted_costs_year_20': (1.0725 ** int(-20)) * 1.2 * float(
            total_annual_cost_context['total_cost_ksh']),
        'extra_NPV_year': ((((1.0725 ** int(-0)) * float(context['incremental_benefits_year_0'])) - (
                    (1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost']))) +
                           (((1.0725 ** int(-1)) * float(context['incremental_benefits_year_1'])) - (
                                       (1.0725 ** int(-1)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-2)) * float(context['incremental_benefits_year_2'])) - (
                                       (1.0725 ** int(-2)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-3)) * float(context['incremental_benefits_year_3'])) - (
                                       (1.0725 ** int(-3)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-4)) * float(context['incremental_benefits_year_4'])) - (
                                       (1.0725 ** int(-4)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-5)) * float(context['incremental_benefits_year_5'])) - (
                                       (1.0725 ** int(-5)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-6)) * float(context['incremental_benefits_year_6'])) - (
                                       (1.0725 ** int(-6)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-7)) * float(context['incremental_benefits_year_7'])) - (
                                       (1.0725 ** int(-7)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-8)) * float(context['incremental_benefits_year_8'])) - (
                                       (1.0725 ** int(-8)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-9)) * float(context['incremental_benefits_year_9'])) - (
                                       (1.0725 ** int(-9)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-10)) * float(context['incremental_benefits_year_10'])) - (
                                       (1.0725 ** int(-10)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-11)) * float(context['incremental_benefits_year_11'])) - (
                                       (1.0725 ** int(-11)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-12)) * float(context['incremental_benefits_year_12'])) - (
                                       (1.0725 ** int(-12)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-13)) * float(context['incremental_benefits_year_13'])) - (
                                       (1.0725 ** int(-13)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-14)) * float(context['incremental_benefits_year_14'])) - (
                                       (1.0725 ** int(-14)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-15)) * float(context['incremental_benefits_year_15'])) - (
                                       (1.0725 ** int(-15)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-16)) * float(context['incremental_benefits_year_16'])) - (
                                       (1.0725 ** int(-16)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-17)) * float(context['incremental_benefits_year_17'])) - (
                                       (1.0725 ** int(-17)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-18)) * float(context['incremental_benefits_year_18'])) - (
                                       (1.0725 ** int(-18)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-19)) * float(context['incremental_benefits_year_19'])) - (
                                       (1.0725 ** int(-19)) * float(total_annual_cost_context['total_cost_ksh']))) +
                           (((1.0725 ** int(-20)) * float(context['incremental_benefits_year_20'])) - (
                                       (1.0725 ** int(-20)) * float(total_annual_cost_context['total_cost_ksh'])))) - (
                                      ((1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost'])) +
                                      ((1.0725 ** int(-1)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-2)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-3)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-4)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-5)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-6)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-7)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-8)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-9)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-10)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-11)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-12)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-13)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-14)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-15)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-16)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-17)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-18)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-19)) * 1.2 * float(
                                          total_annual_cost_context['total_cost_ksh'])) +
                                      ((1.0725 ** int(-20)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']))
                                      ),

        'extra_BCR_year': (((1.0725 ** int(-0)) * float(context['incremental_benefits_year_0'])) +
                           ((1.0725 ** int(-1)) * float(context['incremental_benefits_year_1'])) +
                           ((1.0725 ** int(-2)) * float(context['incremental_benefits_year_2'])) +
                           ((1.0725 ** int(-3)) * float(context['incremental_benefits_year_3'])) +
                           ((1.0725 ** int(-4)) * float(context['incremental_benefits_year_4'])) +
                           ((1.0725 ** int(-5)) * float(context['incremental_benefits_year_5'])) +
                           ((1.0725 ** int(-6)) * float(context['incremental_benefits_year_6'])) +
                           ((1.0725 ** int(-7)) * float(context['incremental_benefits_year_7'])) +
                           ((1.0725 ** int(-8)) * float(context['incremental_benefits_year_8'])) +
                           ((1.0725 ** int(-9)) * float(context['incremental_benefits_year_9'])) +
                           ((1.0725 ** int(-10)) * float(context['incremental_benefits_year_10'])) +
                           ((1.0725 ** int(-11)) * float(context['incremental_benefits_year_11'])) +
                           ((1.0725 ** int(-12)) * float(context['incremental_benefits_year_12'])) +
                           ((1.0725 ** int(-13)) * float(context['incremental_benefits_year_13'])) +
                           ((1.0725 ** int(-14)) * float(context['incremental_benefits_year_14'])) +
                           ((1.0725 ** int(-15)) * float(context['incremental_benefits_year_15'])) +
                           ((1.0725 ** int(-16)) * float(context['incremental_benefits_year_16'])) +
                           ((1.0725 ** int(-17)) * float(context['incremental_benefits_year_17'])) +
                           ((1.0725 ** int(-18)) * float(context['incremental_benefits_year_18'])) +
                           ((1.0725 ** int(-19)) * float(context['incremental_benefits_year_19'])) +
                           ((1.0725 ** int(-20)) * float(context['incremental_benefits_year_20']))
                           ) / (((1.0725 ** int(-0)) * float(capital_cost_context['setup_capital_total_cost'])) +
                                ((1.0725 ** int(-1)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-2)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-3)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-4)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-5)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-6)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-7)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-8)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-9)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-10)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-11)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-12)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-13)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-14)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-15)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-16)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-17)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-18)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-19)) * 1.2 * float(total_annual_cost_context['total_cost_ksh'])) +
                                ((1.0725 ** int(-20)) * 1.2 * float(total_annual_cost_context['total_cost_ksh']))
                                ),
    }

    return render(request,'CBA.html',context2)

def sensitivity_analysis(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    rvf_db = myclient['rvf_db2']

    rvf_CBA_collection = rvf_db['CBA']

    for CBA in rvf_CBA_collection.find({}, {"_id": 0}):
         CBA_context = CBA

    context2 = {
        'NPV_current': CBA_context['NPV_year'],
        'NPV_with_20_percent_increase_annual_cost': CBA_context['extra_NPV_year'],
        'NPV_percent_change': ((float(CBA_context['extra_NPV_year']) - float(CBA_context['NPV_year']))/float(CBA_context['NPV_year']))*100,
        'BCR_current': CBA_context['BCR_year'],
        'BCR_with_20_percent_increase_annual_cost': CBA_context['extra_BCR_year'],
        'BCR_percent_change': ((float(CBA_context['extra_BCR_year']) - float(CBA_context['BCR_year'])) / float(CBA_context['BCR_year'])) * 100,
    }

    return render(request,'sensitivity_analysis.html',context2)